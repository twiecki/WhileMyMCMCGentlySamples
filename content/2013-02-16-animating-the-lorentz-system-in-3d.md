Title: Animating the Lorenz System in 3D
date: 2013-02-16 08:05
comments: true
slug: animating-the-lorentz-system-in-3d

<!-- PELICAN_BEGIN_SUMMARY -->
One of the things I really enjoy about Python is how easy it makes it to solve
interesting problems and visualize those solutions in a compelling way. I've
done several posts on creating animations using matplotlib's relatively new
[animation toolkit](http://matplotlib.sourceforge.net/api/animation_api.html):
(some examples are a chaotic
[double pendulum](/blog/2012/08/18/matplotlib-animation-tutorial/),
the collisions of
[particles in a box](/blog/2012/08/18/matplotlib-animation-tutorial/),
the time-evolution of a
[quantum-mechanical wavefunction](/blog/2012/09/05/quantum-python/),
and even a scene from the classic video game,
[Super Mario Bros.](/blog/2013/01/13/hacking-super-mario-bros-with-python/)).

Recently, a reader [commented](/blog/2012/08/18/matplotlib-animation-tutorial/#comment-799781196) asking whether I might do a 3D animation example.  Matplotlib
has a decent 3D toolkit called
[mplot3D](http://matplotlib.org/mpl_toolkits/mplot3d/index.html),
and though I haven't previously seen it used in conjunction with the
animation tools, there's nothing fundamental that prevents it.

At the commenter's suggestion, I decided to try this out with a simple
example of a chaotic system: the Lorenz equations.

<!-- PELICAN_END_SUMMARY -->

## Solving the Lorenz System ##
The [Lorenz Equations](http://en.wikipedia.org/wiki/Lorenz_system) are a
system of three coupled, first-order, nonlinear differential equations
which describe the trajectory of a particle through time.
The system was originally derived by Lorenz as a model
of atmospheric convection, but the deceptive simplicity
of the equations have made them an often-used example in fields beyond
atmospheric physics.

The equations describe the evolution of the spatial variables $x$, $y$,
and $z$, given the governing parameters $\sigma$, $\beta$, and $\rho$,
through the specification of the time-derivatives of the spatial variables:

${\rm d}x/{\rm d}t = \sigma(y - x)$

${\rm d}y/{\rm d}t = x(\rho - z) - y$

${\rm d}z/{\rm d}t = xy - \beta z$

The resulting dynamics are entirely deterministic giving a starting point
$(x_0, y_0, z_0)$ and a time interval $t$.  Though it looks straightforward,
for certain choices of the parameters $(\sigma, \rho, \beta)$, the
trajectories become chaotic, and the resulting trajectories display some
surprising properties.

Though no general analytic solution exists for this system, the solutions
can be computed numerically.
Python makes this sort of problem very easy to solve: one can
simply use Scipy's interface to
[ODEPACK](https://computation.llnl.gov/casc/odepack/odepack_home.html),
an optimized Fortran package for solving ordinary differential equations.
Here's how the problem can be set up:

``` python
import numpy as np
from scipy import integrate

# Note: t0 is required for the odeint function, though it's not used here.
def lorentz_deriv((x, y, z), t0, sigma=10., beta=8./3, rho=28.0):
    """Compute the time-derivative of a Lorenz system."""
    return [sigma * (y - x), x * (rho - z) - y, x * y - beta * z]

x0 = [1, 1, 1]  # starting vector
t = np.linspace(0, 3, 1000)  # one thousand time steps
x_t = integrate.odeint(lorentz_deriv, x0, t)
```

That's all there is to it!

## Visualizing the results ##
Now that we've computed these results, we can use matplotlib's
animation and 3D plotting toolkits
to visualize the trajectories of several particles.  Because
I've described the animation tools in-depth in a
[previous post](/blog/2012/08/18/matplotlib-animation-tutorial/),
I will skip that discussion here and jump straight into the code:

{% include_code lorentz_animation.py lang:python Lorenz System %}

The resulting animation looks something like this:

{% video /downloads/videos/lorentz_attractor.mp4 360 270 /downloads/videos/lorentz_attractor_frame.png %}

Notice that there are two locations in the space that seem to draw-in all
paths: these are the so-called "Lorenz attractors", and have some interesting
properties which you can read about elsewhere.  The qualitative
characteristics of these Lorenz attractors
vary in somewhat surprising ways as the parameters
$(\sigma, \rho, \beta)$ are changed.  If you are so inclined, you may
wish to download the above code and play with these values to see what
the results look like.

I hope that this brief exercise has shown you the power and flexibility of
Python for understanding and visualizing a large array of problems, and
perhaps given you the inspiration to explore similar problems.

Happy coding!