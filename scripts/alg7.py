"""
Algorithm 7: Engineering Process Phases and Product Lifecycle Integration Map
------------------------------------------------------------------------------
Links engineering activities and system components to RAMI lifecycle phases.
Tracks transitions across lifecycle stages and engineering domains.

Generates timelines and phase associations to support traceability and reuse.

Author: Salman Javed
"""

def run(microsystems):
    """
    Maps engineering processes and product lifecycle phases from microsystem metadata.

    Parameters:
        microsystems (list): List of microsystems with coordinates and process phase info

    Returns:
        dict: {
            'phases': list of unique phases,
            'timeline': list of {
                'id': microsystem ID,
                'phase': phase name,
                'x': RAMI X,
                'y': RAMI Y,
                'description': microsystem name
            }
        }
    """
    timeline = []
    unique_phases = set()

    for m in microsystems:
        phase = m.get("microsystem", {}).get("phase", "unspecified")
        coords = m.get("coordinates", {})
        x = coords.get("x", -1)
        y = coords.get("y", -1)

        unique_phases.add(phase)

        timeline.append({
            "id": m["microsystem"]["id"],
            "phase": phase,
            "x": x,
            "y": y,
            "description": m["microsystem"].get("name", "")
        })

    return {
        "phases": list(unique_phases),
        "timeline": timeline
    }
