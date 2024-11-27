import json

def load_mapping_configuration(config_path):
    """
    Load mapping configuration rules for RAMI 4.0 axes.
    
    Args:
        config_path (str): Path to the mapping configuration JSON file.
    
    Returns:
        dict: Mapping rules.
    """
    with open(config_path, 'r') as file:
        mapping_config = json.load(file)
    return mapping_config

def map_to_rami_axes(json_data, mapping_config):
    """
    Map microsystems to RAMI 4.0 axes using rule-based mapping.
    
    Args:
        json_data (dict): Preprocessed and validated JSON data of microsystems.
        mapping_config (dict): Rule-based mapping configuration.
    
    Returns:
        dict: Mapped data with coordinates for each microsystem.
    """
    system_mapped_data = []
    
    for microsystem in json_data['microsystems']:
        mapped_data = {
            'id': microsystem['id'],
            'coordinates': {}
        }
        
        # Map to X-Axis (Hierarchy Level)
        x_rules = mapping_config['hierarchy_rules']
        mapped_data['coordinates']['X'] = map_to_axis(microsystem, x_rules, axis="X")
        
        # Map to Y-Axis (Lifecycle Stage)
        y_rules = mapping_config['lifecycle_rules']
        mapped_data['coordinates']['Y'] = map_to_axis(microsystem, y_rules, axis="Y")
        
        # Map to Z-Axis (Architecture Layer)
        z_rules = mapping_config['layer_rules']
        mapped_data['coordinates']['Z'] = map_to_axis(microsystem, z_rules, axis="Z")
        
        system_mapped_data.append(mapped_data)
    
    return system_mapped_data

def map_to_axis(microsystem, rules, axis):
    """
    Apply mapping rules for a specific RAMI 4.0 axis.
    
    Args:
        microsystem (dict): Microsystem data to be mapped.
        rules (list): Rules for mapping to a specific axis.
        axis (str): The axis being mapped (X, Y, or Z).
    
    Returns:
        int: Coordinate value for the specified axis.
    """
    for rule in rules:
        if all(microsystem.get(attr) == value for attr, value in rule['conditions'].items()):
            return rule['mapping']
    
    # If no rule matches, prompt user for mapping (mocked here for simplicity)
    print(f"No rule matches for microsystem ID {microsystem['id']} on {axis}-axis.")
    user_input = int(input(f"Please provide a {axis}-axis mapping for microsystem ID {microsystem['id']}: "))
    return user_input

def main(input_path, config_path, output_path):
    """
    Main function to load data, map microsystems, and save the output.
    
    Args:
        input_path (str): Path to the input JSON data file.
        config_path (str): Path to the mapping configuration JSON file.
        output_path (str): Path to save the mapped data.
    """
    # Load input data
    with open(input_path, 'r') as file:
        json_data = json.load(file)
    
    # Load mapping configuration
    mapping_config = load_mapping_configuration(config_path)
    
    # Map microsystems to RAMI 4.0 axes
    system_mapped_data = map_to_rami_axes(json_data, mapping_config)
    
    # Save output data
    with open(output_path, 'w') as file:
        json.dump(system_mapped_data, file, indent=4)
    
    print(f"Mapped data has been saved to {output_path}.")

if __name__ == "__main__":
    input_path = "input.json"  # Replace with actual input file path
    config_path = "mapping_config.json"  # Replace with actual config file path
    output_path = "mapped_output.json"  # Replace with desired output file path
    main(input_path, config_path, output_path)
