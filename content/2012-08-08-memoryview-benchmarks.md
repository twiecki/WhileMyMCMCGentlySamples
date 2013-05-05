Title: Memoryview Benchmarks
date: 2012-08-08 18:50
comments: true
categories: 
---

<!-- PELICAN_BEGIN_SUMMARY -->
There was recently a [thread](https://groups.google.com/forum/?fromgroups#!topic/cython-users/8uuxjB_wbBQ[1-25] "cython-users archive")
on cython-users which caught my eye.  It has to do with 
[memoryviews](http://docs.cython.org/src/userguide/memoryviews.html), a new
way of working with memory buffers in cython.

I've been thinking recently about how to do fast
and flexible memory buffer access in cython.  I contributed the
[BallTree](http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.BallTree.html)
implementation for nearest neighbors searching in
[scikit-learn](http://www.scikit-learn.org), and have been actively thinking
about how to make it faster and more flexible, including adding the ability
to specify distance metrics other than euclidean and minkowski.

In order to accomplish this, I'd like to have a set of distance metric
functions which take two vectors and compute a distance.  There would
be many functions with similar call signatures which could then be
plugged into a code that would iterate over a set of vectors and
compute the appropriate distances.

<!-- PELICAN_END_SUMMARY -->

### Pure python version ###

In pure python, the implementation described above might look something
like this:

``` python
# memview_bench_v1.py
import numpy as np

def euclidean_distance(x1, x2):
    x1 = np.asarray(x1)
    x2 = np.asarray(x2)
    return np.sqrt(np.sum((x1 - x2) ** 2))
```

This looks promising.  Let's create a function based on this which will compute
the pairwise distance between all points in a matrix (this is similar
to [pairwise_distances](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.pairwise_distances.html) in scikit-learn or
[pdist](http://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.pdist.html) in scipy).  The simple form of the function might look
like this:

``` python
# memview_bench_v1 (continued)

def pairwise(X, metric=euclidean_distance):
    X = np.asarray(X)
    
    n_samples, n_dim = X.shape

    D = np.empty((n_samples, n_samples))

    for i in range(n_samples):
        for j in range(n_samples):
            D[i, j] = metric(X[i], X[j])

    return D
```

We could exploit symmetry to reduce the number of computations required, but
we'll skip that step for now: this simple version of the function will give
us a good benchmark for comparison with alternatives below.  Using the
`timeit` magic in ipython, we can learn how fast this implementation is:

    In [1]: import numpy as np

    In [2]:from memview_bench_v1 import pairwise

    In [3]: X = np.random.random((500, 3))

    In [4]: timeit pairwise(X)
    1 loops, best of 3: 6.51 s per loop

It takes nearly seven seconds to compute 250,000 distances.  This is much
too slow.


### Cython Speedup ###

Perhaps we can speed this up using cython declarations.  Before typed
memoryviews were added in cython 0.16, the way to quickly index numpy
arrays in cython was through the numpy specific syntax, adding type
information to each array that specifies its data type, its dimension, and
its order:

``` cython
# memview_bench.pyx
import numpy as np

cimport numpy as np
from libc.math cimport sqrt
cimport cython

# define a function pointer to a metric
ctypedef double (*metric_ptr)(np.ndarray, np.ndarray)

@cython.boundscheck(False)
@cython.wraparound(False)
cdef double euclidean_distance(np.ndarray[double, ndim=1, mode='c'] x1,
                               np.ndarray[double, ndim=1, mode='c'] x2):
    cdef double tmp, d
    cdef np.intp_t i, N

    d = 0
    N = x1.shape[0]
    # assume x2 has the same shape as x1.  This could be dangerous!

    for i in range(N):
        tmp = x1[i] - x2[i]
        d += tmp * tmp

    return sqrt(d)


@cython.boundscheck(False)
@cython.wraparound(False)
def pairwise(np.ndarray[double, ndim=2, mode='c'] X not None,
             metric = 'euclidean'):
    cdef metric_ptr dist_func
    if metric == 'euclidean':
        dist_func = &euclidean_distance
    else:
        raise ValueError("unrecognized metric")

    cdef np.intp_t i, j, n_samples
    n_samples = X.shape[0]

    cdef np.ndarray[double, ndim=2, mode='c'] D = np.empty((n_samples,
                                                            n_samples))
    for i in range(n_samples):
        for j in range(n_samples):
            D[i, j] = dist_func(X[i], X[j])

    return D
```

Notice that we're essentially running the same code, except we have added
type identifiers to speed up function calls and loops.  The `mode='c'`
argument in the `np.ndarray` type says that the array is contiguous in
memory, and C-ordered.

For reference, this can be compiled in-place by running
`python setup.py build_ext --inplace` with the following
setup.py file:

``` python
# setup.py

import os
import numpy

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

module = 'memview_bench_v2'

setup(cmdclass = {'build_ext': build_ext},
      name=module,
      version='1.0',
      ext_modules=[Extension(module,
                             [module + ".pyx"])],
      include_dirs=[numpy.get_include(),
                    os.path.join(numpy.get_include(), 'numpy')]
      )
```

We'll time the resulting function on the same sized array as we did previously:

    In [1]: import numpy as np

    In [2]: from memview_bench_v2 import pairwise

    In [3]: X = np.random.random((500, 3))

    In [4]: timeit pairwise(X)
    1 loops, best of 3: 668 ms per loop

That's a factor of 10 speedup over the pure python version!  It turns out,
though, that we can do better.  In particular, the slicing operation when
we call `X[i]` and `X[j]` must generate a new numpy array each time, which
leads to a lot of python overhead in reference counting, etc.  This is the
reason that the cython team introduced typed memoryviews in cython v0.16.


### Typed Memoryviews ###

The equivalent of the above code using typed memoryviews looks like this:

``` cython
# memview_bench_v3.pyx
import numpy as np

cimport numpy as np
from libc.math cimport sqrt
cimport cython

# define a function pointer to a metric
ctypedef double (*metric_ptr)(double[::1], double[::1])

@cython.boundscheck(False)
@cython.wraparound(False)
cdef double euclidean_distance(double[::1] x1,
                               double[::1] x2):
    cdef double tmp, d
    cdef np.intp_t i, N

    d = 0
    N = x1.shape[0]
    # assume x2 has the same shape as x1.  This could be dangerous!

    for i in range(N):
        tmp = x1[i] - x2[i]
        d += tmp * tmp

    return sqrt(d)


@cython.boundscheck(False)
@cython.wraparound(False)
def pairwise(double[:, ::1] X not None,
             metric = 'euclidean'):
    cdef metric_ptr dist_func
    if metric == 'euclidean':
        dist_func = &euclidean_distance
    else:
        raise ValueError("unrecognized metric")

    cdef np.intp_t i, j, n_samples
    n_samples = X.shape[0]

    cdef double[:, ::1] D = np.empty((n_samples, n_samples))

    for i in range(n_samples):
        for j in range(n_samples):
            D[i, j] = dist_func(X[i], X[j])

    return D
```

The only change is that instead of using the `np.ndarray[...]` type specifier,
we use the typed memoryview `double[:, ::1]` specifier.  The `::1` in the
second position means that we are passing a two-dimensional array, which
is contiguous and C-ordered.  We time the results and see the following:

    In [1]: import numpy as np

    In [2]: from memview_bench_v3 import pairwise

    In [3]: X = np.random.random((500, 3))

    In [4]: timeit pairwise(X)
    10 loops, best of 3: 22 ms per loop

This gives another factor of 30 improvement over the previous version, simply
by switching to typed memoryviews rather than the numpy interface.  Still,
our function is creating memoryview objects each time we slice the array.  We
can determine how much overhead this is generating by using raw C pointers
instead.  It is not as clean, but it should be very fast:

### Raw Pointers ###

The fundamental benchmark for this sort of operation should be working
directly with the pointers themselves.  While this is not a very "pythonic"
way of doing things, it does lead to very fast code, as we will see:

``` cython
# memview_bench_v4.pyx
import numpy as np

cimport numpy as np
from libc.math cimport sqrt
cimport cython

# define a function pointer to a metric
ctypedef double (*metric_ptr)(double*, double*, int)

@cython.boundscheck(False)
@cython.wraparound(False)
cdef double euclidean_distance(double* x1,
                               double* x2,
                               int N):
    cdef double tmp, d
    cdef np.intp_t i

    d = 0

    for i in range(N):
        tmp = x1[i] - x2[i]
        d += tmp * tmp

    return sqrt(d)


@cython.boundscheck(False)
@cython.wraparound(False)
def pairwise(double[:, ::1] X not None,
             metric = 'euclidean'):
    cdef metric_ptr dist_func
    if metric == 'euclidean':
        dist_func = &euclidean_distance
    else:
        raise ValueError("unrecognized metric")

    cdef np.intp_t i, j, n_samples, n_dim
    n_samples = X.shape[0]
    n_dim = X.shape[1]

    cdef double[:, ::1] D = np.empty((n_samples, n_samples))

    cdef double* Dptr = &D[0, 0]
    cdef double* Xptr = &X[0, 0]

    for i in range(n_samples):
        for j in range(n_samples):
            Dptr[i * n_samples + j] = dist_func(Xptr + i * n_dim,
                                                Xptr + j * n_dim,
                                                n_dim)

    return D
```

Instead of passing around slices of arrays, we've accessed the raw memory
buffer using C pointer syntax.  This is not as easy to read, and can lead
to `glibc` errors or segmentation faults if we're not careful.  Testing
this implementation, we find that it is extremely fast:

    In [1]: import numpy as np

    In [2]: from memview_bench_v4 import pairwise

    In [3]: X = np.random.random((500, 3))

    In [4]: timeit pairwise(X)
    100 loops, best of 3: 2.47 ms per loop

This is another factor of 10 faster than the memoryview benchmark above!
Essentially, what this is telling us is that creating a memoryview slice
takes about 0.02 / 500,000 = 40 nanoseconds on our machine.  This is extremely
fast, but because we're performing this operation half a million times, the
cost of the allocations is significant compared to the rest of our
computation.  If our vectors were, say, length 1000, this cost may not be
a significant percentage of the total cost.

So what are we left with?  Do we need to use raw pointers in all circumstances
when working with collections of small vectors?  Perhaps not.

### A Faster Implementation with Memoryviews ###

The creation of memoryview slices, though extremely fast, is causing a problem
simply because we're creating so many slices.  Here is an alternative which
uses no raw pointers, but matches the speed of raw pointers:

``` cython
# memview_bench_v5.pyx
import numpy as np

cimport numpy as np
from libc.math cimport sqrt
cimport cython

# define a function pointer to a metric
ctypedef double (*metric_ptr)(double[:, ::1], np.intp_t, np.intp_t)

@cython.boundscheck(False)
@cython.wraparound(False)
cdef double euclidean_distance(double[:, ::1] X,
                               np.intp_t i1, np.intp_t i2):
    cdef double tmp, d
    cdef np.intp_t j

    d = 0

    for j in range(X.shape[1]):
        tmp = X[i1, j] - X[i2, j]
        d += tmp * tmp

    return sqrt(d)


@cython.boundscheck(False)
@cython.wraparound(False)
def pairwise(double[:, ::1] X not None,
             metric = 'euclidean'):
    cdef metric_ptr dist_func
    if metric == 'euclidean':
        dist_func = &euclidean_distance
    else:
        raise ValueError("unrecognized metric")

    cdef np.intp_t i, j, n_samples, n_dim
    n_samples = X.shape[0]
    n_dim = X.shape[1]

    cdef double[:, ::1] D = np.empty((n_samples, n_samples))

    for i in range(n_samples):
        for j in range(n_samples):
            D[i, j] = dist_func(X, i, j)

    return D
```

Timing this implementation we find the following:

    In [1]: import numpy as np

    In [2]: from memview_bench_v5 import pairwise

    In [3]: X = np.random.random((500, 3))

    In [4]: timeit pairwise(X)
    100 loops, best of 3: 2.45 ms per loop

Just as fast as using raw pointers, but much cleaner and easier to read.

### Summary ###
Here are the timing results we've seen above:

- **Python + numpy**: 6510 ms
- **Cython + numpy**: 668 ms
- **Cython + memviews (slicing)**: 22 ms
- **Cython + raw pointers**: 2.47 ms
- **Cython + memviews (no slicing)**: 2.45 ms

So what have we learned here?  First of all, typed memoryviews are fast.
Blazing fast.  If used correctly, they can be comparable to raw pointers,
but are much cleaner easier to debug.  For example, in the last
version, if we ran into a memory error we could simply turn on bounds-checking
and quickly find the source of the problem.  Slicing with memoryviews is
also fast, but should be used carefully if your operation time on each slice
is compararable to the cost of building the slice.

The moral of the story?  *Use typed memoryviews.*  It will lead to fast cython
code which is cleaner, more readable, and more easily debuggable than any other
alternative.

**Update**: All of the above scripts are now available as an ipython
notebook: [memview_bench.ipynb](/downloads/notebooks/memview_bench.ipynb).
For information on how to view this file, see the
[IPython page](http://ipython.org/ipython-doc/dev/interactive/htmlnotebook.html)
Alternatively, you can view this notebook (but not modify it) using the
nbviewer [here](http://nbviewer.ipython.org/url/jakevdp.github.com/downloads/notebooks/memview_bench.ipynb).

Thanks to Dave for the tip.