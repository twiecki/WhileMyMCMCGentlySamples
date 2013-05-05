Title: Numba vs Cython
date: 2012-08-24 10:41
comments: true

<!-- PELICAN_BEGIN_SUMMARY -->
Often I'll tell people that I use python for computational analysis, and they
look at me inquisitively.  "Isn't python pretty slow?"  They have a point.
Python is an interpreted language, and as such cannot natively perform
many operations as quickly as a compiled language such as C or Fortran.
There is also the issue of the oft-misunderstood and much-maligned
[GIL](http://wiki.python.org/moin/GlobalInterpreterLock),
which calls into question python's ability to allow true parallel computing.

Many solutions have been proposed: [PyPy](http://pypy.org/) is a much faster
version of the core python language; 
[numexpr](http://code.google.com/p/numexpr/) provides optimized performance
on certain classes of operations from within python;
[weave](http://www.scipy.org/Weave/) allows inline inclusion of compiled
C/C++ code;
[cython](http://www.cython.org/) provides extra markup that allows python
and/or python-like code to be compiled into C for fast operations.  But
a naysayer might point out: many of these "python" solutions in practice
are not really python at all, but clever hacks into Fortran or C.

<!-- PELICAN_END_SUMMARY -->

I personally have no problem with this. I like python because it gives me a nice
work-flow: it has a clean syntax, I don't need to spend my time hunting down
memory errors, it's quick to try-out code snippets, it's easy to wrap legacy
code written in C and Fortran, and I'm much more productive when writing
python vs writing C or C++.  [Numpy](http://numpy.scipy.org),
[scipy](http://www.scipy.org), and [scikit-learn](http://www.scikit-learn.org)
give me optimized routines for most of what I need to do on a daily basis,
and if something more specialized comes up, cython has never failed me.
Nevertheless, the whole setup is a bit clunky:
why can't I have the best of both worlds: a beautiful, scripted, dynamically
typed language like python, with the speed of C or Fortran?

In recent years, new languages like [go](http://golang.org/) and
[julia](http://julialang.org/) have popped up which try to address some of
these issues.  Julia in particular has a number of nice properties (see the
[talk](http://www.youtube.com/watch?v=VCp1jUgVRgE) from Scipy 2012 for a
good introduction) and uses [LLVM](http://llvm.org) to enable just-in-time
(JIT) compilation and achieve some impressive benchmarks.  Julia holds promise,
but I'm not yet ready to abandon the incredible code-base and user-base
of the python community.

Enter [numba](http://numba.pydata.org/).  This is an attempt to bring JIT
compilation cleanly to python, using the LLVM framework.  In a
[recent post](/blog/2012/08/08/memoryview-benchmarks/), one commenter pointed
out numba as an alternative to cython.  I had heard about it before (See
Travis Oliphant's scipy 2012 talk
[here](http://www.youtube.com/watch?v=WYi1cymszqY)) but hadn't had the chance
to try it out until now. Installation is a bit involved, but the directions
on the [numba website](http://numba.pydata.org/) are pretty good.

To test this out, I decided to run some benchmarks using the
pairwise distance function I've explored before (see posts
[here](/blog/2012/08/08/memoryview-benchmarks/)
and [here](/blog/2012/08/16/memoryview-benchmarks-2/)).

### Pure Python Version ###
The pure python version of the function looks like this:
``` python
import numpy as np

def pairwise_python(X, D):
    M = X.shape[0]
    N = X.shape[1]
    for i in range(M):
        for j in range(M):
            d = 0.0
            for k in range(N):
                tmp = X[i, k] - X[j, k]
                d += tmp * tmp
            D[i, j] = np.sqrt(d)
```
Not surprisingly, this is very slow.  For an array consisting of 1000 points
in three dimensions, execution takes over 12 seconds on my machine:
```
In [2]: import numpy as np
In [3]: X = np.random.random((1000, 3))
In [4]: D = np.empty((1000, 1000))
In [5]: %timeit pairwise_python(X, D)
1 loops, best of 3: 12.1 s per loop
```

### Numba Version ###
Once numba is installed, we add only a single line to our above definition
to allow numba to interface our code with LLVM:
```
import numpy as np
from numba import double
from numba.decorators import jit

@jit(arg_types=[double[:,:], double[:,:]])
def pairwise_numba(X, D):
    M = X.shape[0]
    N = X.shape[1]
    for i in range(M):
        for j in range(M):
            d = 0.0
            for k in range(N):
                tmp = X[i, k] - X[j, k]
                d += tmp * tmp
            D[i, j] = np.sqrt(d)
```
I should emphasize that this is the *exact same* code, except for numba's
`jit` decorator.  The results are pretty astonishing:
```
In [2]: import numpy as np
In [3]: X = np.random.random((1000, 3))
In [4]: D = np.empty((1000, 1000))
In [5]: %timeit pairwise_numba(X, D)
100 loops, best of 3: 15.5 ms per loop
```
This is a three order-of-magnitude speedup, simply by adding a numba
decorator!

### Cython Version ###
For completeness, let's do the same thing in cython.  Cython
takes a bit more than just some decorators: there are also type specifiers
and other imports required.  Additionally, we'll use the `sqrt` function
from the C math library rather than from numpy.  Here's the code:
``` cython
cimport cython
from libc.math cimport sqrt

@cython.boundscheck(False)
@cython.wraparound(False)
def pairwise_cython(double[:, ::1] X, double[:, ::1] D):
    cdef int M = X.shape[0]
    cdef int N = X.shape[1]
    cdef double tmp, d
    for i in range(M):
        for j in range(M):
            d = 0.0
            for k in range(N):
                tmp = X[i, k] - X[j, k]
                d += tmp * tmp
            D[i, j] = sqrt(d)
```
Running this shows about a 30% speedup over numba:
```
In [2]: import numpy as np
In [3]: X = np.random.random((1000, 3))
In [4]: D = np.empty((1000, 1000))
In [5]: %timeit pairwise_numba(X, D)
100 loops, best of 3: 9.86 ms per loop
```

### The Takeaway ###
So numba is 1000 times faster than a pure python implementation, and only
marginally slower than nearly identical cython code.
There are some caveats here: first of all, I have years of experience with
cython, and only an hour's experience with numba.  I've used every optimization
I know for the cython version, and just the basic vanilla syntax for numba.
There are likely ways to tweak the numba version to make it even faster,
as indicated in the comments of
[this post](/blog/2012/08/08/memoryview-benchmarks/).

All in all, I should say I'm very impressed.  Using numba, I added
just a *single line* to the original python code, and
was able to attain speeds competetive with a highly-optimized (and
significantly less "pythonic")  cython implementation.  Based on this,
I'm extremely excited to see what numba brings in the future.

All the above code is available as an ipython notebook:
[numba_vs_cython.ipynb](/downloads/notebooks/numba_vs_cython.ipynb).
For information on how to view this file, see the
[IPython page](http://ipython.org/ipython-doc/dev/interactive/htmlnotebook.html)
Alternatively, you can view this notebook (but not modify it) using the
nbviewer [here](http://nbviewer.ipython.org/url/jakevdp.github.com/downloads/notebooks/numba_vs_cython.ipynb).