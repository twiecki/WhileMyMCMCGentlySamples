import numpy as np
import matplotlib.pyplot as plt
from time import time

from scipy.sparse import csc_matrix


def sparse_matrix(N1, N2, f, conversion=np.asarray, rseed=0):
    """create NxN matrix with an approximate fraction f of nonzero entries"""
    rng = np.random.RandomState(rseed)
    M = rng.rand(N1, N2)
    M[M > f] = 0
    return conversion(M)


def time_svd(svdfunc, N1, N2, f, rseed=0, bestof=3, args=None, matfunc=np.asarray, **kwargs):
    if args is None:
        args = ()
    
    N1_N2_f = np.broadcast(N1, N2, f)
    times = []
    for (N1, N2, f) in N1_N2_f:
        M = sparse_matrix(N1, N2, f, matfunc, rseed)
        t_best = np.inf
        
        for i in range(bestof):
            t0 = time()
            res = svdfunc(M, *args, **kwargs)
            t1 = time()
            t_best = min(t_best, t1 - t0)
            
        times.append(t_best)
    
    return np.array(times).reshape(N1_N2_f.shape)


def plot_propack(ax, N1, N2, f, k):
    from pypropack import svdp
    print "computing execution times for propack..."
    t = time_svd(svdp, N1, N2, f, k=k, kmax=100,
                 matfunc=csc_matrix)
    ax.plot(N1, t, label='propack (k=%i)' % k)


def plot_arpack(ax, N1, N2, f, k):
    from scipy.sparse.linalg import svds
    print "computing execution times for arpack..."
    t = time_svd(svds, N1, N2, f, k=k, matfunc=csc_matrix)
    ax.plot(N1, t, label='arpack (k=%i)' % k)


def plot_svdlibc(ax, N1, N2, f, k):
    from sparsesvd import sparsesvd
    print "computing execution times for svdlibc..."
    t = time_svd(sparsesvd, N1, N2, f, args=(5,), matfunc=csc_matrix)
    ax.plot(N1, t, label='svdlibc (k=%i)' % k)


def plot_lapack(ax, N1, N2, f, k):
    from scipy.linalg import svd
    print "computing execution times for lapack..."
    t = time_svd(svd, N1, N2, f, full_matrices=False)
    ax.plot(N1, t, label='lapack (full)')


if __name__ == '__main__':
    N = 2 ** np.arange(3, 12)
    f = 0.6
    k = 5

    fig, ax = plt.subplots(subplot_kw=dict(xscale='log', yscale='log'))

    try:
        plot_propack(ax, N, N, f, k)
    except ImportError:
        print "propack cannot be loaded"

    try:
        plot_arpack(ax, N, N, f, k)
    except ImportError:
        print "scipy arpack wrapper cannot be loaded"

    try:
        plot_svdlibc(ax, N, N, f, k)
    except ImportError:
        print "svdlibc cannot be loaded"

    try:
        plot_lapack(ax, N, N, f, k)
    except ImportError:
        print "scipy lapack wrapper cannot be loaded"

    ax.legend(loc=2)
    ax.set_xlabel('N')
    ax.set_ylabel('t (s)')
    ax.set_title('Execution Times for k=5')
    ax.grid(color='gray')

    plt.show()
