"""Extract and draw graphics from Mario

By Jake Vanderplas, 2013 <http://jakevdp.github.com>
License: GPL.
Feel free to use and distribute, but keep this attribution intact.
"""
import zipfile
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap


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


def draw_mario():
    """Draw a grid of mario graphics"""
    NG = NESGraphics()
    cmap = ListedColormap(['white', 'red', 'orange', 'brown'])
    im = 252 + np.zeros((17, 19))

    # Big Mario row 1
    im[1:5, 1:3] = [[0, 1], [2, 3], [4, 5], [6, 7]]
    im[1:5, 4:6] = [[8, 9], [10, 11], [12, 13], [14, 15]]
    im[1:5, 7:9] = [[16, 17], [18, 19], [20, 21], [22, 23]]
    im[1:5, 10:12] = [[24, 25], [26, 27], [28, 29], [30, 31]]
    im[1:5, 13:15] = [[32, 33], [34, 35], [36, 37], [38, 39]]
    im[1:5, 16:18] = [[0, 1], [76, 77], [74, -74], [75, -75]]

    # Small Mario row 1
    im[9:13, 1:3] = [[8, 9], [40, 41], [42, 43], [44, 45]]
    im[9:13, 4:6] = [[8, 9], [10, 11], [12, 48], [49, 45]]
    im[9:13, 7:9] = [[8, 9], [10, 11], [46, 47], [49, 45]]
    im[9:13, 10:12] = [[8, 9], [10, 11], [12, 48], [92, 93]]
    im[9:13, 13:15] = [[8, 9], [10, 11], [12, 48], [94, 95]]
    im[9:13, 16:18] = [[252, 252], [8, 9], [88, 89], [90, -90]]

    # Big Mario row 2
    im[6:8, 1:3] = [[54, 55], [56, 57]]
    im[6:8, 4:6] = [[50, 51], [52, 53]]
    im[6:8, 7:9] = [[58, 55], [59, 60]]
    im[6:8, 10:12] = [[61, 62], [63, 64]]
    im[6:8, 13:15] = [[50, 65], [66, 67]]
    im[6:8, 16:18] = [[58, 55], [79, -79]]

    # Small Mario row 2
    im[14:16, 1:3] = [[50, 51], [68, 69]]
    im[14:16, 4:6] = [[50, 51], [70, 71]]
    im[14:16, 7:9] = [[50, 51], [72, 73]]
    im[14:16, 10:12] = [[50, 51], [144, 145]]
    im[14:16, 13:15] = [[58, 55], [146, 147]]
    im[14:16, 16:18] = [[158, -158], [159, -159]]

    im = NG.generate_image(im)
    
    fig = plt.figure(figsize=(6, 6 * 17. / 19.))
    ax = fig.add_axes((0, 0, 1, 1), xticks=[], yticks=[])
    ax.imshow(im, cmap=cmap, interpolation='nearest', clim=(0, 3))


def draw_graphics():
    """Draw foreground and background mario graphics"""
    NG = NESGraphics()
    cmap = ListedColormap(['#88AACC', 'black', '#EECCCC', '#BB3333',
                           'green', 'orange', 'red', 'gold',
                           '#EEEEEE', 'gray'])
    
    im = 252 + np.zeros((17, 16))
    colors = np.zeros((17, 16, 4))

    # question block
    im[1:3, 1:3] = [[339, 340], [341, 342]]
    colors[1:3, 1:3] = [0, 7, 3, 1]

    # coin
    im[1:3, 4:6] = [[421, 422], [423, 424]]
    colors[1:3, 4:6] = [0, 7, 8, 1]

    # mushroom
    im[1:3, 7:9] = [[118, 119], [120, 121]]
    colors[1:3, 7:9] = [0, 6, 8, 5]

    # 1-up mushroom
    im[1:3, 10:12] = [[118, 119], [120, 121]]
    colors[1:3, 10:12] = [0, 4, 8, 7]

    # fire flower
    im[1:3, 13:15] = [[214, -214], [217, -217]]
    colors[1, 13:15] = [0, 6, 8, 5]
    colors[2, 13:15] = [0, 4, 4, 4]

    # green koopa-troopa
    im[4:7, 1:3] = [[252, 160], [161, 162], [163, 164]]
    im[4:7, 4:6] = [[252, 165], [166, 167], [168, 169]]
    colors[4:7, 1:6] = [0, 4, 8, 5]

    # red koopa-troopa
    im[4:7, 7:9] = [[252, 160], [161, 162], [163, 164]]
    im[4:7, 10:12] = [[252, 165], [166, 167], [168, 169]]
    colors[4:7, 7:12] = [0, 6, 8, 5]

    # cloud turtle
    im[4:7, 13:15] = [[185, 184], [432, 434], [433, 435]]
    colors[4, 13:15] = [0, 4, 8, 5]
    colors[5:7, 13:15] = [0, 8, 8, 4]

    # spiny
    im[8:10, 1:3] = [[148, -148], [149, -149]]
    im[8:10, 4:6] = [[150, 151], [152, 153]]
    im[8:10, 7:9] = [[154, 155], [156, 157]]
    colors[8:10, 1:9] = [0, 6, 8, 5]

    # Goombas
    im[8:10, 10:12] = [[112, 113], [114, 115]]
    im[8:10, 13:15] = [[112, 113], [-115, -114]]
    colors[8:10, 10:15] = [0, 1, 2, 3]

    # fish
    im[11:13, 1:3] = [[178, 179], [180, 181]]
    im[11:13, 4:6] = [[182, 179], [183, 181]]
    colors[11:13, 1:6] = [0, 9, 8, 5]

    # beetle
    im[11:13, 7:9] = [[170, 171], [172, 173]]
    im[11:13, 10:12] = [[174, 175], [176, 177]]
    colors[11:13, 7:12] = [0, 1, 2, 3]

    # flag
    im[14:16, 1:3] = [[84, 85], [86, 87]]
    colors[14:16, 1:3] = [0, 6, 8, 5]

    # brown block
    im[14:16, 4:6] = [[343, 344], [345, 346]]
    colors[14:16, 4:6] = [0, 7, 3, 1]

    # brown block 2
    im[14:16, 7:9] = [[436, 437], [438,439]]
    colors[14:16, 7:9] = [0, 2, 3, 1]

    # bricks
    im[14:16, 10:12] = [[325, 325], [327, 327]]
    colors[14:16, 10:12] = [0, 2, 3, 1]

    # cannon
    im[12:16, 13:15] = [[454, 455], [456, 457], [458, 459], [460, 461]]
    colors[12:16, 13:15] = [0, 2, 3, 1]
    
    im = NG.generate_image(im, colors)
    
    fig = plt.figure(figsize=(5, 5 * 17. / 16.))
    ax = fig.add_axes((0, 0, 1, 1), xticks=[], yticks=[])
    ax.imshow(im, cmap=cmap, interpolation='nearest', clim=(0, 9))

if __name__ == '__main__':
    draw_mario()
    draw_graphics()
    plt.show()
