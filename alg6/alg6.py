import json
import matplotlib.pyplot as plt
import numpy as np

def load_data(system_path, metrics_path):
    """
    Load system and value metrics data from JSON files.

    Args:
        system_path (str): Path to the system data JSON file.
        metrics_path (str): Path to the value metrics JSON file.

    Returns:
        tuple: System data and value metrics as dictionaries.
    """
    with open(system_path, 'r') as system_file:
        system_data = json.load(system_file)
    with open(metrics_path, 'r') as metrics_file:
        metrics_data = json.load(metrics_file)
    return system_data, metrics_data

def map_to_2d(system_data, metrics_data):
    """
    Map microsystems to a 2D plane and apply value metrics.

    Args:
        system_data (dict): Data containing microsystem attributes.
        metrics_data (dict): Value metrics for cost, profit, and environmental impact.

    Returns:
        list: Mapped microsystems with 2D coordinates and metrics.
    """
    mapped_data = []
    for microsystem in system_data['microsystems']:
        microsystem_id = microsystem['id']
        coordinates = microsystem['coordinates']
        metrics = metrics_data.get(microsystem_id, {})
        mapped_data.append({
            "id": microsystem_id,
            "coordinates": (coordinates['X'], coordinates['Y']),
            "profit": metrics.get("profit", 0),
            "cost": metrics.get("cost", 0),
            "environmental_impact": metrics.get("environmental_impact", 0)
        })
    return mapped_data

def visualize_value_projection(mapped_data, visual_config):
    """
    Visualize 2D projections of value addition for microsystems.

    Args:
        mapped_data (list): List of mapped microsystems with metrics.
        visual_config (dict): Configuration for visualization.
    """
    x, y, profit, cost = [], [], [], []

    for data in mapped_data:
        x.append(data['coordinates'][0])
        y.append(data['coordinates'][1])
        profit.append(data['profit'])
        cost.append(data['cost'])

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, s=profit, c=cost, cmap='viridis', alpha=0.7, edgecolors="w")
    plt.colorbar(label="Engineering Cost")
    plt.title("RAMI 4.0 Value Addition Projection")
    plt.xlabel("Hierarchy Levels")
    plt.ylabel("Lifecycle Stages")
    plt.grid(True)

    # Add annotations for each microsystem
    for i, data in enumerate(mapped_data):
        plt.annotate(
            f"ID: {data['id']}",
            (x[i], y[i]),
            textcoords="offset points",
            xytext=(5, 5),
            ha="center"
        )

    plt.show()

def main(system_data_path, metrics_data_path, visual_config_path):
    """
    Main function to execute the value addition projection.

    Args:
        system_data_path (str): Path to the system data JSON file.
        metrics_data_path (str): Path to the value metrics JSON file.
        visual_config_path (str): Path to the visualization configuration JSON file.
    """
    with open(visual_config_path, 'r') as config_file:
        visual_config = json.load(config_file)

    system_data, metrics_data = load_data(system_data_path, metrics_data_path)
    mapped_data = map_to_2d(system_data, metrics_data)
    visualize_value_projection(mapped_data, visual_config)

if __name__ == "__main__":
    # Example file paths
    system_data_path = "system_mapped_data.json"  # Replace with the actual path
    metrics_data_path = "value_metrics.json"      # Replace with the actual path
    visual_config_path = "visual_config.json"     # Replace with the actual path
    main(system_data_path, metrics_data_path, visual_config_path)
