Title: Introducing PyMC Labs: Saving the World with Bayesian Modeling
date: 2021-02-23 10:00
comments: true
draft: true
slug: intro_pymc_labs

After I left Quantopian in 2020, something interesting happened: various companies contacted me inquiring about
consulting to help them with their PyMC3 models.

Usually, I don't hear how people are using [PyMC3](https://docs.pymc.io/) -- they mostly show up on
[GitHub](https://github.com/pymc-devs/pymc3) or [Discourse](https://discourse.pymc.io/) when something isn't working
right. So, hearing about all these really cool projects was quite exciting. However, I couldn't possibly take all of
these projects on by myself.

Thus, it was time to assemble a team of the most badass Bayesian modelers the world had ever seen -- the Bayesian
Avengers, if you will. Fortunately, I did not have to venture far, as PyMC3 had already attracted exactly these types
of people.

<div class="text-center py-5">
    <iframe src="https://giphy.com/embed/5cZbRBLhW4tc4" width="480" height="257"
    frameBorder="0" class="giphy-embed" allowFullScreen></iframe>
</div>

This brings me to the Big Announcement: For the last few months, we have quietly been building
[PyMC Labs](https://pymc-labs.io), a Bayesian modeling consultancy.
[We have an amazing team](https://www.pymc-labs.io/team/) consisting of three neuroscience PhDs, mathematicians,
social scientists, a SpaceX rocket scientist, and the host of the famous
[‘Learning Bayesian Statistics’ podcast](https://www.learnbayesstats.com/). All of us are united in our mission:

<blockquote class="blockquote text-center">
    <p class="mb-0">Saving the world with Bayesian modeling</p>
    <footer class="blockquote-footer">Someone famous who 💙 Bayesian stats</footer>
</blockquote>

Does this sound a bit grandiose? Probably. Is this true? I firmly believe it is. There are so many important problems
the world faces today -- from climate change to COVID19, from education to poverty -- and Bayesian modeling can play a
critical role in solving these problems. Let me explain why.

## It is already doing it

I would not have imagined it when I started contributing to PyMC, but the science PyMC3 has directly enabled ranges
from [climate science](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=pymc3+climate&btnG=) and biology to
astronomy and zoology, and everything in between.

For instance, it was used to predict the spread of COVID19 in a recent
[Science paper](https://science.sciencemag.org/content/369/6500/eabb9789.full),
as well as [track the reproduction factor in real-time](https://rtlive.de/global.html).
In both cases, the benefit of PyMC3 was its ease-of-use and the ability to integrate scientific domain knowledge and
get honest uncertainty estimation in a highly volatile and uncertain situation.

Now I know you’re very observant and I hear you thinking: “wait a minute, those benefits of Bayesian modeling sound
quite general, so why would they be only valid for epidemiology?”. And indeed they aren’t! For similar benefits,
PyMC3 is also used to [find planets outside of our solar system](https://github.com/exoplanet-dev/exoplanet)
and [detect earthquakes](https://github.com/hvasbath/beat). One of my coworkers here at PyMC Labs uses it for
[electoral and political forecasting](https://share.streamlit.io/alexandorra/pollsposition_website/main/gp-popularity-app.py),
because polls are noisy, scarce and need to be completed by domain knowledge -- one of the perfect settings for
Bayesian inference!

With all of this, at the time of writing, the [PyMC3 paper](https://peerj.com/articles/cs-55/) has been cited over 930
times and is in the top 10 most cited articles of the entire PeerJ journal.

## Solving Business Problems

Beyond scientific research, I find that PyMC3 is the perfect tool to also solve various business problems.
And indeed it’s already successfully used in production at companies as big and diverse as SpaceX, Roche,
Netflix, Deliveroo and HelloFresh.

This diversity means that the [PyMC Labs team intervenes](https://www.pymc-labs.io/clients/) to, for instance,
[build complex models from the latest finance research](https://support.everysk.com/hc/en-us/articles/1500001040721-Private-Investments);
optimize supply chains for food delivery; build software from top to bottom for pharmaceutical applications;
speed up and extend models for the farm tech industry; train and enhance any data science team’s Bayesian stats
capacities, etc.

## Prediction vs Inference

As data science has exploded in the last decade I have always been surprised by the over-emphasis on prediction-focused
machine learning. For far too long, it has been hailed as the solution to most of our data science problems.

I believe that the potential of this is way overblown. Not because it doesn't work -- algorithms like deep nets or
random forests are extremely powerful at extracting non-linear predictive patterns from large data sets -- but rather
because most data science problems are not simple _prediction_ but rather _inference_ problems.

In addition, we often already have a lot of knowledge about our problem: knowledge of certain structure in our data
set (like nested data, that some variables relate to some but not other parameters) and knowledge of which range of
values we expect certain parameters of our model to fall into. Prediction-focused ML does not allow us to include any
of this information, that's why it requires so much data.

With Bayesian statistics, we don't have to learn everything from data as we translate this knowledge into a custom model.
Thus, rather than changing our problem to fit the solution, as is common with ML, we can tailor the solution to best
solve the problem at hand. I like to compare this with Playmobil vs Lego:

![](https://www.pymc-labs.io/blog-posts/saving-the-world/playlego.jpeg)

Playmobil just gives you a single toy you can't change while Lego (i.e Bayes here) gives you building blocks to build
the toy you actually want. In Bayesian modeling, these building blocks are probability distributions.

But how do you do this in practice? This is where PyMC3 comes in, as it allows you to specify your models as Python
code and automatically estimate it without requiring manual mathematical derivations. Due to recent theoretical and
technological advances, this also runs quickly and scales to complex models on large(ish) data sets.

## Serving our mission

So how do we best make progress on our mission?

First, we will continue to make PyMC3 the best, most user-friendly and scalable Bayesian modeling package out there.
We are well set up to do this, having a friendly API, a huge user-base, and a large developer team of over 20 active
members. With our renewed focus on
[PyMC3 on Theano with a JAX backend](https://pymc-devs.medium.com/the-future-of-pymc3-or-theano-is-dead-long-live-theano-d8005f8a0e9b)
all our resources will go towards this goal.

Second, our new PyMC consultancy will support this endeavour. It allows us to directly help clients use these powerful,
customizable methods to solve their business problems, thereby increasing adoption and recognition.
As a great side effect, these client projects also help us find things that need to be fixed, improved or optimized
in PyMC3, thereby lifting all (Bayesian) boats instead of just the happy fews’.

So far, this has been an incredibly rewarding and exhilarating journey. Even though it is still early, we are learning
a lot about which areas Bayesian modeling is particularly well suited for but also what would make PyMC3 even better.
Without spoiling a future blog post that will go into more detail about what we have learned applying these methods,
the best use-cases include (but aren’t limited to) **incorporating domain knowledge, building bespoke models and
quantifying uncertainty around estimates**.

_Sounds familiar? If you or your company has a problem for which prediction-based ML is not a good fit, I'd love to talk
to you at <a href="mailto:thomas.wiecki@pymc-labs.io">thomas.wiecki@pymc-labs.io</a>. This is just the beginning and
I hope you will join us on this marvelous journey._
