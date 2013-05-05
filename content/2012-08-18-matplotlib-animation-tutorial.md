Title: Matplotlib Animation Tutorial
date: 2012-08-18 08:01
comments: true

<!-- PELICAN_BEGIN_SUMMARY -->
[Matplotlib](http://matplotlib.sourceforge.net) version 1.1 added some tools
for creating
[animations](http://matplotlib.sourceforge.net/api/animation_api.html)
which are really slick.  You can find some good example animations on
the matplotlib
[examples](http://matplotlib.sourceforge.net/examples/animation/index.html)
page.  I thought I'd share here some of the things I've learned when playing
around with these tools.

### Basic Animation ###
The animation tools center around the `matplotlib.animation.Animation` base
class, which provides a framework around which the animation functionality
is built.  The main interfaces are `TimedAnimation` and `FuncAnimation`,
which you can read more about in the
[documentation](http://matplotlib.sourceforge.net/api/animation_api.html).
Here I'll explore using the `FuncAnimation` tool, which I have found
to be the most useful.

<!-- PELICAN_END_SUMMARY -->

First we'll use `FuncAnimation` to do a basic animation of a sine wave moving
across the screen:

{% include_code basic_animation.py Basic Animation %}

Let's step through this and see what's going on.  After importing required
pieces of `numpy` and `matplotlib`, The script sets up the plot:
``` python
fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
line, = ax.plot([], [], lw=2)
```
Here we create a figure window, create a single axis in the figure, and then
create our line object which will be modified in the animation.  Note that
here we simply plot an empty line: we'll add data to the line later.

Next we'll create the functions which make the animation happen.  `init()`
is the function which will be called to create the base frame upon which
the animation takes place.  Here we use just a simple function which sets
the line data to nothing.  It is important that this function return the
line object, because this tells the animator which objects on the plot to
update after each frame:
``` python
def init():
    line.set_data([], [])
    return line,
```
The next piece is the animation function.  It takes a single parameter, the
frame number `i`, and draws a sine wave with a shift that depends on `i`:
```
# animation function.  This is called sequentially
def animate(i):
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,
```
Note that again here we return a tuple of the plot objects which have been
modified.  This tells the animation framework what parts of the plot should
be animated.

Finally, we create the animation object:
``` python
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=100, interval=20, blit=True)
```
This object needs to persist, so it must be assigned to a variable.  We've
chosen a 100 frame animation with a 20ms delay between frames.  The
`blit` keyword is an important one: this tells the animation to only re-draw
the pieces of the plot which have changed.  The time saved with `blit=True`
means that the animations display much more quickly.

We end with an optional save command, and then a show command to show the
result.  Here's what the script generates:
{% video /downloads/videos/basic_animation.mp4 360 270 /downloads/videos/basic_animation_frame.png %}

This framework for generating and saving animations is very powerful and
flexible: if we put some physics into the `animate` function, the possibilities
are endless.  Below are a couple examples of some physics animations that
I've been playing around with.

### Double Pendulum ###
One of the examples provided on the matplotlib
[example page](http://matplotlib.sourceforge.net/examples/animation/index.html)
is an animation of a double pendulum.  This example operates by precomputing
the pendulum position over 10 seconds, and then animating the results.  I
saw this and wondered if python would be fast enough to compute the dynamics
on the fly.  It turns out it is:

{% include_code double_pendulum.py Double Pendulum %}

Here we've created a class which stores the state of the double pendulum
(encoded in the angle of each arm plus the angular velocity of each arm)
and also provides some functions for computing the dynamics.  The animation
functions are the same as above, but we just have a bit more complicated
update function: it not only changes the position of the points, but also
changes the text to keep track of time and energy (energy should be constant
if our math is correct: it's comforting that it is).  The video below
lasts only ten seconds, but by running the script you can watch the
pendulum chaotically oscillate until your laptop runs out of power:

{% video /downloads/videos/double_pendulum.mp4 360 270 /downloads/videos/double_pendulum_frame.png %}

### Particles in a Box ###

Another animation I created is the elastic collisions of a group of particles
in a box under the force of gravity.  The collisions are elastic: they conserve
energy and 2D momentum, and the particles bounce realistically off the walls
of the box and fall under the influence of a constant gravitational force:

{% include_code particle_box.py Particles in a Box %}

The math should be familiar to anyone with a physics background, and the
result is pretty mesmerizing.  I coded this up during a flight, and ended
up just sitting and watching it for about ten minutes.

{% video /downloads/videos/particle_box.mp4 360 270 /downloads/videos/particle_box_frame.png %}

This is just the beginning: it might be an interesting exercise to add
other elements, like computation of the temperature and pressure to demonstrate
the ideal gas law, or real-time plotting of the velocity distribution to
watch it approach the expected Maxwellian distribution.  It opens up many
possibilities for virtual physics demos...

### Summing it up ###
The matplotlib animation module is an excellent addition to what was already
an excellent package.  I think I've just scratched the surface of what's
possible with these tools... what cool animation ideas can you come up
with?

Edit: in a [followup post](/blog/2012/09/05/quantum-python), I show how
these tools can be used to generate an animation of a simple Quantum
Mechanical system.