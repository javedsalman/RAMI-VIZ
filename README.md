# RAMI4.0 Value Chain Visualization Tool for Smart Manufacturing Ecosystems

<img width="1512" alt="rami-vcvt-s4" src="https://github.com/javedsalman/RAMI4.0-VIZ/assets/71730474/759993d9-d2c7-45c6-975e-0b994de34606">

<img width="1512" alt="rami-vcvt-s1" src="https://github.com/javedsalman/RAMI4.0-VIZ/assets/71730474/03454cc0-befd-49bc-92d2-fa2b21c97bc1">

<img width="1512" alt="rami-vcvt-s2" src="https://github.com/javedsalman/RAMI4.0-VIZ/assets/71730474/c2bf9293-4ce1-4b5b-a6ca-054ac1a1565d">

<img width="1512" alt="rami-vcvt-s3" src="https://github.com/javedsalman/RAMI4.0-VIZ/assets/71730474/b433c1fc-dbe1-4b58-b64b-dc1c48e820b5">


RAMI4.0 Visualizations
This repository contains the Proof of Concept of the RAMI4.0-IZ tool. 
This is a beta version of the code for generating the RAMI4.0 Visualization. It is a work in progress.
The repository contains the executable file 'rami-vcvt-salman-javed', which runs on Windows, Mac OS, and Linux machines without the installation of Python.
There is Platform Independat tool for mobile/tablets as well available at https://javedsalman.github.io/rami4_visualization-salman.html which can be opened in Safari web browser.
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

// The JSON configuration below defines the interaction matrix between microsystems. It specifies the type of interactions, the direction of services, and descriptions of those services.


{
  "interactionMatrix": {
    "microsystems": [
      {
        "id": "MS1",
        "name": "Microsystem 1",
        "interactions": [
          {
            "targetMicrosystem": "MS2",
            "interactionType": "dataExchange",
            "services": [
              {
                "serviceName": "ServiceA",
                "description": "Sends operational data to MS2",
                "direction": "outbound"
              }
            ]
          }
        ]
      },
      {
        "id": "MS2",
        "name": "Microsystem 2",
        "interactions": [
          {
            "targetMicrosystem": "MS1",
            "interactionType": "dataExchange",
            "services": [
              {
                "serviceName": "ServiceB",
                "description": "Receives operational data from MS1",
                "direction": "inbound"
              }
            ]
          },
          {
            "targetMicrosystem": "MS3",
            "interactionType": "serviceRequest",
            "services": [
              {
                "serviceName": "ServiceC",
                "description": "Requests processing service from MS3",
                "direction": "outbound"
              }
            ]
          }
        ]
      }
      // Additional microsystems and their interactions
    ]
  }
}
