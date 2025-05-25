"""
Algorithm 6: RAMI 4.0 Value Addition Projection
-----------------------------------------------
This module projects value-related metrics (e.g., cost, profit) of microsystems
on the X (Hierarchy) and Y (Lifecycle) axes to visualize where value is being created
or costs are being incurred in the system.

Author: Salman Javed
"""

def run(microsystems):
    """
    Projects cost and value metrics of microsystems on RAMI axes.

    Parameters:
        microsystems (list): List of microsystems with 'coordinates' and value info

    Returns:
        list: Each entry contains:
              {
                  'id': microsystem ID,
                  'x': RAMI X-axis (hierarchy level),
                  'y': RAMI Y-axis (lifecycle stage),
                  'cost': numeric cost value,
                  'value': numeric value addition
              }
    """
    projections = []

    for m in microsystems:
        coords = m.get("coordinates", {})
        x = coords.get("x", -1)
        y = coords.get("y", -1)

        # Retrieve cost/value metrics
        cost = m.get("metrics", {}).get("cost", 0)
        value = m.get("metrics", {}).get("value", 0)

        projections.append({
            "id": m["microsystem"]["id"],
            "x": x,
            "y": y,
            "cost": cost,
            "value": value
        })

    return projections
