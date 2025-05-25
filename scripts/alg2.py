"""
Algorithm 2: Mapping of Microsystems to RAMI 4.0 Axes
-----------------------------------------------------
This module maps validated microsystems onto the three RAMI 4.0 axes:
- X-axis: Hierarchy Levels (e.g., field device, control device)
- Y-axis: Lifecycle & Value Stream (e.g., development, production)
- Z-axis: Architecture Layers (e.g., asset, integration)

Each axis uses rule-based mapping logic, with dynamic prompting or fallbacks.

Author: Salman Javed
"""

# Rule sets for X, Y, and Z axes
X_RULES = {
    ("Field Device", "sensor"): 1.0,
    ("Control Device", "controller"): 2.0,
    ("Station", "assembly"): 3.0,
    ("Work Center", "workflow"): 4.0,
    ("Enterprise", "analytics"): 5.0,
    ("Connected World", "cloud"): 6.0
}

Y_RULES = {
    "provides": {
        "design_docs": 0.0,  # Development (Type)
        "support_data": 1.0, # Maintenance/Usage (Type)
        "machine_data": 2.0, # Production (Instance)
        "maintenance_logs": 3.0 # Maintenance/Usage (Instance)
    }
}

Z_RULES = {
    "shell": {
        "physical": 0,
        "integration": 1,
        "communication": 2,
        "information": 3,
        "function": 4,
        "business": 5
    }
}

def map_x_axis(micro):
    key = (micro["microsystem"]["type"], micro["microsystem"]["role"])
    return X_RULES.get(key, -1.0)  # -1.0 means unmapped or undefined

def map_y_axis(micro):
    provides = micro["microsystem"].get("provides", [])
    for item in provides:
        for ref, y_val in Y_RULES["provides"].items():
            if ref in item:
                return y_val
    return -1.0  # default/fallback

def map_z_axis(micro):
    shell = micro["microsystem"].get("shell", [])
    z_vals = []
    for item in shell:
        for key, z in Z_RULES["shell"].items():
            if key in item.lower():
                z_vals.append(z)
    return list(set(z_vals))  # unique Z-layers

def run(validated_microsystems):
    """
    Maps each microsystem to RAMI 4.0 X, Y, Z axes.

    Parameters:
        validated_microsystems (list): List of valid microsystem dicts from Algorithm 1

    Returns:
        list: List of microsystems enriched with x, y, z coordinates
    """
    result = []
    for micro in validated_microsystems:
        mapped = micro.copy()
        mapped["coordinates"] = {
            "x": map_x_axis(micro),
            "y": map_y_axis(micro),
            "z": map_z_axis(micro)
        }
        result.append(mapped)
    return result
