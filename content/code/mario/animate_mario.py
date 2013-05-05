"""Extract and draw graphics from Mario

By Jake Vanderplas, 2013 <http://jakevdp.github.com>
License: GPL.
Feel free to use and distribute, but keep this attribution intact.
"""
from collections import defaultdict
import zipfile
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib import animation


class NESGraphics(object):
    """Class interface for stripping graphics from an NES ROM"""
    def __init__(self, filename='mario_ROM.zip', offset=2049):
        self.offset = offset
        if zipfile.is_zipfile(filename):
            zp = zipfile.ZipFile(filename)
            data = np.unpackbits(np.frombuffer(zp.read(zp.filelist[0]),
                                               dtype=np.uint8))
        else:
            data = np.unpackbits(np.fromfile(filename, dtype=np.uint8))
        self.data = data.reshape((-1, 8, 8))

    def generate_image(self, A, C=None, transparent=False):
        """Generate an image from the pattern table.

        Parameters
        ----------
        A : array_like
            an array of integers indexing the thumbnails to use.
            The upper-left corner of the image is A[0, 0], and the
            bottom-right corner is A[-1, -1].  A negative index indicates
            that the thumbnail should be flipped horizontally.
        C : array-like
            The color table for A.  C should have shape A.shape + (4,).
            C[i, j] gives the values associated with the four bits of A
            for the output image.
        transparent : array_like
            if true, then zero-values in A will be masked for transparency

        Returns
        -------
        im : ndarray or masked array
             the image encoded by A and C
        """
        A = np.asarray(A)
        if C is None:
            C = range(4)

        # broadcast C to the shape of A
        C = np.asarray(C) + np.zeros(A.shape + (1,))

        im = np.zeros((8 * A.shape[0], 8 * A.shape[1]))
        for i in range(A.shape[0]):
            for j in range(A.shape[1]):
                # extract bits
                ind = 2 * (abs(A[i, j]) + self.offset)
                thumb = self.data[ind] + 2 * self.data[ind + 1]

                # set bit colors
                thumb = C[i, j, thumb]

                # flip image if negative
                if A[i, j] < 0:
                    thumb = thumb[:, ::-1]
                im[8 * i:8 * (i + 1), 8 * j:8 * (j + 1)] = thumb

        if transparent:
            im = np.ma.masked_equal(im, 0)

        return im


class NESAnimator():
    """Class for animating NES graphics"""
    def __init__(self, framesize, figsize=(8, 6),
                 filename='mario_ROM.zip', offset=2049):
        self.NG = NESGraphics()
        self.figsize = figsize
        self.framesize = framesize
        self.frames = defaultdict(lambda: [])
        self.ims = {}

    def add_frame(self, key, A, C=None, ctable=None,
                  offset=(0, 0), transparent=True):
        """add a frame to the animation.
        A & C are passed to NESGraphics.generate_image"""
        cmap = ListedColormap(ctable)
        im = self.NG.generate_image(A, C, transparent=transparent)
        self.frames[key].append((im, cmap, offset))

    def _initialize(self):
        """initialize animation"""
        A = np.ma.masked_equal(np.zeros((2, 2)), 0)
        for i, key in enumerate(sorted(self.frames.keys())):
            self.ims[key] = self.ax.imshow(A, interpolation='nearest',
                                           zorder=i + 1)
        self.ax.set_xlim(0, self.framesize[1])
        self.ax.set_ylim(0, self.framesize[0])

        return tuple(self.ims[key] for key in sorted(self.ims.keys()))

    def _animate(self, i):
        """animation step"""
        for key in sorted(self.frames.keys()):
            im, cmap, offset = self.frames[key][i % len(self.frames[key])]

            self.ims[key].set_data(im)
            self.ims[key].set_cmap(cmap)
            self.ims[key].set_clim(0, len(cmap.colors) - 1)
            self.ims[key].set_extent((offset[1],
                                      im.shape[1] / 8 + offset[1],
                                      offset[0],
                                      im.shape[0] / 8 + offset[0]))

        return tuple(self.ims[key] for key in sorted(self.ims.keys()))

    def animate(self, interval, frames, blit=True):
        """animate the frames"""
        self.fig = plt.figure(figsize=self.figsize)
        self.ax = self.fig.add_axes([0, 0, 1, 1], frameon=False,
                                    xticks=[], yticks=[])
        self.ax.xaxis.set_major_formatter(plt.NullFormatter())
        self.ax.yaxis.set_major_formatter(plt.NullFormatter())
        self.anim = animation.FuncAnimation(self.fig,
                                            self._animate,
                                            init_func=self._initialize,
                                            frames=frames, interval=interval,
                                            blit=blit)
        self.fig.anim = self.anim
        return self.anim


def animate_mario():
    NA = NESAnimator(framesize=(12, 16), figsize=(4, 3))

    # Set up the background frames
    bg = np.zeros((12, 18), dtype=int)
    bg_colors = np.arange(4) + np.zeros((12, 18, 4))
    bg_ctable = ['#88AACC', 'tan', 'brown', 'black',
                 'green', '#DDAA11', '#FFCC00']

    # blue sky
    bg.fill(292)

    # brown bricks on the ground
    bg[10] = 9 * [436, 437]
    bg[11] = 9 * [438, 439]

    # little green hill 
    bg[8, 3:5] = [305, 306]
    bg[9, 2:6] = [304, 308, 294, 307]
    bg_colors[8, 3:5] = [0, 1, 4, 3]
    bg_colors[9, 2:6] = [0, 1, 4, 3]

    # brown bricks
    bg[2, 10:18] = 325
    bg[3, 10:18] = 327

    # gold question block
    bg[2, 12:14] = [339, 340]
    bg[3, 12:14] = [341, 342]
    bg_colors[2:4, 12:14] = [0, 6, 2, 3]
    
    # duplicate background for clean wrapping
    bg = np.hstack([bg, bg])
    bg_colors = np.hstack([bg_colors, bg_colors])

    # get index of yellow pixels to make them flash
    i_yellow = np.where(bg_colors == 6)

    # create background frames by offsetting the image
    for offset in range(36):
        bg_colors[i_yellow] = [6, 6, 6, 6, 5, 5, 2, 5, 5][offset % 9]
        NA.add_frame('bg', bg, bg_colors, bg_ctable,
                     offset=(0, -0.5 * offset),
                     transparent=False)

    # Create mario frames
    mario_colors = ['white', 'red', 'orange', 'brown']
    NA.add_frame('mario', [[0, 1], [2, 3], [4, 5], [6, 7]],
                 ctable=mario_colors, offset=(2, 10))
    NA.add_frame('mario', [[8, 9], [10, 11], [12, 13], [14, 15]],
                 ctable=mario_colors, offset=(2, 10))
    NA.add_frame('mario', [[16, 17], [18, 19], [20, 21], [22, 23]],
                 ctable=mario_colors, offset=(2, 10))

    # Create koopa-troopa frames
    troopa_colors = ['white', 'green', 'white', 'orange']
    NA.add_frame('troopa', [[252, 160], [161, 162], [163, 164]],
                 ctable=troopa_colors, offset=(2, 7))
    NA.add_frame('troopa', [[252, 165], [166, 167], [168, 169]],
                 ctable=troopa_colors, offset=(2, 7))

    # Create goomba frames
    goomba_colors = ['white', 'black', '#EECCCC', '#BB3333']
    NA.add_frame('goomba', [[112, 113], [114, 115]],
                 ctable=goomba_colors, offset=(2, 4))
    NA.add_frame('goomba', [[112, 113], [-115, -114]],
                 ctable=goomba_colors, offset=(2, 4))

    return NA.animate(interval=100, frames=36)


if __name__ == '__main__':
    anim = animate_mario()

    # saving as animated gif requires matplotlib 0.13+ and imagemagick
    #anim.save('mario_animation.gif', writer='imagemagick', fps=10)

    plt.show()
