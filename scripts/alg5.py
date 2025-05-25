"""
Algorithm 5: 3D Visualization of Microsystems in RAMI 4.0 Cubes
----------------------------------------------------------------
This algorithm prepares the 3D spatial coordinates for each microsystem
within the RAMI 4.0 cube using (x, y, z) mapped values and interaction clusters.

The output is a structured dataset ready for 3D Plotly visualization.

Author: Salman Javed
"""

import random

def generate_3d_points(microsystems, clusters):
    """
    Assigns spatial 3D positions to each microsystem in the RAMI 4.0 cube.

    Parameters:
        microsystems (list): List of microsystems with 'coordinates'
        clusters (dict): Dictionary mapping microsystem index to cluster ID

    Returns:
        list: Each entry contains:
              {
                  'id': microsystem ID,
                  'name': name,
                  'x': RAMI hierarchy axis (0–6),
                  'y': lifecycle axis (0–3),
                  'z': RAMI layer (0–5),
                  'cluster': cluster ID,
                  'stakeholder': stakeholder description,
                  'type': type
              }
    """
    spatial_data = []

    for idx, m in enumerate(microsystems):
        coords = m.get("coordinates", {})
        x = coords.get("x", -1)
        y = coords.get("y", -1)
        z_list = coords.get("z", [])
        z_list = z_list if isinstance(z_list, list) else [z_list]
        cluster = clusters.get(idx, -1)

        for z in z_list:
            spatial_data.append({
                "id": m["microsystem"]["id"],
                "name": m["microsystem"]["name"],
                "x": x + random.uniform(-0.1, 0.1),
                "y": y + random.uniform(-0.1, 0.1),
                "z": z + random.uniform(-0.1, 0.1),
                "cluster": cluster,
                "stakeholder": m["microsystem_stakeholder"]["description"],
                "type": m["microsystem"]["type"]
            })

    return spatial_data
