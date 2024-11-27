import json


def filter_dynamic_workflow(system_mapped_data, workflow_data):
    """
    Filters system mapped data based on a selected workflow and lifecycle phase.

    Args:
        system_mapped_data (dict): The mapped data of microsystems from previous steps.
        workflow_data (dict): Data of the selected workflow, including steps, services, and interactions.

    Returns:
        dict: Filtered data with microsystems and interactions specific to the selected workflow.
    """
    # Initialize structure for storing relevant microsystems and interactions
    usecase_mapped_data = {"microsystems": [], "interactions": []}

    # Process each workflow step
    for step in workflow_data['steps']:
        step_id = step['step_id']
        services = step['services']
        interactions = step['interactions']

        # Filter microsystems based on services
        filtered_microsystems = [
            m for m in system_mapped_data['microsystems']
            if any(service in m['provides'] for service in services) or
               any(service in m['consumes'] for service in services)
        ]
        usecase_mapped_data['microsystems'].extend(filtered_microsystems)

        # Filter interactions between these microsystems
        for interaction in interactions:
            if interaction['source_id'] in [m['id'] for m in filtered_microsystems] and \
               interaction['target_id'] in [m['id'] for m in filtered_microsystems]:
                usecase_mapped_data['interactions'].append(interaction)

    # Remove duplicates
    usecase_mapped_data['microsystems'] = list({m['id']: m for m in usecase_mapped_data['microsystems']}.values())
    usecase_mapped_data['interactions'] = list({f"{i['source_id']}-{i['target_id']}": i
                                                for i in usecase_mapped_data['interactions']}.values())

    return usecase_mapped_data


def main(system_data_path, workflow_data_path, output_path):
    """
    Main function to filter data dynamically based on workflows.

    Args:
        system_data_path (str): Path to the system mapped data file (JSON format).
        workflow_data_path (str): Path to the workflow data file (JSON format).
        output_path (str): Path to save the filtered data.
    """
    # Load system mapped data
    with open(system_data_path, 'r') as system_file:
        system_mapped_data = json.load(system_file)

    # Load workflow data
    with open(workflow_data_path, 'r') as workflow_file:
        workflow_data = json.load(workflow_file)

    # Perform dynamic workflow filtering
    filtered_data = filter_dynamic_workflow(system_mapped_data, workflow_data)

    # Save the filtered data
    with open(output_path, 'w') as output_file:
        json.dump(filtered_data, output_file, indent=4)

    print(f"Filtered data saved to {output_path}")


if __name__ == "__main__":
    # Example file paths
    system_data_path = "system_mapped_data.json"  # Replace with actual file path
    workflow_data_path = "workflow_data.json"    # Replace with actual file path
    output_path = "usecase_mapped_data.json"     # Replace with desired output file path

    main(system_data_path, workflow_data_path, output_path)
