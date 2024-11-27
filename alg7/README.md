### README.md for Algorithm 7: Engineering Process Phases and Product Lifecycle Integration Map

```markdown
# Algorithm 7: Engineering Process Phases and Product Lifecycle Integration Map

This repository contains the implementation of **Algorithm 7** from the RAMI 4.0 Value Chain Analysis methodology. The algorithm creates an integration map aligning engineering process phases with product lifecycle stages, annotates it with value metrics, and visualizes it as a heatmap.

---

## Overview

Algorithm 7 provides insights into stakeholder interactions and involvement levels across:
1. **Engineering Phases**: Captures contributions in design, development, production, and maintenance.
2. **Lifecycle Stages**: Tracks involvement from concept to operation and disposal.
3. **Value Metrics**: Annotates cost, profit, and environmental impact metrics for stakeholders.

The output is a heatmap visualization of the integration map.

---

## Prerequisites

- **Python**: Version 3.7 or later
- **Libraries**:
  - `pandas` (for data manipulation)
  - `matplotlib` (for visualization)
  - `json` (Python standard library for JSON handling)

Install dependencies using:
```bash
pip install pandas matplotlib
```

---

## Files in This Directory

```
.
├── algorithm7.py             # Python script implementing Algorithm 7
├── usecase_mapped_data.json  # Input JSON file containing use-case data
├── value_metrics.json        # Input JSON file with value metrics for stakeholders
├── system_components.json    # Input JSON file with system components and stakeholders
├── README.md                 # Documentation for Algorithm 7
```

---

## How to Use

1. **Prepare Files**:
   - Place `usecase_mapped_data.json`, `value_metrics.json`, and `system_components.json` in the working directory.

2. **Run the Script**:
   ```bash
   python algorithm7.py
   ```

3. **Output**:
   - The script generates a heatmap visualizing stakeholder involvement and value metrics across phases and lifecycle stages.

---

## Input and Configuration

### Input File 1 (`usecase_mapped_data.json`):
Contains interactions and microsystems relevant to the selected use case. Example structure:
```json
{
    "microsystems": [
        {"id": "123", "stakeholder": "Stakeholder-A"},
        {"id": "124", "stakeholder": "Stakeholder-B"}
    ],
    "interactions": [
        {"source_id": "123", "target_id": "124"}
    ]
}
```

### Input File 2 (`value_metrics.json`):
Provides cost, profit, and environmental impact metrics for stakeholders. Example structure:
```json
{
    "Stakeholder-A": {
        "Design": 2000,
        "Development": 5000,
        "Production": 8000
    },
    "Stakeholder-B": {
        "Maintenance": 3000,
        "Operation": 7000
    }
}
```

### Input File 3 (`system_components.json`):
Defines system components and their stakeholders. Example structure:
```json
{
    "components": [
        {"id": "123", "stakeholder": "Stakeholder-A"},
        {"id": "124", "stakeholder": "Stakeholder-B"}
    ]
}
```

### Configurations:
Define phases and lifecycle stages directly in the script:
```python
phases = ["Design", "Development", "Production", "Maintenance"]
lifecycle_stages = ["Concept", "Operation", "Disposal"]
```

---

## Visualization Example

The heatmap includes:
1. **Stakeholders (Rows)**: Represent each stakeholder involved.
2. **Phases and Lifecycle Stages (Columns)**: Engineering process phases and lifecycle stages.
3. **Color Intensity**: Represents the level of involvement or value metrics.

Example heatmap:

![javed6](https://github.com/user-attachments/assets/d5e7cd7f-6111-47af-8c7e-9de99af0e2bf)


---

## Troubleshooting

1. **Missing Data**:
   - Ensure `usecase_mapped_data.json`, `value_metrics.json`, and `system_components.json` are present in the working directory.

2. **Invalid Input**:
   - Verify that the JSON files are well-formed and contain valid data structures.

3. **Visualization Errors**:
   - Ensure `pandas` and `matplotlib` are installed correctly.

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
