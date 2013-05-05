Title: Memoryview Benchmarks 2
date: 2012-08-16 14:19
comments: true

<!-- PELICAN_BEGIN_SUMMARY -->
In the [previous post](/blog/2012/08/08/memoryview-benchmarks/), I explored
how cython typed memoryviews can be used to speed up repeated array
operations.  It became clear that typed memoryviews are superior to
the ndarray syntax for slicing, and as fast as raw pointers for single
element access.  In the comments, Mathieu brought up an interesting
question: is the ndarray syntax as good as typed memoryviews if you're
not doing slicing?

The answer turns out to be yes, *unless* the compiler tries to inline your
function.

<!-- PELICAN_END_SUMMARY -->

### Inlined Memoryview ###

We'll use a slightly simpler benchmark script here for simplicity.  We'll
use inlined typed memoryviews for the inner function, and call this function
within an outer loop:

``` cython
import numpy as np
cimport numpy as np
cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
cdef inline double inner_func(double[:, ::1] X):
    return X[0, 0]

def loop_1(int N, switch=True):
    cdef double[:, ::1] X = np.zeros((100, 100))
    cdef int i
    for i in range(N):
        # this should be inlined by the compiler
        inner_func(X)
```

The inner function is called `N` times.  We've used the "inline" keyword here:
it turns out this is optional with common compiler optimizations turned on.
`gcc` and other compilers are smart enough to figure out that this function
should be inlined, even if the cython code doesn't mark it as such.  Timing
the function on one million loops gives us our comparison benchmark:

    %timeit loop_1(1E6)
    100000 loops, best of 3: 10.1 us per loop

Just over a millisecond to perform this loop one million times.

### Non-inlined Memoryview ###
Because the compilers are generally so smart, we actually need to be a bit
clever to make sure our function is *not* inlined.  We'll do that through
a switch statement in the loop call, which selects between two possible
inner functions.  This may seem a bit contrived, but it could come up
in practice: for example, if we wanted to create a KDTree for nearest neighbor
searches which can use one of several distance metrics within a single tree
framework, we might be tempted to try a solution like this:

``` cython
import numpy as np
cimport numpy as np
cimport cython

ctypedef double (*inner_func_ptr)(double[:, ::1])

@cython.boundscheck(False)
@cython.wraparound(False)
cdef double inner_func_1(double[:, ::1] X):
    return X[0, 0]

@cython.boundscheck(False)
@cython.wraparound(False)
cdef double inner_func_2(double[:, ::1] X):
    return X[0, 0]

def loop_2(int N, switch=True):
    # use a switch to ensure that inlining can't happen: compilers
    # are usually smart enough to figure it out otherwise.
    cdef inner_func_ptr func
    if switch:
        func = inner_func_1
    else:
        func = inner_func_2
        
    cdef double[:, ::1] X = np.zeros((100, 100))
    cdef int i
    for i in range(N):
        func(X)
```
By adding the switch function, it means the compiler cannot know at compile
time which of the inner functions will be used in the loop, and they
cannot be inlined.  The timing results are as follows:

    %timeit loop_2(1E6)
    10 loops, best of 3: 22.9 ms per loop

Using a non-inlined function makes things significantly slower in this case!
So, if you're repeatedly calling a small function, inlining can be *very*
important for optimal execution times.

### The Problem with ndarray ###
It turns out that beyond slicing, the problem with the ndarray type is that
multi-dimensional arrays require relatively expensive buffer checks whenever
a function is called.  This causes similar code with ndarrays to be
significantly slower:

``` cython
import numpy as np
cimport numpy as np
cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
cdef inline double inner_func(np.ndarray[double, ndim=2, mode='c'] X):
    return X[0, 0]

def loop_3(int N, switch=True):
    cdef np.ndarray[double, ndim=2, mode='c'] X = np.zeros((100, 100))
    cdef int i
    for i in range(N):
        inner_func(X)
```
Compiling this gives the following warning:

    warning: Buffer unpacking not optimized away.

The result of this buffer unpacking in each loop is a much slower execution
time:

    %timeit loop_3(1E6)
    1 loops, best of 3: 617 ms per loop

This is about 30 times slower than the non-inlined version of the memoryview,
and 6000 times slower than the inlined memoryview above!
Is there any way around this?
Well, there are two options: raw pointers, or explicit inlining in the
code (that is, copying and pasting your code).  Both options will have
speeds similar to that of the inlined memoryviews, but each solution
is inconvenient in its own way.

So why wouldn't you use memoryviews?  Well, several projects strive to
remain compatible with python 2.4 (one example is scipy) and python 2.4 is
not compatible with cython's typed memoryviews.  Other projects seek to
remain compatible with earlier cython versions which don't support
the relatively new memoryview syntax.
In these situations, one of the two partial solutions above
probably need to be used.  In practice, I have usually resorted to passing
around raw pointers.

### Summary ###
Here are the timings we found above:

- Inlined memoryviews: 0.1 ms
- Non-inlined memoryviews: 22.9 ms
- Inlined ndarray: 617 ms

So we see yet another reason that typed memoryviews are superior to
the ndarray syntax: they not only have very speedy slicing, but also
play well with the compiler's inlining optimization.  Granted, these
time differences will be insignificant if your inlined function does
some non-negligible amount of computation, but there may be situations
where this affects things.

### Back to my problem ###
If you recall, I started all of this because I wanted to create a binary tree
that can compute pairwise distances with arbitrary distance metrics.  Where
do these results put me?  Not in a great position, it turns out.  Abstracting
out the distance function so that the same machinery can be used with
different functions will lead to speed penalties from the inability to inline.
C++ libraries accomplish this through compile-time conditionals (i.e. templates)
but cython doesn't have this capability.  Duplicating the tree
framework with a new hard-coded (and thus inlinable) distance metric may
be the only option.  That, or wrapping a templated C++ implementation.

All of the above scripts are available as an ipython
notebook: [memview_bench_2.ipynb](/downloads/notebooks/memview_bench_2.ipynb).
For information on how to view this file, see the
[IPython page](http://ipython.org/ipython-doc/dev/interactive/htmlnotebook.html)
Alternatively, you can view this notebook (but not modify it) using the
nbviewer [here](http://nbviewer.ipython.org/url/jakevdp.github.com/downloads/notebooks/memview_bench_2.ipynb).