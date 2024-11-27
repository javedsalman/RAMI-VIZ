### README.md for Algorithm 6: RAMI 4.0 Value Addition Projection with Metrics

```markdown
# Algorithm 6: RAMI 4.0 Value Addition Projection with Metrics

This repository contains the implementation of **Algorithm 6** from the RAMI 4.0 Value Chain Analysis methodology. The algorithm visualizes value addition metrics such as cost, profit, and environmental impact across the RAMI 4.0 axes, providing stakeholders with insights into microsystem performance.

---

## Overview

Algorithm 6 provides a 2D projection of microsystems in the RAMI 4.0 space:
1. Maps microsystems to a 2D plane based on hierarchy levels and lifecycle stages.
2. Visualizes value metrics as:
   - **Marker Size**: Represents profit.
   - **Marker Color**: Represents cost.
3. Provides annotations for microsystems to enhance interpretability.

---

## Prerequisites

- **Python**: Version 3.7 or later
- **Libraries**:
  - `matplotlib` (for visualization)
  - `numpy` (for numerical operations)
  - `json` (Python standard library for JSON handling)

Install dependencies using:
```bash
pip install matplotlib numpy
```

---

## Files in This Directory

```
.
├── algorithm6.py            # Python script implementing Algorithm 6
├── system_mapped_data.json  # Input JSON file containing mapped microsystem data (from Algorithm 2)
├── value_metrics.json       # Input JSON file with value metrics for microsystems
├── visual_config.json       # Configuration file for visualization settings
├── README.md                # Documentation for Algorithm 6
```

---

## How to Use

1. **Prepare Files**:
   - Place `system_mapped_data.json` (from Algorithm 2) and `value_metrics.json` in the working directory.
   - Create or update `visual_config.json` to customize visualization settings.

2. **Run the Script**:
   ```bash
   python algorithm6.py
   ```

3. **Output**:
   - The script generates a 2D scatter plot visualizing value metrics for microsystems.

---

## Input and Configuration

### Input File 1 (`system_mapped_data.json`):
This file contains system-level data with microsystem coordinates and attributes. Example structure:
```json
{
    "microsystems": [
        {
            "id": "123",
            "coordinates": {"X": 2, "Y": 1, "Z": 3}
        },
        {
            "id": "124",
            "coordinates": {"X": 4, "Y": 2, "Z": 1}
        }
    ]
}
```

### Input File 2 (`value_metrics.json`):
This file contains value metrics for microsystems, including cost, profit, and environmental impact. Example structure:
```json
{
    "123": {
        "profit": 5000,
        "cost": 2000,
        "environmental_impact": 100
    },
    "124": {
        "profit": 3000,
        "cost": 1500,
        "environmental_impact": 50
    }
}
```

### Configuration File (`visual_config.json`):
This file defines visualization settings, such as axis labels and marker properties. Example structure:
```json
{
    "x_limits": [0, 6],
    "y_limits": [0, 4],
    "z_limits": [0, 5],
    "marker_scale_factor": 0.05,
    "axis_labels": {
        "x": "Hierarchy Levels",
        "y": "Lifecycle Stages",
        "z": "Architecture Layers"
    }
}
```

---

## Visualization Example

The scatter plot includes:
1. **Marker Size**: Proportional to the profit metric.
2. **Marker Color**: Represents the cost metric.

Example plot:

![javed4](https://github.com/user-attachments/assets/6a97e99e-0115-45c3-a8d2-af64391ebc41)

---

## Troubleshooting

1. **Missing Data**:
   - Ensure `system_mapped_data.json`, `value_metrics.json`, and `visual_config.json` are present in the working directory.

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
