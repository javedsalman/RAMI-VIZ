
```markdown
# Algorithm 1: Input Specification and Preprocessing

This repository contains the implementation of **Algorithm 1** from the RAMI 4.0 Value Chain Analysis methodology. The algorithm is responsible for validating and preprocessing input data files (e.g., DSL/XMI format) against the RAMI 4.0 schema and transforming them into a structured JSON format for further analysis.

---

## Overview

Algorithm 1 ensures input data conforms to the RAMI 4.0 schema, allowing for accurate analysis and integration into subsequent steps of the methodology. Key features include:
- **Validation**: Checks if input files meet the RAMI 4.0 XML schema requirements.
- **Transformation**: Converts the validated data into JSON format.
- **Error Handling**: Provides feedback if validation fails.

---

## Prerequisites

- **Python**: Version 3.7 or later
- **Libraries**:
  - `xmlschema` (for schema validation)
  - `json` (Python standard library for JSON serialization)

Install dependencies using:
```bash
pip install xmlschema
```

---

## Files in This Directory

```
.
├── algorithm1.py        # Python script implementing Algorithm 1
├── schem_rami_xsd.tex   # RAMI 4.0 schema file (XSD format)
├── input_file.tex       # Example input data file (DSL/XMI format)
├── output.json          # Generated JSON file (after successful execution)
└── README.md            # Documentation for Algorithm 1
```

---

## How to Use

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/javedsalman/RAMI4.0-VIZ/tree/2d5c90b7e7ea7d6e629f03e036319c2ef491a5cf/alg1.git
   cd alg1
   ```

2. **Prepare Files**:
   - Place your RAMI schema file (`schem_rami_xsd.tex`) and input data file (`input_file.tex`) in the working directory.

3. **Set File Paths**:
   - Update the `SCHEMA_FILE`, `INPUT_FILE`, and `OUTPUT_JSON` variables in `algorithm1.py` to match your file locations.

4. **Run the Script**:
   ```bash
   python algorithm1.py
   ```

5. **Output**:
   - The script validates the input file. If successful, a structured JSON file (`output.json`) is generated in the specified location.
   - If validation fails, error details are printed in the console.

---

## Python Code

### algorithm1.py

```python
import xmlschema
import json

# Paths to input and schema files
SCHEMA_FILE = "path/to/schem_rami_xsd.tex"  # Replace with the schema file path
INPUT_FILE = "path/to/input_file.tex"       # Replace with the DSL or XMI input file path
OUTPUT_JSON = "path/to/output.json"         # Replace with the desired output JSON file path

def validate_and_transform(input_file, schema_file, output_file):
    """
    Validate the input XML file against the RAMI schema and convert it to JSON.
    Args:
        input_file (str): Path to the XML input file (e.g., DSL or XMI format).
        schema_file (str): Path to the RAMI schema file.
        output_file (str): Path to the output JSON file.
    Returns:
        str: Success or failure message.
    """
    try:
        # Load the schema
        schema = xmlschema.XMLSchema(schema_file)

        # Validate the input file
        if schema.is_valid(input_file):
            # Parse the file to a dictionary
            data_dict = schema.to_dict(input_file)
            
            # Write the dictionary as JSON
            with open(output_file, 'w') as json_file:
                json.dump(data_dict, json_file, indent=4)
            
            return f"Validation successful. JSON saved at {output_file}"
        else:
            return "Validation failed. Input file does not conform to the schema."
    except Exception as e:
        return f"Error: {str(e)}"

# Execution
result = validate_and_transform(INPUT_FILE, SCHEMA_FILE, OUTPUT_JSON)
print(result)
```

---

## Input and Output Examples

### Input File (`input_file.tex`):
```xml
<microsystem>
    <id>123</id>
    <name>Example Microsystem</name>
    <description>Test Microsystem</description>
    <type>Field Device</type>
    <role>Data Acquisition</role>
</microsystem>
```

### Output File (`output.json`):
```json
{
    "id": "123",
    "name": "Example Microsystem",
    "description": "Test Microsystem",
    "type": "Field Device",
    "role": "Data Acquisition"
}
```

---

## Error Handling

1. **Validation Failure**:
   - If the input file doesn't conform to the schema, the script outputs a validation failure message.
   - No JSON file is created.
2. **File Not Found**:
   - Ensure the paths for the schema and input files are correct.

---

## Troubleshooting

- **Incorrect File Format**:
  - Ensure the input file is well-formed XML and adheres to the RAMI 4.0 schema.
- **Schema Errors**:
  - Verify the schema file (`schem_rami_xsd.tex`) is properly formatted.

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
