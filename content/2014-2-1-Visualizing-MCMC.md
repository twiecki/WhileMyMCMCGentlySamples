Title: Animating MCMC with PyMC3 and Matplotlib
date: 2014-2-1 09:00
comments: true
slug: visualizing-mcmc
tags: bayesian statistics

Here's the deal: I used [PyMC3](https://github.com/pymc-devs/pymc),
[matplotlib](http://matplotlib.org/), and [Jake Vanderplas'](http://jakevdp.github.io/)
[JSAnimation](https://github.com/jakevdp/JSAnimation) to create
javascript animations of three MCMC sampling algorithms --
[Metropolis-Hastings](https://en.wikipedia.org/wiki/Metropolis%E2%80%93Hastings_algorithm), [slice sampling](https://en.wikipedia.org/wiki/Slice_sampling) and [NUTS](http://arxiv.org/abs/1111.4246).

I like visualizations because they provide a good intuition for how
the samplers work and what problems they can run into.

You can download the full notebook [here](https://rawgithub.com/twiecki/WhileMyMCMCGentlySamples/master/content/downloads/notebooks/sample_animation.ipynb) or [view it in your browser](http://nbviewer.ipython.org/github/twiecki/WhileMyMCMCGentlySamples/blob/master/content/downloads/notebooks/sample_animation.ipynb?create=1). Note that for this post I used
video embedding due to the size of the animations if they are not
compressed. The notebook contains code for both.

The model is a simple linear model as explained in my [previous blog post on Bayesian GLMs](http://twiecki.github.io/blog/2013/08/12/bayesian-glms-1/). Essentially,
I generated some data and estimate `intercept` and `slope`. In the
lower left corner is the *joint* posterior while the plot above shows
the *trace* of the *marginal* posterior of the `intercept` while the
right plot shows the *marginal* posterior trace of the `slope` (think
of these as a ticker that over time tracks one of the two axes). Each
point represents a sample drawn from the posterior. At 3 quarters of the way I added a thousand samples to show that they all sample from the posterior eventually.

As you will see, there is quite some correlation between `intercept`
and `slope` -- if we believe in a higher intercept we must also
believe in a lower slope (which makes geometrical sense if you think
how lines could fit through the point clouds). This often makes it
difficult for the MCMC algorithm to converge (i.e. sample from the
true posterior).

First, lets see how our old-school Metropolis-Hastings (MH)
performs. The code uses matplotlib's handy `FuncAnimation` (see
[here](http://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/)
for a tutorial), my own animation code, and the [recently merged iterative sampling function `iter_sample()`](https://github.com/pymc-devs/pymc/pull/433).

{% notebook sample_animation.ipynb cells[5:6] %}

Unfortunately, not that well. The reason why nothing happens in the
beginning is that MH proposes jumps that are not accepted. PyMC then
tunes the proposal distribution so that smaller jumps are
proposed. These smaller jumps however lead to the random-walk behavior
you can see which makes sampling inefficient.

Lets see how slice sampling fares.

{% notebook sample_animation.ipynb cells[6:7] %}

As you can see, slice sampling does a much better job. For one thing,
there are no rejections (which is a property of the algorithm). But
there's still room for improvement. At the core, slice sampling is a
Gibbs sampling method which means that it always updates one random
variable at a time while keeping all others constant. This property
leads to small steps being taken (imagine trying to move along a
diagonal area on the chess board with Rook) and makes sampling from
correlated posteriors inefficient.

NUTS on the other hand is a newer gradient-based sampler that operates
on the joint posterior. Correlations are not a problem because this
sampler can actually move diagonally as well (more like the Queen). As
you can see, it does a much better job at exploring the posterior and
takes much wider steps.

{% notebook sample_animation.ipynb cells[7:8] %}

Mesmerizing, ain't it?

What surprised me about the slice sampling is that if I looked at the
individual traces (top and right plot) only, I'd say they hadn't
converged. But rather it seems that while the step-size is small,
averaging samples over a longer run should still provide meaningful
inference.

## Where to go from here

I was initially setting out to get real-time plotting while sampling
into PyMC. What I've shown here just creates an animation after
sampling has finished. Unfortunately, I don't think it's currently
possible to so in the IPython Notebook as it requires embedding of
HTML for which we need the finished product. If anyone has an idea
here that might be a very interesting extension.

## Further reading

* [Jake's tutorial on matplotlib animations](http://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/)
* [Jake's blog post on embedding JS animations in the notebook](http://jakevdp.github.io/blog/2013/05/19/a-javascript-viewer-for-matplotlib-animations/)
* [Abe Flaxman's much prettier videos on MCMC](http://healthyalgorithms.com/2011/01/28/mcmc-in-python-pymc-step-methods-and-their-pitfalls/)
  (Would be nice to replace my crappy plotting code with his -- PRs welcome.)