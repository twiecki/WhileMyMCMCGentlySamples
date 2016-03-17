Title: Will Scientists Ever Move to Python 3?
date: 2013-01-03 17:08
comments: true
slug: will-scientists-ever-move-to-python-3

<!-- PELICAN_BEGIN_SUMMARY -->
*March 2016: Please note the date on this post. Given the developments in the last three years, I would no longer agree with much of what I've written here. In particular, I substantially underestimated the ability of tools like [six](http://pythonhosted.org/six/) and [python-future](http://python-future.org/) to enable single-codebase Python 2/3 support, and virtually all scientific packages now use such tools to support both. Short version: just use Python 3. There's almost no reason not to any more.*

It's been just over four years since the introduction of Python 3, and there
are still about as many opinions on it as there are Python users.  For
those who haven't been following, Python 3 is a release
which offers several nice improvements over the 2.x series
(summarized [here](http://docs.python.org/3/whatsnew/3.0.html))
with the distinct disadvantage that it broke backward compatibility:
though Python 3.x (often referred to as "Py3k" for short)
is true to the spirit of earlier Python versions,
there are a few valid 2.x constructions which will not parse under 3.x.

Breaking backward compatibility was controversial, to say the least.  I
think of the debate as one between the pragmatists -- those who see Python
as an extremely useful tool, which should not be unnecessarily tampered with --
and the idealists -- those who view the Python language
as a living, breathing entity, which should be allowed to grow into the
fullest and most Pythonic possible version of itself.

<!-- PELICAN_END_SUMMARY -->

The scientific Python community has largely leaned to the pragmatist side.  Some
of this is due to the pragmatism inherent to science (in the publish-or-perish
world, one does not often have time for idealistic thinking about one's tools),
and some of this is due to institutional pressures, which I'll mention below.
But regardless of the cause, the scientific Python community has been
particularly slow in moving to Py3k.  [Numpy](http://www.numpy.org), the
core of the scientific Python ecosystem, first supported Py3k in version
1.5, released in 2010, nearly two years after the release of Py3k.
[Scipy](http://www.scipy.org) followed suit with version 0.9
in March 2011.  [IPython](http://www.ipython.org) added Py3k support
with version 0.12 in December 2011.  The final holdout among
the core scientific packages was matplotlib, which now supports Py3k in the
1.2 release as of November 2012.

The casual observer might look at this progress
and infer that the transition is near
complete: scientists can now start moving to Py3k without fear of losing
access to the tools of their trade.  But in reality, nothing could be further
from the truth.  Consider that the Numpy and Scipy development teams only
last month made the decision to drop support for Python 2.4 (which was first
released in March of 2005).  Even then, there has been considerable talk of how
to make sure the final 2.4-compatible release is long-term-stable for those
users who will use 2.4 well into the future (many institutional Linux
distributions, such as Red Hat Linux, are very slow to update their
native Python version).
All else being equal, we might extrapolate and say that support for Python 2.7
(first released in July 2010) might be dropped by mid 2018.  But this would
be an overly simplistic expectation, for reasons I'll outline below.
There's a vital component of this transition that I haven't yet heard
mentioned by anyone else:
I would argue that the main limitation to the adoption of Python 3
by the scientific community lies in *the lack of a well-developed 3-to-2
conversion tool*.  I'll explain this thought below.

## The Types of Users ###

To begin to evaluate what it will take for the
scientific community to transition to
Python 3, I'd like to divide members of the community into three general
categories.  These are certainly not mutually exclusive (I fall pretty
squarely in all three), but the categories will
help us think about the forces involved in the
decision to switch to Py3k.  The groups are as follows:

- **Individual Scientists** are the researchers who primarily use
  Python for their own individual tasks: statistical analysis of their data,
  creation of figures, and writing scripts to stitch together various legacy
  codes.

- **Institutional Scientists** are the researchers who are part of a large
  research team or collaboration with a common Python code-base.  An example
  that I personally am
  familiar with is the [LSST](http://www.lsst.org) collaboration:
  the LSST software stack has been developed by a large team over the course
  of several years, and is written primarily in C++ and Python 2.x.

- **Scientific Python Developers**
  are the scientists who may be part of one or both of the above groups,
  but also go the extra mile and contribute to the packages that
  make the scientific Python ecosystem what it is.  I wouldn't limit this to
  just the NumPy/SciPy/IPython/Matplotlib packages mentioned above, but also
  the expanding circle of packages geared toward specific fields and
  applications.

Members of these three groups have very different needs and constraints that
will affect how easily they can move to Py3k:

### Individual Scientists ###
This group is probably the most flexible of the three, and for that reason
are perhaps the lowest-hanging fruit of the bunch.
Free from the constraints of a large legacy
code-base, they can adopt Py3k virtually at-will.  I witnessed
a similar transition take place
over the course of my graduate schooling at University of Washington: at the
beginning of my PhD program, nearly everybody in the department was
using the proprietary language [IDL](http://www.exelisvis.com/idl/).
By the time I graduated,
close to half the department was primarily using Python.

As much as I'd like
to take some of the credit for that transition (I was a tireless proseletizer
of the virtues of Python over IDL),
it likely had more to do with the adoption of
Python by several important astronomical research collaborations, as well
as the influence of several newer professors who recommended Python to
their advisees.  This points to the fact that
although an individual could easily upgrade to Py3k virtually at
will, in practice it is unlikely to happen unless others around them have
begun to do so as well.

### Institutional Scientists ###
As hinted above, even the most independent scientists are not entirely
insulated from their colleagues, and the tools chosen by influential
members of their team will affect their choice of tools for their own tasks.
But aside from this peer pressure, scientists who are part of a large
collaboration are additionally constrained by the countless hours
already invested in their present code-base. And if that code-base is
in Python 2.x, it will take a lot more than some unicode and iterator
enhancements to effect a transition to Python 3.

Because of this, I've seen a lot of incredulity (and even some
anger) about the decision of the Python core devs to move forward with a
backward-incompatible release.  In a conversation, one Princeton
astrophysicist I know (who is famous for -- among other things --
the brashness of his opining) called
the py3k release "utterly inane", and went on to say that astronomy will
*never* adopt Python 3.  I'm a bit more optimistic myself, but this is
indicative of the general attitude toward Py3k within the scientific
community.

### Scientific Python Developers ###
Those scientists who take the time to contribute to the greater community are
a bit of a special case.  They tend to be less pragmatic about Python than
their peers, and may have some silly hobbies (like using their free time
to write blog posts with "Python" in the title).
They are generally comfortable using multiple Python installs
on each of their several computers, and as such are less influenced by the
preferences of whatever research group they may be in at the time.
Yet even this group is unlikely to be using Python 3.x currently.
It might be because Matplotlib -- a core scientific tool -- only just moved
to Py3k compatibility, but I think it's even deeper than that.  I, for one,
did not jump up to make the switch the minute the matplotlib 1.2 announcement
came out, and I doubt that others did either.

The core of the problem is this: even though NumPy/SciPy/IPython/Matplotlib
are compatible with Py3k, the *development* still takes place in Python 2.x.
The Py3k compatibility is bootstrapped in using
[2to3](http://wiki.python.org/moin/2to3)
and other scripts of that ilk.  And herein lies the problem:
absent another compelling reason, as long as the development takes place
in Python 2.x, these developers will be very unlikely to move
their own work to Py3k.

## The Outlook ##
Exploring the needs and drivers of these three groups paints a pretty dim
picture for Py3k in the scientific world.
Individuals have no pressure to switch, and
collaborations become so entrenched that switching is near impossible.
Even those who are actively contributing to the Numpy and Scipy codebases
cannot use Python 3 for this task, and thus have no big driver for change.
This final piece holds perhaps the biggest opportunity,
because the Scientific Python developers have the potential
to catalyze change in the rest of the community: these are the folks who write
the online Python documentation and tutorials; they give talks and tutorials
at [SciPy](http://conference.scipy.org/), [PyData](http://www.pydata.org),
[PyCon](http://www.pycon.org),
and conferences specific to their own field; they influence the
curricula used in Python bootcamps like those facilitated by
[Software Carpentry](http://software-carpentry.org/).  In short, perhaps the
sole hope of moving the scientific community to Python 3 lies in the
scientific python developers.  Move the *development* of Numpy, Scipy, IPython,
Matplotlib, and other core packages to Python 3, and the rest of the
community will follow.

The problem is, this is impossible right now.  Realistically, Python 2.x will
have to be supported by Numpy and Scipy for at least another decade.
If Numpy & Scipy development is to be moved to Py3k, what is needed is a
fully-developed, mature 3-to-2 conversion tool which can convert 3.x back as
far as Python 2.5.  With this, development could continue in Py3k while still
maintaining 2.x support.  A basic form of such a tool
[is available](http://wiki.python.org/moin/3to2), but it is not nearly
as mature (nor as easy a task)
as the [2to3](http://wiki.python.org/moin/2to3) tool.
The tool's relative immaturity
is understandable: converting the new to the old is not nearly as sexy as
converting the old to the new.  But for the reasons I outlined above, I
believe it to be vital.

So here's my challenge to any Python idealists out there:
*if you want the scientific community to ever fully adopt Python 3,
prioritize the development of a full-featured 3to2 tool,
and start doing all you can to encourage NumPy to move to
developing in Py3k*.  I'd do it myself, but I'm too much of
a pragmatist: python 2.7 is more than sufficient for my own research.
But I'd be willing to bet -- if someone does this, the rest of us will
soon follow.