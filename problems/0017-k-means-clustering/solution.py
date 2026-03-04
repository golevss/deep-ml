def euclid_dist(point: tuple, centroid: tuple):
	sum_l = 0
	for i in range(len(point)):
		sum_l += (point[i] - centroid[i])**2
	return sum_l

def calc_new_centroids(cluster):
	sum_list = [0.0] * len(cluster[0])
	
	for el in cluster:
		for i in range(len(el)):
			sum_list[i] += el[i]
	
	rounded_list = list()
	for el in sum_list:
		rounded_list.append(el/len(cluster))
	
	return tuple(rounded_list)

def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:
	for _ in range(max_iterations):		
		clusters = [[] for _ in range(k)]

		for point in points:
			max_lenght = -1
			idx = None
			for i in range(k):
				if max_lenght != max(euclid_dist(point, initial_centroids[i]), max_lenght):
					idx = i
				max_lenght = max(euclid_dist(point, initial_centroids[i]), max_lenght)
			
			clusters[idx].append(point)


		for i in range(k):
			initial_centroids[i] = calc_new_centroids(clusters[i])
	
	return