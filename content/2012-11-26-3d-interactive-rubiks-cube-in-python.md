Title: 3D Interactive Rubik's Cube in Python
date: 2012-11-26 22:00
comments: true
slug: 3d-interactive-rubiks-cube-in-python

<!-- PELICAN_BEGIN_SUMMARY -->
Over the weekend, I built a interactive 3D Rubik's cube simulator in python
using only [matplotlib](http://matplotlib.org) for all the graphics and
interaction.  Check out the demonstration here:

{% video /downloads/videos/MagicCube.mp4 680 400 /downloads/videos/MagicCube_frame.jpg %}

You can browse the source code at the MagicCube github repository:
[http://github.com/davidwhogg/MagicCube](http://github.com/davidwhogg/MagicCube).

<!-- PELICAN_END_SUMMARY -->

The 3D rendering is based on the quaternions and projections  discussed in
my [previous post](/blog/2012/11/24/simple-3d-visualization-in-matplotlib/),
and many of the key bindings discussed there are used here.
The additional component is the turning of each face.  This is actually
fairly simple to accomplish using the tools discussed above.

For example, the right face is perpendicular to the x-axis in the cube-frame.
Thus to turn it, you only need to manipulate polygons with x-coordinate
between 1/3 and 1 inclusive (the cube has side-length 2 and is centered on
the origin).  The correct faces are found quickly using
numpy's ``where`` statement, and a quaternion rotation is applied only to
these faces.  Easy!

The code and interface still needs some work, and I'm hoping to add more
features as I have time.  After spending my long weekend working on this,
I have some real work to catch-up on...

*Update: I've heard from some folks that the key and mouse bindings don't
work on some operating systems or backends.  If you experience
system-dependent bugs and have any insight into the problem, I'd appreciate
help working out what's happening!*