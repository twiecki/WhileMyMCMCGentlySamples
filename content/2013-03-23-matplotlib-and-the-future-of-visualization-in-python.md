Title: Matplotlib and the Future of Visualization in Python
date: 2013-03-23 08:31
comments: true

<!-- PELICAN_BEGIN_SUMMARY -->
Last week, I had the privilege of attending and speaking at the
PyCon and PyData conferences in Santa Clara, CA.  As usual, there were some
amazing and inspiring talks throughout: I would highly recommend browsing
through the videos as they are put up on
[pyvideo](http://pyvideo.org/category/33/pycon-us-2013).

One thing I spent a lot of time thinking, talking, and learning about
during these two conferences was the topic of data visualization in Python.
Data visualization seemed to be everywhere: PyData had
[two](http://sv2013.pydata.org/abstracts/#11)
[tutorials](http://sv2013.pydata.org/abstracts/#15)
on matplotlib (the second given by yours truly), as well as a talk about
[NodeBox OpenGL](http://sv2013.pydata.org/abstracts/#41) and a
[keynote](http://sv2013.pydata.org/keynotes/#abstract_33) by
Fernando Perez about IPython, including the notebook and the
nice interactive data-visualization it allows. Pycon had a tutorial on
[network visualization](https://us.pycon.org/2013/schedule/presentation/29/),
a talk on [generating art](https://us.pycon.org/2013/schedule/presentation/58/)
in Python, and a talk on
[visualizing Github](https://us.pycon.org/2013/schedule/presentation/108/). 

<!-- PELICAN_END_SUMMARY --> 

The latter of these I found to be a bit abstract -- more discussion of visual
design principles than particular tools or results -- but contained one
interesting nugget: though D3 is the current state-of-the-art for
publication-quality online, interactive visualization, practitioners often
use simpler tools like matplotlib or ggplot for their initial data exploration.
This was a thought echoed by Lynn Cherny in her presentation about NodeBox
OpenGL: it has some really nice features which allow the creation of beautiful,
flexible, and interactive graphics within Python.  But if you just want to
scatter-plot x versus y to see what your data looks like, matplotlib might
be a better option.

I found Lynn’s talk incredibly interesting, and not just because of the
good-natured heckling I received from the stage!  Her main point was that
in the case of interactive & animated visualization, matplotlib is relatively
limited.  She introduced us to a project called
[NodeBox OpenGL](http://www.cityinabottle.org/nodebox/), which is a
cross-platform graphics creation package that has some nice Python bindings,
and can create some absolutely beautiful graphics.  This is one example of a
physics flow visualization, taken from the above website:

{% img center /downloads/images/nodebox-physics-flock.jpg 'NodeBox OpenGL visualization' %}

Despite Lynn’s admission that, with regards to the limitations of matplotlib,
I had taken a bit of the wind out of her sails with my interactive matplotlib
tutorial the day before (in which many of the examples I used will be familiar
to readers of this blog), I think her point on the limitations of matplotlib
is very well-put.  Though it remains my tool of choice for data visualization
and the creation of publication-quality scientific graphics, matplotlib is
also a decade-old platform, and sometimes shows its age.

## Matplotlib’s History ##

Matplotlib is a multi-platform data visualization tool built upon the Numpy
and Scipy framework.  It was conceived by John Hunter in 2002, originally as
a patch to IPython to enable interactive MatLab-style plotting via gnuplot
from the IPython command-line.  Fernando Perez was, at the time, scrambling
to finish his PhD, and let John know he wouldn’t have time to review the patch
for several months.  John took this as a cue to set out on his own, and the
matplotlib package was born, with version 0.1 released in 2003.  It received
an early boost when it was adopted as the plotting package of choice of the
Space Telescope Science Institute, which financially supported matplotlib’s
development and led to greatly expanded capabilities.

One of matplotlib’s most important features is its ability to play well with
many operating systems and graphics backends. John Hunter highlighted this
fact in a keynote talk he gave last summer, shortly before his sudden and
tragic passing ([video link](http://pyvideo.org/video/1192/matplotlib-lessons-from-middle-age-or-how-you)):
“We didn’t try to be the best in the beginning, we just tried to be *there*...”
and fill-in the features as needed.  In this talk, John outlined the reasons
he thinks matplotlib succeeded in outlasting the dozens of competing packages:

- it could be used on any operating system via its array of backends
- it had a familiar interface: one similar to MatLab
- it had a coherent vision: to do 2D graphics, and do them well
- it found early institutional support, from astronomers at STScI and JPL
- it had an outspoken advocate in Hunter himself, who enthusiastically
  promoted the project within the Python world

## Matplotlib’s Challenge ##

This cross-platform, everything-to-everyone approach has been one of the great
strengths of matplotlib.  It has led to a large user-base, which in turn
has led to an active developer base and matplotlib’s powerful tools and
ubiquity within the scientific Python world.  But as the
world of graphics visualization has changed, this strength has started to
become matplotlib’s main weakness.  The hooks into multiple backends work
well for static images, but can be cumbersome and unpredictable for more
dynamic, interactive plots (for example, the animation toolkit still does
not work with the MacOSX backend, and this is
[unlikely to improve](https://github.com/matplotlib/matplotlib/issues/531)
any time soon).

Contrast this with one of the other great success stories in the scientific
Python world, the IPython Notebook.  It brings powerful, interactive computing
tools to the fingertips of the user, and works well across all platforms.
The IPython team, rather than spending time creating backend hooks for all
possible graphics toolkits, built the notebook to work in the browser,
effectively outsourcing the cross-platform compatibility problem to browser
providers.  This decision, I believe, is a fundamental piece which enabled
IPython notebook to become so widely adopted during its short existence.
The developers have been freed to spend their time implementing features,
rather than struggling with cross-platform compatibility.  Drawing from this
lesson, I would venture to predict that whichever graphics package is the
community standard five years from now will have adopted this approach as well.

The matplotlib developers, of course, know this very well.  In his SciPy 2012
keynote mentioned above, John Hunter talked about lessons learned from ten
years of growing matplotlib, the challenges matplotlib faces, and the path
toward the future.  Prominently mentioned among the challenges was the fact
that users have come to expect dynamic, interactive, client-side graphics
rendering seen in popular tools like Protovis and D3.  Further, they’ve come
to value and desire graphical tools which fit naturally in the research flow
enabled by the IPython notebook (just look at the spontaneous applause Fernando
received when showing off the IPython notebook/D3 integration in his
[PyCon Canada keynote](http://www.youtube.com/watch?feature=player_embedded&v=F4rFuIb1Ie4)

I would add one more challenge to that: even simple, static 2D visualization
concepts have come a long way since gnuplot and the advent of matplotlib:
in particular,
[The Grammar of Graphics](http://www.amazon.com/Grammar-Graphics-Statistics-Computing/dp/0387245448)
has helped evolve views on best practices for exploratory data visualization.
The ggplot integraion in R is one feature that users cite as a clear advantage
over Python.  Yes, matplotlib is powerful enough to allow implemention of
[some of these ideas](http://messymind.net/2012/07/making-matplotlib-look-like-ggplot/),
but its plotting commands remain rather verbose, and its no-frills, default
output looks much more like Excel circa 1993 than ggplot circa 2013. 
(for a quick look at Grammar of Graphics in a Python context, see Peter Wang’s
[Bokeh talk](http://pyvideo.org/video/1224/bokeh-an-extensible-implementation-of-the-gramma) from Scipy 2012).

## The Future of Visualization in Python ##

Looking toward the future, these are significant challenges for matplotlib.
I have no doubt that with a healthy effort from the development community,
along with a good dose of vision and leadership, matplotlib could adapt and
remain the leading visualization package in Python.  But there are challengers:
[NodeBox OpenGL](http://www.cityinabottle.org/nodebox/) solves some of the
interactivity problems by providing a powerful interface on a single,
universally available graphics backend.
Packages like [Chaco](http://code.enthought.com/chaco/) and
[MayaVi](http://code.enthought.com/projects/mayavi/) push the boundaries in
interaction, extensibility, and 3D capabilities. But all three of these
options are still married to the old server-side paradigm of tools like
matplotlib and gnuplot rather than the client-side paradigm of tools like
IPython notebook, Protovis, and D3.

A more exciting option right now, in my view, is
[Bokeh](https://github.com/continuumio/bokeh), a project of Peter Wang,
Hugo Shi, and others at Continuum Analytics.  Bokeh is an effort to create
a ggplot-inspired graphics package in Python which can produce beautiful,
dynamic data visualizations in the web browser.  Though Bokeh is young and
still missing a lot of features, I think it’s well-poised to address the
challenges mentioned above.  In particular, it’s explicitly built around the
ideas of Grammar of Graphics.  It is being designed toward a client-side,
in-browser javascript backend to enable the sharing of interactive graphics,
*a la* D3 and Protovis.  And comparing to matplotlib’s success story, Bokeh
displays many parallels:

- Just as matplotlib achieves cross-platform ubiquity using the old model of
  multiple backends, Bokeh achieves cross-platform ubiquity through IPython’s
  new model of in-browser, client-side rendering.
- Just as matplotlib uses a syntax familiar to MatLab users, Bokeh uses a
  syntax familiar to R/ggplot users
- Just as matplotlib had a coherent vision of focusing on 2D cross-platform
  graphics, Bokeh has a coherent vision of building a ggplot-inspired,
  in-browser interactive visualization tool
- Just as matplotlib found institutional support from STScI and JPL, Bokeh
  has institutional support from Continuum Analytics and the recent $3 million
  [DARPA XDATA grant](http://continuum.io/press/continuum-receives-darpa-xdata-funding).
- Just as matplotlib had John Hunter’s vision and enthusiastic advocacy,
  Bokeh has the same from Peter Wang.  Anyone who has met Peter will know
  that once you get him talking about projects he’s excited about, it’s hard
  to make him stop!

Above all that, Bokeh, like matplotlib, is entirely open-sourced.  Now, I
should make clear that Bokeh still has a long way to go.  Its installation
instructions & examples are still a bit incomplete and opaque.  It currently
provides no way of outputting PNG or PDF versions of the graphics it produces.
Many of its goals still lie more firmly in the realm of vision than in the
realm of implementation. But for the reasons I gave above, I think it’s
a project to keep watching.

And where does that leave matplotlib?  I would not, by any means, discount
it just yet.
Still, as John Hunter noted last summer, it faces some significant challenges,
particularly in the area of client-rendered, dynamic visualizations.  Any
core matplotlib developers reading this should go back and re-watch John’s
SciPy keynote: it was his last public outline of his vision for the project
he started and led over the course of a decade.  An IPython
notebook-compatible client-side matplotlib viewer along the lines of the
ideas John mentioned at the end of his talk would be the killer app
that would, in all likelihood, allow matlotlib to maintain its position
as the *de facto*
standard visualization package for the Scientific Python community.

And all that being said, regardless of what the future brings, you can be
assured that in the meantime I and many others will still be doing all our
daily work and research using matplotlib. Despite its weaknesses and the
challenges it faces, matplotlib is a powerful tool, and I don’t anticipate
it withering away any time soon.
