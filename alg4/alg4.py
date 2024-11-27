import numpy as np
import json
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt

def create_interaction_matrix(system_data, usecase_data):
    """
    Create an interaction matrix for the system-of-microsystems.
    
    Args:
        system_data (dict): System mapped data containing microsystems and interactions.
        usecase_data (dict): Usecase mapped data filtered for the workflow.
    
    Returns:
        np.ndarray: Interaction matrix.
        list: List of microsystem IDs in the order of the matrix rows/columns.
    """
    microsystems = {m['id']: idx for idx, m in enumerate(system_data['microsystems'])}
    n = len(microsystems)
    interaction_matrix = np.zeros((n, n))

    for interaction in usecase_data['interactions']:
        source_idx = microsystems.get(interaction['source_id'])
        target_idx = microsystems.get(interaction['target_id'])
        if source_idx is not None and target_idx is not None:
            interaction_matrix[source_idx, target_idx] = 1
            interaction_matrix[target_idx, source_idx] = 1  # Assuming bidirectional interaction
    
    return interaction_matrix, list(microsystems.keys())

def assign_phases(system_data, phases):
    """
    Assign engineering phases to microsystems.

    Args:
        system_data (dict): System mapped data containing microsystems.
        phases (list): List of engineering phases.
    
    Returns:
        dict: Microsystems with assigned phases.
    """
    for microsystem in system_data['microsystems']:
        microsystem['phases'] = [phase for phase in phases if phase in microsystem.get('involvement', [])]
    return system_data

def cluster_interactions(interaction_matrix, n_clusters):
    """
    Perform clustering on the interaction matrix.

    Args:
        interaction_matrix (np.ndarray): Interaction matrix.
        n_clusters (int): Number of clusters to form.
    
    Returns:
        np.ndarray: Cluster labels for each microsystem.
    """
    clustering_model = AgglomerativeClustering(n_clusters=n_clusters, affinity='precomputed', linkage='average')
    distance_matrix = 1 - interaction_matrix  # Convert to distance matrix
    labels = clustering_model.fit_predict(distance_matrix)
    return labels

def visualize_interaction_matrix(interaction_matrix, labels, microsystem_ids):
    """
    Visualize the interaction matrix with clusters.

    Args:
        interaction_matrix (np.ndarray): Interaction matrix.
        labels (np.ndarray): Cluster labels for each microsystem.
        microsystem_ids (list): List of microsystem IDs.
    """
    sorted_indices = np.argsort(labels)
    sorted_matrix = interaction_matrix[sorted_indices, :][:, sorted_indices]
    sorted_ids = [microsystem_ids[i] for i in sorted_indices]

    plt.figure(figsize=(10, 8))
    plt.imshow(sorted_matrix, cmap='Blues', interpolation='none')
    plt.colorbar(label='Interaction Strength')
    plt.xticks(range(len(sorted_ids)), sorted_ids, rotation=90)
    plt.yticks(range(len(sorted_ids)), sorted_ids)
    plt.title("Interaction Matrix with Clustering")
    plt.show()

def main(system_data_path, usecase_data_path, phases, n_clusters, output_path):
    """
    Main function to execute the algorithm.

    Args:
        system_data_path (str): Path to system mapped data JSON.
        usecase_data_path (str): Path to usecase mapped data JSON.
        phases (list): List of engineering phases.
        n_clusters (int): Number of clusters to form.
        output_path (str): Path to save the updated system data.
    """
    with open(system_data_path, 'r') as system_file:
        system_data = json.load(system_file)
    
    with open(usecase_data_path, 'r') as usecase_file:
        usecase_data = json.load(usecase_file)
    
    interaction_matrix, microsystem_ids = create_interaction_matrix(system_data, usecase_data)
    system_data = assign_phases(system_data, phases)
    labels = cluster_interactions(interaction_matrix, n_clusters)

    visualize_interaction_matrix(interaction_matrix, labels, microsystem_ids)

    # Add cluster labels to microsystems
    for microsystem, label in zip(system_data['microsystems'], labels):
        microsystem['cluster'] = int(label)
    
    with open(output_path, 'w') as output_file:
        json.dump(system_data, output_file, indent=4)
    
    print(f"Updated system data saved to {output_path}")

if __name__ == "__main__":
    # Example paths and parameters
    system_data_path = "system_mapped_data.json"  # Replace with actual path
    usecase_data_path = "usecase_mapped_data.json"  # Replace with actual path
    phases = ["Design", "Development", "Production", "Maintenance"]  # Example phases
    n_clusters = 3  # Number of clusters to form
    output_path = "updated_system_data.json"  # Replace with desired output path
    
    main(system_data_path, usecase_data_path, phases, n_clusters, output_path)
