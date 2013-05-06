import zipfile
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap

BGCOLOR = '#AAAACC'
background = ListedColormap([BGCOLOR])
mario = ListedColormap([BGCOLOR, 'red', 'orange', 'brown'])
fire_mario = ListedColormap([BGCOLOR, 'white', 'orange', 'red'])

NUL = 252


class MarioDisplay(object):
    @classmethod
    def show_mario(cls):
        return cls(np.array(
                [[[0, 1], [2, 3], [4, 5], [6, 7]],
                 [[8, 9], [10, 11], [12, 13], [14, 15]],
                 [[16, 17], [18, 19], [20, 21], [22, 23]],
                 [[24, 25], [26, 27], [28, 29], [30, 31]],
                 [[32, 33], [34, 35], [36, 37], [38, 39]],
                 [[8, 9], [40, 41], [42, 43], [44, 45]],
                 [[8, 9], [10, 11], [12, 48], [49, 45]],
                 [[8, 9], [10, 11], [46, 47], [49, 45]],
                 [[0, 1], [76, 77], [74, -74], [75, -75]],
                 [[NUL, NUL], [8, 9], [88, 89], [90, -90]],
                 [[8, 9], [10, 11], [12, 48], [92, 93]],
                 [[8, 9], [10, 11], [12, 48], [94, 95]],
                 [[NUL, NUL], [NUL, NUL], [50, 51], [52, 53]],
                 [[NUL, NUL], [NUL, NUL], [54, 55], [56, 57]],
                 [[NUL, NUL], [NUL, NUL], [58, 55], [59, 60]],
                 [[NUL, NUL], [NUL, NUL], [61, 62], [63, 64]],
                 [[NUL, NUL], [NUL, NUL], [50, 65], [66, 67]],
                 [[NUL, NUL], [NUL, NUL], [50, 51], [68, 69]],
                 [[NUL, NUL], [NUL, NUL], [50, 51], [70, 71]],
                 [[NUL, NUL], [NUL, NUL], [50, 51], [72, 73]],
                 [[NUL, NUL], [NUL, NUL], [58, 55], [79, -79]],
                 [[NUL, NUL], [NUL, NUL], [50, 51], [144, 145]],
                 [[NUL, NUL], [NUL, NUL], [58, 55], [146, 147]],
                 [[NUL, NUL], [NUL, NUL], [158, -158], [159, -159]]]),
                   cmap=mario)

    @classmethod
    def show_random(cls):
        return cls(np.array(
                [[[NUL, NUL], [NUL, NUL], [112, 113], [114, 115]],
                 [[NUL, NUL], [NUL, NUL], [112, 113], [-115, -114]],
                 [[NUL, NUL], [NUL, NUL], [118, 119], [120, 121]],
                 [[NUL, NUL], [NUL, NUL], [150, 151], [152, 153]],
                 [[NUL, NUL], [NUL, NUL], [154, 155], [156, 157]],
                 [[NUL, NUL], [NUL, 160], [161, 162], [163, 164]],
                 [[NUL, NUL], [NUL, 165], [166, 167], [168, 169]],
                 [[NUL, NUL], [NUL, NUL], [170, 171], [172, 173]],
                 [[NUL, NUL], [NUL, NUL], [174, 175], [176, 177]],
                 [[NUL, NUL], [NUL, NUL], [339, 340], [341, 342]],
                 [[NUL, NUL], [NUL, NUL], [343, 344], [345, 346]],
                 [[NUL, NUL], [NUL, NUL], [432, 434], [433, 435]]]))

    def __init__(self, frames, filename='mario_ROM.zip',
                 pattern_offset=2049, cmap=plt.cm.binary):
        zp = zipfile.ZipFile(filename)
        self.data = np.unpackbits(np.frombuffer(zp.read(zp.filelist[0]),
                                                dtype=np.uint8))

        self.frames = frames
        self.pattern_offset = pattern_offset
        self.cmap = cmap

        self.fig, self.ax = plt.subplots(subplot_kw=dict(xticks=[], yticks=[]))

        xlim = (-32.5, 47.5)
        ylim = (-16.5, 31.5)

        self.ax.set_xlim(xlim)
        self.ax.set_ylim(ylim[::-1])

        self.bg = plt.imshow(np.ones((2, 2)),
                             extent=xlim + ylim,
                             cmap=background)

        self.fig.canvas.mpl_connect('key_press_event', self.key_press)
        self.show_frame(0)
        self.im.set_cmap(cmap)
        self.im.set_interpolation('nearest')
        self.im.set_clim(0, 3)

    def get_tile(self, offset, flatten=True):
        bit_index = (offset + self.pattern_offset) * 128
        thumb = self.data[bit_index:bit_index + 128].reshape((2, 8, 8))

        if flatten:
            return thumb[0] + 2 * thumb[1]
        else:
            return thumb

    def _get_tiles(self, arr):
        arr = np.atleast_2d(arr)
        assert arr.ndim == 2
        imarr = np.zeros((8 * arr.shape[0], 8 * arr.shape[1]),
                         dtype=int)

        for i in range(arr.shape[0]):
            for j in range(arr.shape[1]):
                tile = self.get_tile(abs(arr[i, j]))
                if arr[i, j] < 0:
                    tile = tile[:, ::-1]
                imarr[8 * i:8 * (i + 1), 8 * j:8 * (j + 1)] = tile
        return np.ma.masked_where(np.equal(imarr, 0), imarr)

    def show_tiles(self, arr):
        imarr = self._get_tiles(arr)
        if hasattr(self, 'im'):
            self.im.set_data(imarr)
        else:
            self.im = self.ax.imshow(imarr)

    def show_frame(self, i):
        self.curr_frame = i
        self.show_tiles(self.frames[i])

    def key_press(self, event):
        if not hasattr(self, 'curr_frame'):
            self.curr_frame = -1
        if event.key == 'right':
            self.show_frame((self.curr_frame + 1) % len(self.frames))
            self.fig.canvas.draw()
        elif event.key == 'left':
            self.show_frame((self.curr_frame - 1 + len(self.frames))
                            % len(self.frames))
            self.fig.canvas.draw()

#m = MarioDisplay.show_mario()
m = MarioDisplay.show_random()
        
plt.show()
