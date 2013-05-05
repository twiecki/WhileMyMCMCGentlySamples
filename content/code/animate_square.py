"""
Optical Illusion in Matplotlib

author: Jake Vanderplas
email: vanderplas@astro.washington.edu
website: http://jakevdp.github.com
license: BSD
Please feel free to use and modify this, but keep the above information.
Thanks!
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.patches import RegularPolygon

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(-2.5, 2.5), ylim=(-2.5, 2.5), aspect='equal')

# Add lines and patches
lines = ax.plot(np.zeros((2, 4)), np.zeros((2, 2)), lw=2, color='black')
squares = [RegularPolygon((np.sqrt(2) * x, np.sqrt(2) * y),
                          4, radius=0.6, orientation=0, color='black')
           for (x, y) in [(1, 0), (-1, 0), (0, 1), (0, -1)]]
for sq in squares:
    ax.add_patch(sq)


# initialization function: plot the background of each frame
def init():
    for line in lines:
        line.set_data([], [])
    for sq in squares:
        sq.set_alpha(0)
    return lines + squares


# animation function.  This is called sequentially
def animate(i):
    # Set transparency level for squares
    level = 0.5 - 0.8 * np.cos(0.005 * i * np.pi)
    level = min(level, 1)
    level = max(level, 0)

    for sq in squares:
        sq.set_alpha(level)

    # Set location for lines
    s = 0.6
    d1 = 0.2 * np.sin(0.05 * i * np.pi)
    d2 = 0.2 * np.cos(0.05 * i * np.pi)

    lines[0].set_data([(1 + d1 - s) / np.sqrt(2),
                      (1 + d1 + s) / np.sqrt(2)],
                     [(1 + d1 + s) / np.sqrt(2),
                      (1 + d1 - s) / np.sqrt(2)])

    lines[1].set_data([(-1 + d1 - s) / np.sqrt(2),
                      (-1 + d1 + s) / np.sqrt(2)],
                     [(-1 + d1 + s) / np.sqrt(2),
                      (-1 + d1 - s) / np.sqrt(2)])

    lines[2].set_data([(-1 - d2 - s) / np.sqrt(2),
                      (-1 - d2 + s) / np.sqrt(2)],
                     [(1 + d2 - s) / np.sqrt(2),
                      (1 + d2 + s) / np.sqrt(2)])

    lines[3].set_data([(1 - d2 - s) / np.sqrt(2),
                      (1 - d2 + s) / np.sqrt(2)],
                     [(-1 + d2 - s) / np.sqrt(2),
                      (-1 + d2 + s) / np.sqrt(2)])

    return lines + squares

# call the animator.  blit=True means only re-draw parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=400, interval=28, blit=True)


# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
#anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()
