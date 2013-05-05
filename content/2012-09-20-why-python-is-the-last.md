Title: Why Python is the Last Language You'll Have To Learn
date: 2012-09-20 20:50
comments: true

<!-- PELICAN_BEGIN_SUMMARY -->
This week, for part of a textbook I'm helping to write,
I spent some time reading and researching the history of Python as
a scientific computing tool.  I had heard bits and pieces of this in the past,
but it was fascinating to put it all together and learn about how all the
individual contributions that have made Python what it is today.
All of this got me thinking: for most of us, Python was a replacement for
something: IDL, MatLab, Java, Mathematica, Perl... you name it.
But what will replace Python?
Ten years down the road, what language will people be espousing in
blogs with awkwardly-alliterated titles?  As I thought it through, I
became more and more convinced that, at least in the scientific computing
world, Python is here to stay.

<!-- PELICAN_END_SUMMARY -->

Now I’m not simply talking about inertia.  Javascript has inertia, and that's
a main reason that web admins still begrudgingly use it.  But Python is 
different.  Yes, it's everywhere, and yes, something so ubiquitous is
hard to shake.  But look at the 1970s: punch card programming was
everywhere, and now it's nothing but a footnote. Inertia can be overcome
with time.  But I think Python’s hold is much deeper than that: I think it
will remain relevant long into the future.  Here’s why:



## GitHub ##
The first reason Python will be around for a while is
[GitHub](http://github.com).  GitHub has done wonders both for Python
and for the broader open source community. 
It has replaced the clunky Trac system of
submitting static patches to projects, and removed the contribution barrier
for the core scientific python projects.  Numpy, Scipy, and Matplotlib were
all moved to GitHub in late 2010, and the results have been impressive.
I did some quick data mining of the commit logs on GitHub to learn
about the rate of new author contributions to core python projects with
time, and this is what I found:

{% img /downloads/figures/author_count.png 600 [Cumulative number of contributors for python packages] %}

See it? The late 2010 transition to GitHub is extremely apparent,
and this reflects the first reason that NumPy, SciPy, Matplotlib,
and Python will remain relevant far into the future.
Python not only has an astoundingly large user-base; thanks to GitHub,
it has an astoundingly large and ever-increasing *developer* base.
And that means Python is well-poised to evolve as the needs of users change.



## Julia ##
The second reason Python will be around for a while is 
[Julia](http://julialang.org/).  This statement may strike some as strange:
Julia is a 
language which aims to improve on many of Python’s weaknesses.
It uses JIT compilation and efficient built-in array 
support to beat Python on nearly every benchmark.  It seems a likely 
candidate to *replace* Python, not a support for my assertion that Python will 
remain relevant. But this is the thing: Python’s strength lies in community, 
and that community is incredibly difficult to replicate.

A recent
[thread](https://groups.google.com/forum/?fromgroups=#!topic/julia-dev/YftOOEfcwrk)
on the julia-dev list highlights what I’m talking about:
in it, Dag Seljebotn, a core developer of Cython, contrasts the
strengths of Python (large user- and developer-base, large collection of
libraries) with the strengths of Julia (state-of-the-art performance,
JIT compilation).  He
proposes that the two languages should work together, each drawing from the
strengths of the other.  The response from the Julia community was incredibly
positive.

The Julia developers know that Julia can’t succeed as a scientific
computing platform without building an active community, and currently the
best way to do that is to work hand-in-hand with Python.  After this thread
on julia-dev, the Julia  developers were invited to give 
[a talk](http://pyvideo.org/video/1204/julia-a-fast-dynamic-language-for-technical-comp) 
at the Scipy2012 conference,
and I think many would say that some good bridges were built.
I'm extremely excited about the prospects of Julia as a scientific computing
platform, but it will only succeed if it can embrace Python, and if Python
can embrace it.



## The next Travis Oliphant ##
The third reason Python will be around for a while is this: *there will be 
another Travis Oliphant*.  What do I mean by this?  Well, if you go back 
ten years or so, the Python scientific community was looking a bit weak.
Numeric was a 
well-established array interface, and the beginnings of SciPy were built 
upon it.  But Numeric was clunky, so some folks got together and built 
Numarray.  Numarray fixed some of the problems, but had its own weaknesses.
The biggest problem, though, was that it split the community:
when the core of your platform has divided allegiances, neither side wins.
Travis realized this, and against the advice of many, audaciously set out 
on a quest to unify the two.  The result was NumPy, which is now the 
unrivaled basis for nearly all scientific tools in Python.

Python faces a similar crisis today: it is split in the area of
High-performance and parallel computing.  There is an alphabet soup of 
packages which aim to address this:
Cython, PyPy, Theano, Numba, Numexpr, and more.  But 
here’s the thing: someone *will* come along who has the audacity to strike
out and unify them.  I love this recent
[tweet](http://twitter.com/dwf/status/246756226367643650) by Dave Warde-Farley:

{% img /downloads/images/dwf_tweet.png 400 [Cumulative number of contributors for python packages] %}

Somebody is going to do this: somebody will be the next Travis Oliphant
and create NumTron to re-unite the community.
Maybe Dave will be the next Travis Oliphant: he's done some great work on
[Theano](http://deeplearning.net/software/theano/).
But then again, the merging of Python and LLVM in Travis'
[Numba](http://numba.pydata.org/) project is
[pretty exciting](/blog/2012/08/24/numba-vs-cython/):
maybe Travis Oliphant will be the next Travis Oliphant --
he’s done it before, after all.  Or perhaps it will be someone
we’ve never heard of, who as we speak is brewing a new idea in
an unwatched GitHub repository. Time will tell,
but I’m confident that it will happen.



## Conclusion ##
Maybe I’ve convinced you, maybe I haven’t.  But I’m going to continue using 
Python, and I predict you will too.  We'll see what the future holds for 
scientific computing, but in my mind, Python remains a pretty solid bet.

*Finally, a brief post-script on the history of Python:
some of the most interesting sources I found were
[this interview](http://www.artima.com/intv/pythonP.html) with Guido Van Rossum,
the official [Scipy history page](http://www.scipy.org/History_of_SciPy), the
[Scipy2012 talk](http://pyvideo.org/video/1192/matplotlib-lessons-from-middle-age-or-how-you)
John Hunter gave this summer shortly before his sudden passing,
and the [numpy-discussion post](http://mail.scipy.org/pipermail/numpy-discussion/2012-February/060640.html)
John referenced in his talk.  If you use Python regularly and have some
time, I’d highly recommend browsing these: it’s incredible to see
how the unwavering vision of folks throughout the years has led to what we
have today: an unmatched open-source environment for scientific computing.*

*Edit: also check out the
[History of Python](http://python-history.blogspot.com/) blog.  Thanks to
Fernando for the tip.*