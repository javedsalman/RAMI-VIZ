Title: Algorithm 1 - Input Specification and Preprocessing

Description: This Python script validates input data files (e.g., DSL or XMI format) against the RAMI 4.0 schema. Upon successful validation, the input is transformed into a structured JSON format for further processing.

File Structure
schem_rami_xsd.tex: The XML Schema Definition (XSD) file for validating RAMI-compliant data.
input_file.tex: Input data file in DSL or XMI format.
output.json: Output file in structured JSON format after successful validation and transformation.
How to Use
Install Dependencies:

Install xmlschema for schema validation:
bash
Copy code
pip install xmlschema
Prepare Files:

Place your RAMI schema file (schem_rami_xsd.tex) in the appropriate directory.
Ensure the input file is in DSL or XMI format.
Set File Paths:

Update the SCHEMA_FILE, INPUT_FILE, and OUTPUT_JSON paths in the script.
Run the Script:

Execute the script:
bash
Copy code
python algorithm1.py
Check Output:

If validation is successful, the structured JSON will be saved at the specified path.
Expected Outputs
Success: The script outputs a message confirming validation and provides the location of the saved JSON file.
Failure: The script outputs an error message if validation fails or the input file is not compliant with the schema.
Example
Input File (input_file.tex):

xml
Copy code
<microsystem>
    <id>123</id>
    <name>Example Microsystem</name>
    <description>Test Microsystem</description>
    <type>Field Device</type>
    <role>Data Acquisition</role>
</microsystem>
Output File (output.json):

json
Copy code
{
    "id": "123",
    "name": "Example Microsystem",
    "description": "Test Microsystem",
    "type": "Field Device",
    "role": "Data Acquisition"
}
