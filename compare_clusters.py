from source.qbca import QBCA
from sklearn.cluster import KMeans
import time
from source.utils import load_data, plot_comparison

if __name__ == '__main__':
    n_clusters = 4
    thr = 0.0001
    max_iter = 50
    dataset = 'test'

    X, _ = load_data(dataset, n_dims=5, has_labels=True)
    q = QBCA(n_seeds=n_clusters, thr=thr, max_iter=max_iter)
    km = KMeans(n_clusters=n_clusters, tol=thr, max_iter=50, precompute_distances=False, algorithm='full', n_init=1)

    t = time.time()
    y_k = km.fit_predict(X)
    print('Kmeans took {} seconds'.format(time.time() - t))


    t = time.time()
    X_2, y = q.fit_predict(X)
    print('Qbca took {} seconds'.format(time.time() - t))

    plot_comparison(X, y_k, X_2, y, 'K-Means', 'QBCA', dataset)