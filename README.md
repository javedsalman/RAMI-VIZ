# RAMI4.0 Value Chain Visualization Tool for Smart Manufacturing Ecosystems

<img width="1512" alt="RAMI4 0-Value-Chain-Visualization-Tool" src="https://github.com/javedsalman/RAMI4.0-VIZ/assets/71730474/b0ff3bcc-75cd-4b8b-afd7-e1b8ff25ebf0">

RAMI4.0 Visualizations
This repository contains the Proof of Concept of the RAMI4.0-IZ tool. 
This is a beta version of the code for generating the RAMI4.0 Visualization. It is a work in progress.
The repository contains the executable file named as 'rami-vcvt-salman-javed' for RAMI4.0 Value Chain Visualization. It runs on Windows, Mac OS, and Linux machines without the installation of Python.
The repository also contains the output file 'RAMI4.0-Value-Chain-Visualization-Tool.png' generated from the executable mentioned above.
Below are the JSON templates that are crucial for setting up the configuration of smart manufacturing ecosystems. These configurations are designed to map out the RAMI 4.0 Cube dimensions and to define the interactions between different microsystems within the ecosystem.

## RAMI 4.0 Cube Configuration and System of Microsystems Interaction Matrix Configuration


The following JSON structure represents the configuration of the RAMI 4.0 Cube, which outlines the dimensions and coordinates of various microsystems.

```json
{
  "RAMI4.0Cube": {
    "dimensions": {
      "xAxis": "Value Stream",
      "yAxis": "Hierarchy Levels",
      "zAxis": "Business Layers"
    },
    "microsystems": [
      {
        "id": "MS1",
        "name": "Microsystem 1",
        "coordinates": {"x1": 0, "x2": 5, "y1": 0, "y2": 5, "z1": 0, "z2": 5},
        "ellipsoidDimensions": {"a": 2.5, "b": 2.5, "c": 2.5}
      }
      // Additional microsystems
    ]
  }
}

