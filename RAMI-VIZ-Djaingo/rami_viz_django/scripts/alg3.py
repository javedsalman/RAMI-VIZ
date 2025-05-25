"""
Algorithm 3: Dynamic Workflow and Lifecycle Phase Mapping
----------------------------------------------------------
This module filters and maps microsystems relevant to a specific workflow.
It narrows down the list of microsystems based on services they provide or consume,
focusing the analysis on a specific operational or engineering workflow.

Author: Salman Javed
"""

def run(mapped_microsystems, workflow_services):
    """
    Filters microsystems based on relevance to a workflow.

    Parameters:
        mapped_microsystems (list): List of microsystems with x, y, z coordinates (from Algorithm 2)
        workflow_services (list): List of services relevant to the workflow

    Returns:
        list: Filtered microsystems relevant to the workflow
    """
    relevant = []

    for micro in mapped_microsystems:
        provides = micro["microsystem"].get("provides", [])
        consumes = micro["microsystem"].get("consumes", [])

        if any(service in provides for service in workflow_services) or            any(service in consumes for service in workflow_services):
            relevant.append(micro)

    return relevant
