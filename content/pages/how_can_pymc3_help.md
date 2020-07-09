Title: How can PyMC3 help me?

[PyMC3](https://docs.pymc.io) allows you to solve data science problems of varying complexity that you can hardly solve any other way. The tool is highly versatile and is being used successfully by various companies. For example, SpaceX used PyMC3 to optimize its supply chains (as explained in [this blog post](https://twiecki.io/blog/2019/01/14/supply_chain/)). But it's also being used to [find planets outside of our solar-system](https://github.com/exoplanet-dev/exoplanet), [detect earthquakes](https://github.com/hvasbath/beat), or [estimate the spread of COVID-19 on rt.live](https://rt.live/).

PyMC3 allows you to easily build Bayesian statistical models in Python. A central benefit of Bayesian statistics is the *quantification of uncertainty*. Whenever you make business decisions you need to take uncertainty into account or you end up making suboptimal decisions based on the most likely outcome, rather than *the best decision taking all possible outcomes into account*.

Another benefit of probabilistic programming is that it allows you to incorporate the structure of your data into the model directly. This is different from machine learning which tries to infer all structure from large amounts of training data. PyMC3 on the other hand allows you to incorporate any knowledge you might have about your problem into your model directly which allows you to make better inference with fewer data or solve problems for which machine learning is not a good fit. For example, many data sets have a nested or hierarchical structure that is impossible to map adequately in a machine learning algorithm, but is [very naturally supported by PyMC3](https://twiecki.io/blog/2014/03/17/bayesian-glms-3/).

Finally, if you struggle with having your data science models have any actual business impact it's likely that you are solving the wrong problem: rather than have a model make predictions or forecasts, you want to push the model outputs all the way through to the actual decision you want to make. For more information, see [my post on Bayesian decision making to optimmize supply chains](https://twiecki.io/blog/2019/01/14/supply_chain/).

## An Intuitive Guide to Bayesian Statistics

I'm currently preparing an [online course to teach Bayesian statistics](https://twiecki.io/pages/an-intuitive-guide-to-bayesian-statistics.html) with a focus on building strong intuitions rather than a heavy focus on math. 

## Consulting

If you already use PyMC3 in your organization or think the problem you are facing would be a good fit for this tool, [I would love to hear from you](mailto:thomas.wiecki@gmail.com). 

I have developed Bayesian models that are widely used, like [HDDM](http://ski.clps.brown.edu/hddm_docs/) which is a tool used by research labs around the world to study decision making. With Adrian Seyboldt I also developed [BayesAlpha](https://www.github.com/quantopian/bayesalpha), a tool for portfolio optimization we used to great success at [Quantopian](https://www.quantopian.com).

Together with other PyMC3 core developers we form a worldclass team of Bayesian modelers.

## Corporate Workshops

Together with [Chris Fonnesbeck](https://twitter.com/fonnesbeck) I provide corporate training workshops for probabilistic programming and Bayesian statistics. 

Empower your data science team to solve problems in a new way. [Email me](mailto:thomas.wiecki@gmail.com) if you are interested.