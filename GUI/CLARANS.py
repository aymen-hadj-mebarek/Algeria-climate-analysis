import random
import numpy as np

def clarans_algo(data, number_clusters, num_local, max_neighbors):
    """
    Implémentation de l'algorithme CLARANS pour le clustering.

    :param data: ndarray, ensemble de données pour le clustering
    :param number_clusters: int, nombre de clusters (k)
    :param num_local: int, nombre de recherches locales
    :param max_neighbors: int, nombre maximum de voisins à tester par itération
    :return: tuple, (meilleurs medoids, meilleure affectation des points)
    """
    def calculate_cost(medoids, data):
        """Calcule le coût total (somme des distances entre chaque point et son médoïde le plus proche)."""
        cost = 0
        for point in data:
            distances = [np.linalg.norm(point - data[medoid]) for medoid in medoids]
            cost += min(distances)
        return cost

    def assign_points_to_medoids(medoids, data):
        """Assigne chaque point au médoïde le plus proche."""
        clusters = {medoid: [] for medoid in medoids}
        labels = []
        for idx, point in enumerate(data):
            closest_medoid = min(medoids, key=lambda m: np.linalg.norm(point - data[m]))
            clusters[closest_medoid].append(idx)
            labels.append(medoids.index(closest_medoid))
        return clusters, labels

    n_points = len(data)
    best_medoids = None
    best_cost = float('inf')

    for i in range(num_local):
        # Initialiser aléatoirement les médoïdes
        medoids = random.sample(range(n_points), number_clusters)
        current_cost = calculate_cost(medoids, data)

        improved = True
        while improved:
            improved = False
            for j in range(max_neighbors):
                # Sélectionner un médoïde courant aléatoire
                medoid_to_replace = random.choice(medoids)
                non_medoids = [idx for idx in range(n_points) if idx not in medoids]
                candidate = random.choice(non_medoids)

                # Tester un remplacement
                new_medoids = medoids[:]
                new_medoids.remove(medoid_to_replace)
                new_medoids.append(candidate)
                new_cost = calculate_cost(new_medoids, data)

                if new_cost < current_cost:
                    medoids = new_medoids
                    current_cost = new_cost
                    improved = True
                    break

        # Mettre à jour les meilleurs médoïdes si nécessaire
        if current_cost < best_cost:
            best_medoids = medoids
            best_cost = current_cost

    # Affecter les points aux meilleurs médoïdes
    best_clusters, labels = assign_points_to_medoids(best_medoids, data)
    noise_points = len([label for label in labels if label == -1])

    return best_medoids, best_clusters, labels, noise_points