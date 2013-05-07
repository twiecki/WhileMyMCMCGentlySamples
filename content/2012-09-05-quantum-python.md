Title: Quantum Python: Animating the Schrodinger Equation
date: 2012-09-05 20:12
comments: true
slug: quantum-python

<!-- PELICAN_BEGIN_SUMMARY -->
*Update: a reader contributed some improvements to the Python code presented
 below.  Please see the
[pySchrodinger](https://github.com/jakevdp/pySchrodinger) github repository
for updated code*

In a [previous post](/blog/2012/08/18/matplotlib-animation-tutorial/)
I explored the new animation capabilities of the latest
[matplotlib](http://matplotlib.sourceforge.net) release.
It got me wondering whether it would be possible to simulate more complicated
physical systems in real time in python.  Quantum Mechanics was the first
thing that came to mind.  It turns out that by mixing a bit of Physics
knowledge with a bit of computing knowledge, it's quite straightforward
to simulate and animate a simple quantum mechanical system with python.

## The Schrodinger Equation ##

The dynamics of a one-dimensional quantum system are governed by the
time-dependent Schrodinger equation:

$$
i\hbar\frac{\partial \psi}{\partial t}
  = \frac{-\hbar^2}{2m} \frac{\partial^2 \psi}{\partial x^2} + V \psi
$$

<!-- PELICAN_END_SUMMARY -->

The *wave function* $\psi$ is a function of both position $x$ and time $t$,
and is the fundamental description of the realm of the very small.
Imagine we are following the motion of a single particle in one
dimension.  This wave function represents a probability of measuring
the particle at a position $x$ at a time $t$. Quantum mechanics tells us that
(contrary to our familiar classical reasoning) this probability is not
a limitation of our knowledge of the system, but a reflection of an
unavoidable uncertainty about the position and time of events in the realm
of the very small.

Still, this equation is a bit opaque, but to visualize the results we'll need
to solve this numerically.  We'll approach this using the split-step Fourier
method.

## The Split-step Fourier Method ##

A standard way to numerically solve certain differential equations is
through the use of the Fourier transform.  We'll use a Fourier convention
of the following form:

$$
\widetilde{\psi}(k, t) = \frac{1}{\sqrt{2\pi}}
  \int_{-\infty}^{\infty} \psi(x, t) e^{-ikx} dx
$$

Under this convention, the associated inverse Fourier Transform is given by:

$$
\psi(x, t) = \frac{1}{\sqrt{2\pi}}
  \int_{-\infty}^{\infty} \widetilde{\psi}(k, t) e^{ikx} dk
$$

Substituting this into the Schrodinger equation and simplifying gives the
Fourier-space form of the Schrodinger equation:

$$
i\hbar\frac{\partial \widetilde{\psi}}{\partial t}
  = \frac{\hbar^2 k^2}{2m} \widetilde{\psi}
  + V(i\frac{\partial}{\partial k})\widetilde{\psi}
$$

The two versions of the Schrodinger equation contain an interesting symmetry:
the time step in each case depends on a straightforward multiplication of
the wave function $\psi$, as well as a more complicated term involving
derivatives with respect to $x$ or $k$.  The key observation is that while
the equation is difficult to evaluate fully within one of the forms, each
basis offers a straightforward calculation of one of the two contributions.
This suggests an efficient strategy to numerically solve the Schrodinger
Equation.

First we solve the straightforward part of the $x$-space Schrodinger
equation:
   
$$
i\hbar\frac{\partial \psi}{\partial t}
  = V(x) \psi
$$

For a small time step $\Delta t$, this has a solution of the form
   
$$
\psi(x, t + \Delta t) = \psi(x, t) e^{-i V(x) \Delta t / \hbar}
$$

Second, we solve the straightforward part of the $k$-space Schrodinger
equation:
   
$$
i\hbar\frac{\partial \widetilde{\psi}}{\partial t}
  = \frac{\hbar^2 k^2}{2 m} \widetilde{\psi}
$$

For a small time step $\Delta t$, this has a solution of the form

$$
\widetilde{\psi}(k, t + \Delta t)
    = \widetilde{\psi}(k, t) e^{-i \hbar k^2 \Delta t / 2m}
$$

## Numerical Considerations ##
Solving this system numerically will require repeated computations of the
Fourier transform of $\psi(x, t)$ and the inverse Fourier transform of
$\widetilde{\psi}(k, t)$.  The best-known algorithm for computation of
numerical Fourier transforms is the Fast Fourier Transform (FFT), which
is [available in scipy](http://docs.scipy.org/doc/scipy/reference/fftpack.html)
and efficiently computes the following form of the
discrete Fourier transform:

$$
  \widetilde{F_m} = \sum_{n=0}^{N-1} F_n e^{-2\pi i n m / N}
$$

and its inverse

$$
  F_n = \frac{1}{N} \sum_{m=0}^{N-1} \widetilde{F_m} e^{2\pi i n m / N}
$$

We need to know how these relate to the continuous Fourier transforms defined
and used above.  Let's take the example of the forward transform.  Assume that
the infinite integral is well-approximated by the finite integral from
$a$ to $b$, so that we can write

$$
\widetilde{\psi}(k, t) = \frac{1}{\sqrt{2\pi}}
   \int_a^b \psi(x, t) e^{-ikx} dx
$$

This approximation ends up being equivalent to assuming that the potential
$V(x) \to \infty$ at $x \le a$ and $x \ge b$.  We'll now approximate this
integral as a Riemann sum of $N$ terms, and define $\Delta x = (b - a) / N$,
and $x_n = a + n\Delta x$:

$$
\widetilde{\psi}(k, t) \simeq \frac{1}{\sqrt{2\pi}}
   \sum_{n=0}^{N-1} \psi(x_n, t) e^{-ikx_n} \Delta x
$$

This is starting to look like the discrete Fourier transform!  To bring it
even closer, let's define $k_m = k_0 + m\Delta k$, with
$\Delta k = 2\pi / (N\Delta x)$.  Then our approximation becomes

$$
\widetilde{\psi}(k_m, t) \simeq \frac{1}{\sqrt{2\pi}}
   \sum_{n=0}^{N-1} \psi(x_n, t) e^{-ik_m x_n} \Delta x
$$

(Note that just as we have limited the range of $x$ above, we have here limited
the range of $k$ as well.  This means that high-frequency components of the
signal will be lost in our approximation.  The Nyquist sampling theorem tells
us that this is an unavoidable consequence of choosing discrete steps in
space, and it can be shown that the spacing we chose above exactly satisfies
the Nyquist limit if we choose $k_0 = - \pi / \Delta x$).

Plugging our expressions for $x_n$ and $k_m$ into the Fourier
approximation and rearranging, we find the following:

$$
\left[\widetilde{\psi}(k_m, t) e^{i m x_0 \Delta k}\right]
   \simeq \sum_{n=0}^{N-1} 
   \left[ \frac{\Delta x}{\sqrt{2\pi}}
   \psi(x_n, t) e^{-ik_0 x_n} \right]
   e^{-2\pi i m n / N}
$$

Similar arguments from the inverse Fourier transform yield:

$$
\left[\frac{\Delta x}{\sqrt{2 \pi}} \psi(x_n, t) e^{-i k_0 x_n}\right]
   \simeq \frac{1}{N} \sum_{m=0}^{N-1} 
   \left[\widetilde{\psi}(k_m, t) e^{-i m x_0 \Delta k} \right]
   e^{2\pi i m n / N}
$$

Comparing these to the discrete Fourier transforms above, we find that the
*continuous* Fourier pair

$$
   \psi(x, t) \Longleftrightarrow \widetilde{\psi}(k, t)
$$

corresponds to the *discrete* Fourier pair

$$
   \frac{\Delta x}{\sqrt{2 \pi}} \psi(x_n, t) e^{-i k_0 x_n}
   \Longleftrightarrow
   \widetilde{\psi}(k_m, t) e^{-i m x_0 \Delta k}
$$

subject to the approximations mentioned above.  This allows a fast numerical
evaluation of the Schrodinger equation.

## Putting It All Together: the Algorithm ##

We now put this all together using the following algorithm

1. Choose $a$, $b$, $N$, and $k_0$ as above, sufficient to represent the
   initial state of your wave function $\psi(x)$. (**Warning:** this is perhaps
   the hardest part of the entire solution. If limits in $x$ or $k$ are chosen
   which do not suit your problem, then the approximations used above can
   destroy the accuracy of the calculation!)  Once these are chosen, then
   $\Delta x = (b - a) / N$ and $\Delta k = 2\pi / (b - a)$.  Define
   $x_n = a + n \Delta x$ and $k_m = k_0 + m \Delta k$.

2. Discretize the wave-functions on this grid.  Let $\psi_n(t) = \psi(x_n, t)$,
   $V_n = V(x_n)$, and $\widetilde{\psi}_m = \widetilde{\psi}(k_m, t)$.

3. To progress the system by a time-step $\Delta t$, perform the following:

   1. Compute a half-step in $x$:
      $\psi_n \longleftarrow \psi_n
       \exp[-i (\Delta t / 2) (V_n / \hbar)]$

   2. Calculate $\widetilde{\psi}_m$ from $\psi_n$ using the FFT.

   3. Compute a full-step in $k$:
      $\widetilde{\psi}\_m \longleftarrow \widetilde{\psi}\_m
      \exp[-i \hbar (k \cdot k) \Delta t / (2 m)]$

   4. Calculate $\psi_n$ from $\widetilde{\psi}_m$ using the inverse FFT.

   5. Compute a second half-step in $x$:
      $\psi_n \longleftarrow \psi_n
       \exp[-i (\Delta t / 2)(V_n / \hbar)]$

4. Repeat step 3 until the desired time is reached.

Note that we have split the $x$-space time-step into two half-steps: this
turns out to lead to a more stable numerical solution than performing
the step all at once. Those familiar with numerical integration
algorithms may recognize this as an example of the
well-known leap-frog integration technique.

To test this out, I've written a python code which sets up a particle in a
box with a potential barrier.  The barrier is high enough that a classical
particle would be unable to penetrate it.  A quantum particle, however, can
"tunnel" through, leading to a non-zero probability of finding the particle
on the other side of the partition.  This quantum tunneling effect lies at
the core of technologies as diverse as electron microsopy, semiconding diodes,
and perhaps even the future of low-powered transistors.

The animation of the result is below (for a brief introduction to the animation
capabilities of python, see
[this post](/blog/2012/08/18/matplotlib-animation-tutorial/)).
The top panel shows the position-space wave function, while the bottom panel
shows the momentum-space wave function.

{% video /downloads/videos/schrodinger_barrier.mp4 360 270 /downloads/videos/schrodinger_barrier_frame.png %}

Notice that the height of the potential barrier (denoted by the dashed line in
the bottom panel) is far larger than the energy of the particle.  Still, due
to quantum effects, a small part of the wave function is able to tunnel through
the barrier and reach the other side.

The python code used to generate this animation is included below.  It's pretty
long, but I've tried to comment extensively to make the algorithm more clear.
If you're so inclined, you might try running the example and adjusting the
potential or the input wave function to see the effect on the dynamics of
the quantum system.

{% include_code schrodinger.py Schrodinger %}

*Edit: I changed the legend font properties to play nicely with older
 matplotlib versions.  Thanks to Yann for pointing it out.*