import xmlschema
import json
import os

# Paths to input and schema files
SCHEMA_FILE = "path/to/schem_rami_xsd.tex"  # Replace with the actual schema file path
INPUT_FILE = "path/to/XMI_or_DSL_file.tex"  # Replace with the DSL or XMI input file path
OUTPUT_JSON = "path/to/output.json"  # Replace with the desired output JSON file path

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
