"""
Algorithm 1: Input Specification and Preprocessing
---------------------------------------------------
This module handles the initial preprocessing of the input DSL (Domain-Specific Language) file,
validates it against the expected RAMI 4.0 schema, and converts it into a standardized JSON format.

Expected Input:
- JSON file representing a list of microsystems and their attributes

Key Tasks:
- Load and parse the JSON input
- Validate required fields for each microsystem
- Return structured microsystem list for downstream algorithms

Author: Salman Javed
"""

import json

# Define required keys based on the RAMI 4.0 microsystem schema
REQUIRED_KEYS = [
    "microsystem.id",
    "microsystem.name",
    "microsystem.description",
    "microsystem.type",
    "microsystem.role",
    "microsystem.asset",
    "microsystem.shell",
    "microsystem.provides",
    "microsystem.consumes",
    "microsystem_stakeholder.id",
    "microsystem_stakeholder.description"
]

def validate_microsystem(micro):
    """
    Validates a single microsystem dictionary to ensure all required fields are present.
    Returns a tuple (is_valid, error_message)
    """
    for key in REQUIRED_KEYS:
        keys = key.split('.')
        val = micro
        for k in keys:
            if k in val:
                val = val[k]
            else:
                return False, f"Missing required field: {key}"
    return True, ""

def run(input_json):
    """
    Main entry point for Algorithm 1.

    Parameters:
        input_json (dict): Parsed JSON input from uploaded file

    Returns:
        (list, list): Tuple of valid microsystems and list of validation errors
    """
    microsystems = input_json.get("microsystems", [])
    validated = []
    errors = []

    for idx, micro in enumerate(microsystems):
        is_valid, err = validate_microsystem(micro)
        if is_valid:
            validated.append(micro)
        else:
            errors.append({"index": idx, "error": err})

    return validated, errors
