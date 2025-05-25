"""
Algorithm 4: System-of-Microsystems Interaction Matrix with Clustering
-----------------------------------------------------------------------
Constructs a 2D matrix representing interactions (source → target) between microsystems.
Also clusters microsystems with high interaction density using a basic density heuristic.

Author: Salman Javed
"""

import numpy as np

def build_interaction_matrix(microsystems):
    """
    Creates a square interaction matrix from microsystem interaction tuples.

    Parameters:
        microsystems (list): List of microsystems, each including a unique microsystem.id
                             and interaction info under microsystem['interactions'] (list of target ids)

    Returns:
        tuple: (matrix (np.ndarray), index_map (dict of id:index), reverse_map (list of id))
    """
    ids = [m["microsystem"]["id"] for m in microsystems]
    index_map = {id_: idx for idx, id_ in enumerate(ids)}
    reverse_map = ids
    size = len(ids)
    matrix = np.zeros((size, size))

    for source in microsystems:
        src_id = source["microsystem"]["id"]
        src_idx = index_map[src_id]
        interactions = source["microsystem"].get("interactions", [])
        for tgt_id in interactions:
            if tgt_id in index_map:
                tgt_idx = index_map[tgt_id]
                matrix[src_idx][tgt_idx] += 1  # basic frequency count

    return matrix, index_map, reverse_map

def cluster_microsystems(matrix, threshold=1):
    """
    Performs a naive clustering based on row-wise interaction count.

    Parameters:
        matrix (np.ndarray): Interaction matrix
        threshold (int): Minimum number of interactions to form a cluster

    Returns:
        dict: Mapping from row index to cluster id
    """
    clusters = {}
    current_cluster = 0

    for i in range(matrix.shape[0]):
        row_sum = np.sum(matrix[i])
        if row_sum >= threshold:
            clusters[i] = current_cluster
            current_cluster += 1
        else:
            clusters[i] = -1  # unclustered

    return clusters

def run(microsystems, threshold=1):
    """
    Full interaction matrix and clustering execution.

    Parameters:
        microsystems (list): List of mapped microsystems with interaction lists
        threshold (int): Threshold for forming a cluster

    Returns:
        dict: {
            'matrix': 2D list,
            'index_map': id:index,
            'reverse_map': index:id,
            'clusters': index:cluster_id
        }
    """
    matrix, index_map, reverse_map = build_interaction_matrix(microsystems)
    clusters = cluster_microsystems(matrix, threshold)
    return {
        "matrix": matrix.tolist(),
        "index_map": index_map,
        "reverse_map": reverse_map,
        "clusters": clusters
    }
