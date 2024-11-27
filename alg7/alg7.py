import json
import matplotlib.pyplot as plt
import pandas as pd

def load_data(usecase_data_path, value_metrics_path, system_components_path):
    """
    Load data from JSON files.

    Args:
        usecase_data_path (str): Path to the use case mapped data JSON file.
        value_metrics_path (str): Path to the value metrics JSON file.
        system_components_path (str): Path to the system components data JSON file.

    Returns:
        tuple: Data from the respective JSON files.
    """
    with open(usecase_data_path, 'r') as usecase_file:
        usecase_data = json.load(usecase_file)
    with open(value_metrics_path, 'r') as metrics_file:
        value_metrics = json.load(metrics_file)
    with open(system_components_path, 'r') as components_file:
        system_components = json.load(components_file)
    
    return usecase_data, value_metrics, system_components

def create_integration_map(usecase_data, value_metrics, system_components, phases, lifecycle_stages):
    """
    Create an integration map aligning engineering process phases with product lifecycle stages.

    Args:
        usecase_data (dict): Data related to use case.
        value_metrics (dict): Value metrics such as cost, profit, and environmental impact.
        system_components (dict): Data related to system components and stakeholders.
        phases (list): List of engineering process phases.
        lifecycle_stages (list): List of product lifecycle stages.

    Returns:
        pd.DataFrame: Integration map matrix.
    """
    stakeholders = {comp['stakeholder'] for comp in system_components['components']}
    integration_map = pd.DataFrame(0, index=stakeholders, columns=phases + lifecycle_stages)

    for interaction in usecase_data['interactions']:
        source = interaction['source_id']
        target = interaction['target_id']
        source_stakeholder = next(comp['stakeholder'] for comp in system_components['components'] if comp['id'] == source)
        target_stakeholder = next(comp['stakeholder'] for comp in system_components['components'] if comp['id'] == target)
        
        for phase in phases:
            integration_map.loc[source_stakeholder, phase] += 1
            integration_map.loc[target_stakeholder, phase] += 1
        
        for stage in lifecycle_stages:
            integration_map.loc[source_stakeholder, stage] += 1
            integration_map.loc[target_stakeholder, stage] += 1
    
    return integration_map

def annotate_value_metrics(integration_map, value_metrics):
    """
    Annotate the integration map with value metrics.

    Args:
        integration_map (pd.DataFrame): Integration map matrix.
        value_metrics (dict): Value metrics to annotate.

    Returns:
        pd.DataFrame: Annotated integration map.
    """
    for stakeholder in integration_map.index:
        for phase in integration_map.columns:
            if phase in value_metrics.get(stakeholder, {}):
                integration_map.loc[stakeholder, phase] += value_metrics[stakeholder][phase]
    return integration_map

def visualize_integration_map(integration_map):
    """
    Visualize the integration map as a heatmap.

    Args:
        integration_map (pd.DataFrame): Annotated integration map.
    """
    plt.figure(figsize=(12, 8))
    plt.imshow(integration_map, cmap="YlGnBu", aspect="auto")
    plt.colorbar(label="Involvement Level / Value Metric")
    plt.xticks(range(len(integration_map.columns)), integration_map.columns, rotation=90)
    plt.yticks(range(len(integration_map.index)), integration_map.index)
    plt.title("Engineering Process Phases and Product Lifecycle Integration Map")
    plt.xlabel("Phases and Lifecycle Stages")
    plt.ylabel("Stakeholders")
    plt.tight_layout()
    plt.show()

def main(usecase_data_path, value_metrics_path, system_components_path, phases, lifecycle_stages):
    """
    Main function to execute Algorithm 7.

    Args:
        usecase_data_path (str): Path to the use case mapped data JSON file.
        value_metrics_path (str): Path to the value metrics JSON file.
        system_components_path (str): Path to the system components JSON file.
        phases (list): List of engineering process phases.
        lifecycle_stages (list): List of product lifecycle stages.
    """
    usecase_data, value_metrics, system_components = load_data(usecase_data_path, value_metrics_path, system_components_path)
    integration_map = create_integration_map(usecase_data, value_metrics, system_components, phases, lifecycle_stages)
    annotated_map = annotate_value_metrics(integration_map, value_metrics)
    visualize_integration_map(annotated_map)

if __name__ == "__main__":
    # Example paths and configurations
    usecase_data_path = "usecase_mapped_data.json"  # Replace with actual path
    value_metrics_path = "value_metrics.json"       # Replace with actual path
    system_components_path = "system_components.json"  # Replace with actual path

    phases = ["Design", "Development", "Production", "Maintenance"]
    lifecycle_stages = ["Concept", "Operation", "Disposal"]

    main(usecase_data_path, value_metrics_path, system_components_path, phases, lifecycle_stages)
