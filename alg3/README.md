### README.md for Algorithm 3: Dynamic Workflow and Lifecycle Phase Mapping

```markdown
# Algorithm 3: Dynamic Workflow and Lifecycle Phase Mapping

This repository contains the implementation of **Algorithm 3** from the RAMI 4.0 Value Chain Analysis methodology. The algorithm dynamically maps workflows and lifecycle phases to filtered microsystem data, enabling stakeholders to focus on specific workflows or lifecycle stages in the RAMI 4.0 cube.

---

## Overview

Algorithm 3 filters and maps microsystems and interactions based on:
1. **Workflow Steps**: Identifies microsystems relevant to a specific workflow.
2. **Lifecycle Phases**: Maps interactions and services associated with a given lifecycle phase.
3. **Use Case-Specific Mapping**: Dynamically adjusts mapping for different workflows or lifecycle phases.

The output is a filtered dataset containing only the relevant microsystems and their interactions.

---

## Prerequisites

- **Python**: Version 3.7 or later
- **Libraries**:
  - `json` (Python standard library for JSON handling)

---

## Files in This Directory

```
.
├── algorithm3.py           # Python script implementing Algorithm 3
├── system_mapped_data.json # Input JSON file containing mapped microsystem data (from Algorithm 2)
├── workflow_data.json      # Input JSON file defining workflow steps and interactions
├── usecase_mapped_data.json# Output JSON file with filtered data for the workflow
└── README.md               # Documentation for Algorithm 3
```

---

## How to Use

1. **Prepare Files**:
   - Place `system_mapped_data.json` (output from Algorithm 2) in the working directory.
   - Create or update `workflow_data.json` to define workflow steps and interactions.

2. **Run the Script**:
   ```bash
   python algorithm3.py
   ```

3. **Output**:
   - The script processes the input data and saves the filtered results to `usecase_mapped_data.json`.

---

## Input and Output

### Input File 1 (`system_mapped_data.json`):
This file contains mapped data of microsystems and interactions from Algorithm 2. Example structure:
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

### Input File 2 (`workflow_data.json`):
This file defines workflows and their steps, including services and interactions. Example structure:
```json
{
    "steps": [
        {
            "step_id": "Step1",
            "services": ["ServiceA", "ServiceC"],
            "interactions": [
                {"source_id": "123", "target_id": "124"}
            ]
        }
    ]
}
```

### Output File (`usecase_mapped_data.json`):
This file contains microsystems and interactions filtered for the selected workflow. Example structure:
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

---

## Workflow Example

1. **Input**:
   - A workflow requires `ServiceA` and involves interactions between microsystems `123` and `124`.

2. **Filtering**:
   - Microsystem `123` is selected because it provides `ServiceA`.
   - Interaction between `123` and `124` is included since it matches the workflow definition.

3. **Output**:
   - Filtered data includes microsystem `123` and its interaction with `124`.

---

## Error Handling

1. **Missing Workflow Data**:
   - Ensure `workflow_data.json` exists and follows the expected structure.

2. **No Matching Microsystems**:
   - If no microsystems match the workflow's required services, the output will be empty.

3. **Invalid Input**:
   - Verify that both `system_mapped_data.json` and `workflow_data.json` contain valid JSON.

---

## Troubleshooting

- **Empty Output**:
  - Check the workflow definitions in `workflow_data.json` to ensure they align with the services and interactions in `system_mapped_data.json`.
- **File Not Found**:
  - Ensure the file paths for the input files are correct.

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
