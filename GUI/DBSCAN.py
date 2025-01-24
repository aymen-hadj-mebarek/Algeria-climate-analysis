import numpy as np

def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))

def manhattan_distance(point1, point2):
    return np.sum(np.abs(point1 - point2))

def cosine_distance(point1, point2):
    return 1 - np.dot(point1, point2) / (np.linalg.norm(point1) * np.linalg.norm(point2))

def region_query(data, point_idx, eps, distance_func):
    neighbors = []
    for idx in range(len(data)):
        if distance_func(data.iloc[point_idx].to_numpy(), data.iloc[idx].to_numpy()) <= eps:
            neighbors.append(idx)
    return neighbors


def expand_cluster(data, labels, point_idx, cluster_id, neighbors, eps, min_samples, distance_func):
    labels[point_idx] = cluster_id
    i = 0
    while i < len(neighbors):
        neighbor_idx = neighbors[i]
        if labels[neighbor_idx] == -1:  # Change noise to border point
            labels[neighbor_idx] = cluster_id
        elif labels[neighbor_idx] == 0:  # Unvisited point
            labels[neighbor_idx] = cluster_id
            new_neighbors = region_query(data, neighbor_idx, eps, distance_func)
            if len(new_neighbors) >= min_samples:
                neighbors += new_neighbors
        i += 1

def dbscan_algo(data, eps, min_samples, distance_metric='euclidean'):
    if distance_metric == 'euclidean':
        distance_func = euclidean_distance
    elif distance_metric == 'manhattan':
        distance_func = manhattan_distance
    elif distance_metric == 'cosine':
        distance_func = cosine_distance
    else:
        raise ValueError("Unsupported distance metric. Choose 'euclidean' or 'manhattan'.")

    labels = np.zeros(len(data), dtype=int)  # 0: unvisited, -1: noise, positive integers: cluster IDs
    cluster_id = 0

    for point_idx in range(len(data)):
        if labels[point_idx] != 0:
            continue

        neighbors = region_query(data, point_idx, eps, distance_func)

        if len(neighbors) < min_samples:
            labels[point_idx] = -1  # Mark as noise
        else:
            cluster_id += 1
            expand_cluster(data, labels, point_idx, cluster_id, neighbors, eps, min_samples, distance_func)

    return labels