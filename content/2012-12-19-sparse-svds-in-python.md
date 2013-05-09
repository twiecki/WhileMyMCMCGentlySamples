Title: Sparse SVDs in Python
date: 2012-12-19 08:21
comments: true
slug: sparse-svds-in-python

<!-- PELICAN_BEGIN_SUMMARY -->

After [Fabian's post](http://fseoane.net/blog/2012/singular-value-decomposition-in-scipy/) on the topic, I have recently returned to thinking about the
subject of sparse singular value decompositions (SVDs) in Python.

For those who haven't used it, the SVD is an extremely powerful technique.
It is the core routine of many applications,
from filtering to dimensionality
reduction to graph analysis to supervised classification and much, much more.

I first came across the need for a fast sparse SVD when applying a technique
called Locally Linear Embedding (LLE) to astronomy spectra: it was the first
astronomy paper I published, and you can read it [here](http://adsabs.harvard.edu/abs/2009AJ....138.1365V).  In LLE, one visualizes the nonlinear relationship
between high-dimensional observations.  The computational cost is extreme: for
*N* objects, one must compute the null space (intimately related to the SVD)
of a *N* by *N* matrix.  Using direct methods (e.g. LAPACK), this can scale
as bad as $\mathcal{O}[N^3]$ in both memory and speed!

<!-- PELICAN_END_SUMMARY -->

I needed a better option.  I came across the package
[ARPACK](http://www.caam.rice.edu/software/ARPACK/), a well-tested
implementation of iterative Arnoldi Factorization written in Fortran.
The shift-invert mode of ARPACK served my needs, so I spent some time
extending the [scipy ARPACK wrapper](http://docs.scipy.org/doc/scipy/reference/tutorial/arpack.html) so I could address my problem.  I also helped
Fabian and others implement the beginnings of the [manifold learning](http://scikit-learn.org/dev/modules/manifold.html) module in scikit-learn.

Even after moving on to other problems, I found that
the SVD was at the core of nearly every component of my research
while working toward my PhD.  You can see this in
[several](http://adsabs.harvard.edu/abs/2011AAS...21715304C)
[other](http://adsabs.harvard.edu/abs/2011ApJ...727..118V)
[projects](http://adsabs.harvard.edu/abs/2011AJ....142..203D)
I was involved with over the years, including my
[PhD Thesis](http://gradworks.umi.com/35/42/3542228.html), which centered
on Astronomical applications of Karhunen-Loeve analysis -- a method, again,
intimately linked with the SVD.

Hopefully this brief tour has convinced you of the power of the SVD in
addressing real research problems.  Now to the code.

# Sparse SVD Implementations #
What I didn't know at the time I worked on the ARPACK wrapper is that there
are several more good options available for computing SVDs - and most now have
passable Python wrappers which integrate well with scipy's sparse matrices.
I'll briefly describe them here.

## LAPACK ##
[LAPACK](http://www.netlib.org/lapack/)
is the standard specification of efficient linear algebra routines
across computing systems, and contains routines to
compute a direct (i.e. non-iterative)
SVD of a dense matrix.  The performance of LAPACK varies from system to
system, and implementation to implementation.  The algorithm is generally
$\mathcal{O}[N^3]$,
and partial decompositions are (in general) not available.  Though
not technically the same, I would group alternatives like
[ATLAS](http://math-atlas.sourceforge.net/) (an optimized open-source
matrix library) and [MKL](http://software.intel.com/en-us/intel-mkl)
(Intel's proprietery library for fast numerics) in the same category.
I don't have much personal experience with MKL, so if I'm not doing it justice,
please feel free to admonish me in the comments!

LAPACK is wrapped by Numpy and Scipy, and is
at the core of many of the routines in ``numpy.linalg`` and
``scipy.linalg``, including the ``svd`` function in each.

## ARPACK ##
As I mentioned above, [ARPACK](http://www.caam.rice.edu/software/ARPACK/)
implements a fast iterative/partial eigenvalue decomposition on a general
linear operator.  One of its strengths is that unlike LAPACK, it does not
depend on your matrix being stored in any standard layout: all that is required
is to provide a routine which implements matrix-vector multiplication.  This
means that as well as dense matrices, ARPACK can be used on any sparse matrix
or even a general linear operator which maps one vector space to another.

ARPACK does not have a native SVD implementation, but it is possible to
exploit the relationship between eigenvalue decompositions and singular
value decompositions to compute an ARPACK svd: this is what the current
``svds`` routine in ``scipy.sparse.linalg`` does: see the documentation
[here](http://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.svds.html).  One issue with this implementation is that to compute the SVD of
a matrix *M*, it must implicitly compute $M^T M$,
and that may lead to issues of both
numerical accuracy and computational efficiency.

## SVDLIBC ##
Before Fabian's blog post, mentioned above, I had never heard of
[SVDLIBC](http://tedlab.mit.edu/~dr/SVDLIBC/).  It
is also an Arnoldi-iteration based implementation, but SVDLIBC requires a
specific sparse matrix format to operate.  Fortunately for scipy users, this
storage format maps directly to the CSC sparse matrix format, so the SVDLIBC
svd can be computed without any memory copies of the scipy matrix (assuming,
of course, your matrix is already stored as CSC or CSR!).  A bare-bones python
wrapper for the routine exists in the [sparsesvd](http://pypi.python.org/pypi/sparsesvd/) package.

## PROPACK ##
[PROPACK](http://soi.stanford.edu/~rmunk/PROPACK/) is another well-tested
Fortran package which computes the SVD directly using an Arnoldi Factorization
scheme: like ARPACK, it only depends on a callback implementing left- and
right-multiplication operations, rather than making use of any specific
sparse storage format.  Like SVDLIBC, it  computes the svd directly, saving
computation time and leading to greater numerical accuracy.  From my brief
search, it seems that
no python wrapper is readily available (though I heard that David Cournapeau
had worked on one).  Until recently, the PROPACK license was unspecified,
precluding its inclusion in Scipy or other BSD-licensed packages.  It appears
that just recently, PROPACK itself was moved to a BSD license, so there is
now the possibility of including it in the Scipy universe.

I have begun working on a full-featured PROPACK wrapper in the Scipy style,
using the excellent F2Py Fortran interface generator.  You can find the 
code in my [pypropack repository](https://github.com/jakevdp/pypropack)
on Github.  As of this writing, there is still a lot to do to make the
code releasable, but there is enough there to enable some quick benchmarks.

# Benchmark Comparisons #
To benchmark these four SVD options, I used the following code:

{% include_code plot_svd_benchmarks.py lang:python SVD Benchmarks %}

This creates square sparse matrices, measures the computation time as a function
of the matrix size, and plots the results.  The results on my 3-year old
linux box are below:

{% img /figures/svd_benchmarks.png [SVD benchmarks] %}

A few comments: First, as expected, LAPACK is much slower than the rest.  This
is due to two factors: first, LAPACK computes the full SVD, while the other
methods compute only partial SVDs (the *k=5* largest singular values).
Second, the LAPACK on my system is not
well-optimized: I could probably reduce this by at least an order of magnitude
if I were to use an ATLAS install optimized for my system.  If you need a
full SVD, it will be hard to beat LAPACK/ATLAS/MKL in terms of speed (but
in terms of memory consumption, as
[Fabian showed](http://fseoane.net/blog/2012/singular-value-decomposition-in-scipy/),
LAPACK can be pretty bad).  Because SVDLIBC, ARPACK, and PROPACK all use
Lanczos/Arnoldi iteration, they should all similarly out-perform LAPACK on
the memory question.

Second, the good performance of SVDLIBC for small matrices is probably due to
its direct use of the CSC memory within the Fortran code.  For matrices this
size, the Python overhead of invoking the callback in ARPACK and PROPACK kills
any performance gains from the more sophisticated algorithms.  As the matrices
grow, we see that ARPACK and PROPACK begin to out-perform SVDLIBC.

Finally, we see that for these test cases, PROPACK is consistently
faster than ARPACK by a factor of 5 or so: nothing to scoff at!
I haven't rigorously tested the claims of increased numerical stability
in PROPACK, but those two pieces point to PROPACK as the
preferred method by far.

# Next Steps #
I hope to continue developing the ``pypropack`` wrapper on github, and once
I'm happy with it, incorporate it into Scipy's sparse linear algebra tools.
I would love help with this: in particular, if there are any F2Py wizards out
there, I'm currently having what I think is a
[memory issue](https://github.com/jakevdp/pypropack/issues/1)
with the callback function that I can't seem to track down.

Hopefully this post has helped convince you of the importance of SVDs in
scientific computing, and also of the benefits of working on PROPACK
incorporation in the scientific Python universe.  This sort of thing
won't happen unless someone like **you** decides to work on it!  That
fact ends up being both a weakness and an incredible strength of
open-source packages.

Happy coding!