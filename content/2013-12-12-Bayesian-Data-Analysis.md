Title: Bayesian Data Analysis with PyMC3
date: 2013-12-12 07:00
comments: true
slug: bayesian-data-analysis-pymc3
tags: bayesian statistics

I recently gave a talk at [PyData NYC 2013](http://pydata.org/nyc2013/) about Bayesian Data Analysis. See below for the video.

I also wrote a related blog post over at [Quantopian](https://www.quantopian.com), called:
[Probabilistic Programming in Quantitative Finance](http://blog.quantopian.com/probabilistic-programming-quant-finance/).

<iframe src="//player.vimeo.com/video/79518830" width="500" height="281" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe> <p><a href="http://vimeo.com/79518830">Bayesian Data Analysis with PyMC3 - Thomas Wiecki</a> from <a href="http://vimeo.com/pydata">PyData</a> on <a href="https://vimeo.com">Vimeo</a>.</p>

Links to the content:

* [IPython Notebook used during the talk](http://nbviewer.ipython.org/github/twiecki/pymc3_talk/blob/master/bayesian_pymc3.ipynb)
* [The reveal slide show](https://rawgithub.com/twiecki/pymc3_talk/master/bayesian_pymc3.slides.html)
* [GitHub repo of materials](https://github.com/twiecki/pymc3_talk)
* [PyMC repo](https://github.com/pymc-devs/pymc)

Abstract
--------

Probabilistic Programming allows flexible specification of statistical models to gain insight from data. Estimation of best fitting parameter values, as well as uncertainty in these estimations, can be automated by sampling algorithms like Markov chain Monte Carlo (MCMC). The high interpretability and flexibility of this approach has lead to a huge paradigm shift in scientific fields ranging from Cognitive Science to Data Science and Quantitative Finance.

PyMC3 is a new Python module that features next generation sampling algorithms and an intuitive model specification syntax. The whole code base is written in pure Python and Just-in-time compiled via Theano for speed.

In this talk I will provide an intuitive introduction to Bayesian statistics and how probabilistic models can be specified and estimated using PyMC3.
