### README.md for Algorithm 2: Mapping Microsystems to RAMI 4.0 Axes

```markdown
# Algorithm 2: Mapping Microsystems to RAMI 4.0 Axes

This repository contains the implementation of **Algorithm 2** from the RAMI 4.0 Value Chain Analysis methodology. The algorithm maps microsystems to the three axes of the RAMI 4.0 cube:
- **X-Axis**: Hierarchy Levels
- **Y-Axis**: Lifecycle & Value Stream Stages
- **Z-Axis**: Architecture Layers

---

## Overview

The purpose of this algorithm is to assign coordinate positions to microsystems based on a set of rule-based mapping configurations. Each microsystem is analyzed, and its attributes are matched against predefined conditions to determine its position along the RAMI 4.0 cube axes.

---

## Prerequisites

- **Python**: Version 3.7 or later
- **Libraries**:
  - `json` (Python standard library for JSON handling)

---

## Files in This Directory

```
.
├── algorithm2.py          # Python script implementing Algorithm 2
├── input.json             # Preprocessed JSON data from Algorithm 1
├── mapping_config.json    # Configuration file with rules for mapping
├── mapped_output.json     # Output JSON file with mapped coordinates
└── README.md              # Documentation for Algorithm 2
```

---

## How to Use

1. **Prepare Files**:
   - Ensure `input.json` (output from Algorithm 1) is placed in the working directory.
   - Create or edit `mapping_config.json` to define the mapping rules for each RAMI 4.0 axis.

2. **Run the Script**:
   ```bash
   python algorithm2.py
   ```

3. **Output**:
   - The script processes the input data and saves the mapped coordinates to `mapped_output.json`.

---

## Input and Output

### Input File (`input.json`):
This file contains preprocessed data from Algorithm 1. Example structure:
```json
{
    "microsystems": [
        {
            "id": "123",
            "name": "Example Microsystem",
            "description": "Test Microsystem",
            "type": "Field Device",
            "role": "Data Acquisition"
        }
    ]
}
```

### Mapping Configuration File (`mapping_config.json`):
This file defines rules for mapping each axis. Example structure:
```json
{
    "hierarchy_rules": [
        {
            "conditions": {
                "type": "Field Device"
            },
            "mapping": 1
        }
    ],
    "lifecycle_rules": [
        {
            "conditions": {
                "role": "Data Acquisition"
            },
            "mapping": 2
        }
    ],
    "layer_rules": [
        {
            "conditions": {
                "description": "Test Microsystem"
            },
            "mapping": 0
        }
    ]
}
```

### Output File (`mapped_output.json`):
This file contains the mapped coordinates for each microsystem. Example structure:
```json
[
    {
        "id": "123",
        "coordinates": {
            "X": 1,
            "Y": 2,
            "Z": 0
        }
    }
]
```

---

## Example Workflow

1. **Input**:
   - A microsystem with `type` = "Field Device", `role` = "Data Acquisition", and `description` = "Test Microsystem".

2. **Mapping Rules**:
   - `X-Axis` (Hierarchy Level): Maps "Field Device" to `1`.
   - `Y-Axis` (Lifecycle Stage): Maps "Data Acquisition" to `2`.
   - `Z-Axis` (Architecture Layer): Maps "Test Microsystem" to `0`.

3. **Output**:
   - The resulting coordinate mapping: `{"X": 1, "Y": 2, "Z": 0}`.

---

## Error Handling

1. **Missing Mapping Rules**:
   - If no rule matches, the script prompts the user to input the axis value manually.

2. **File Not Found**:
   - Ensure the paths to `input.json` and `mapping_config.json` are correct.

3. **Invalid Input**:
   - Ensure that the input file follows the expected structure and contains valid JSON.

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

