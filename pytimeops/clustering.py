from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.metrics import calinski_harabasz_score


def apply_clustering(data, max_clusters, method):
    """
    This function gets the dataset, finds the optimal number of
    clusters and applied kmeans clustering on that and
    returns groups the center of each cluster.
    """

    best_score = -1
    best_n_clusters = 2
    # Iterate over different numbers of clusters
    for n_clusters in range(2, max_clusters + 1):
        kmeans = KMeans(n_clusters=n_clusters, n_init=10)
        kmeans.fit(data)
        labels = kmeans.labels_
        if method == 'silhouette':
            score = silhouette_score(data, labels)
        else:
            score = calinski_harabasz_score(data, kmeans.labels_)

        # Update the best number of clusters if a higher silhouette
        # score is found
        if score > best_score:
            best_score = score
            best_n_clusters = n_clusters

    # Apply K-means clustering with the best number of clusters
    kmeans = KMeans(n_clusters=best_n_clusters)
    kmeans.fit(data)
    centroids = kmeans.cluster_centers_
    Result = [best_n_clusters, centroids]
    return Result
