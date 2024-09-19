'''
Write a Python function that implements the k-Means
algorithm for clustering, starting with specified initial
centroids and a set number of iterations. The function
should take a list of points (each represented as a tuple
of coordinates), an integer k representing the number of
clusters to form, a list of initial centroids (each a tuple of
coordinates), and an integer representing the maximum
number of iterations to perform. The function will
iteratively assign each point to the nearest centroid and
update the centroids based on the assignments until the
centroids do not change significantly, or the maximum
number of iterations is reached. The function should
return a list of the final centroids of the clusters. Round
to the nearest fourth decimal.
'''
def k_means_clustering(points: list[tuple[float, float]], k: int, initial_centroids: list[tuple[float, float]], max_iterations: int) -> list[tuple[float, float]]:
    centroids = initial_centroids
    for iteration in range(max_iterations): 
        cluster1 = []
        cluster2 = []
        distance = []    
        for i in range(len(points)):
                ds = tuple((points[i][0] - centroids[x][0]) ** 2 + (points[i][1] - centroids[x][1]) ** 2 for x in range(2))
                distance.append(ds)
        
        for i in range(len(distance)):
            x, y = distance[i]
            if x < y:
                cluster1.append(points[i])
            else:
                cluster2.append(points[i])
                    
        new_centroids = [tuple(sum(xy_c1) / len(cluster1) for xy_c1 in zip(*cluster1)),\
                tuple(sum(xy_c2) / len(cluster2) for xy_c2 in zip(*cluster2))]
        centroids = new_centroids
    
    return centroids

