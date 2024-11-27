### README.md for Algorithm 4: System-of-Microsystems Interaction Matrix, Clustering, and Phase Assignment

```markdown
# Algorithm 4: System-of-Microsystems Interaction Matrix, Clustering, and Phase Assignment

This repository contains the implementation of **Algorithm 4** from the RAMI 4.0 Value Chain Analysis methodology. The algorithm constructs an interaction matrix for a system-of-microsystems, performs clustering to group microsystems based on interaction density, and assigns engineering phases to the microsystems.

---

## Overview

Algorithm 4 helps visualize and analyze microsystem interactions by:
1. Creating an **Interaction Matrix** based on system and use case data.
2. Performing **Clustering** to group microsystems based on their interactions.
3. Assigning relevant **Engineering Phases** to each microsystem.
4. **Visualizing** the clustered interaction matrix.

---

## Prerequisites

- **Python**: Version 3.7 or later
- **Libraries**:
  - `numpy` (for numerical operations)
  - `json` (Python standard library for JSON handling)
  - `scikit-learn` (for clustering)
  - `matplotlib` (for visualization)

Install dependencies using:
```bash
pip install numpy scikit-learn matplotlib
```

---

## Files in This Directory

```
.
├── algorithm4.py                # Python script implementing Algorithm 4
├── system_mapped_data.json      # Input JSON file containing mapped microsystem data (from Algorithm 2)
├── usecase_mapped_data.json     # Input JSON file containing filtered data for the workflow (from Algorithm 3)
├── updated_system_data.json     # Output JSON file with clustered and phase-assigned microsystem data
└── README.md                    # Documentation for Algorithm 4
```

---

## How to Use

1. **Prepare Files**:
   - Place `system_mapped_data.json` (from Algorithm 2) and `usecase_mapped_data.json` (from Algorithm 3) in the working directory.

2. **Run the Script**:
   ```bash
   python algorithm4.py
   ```

3. **Output**:
   - The script saves the updated system data with cluster assignments and engineering phases to `updated_system_data.json`.
   - A clustered interaction matrix is displayed for visualization.

---

## Input and Output

### Input File 1 (`system_mapped_data.json`):
This file contains system data with microsystems and interactions. Example structure:
```json
{
    "microsystems": [
        {
            "id": "123",
            "provides": ["ServiceA"],
            "consumes": ["ServiceB"],
            "involvement": ["Design", "Production"]
        },
        {
            "id": "124",
            "provides": ["ServiceB"],
            "consumes": ["ServiceA"],
            "involvement": ["Maintenance"]
        }
    ],
    "interactions": [
        {
            "source_id": "123",
            "target_id": "124",
            "service": "ServiceA"
        }
    ]
}
```

### Input File 2 (`usecase_mapped_data.json`):
This file contains filtered data specific to a workflow. Example structure:
```json
{
    "microsystems": [
        {
            "id": "123",
            "provides": ["ServiceA"],
            "consumes": ["ServiceB"]
        }
    ],
    "interactions": [
        {
            "source_id": "123",
            "target_id": "124",
            "service": "ServiceA"
        }
    ]
}
```

### Output File (`updated_system_data.json`):
This file contains microsystem data with cluster labels and assigned phases. Example structure:
```json
{
    "microsystems": [
        {
            "id": "123",
            "provides": ["ServiceA"],
            "consumes": ["ServiceB"],
            "involvement": ["Design", "Production"],
            "phases": ["Design", "Production"],
            "cluster": 0
        },
        {
            "id": "124",
            "provides": ["ServiceB"],
            "consumes": ["ServiceA"],
            "involvement": ["Maintenance"],
            "phases": ["Maintenance"],
            "cluster": 1
        }
    ]
}
```

---

## Workflow Example

1. **Input**:
   - System data with interactions and workflow-specific filtered data.

2. **Interaction Matrix**:
   - Constructs a binary matrix showing interactions between microsystems.

3. **Clustering**:
   - Groups microsystems based on interaction density. Example clusters:
     - Cluster 0: Microsystem `123`
     - Cluster 1: Microsystem `124`

4. **Phase Assignment**:
   - Assigns phases like "Design" or "Maintenance" to microsystems based on their involvement.

5. **Output**:
   - Clustered and phase-assigned microsystem data.

---

## Visualization

The script visualizes the interaction matrix with clusters:

- **Rows/Columns**: Microsystem IDs, reordered by cluster assignment.
- **Color Intensity**: Interaction strength (binary in this case).

Example visualization:

![Interaction Matrix Visualization](https://via.placeholder.com/600x400?text=Interaction+Matrix)

---

## Error Handling

1. **Missing Data**:
   - Ensure both `system_mapped_data.json` and `usecase_mapped_data.json` exist and are valid.

2. **Clustering Errors**:
   - Ensure the interaction matrix has sufficient data for clustering.

3. **Invalid Input**:
   - Verify that all input files are in valid JSON format.

---

## Troubleshooting

- **Empty Clusters**:
  - Check the use case data to ensure it contains relevant interactions.
- **Incorrect Visualization**:
  - Verify that the system data and use case data align correctly.

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
