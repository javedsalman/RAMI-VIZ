### README.md for Algorithm 5: 3D Visualization of Microsystems in RAMI 4.0 Cubes

```markdown
# Algorithm 5: 3D Visualization of Microsystems in RAMI 4.0 Cubes

This repository contains the implementation of **Algorithm 5** from the RAMI 4.0 Value Chain Analysis methodology. The algorithm visualizes microsystems and their interactions in a 3D RAMI 4.0 cube, enabling stakeholders to analyze system dependencies and relationships.

---

## Overview

Algorithm 5 creates a 3D representation of the RAMI 4.0 cube:
- **Microsystems**: Represented as ellipsoids positioned by their X, Y, Z coordinates.
- **Interactions**: Represented as lines connecting microsystems.
- **Customization**: Configurable cube dimensions, ellipsoid sizes, and stakeholder-specific colors.

---

## Prerequisites

- **Python**: Version 3.7 or later
- **Libraries**:
  - `matplotlib` (for 3D visualization)
  - `numpy` (for ellipsoid geometry)
  - `json` (Python standard library for JSON handling)

Install dependencies using:
```bash
pip install matplotlib numpy
```

---

## Files in This Directory

```
.
├── algorithm5.py            # Python script implementing Algorithm 5
├── system_mapped_data.json  # Input JSON file containing mapped microsystem data (from Algorithm 2)
├── usecase_mapped_data.json # Input JSON file containing filtered use-case data (from Algorithm 3)
├── visual_config.json       # Configuration file for 3D visualization
├── README.md                # Documentation for Algorithm 5
```

---

## How to Use

1. **Prepare Files**:
   - Place `system_mapped_data.json` (from Algorithm 2) and `usecase_mapped_data.json` (from Algorithm 3) in the working directory.
   - Create or update `visual_config.json` to customize visualization settings.

2. **Run the Script**:
   ```bash
   python algorithm5.py
   ```

3. **Output**:
   - The script generates a 3D visualization of the RAMI 4.0 cube, displaying microsystems and their interactions.

---

## Input and Configuration

### Input File 1 (`system_mapped_data.json`):
This file contains system-level data with microsystem coordinates and attributes. Example structure:
```json
{
    "microsystems": [
        {
            "id": "123",
            "coordinates": {"X": 2, "Y": 1, "Z": 3},
            "stakeholder": "Stakeholder-1"
        },
        {
            "id": "124",
            "coordinates": {"X": 4, "Y": 2, "Z": 1},
            "stakeholder": "Stakeholder-2"
        }
    ]
}
```

### Input File 2 (`usecase_mapped_data.json`):
This file contains use-case-specific filtered microsystems and interactions. Example structure:
```json
{
    "microsystems": [
        {
            "id": "123",
            "coordinates": {"X": 2, "Y": 1, "Z": 3},
            "stakeholder": "Stakeholder-1"
        },
        {
            "id": "124",
            "coordinates": {"X": 4, "Y": 2, "Z": 1},
            "stakeholder": "Stakeholder-2"
        }
    ],
    "interactions": [
        {
            "source_id": "123",
            "target_id": "124"
        }
    ]
}
```

### Configuration File (`visual_config.json`):
This file defines visualization settings such as cube dimensions, ellipsoid radii, and stakeholder colors. Example structure:
```json
{
    "x_limits": [0, 6],
    "y_limits": [0, 4],
    "z_limits": [0, 5],
    "ellipsoid_radii": [0.2, 0.1, 0.3],
    "stakeholder_colors": {
        "Stakeholder-1": "red",
        "Stakeholder-2": "green",
        "Stakeholder-3": "blue"
    }
}
```

---

## Workflow Example

1. **Input**:
   - Two microsystems (`123` and `124`) are filtered for a use case.
   - Interaction exists between `123` and `124`.

2. **Visualization**:
   - Ellipsoids are drawn for microsystems based on their X, Y, Z coordinates.
   - Lines are drawn between `123` and `124` to represent interactions.

3. **Customization**:
   - Ellipsoid sizes and colors are set using the visualization configuration file.

---

## Visualization Output

The visualization includes:
1. **Microsystems**:
   - Ellipsoids positioned at X, Y, Z coordinates.
   - Color-coded based on stakeholder ownership.

2. **Interactions**:
   - Dashed lines connecting microsystems to show dependencies.

Example visualization:

![javed7](https://github.com/user-attachments/assets/fd4cf83e-8c61-46ef-a6ce-42dad4997210)

---

## Troubleshooting

1. **Missing Data**:
   - Ensure `system_mapped_data.json`, `usecase_mapped_data.json`, and `visual_config.json` are present in the working directory.

2. **Invalid Input**:
   - Verify that the JSON files are well-formed and contain valid data structures.

3. **Visualization Errors**:
   - Ensure `matplotlib` and `numpy` are installed correctly.

---

## Contributing

We welcome contributions to improve this implementation! Feel free to:
- Open issues for bug reports or feature requests.
- Submit pull requests with your improvements.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact

For questions or feedback, contact:
[Salman Javed](mailto:salman.jvd@gmail.com)
```
