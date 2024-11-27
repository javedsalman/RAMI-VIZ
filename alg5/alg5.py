import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def load_visual_config(config_path):
    """
    Load the visualization configuration for RAMI 4.0 cube.
    
    Args:
        config_path (str): Path to the configuration file (JSON).
    
    Returns:
        dict: Visualization configuration.
    """
    with open(config_path, 'r') as file:
        return json.load(file)

def draw_ellipsoid(ax, center, radii, color):
    """
    Draw an ellipsoid representing a microsystem.
    
    Args:
        ax (mpl_toolkits.mplot3d.Axes3D): 3D Axes instance.
        center (tuple): Center of the ellipsoid (x, y, z).
        radii (tuple): Radii of the ellipsoid (a, b, c).
        color (str): Color of the ellipsoid.
    """
    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)
    x = radii[0] * np.outer(np.cos(u), np.sin(v)) + center[0]
    y = radii[1] * np.outer(np.sin(u), np.sin(v)) + center[1]
    z = radii[2] * np.outer(np.ones_like(u), np.cos(v)) + center[2]
    ax.plot_surface(x, y, z, color=color, alpha=0.6)

def visualize_3d_rami_cube(system_data, usecase_data, visual_config):
    """
    Visualize the 3D RAMI 4.0 cube for microsystems.
    
    Args:
        system_data (dict): Data for system mapped microsystems.
        usecase_data (dict): Data for use-case mapped microsystems.
        visual_config (dict): Visualization configuration.
    """
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Plot RAMI 4.0 cube boundaries
    ax.set_xlim(visual_config['x_limits'])
    ax.set_ylim(visual_config['y_limits'])
    ax.set_zlim(visual_config['z_limits'])
    ax.set_xlabel("Hierarchy Levels (X-Axis)")
    ax.set_ylabel("Lifecycle Stages (Y-Axis)")
    ax.set_zlabel("Architecture Layers (Z-Axis)")
    ax.set_title("3D Visualization of Microsystems in RAMI 4.0 Cube")

    # Visualize microsystems
    for microsystem in usecase_data['microsystems']:
        center = (
            microsystem['coordinates']['X'],
            microsystem['coordinates']['Y'],
            microsystem['coordinates']['Z']
        )
        radii = visual_config['ellipsoid_radii']
        color = visual_config['stakeholder_colors'].get(microsystem['stakeholder'], 'blue')
        draw_ellipsoid(ax, center, radii, color)

    # Visualize interactions
    for interaction in usecase_data['interactions']:
        source = next(m for m in usecase_data['microsystems'] if m['id'] == interaction['source_id'])
        target = next(m for m in usecase_data['microsystems'] if m['id'] == interaction['target_id'])
        ax.plot(
            [source['coordinates']['X'], target['coordinates']['X']],
            [source['coordinates']['Y'], target['coordinates']['Y']],
            [source['coordinates']['Z'], target['coordinates']['Z']],
            color='black', linestyle='--', alpha=0.8
        )

    plt.show()

def main(system_data_path, usecase_data_path, config_path):
    """
    Main function to execute the 3D visualization.

    Args:
        system_data_path (str): Path to the system mapped data file (JSON).
        usecase_data_path (str): Path to the use-case mapped data file (JSON).
        config_path (str): Path to the visualization configuration file (JSON).
    """
    with open(system_data_path, 'r') as system_file:
        system_data = json.load(system_file)
    
    with open(usecase_data_path, 'r') as usecase_file:
        usecase_data = json.load(usecase_file)
    
    visual_config = load_visual_config(config_path)
    visualize_3d_rami_cube(system_data, usecase_data, visual_config)

if __name__ == "__main__":
    system_data_path = "system_mapped_data.json"  # Replace with actual path
    usecase_data_path = "usecase_mapped_data.json"  # Replace with actual path
    config_path = "visual_config.json"  # Replace with actual path
    main(system_data_path, usecase_data_path, config_path)
