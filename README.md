# RAMI4.0-VIZ
RAMI4.0 Visualizations

# Smart Manufacturing Ecosystem Configurations

This repository contains JSON templates that are crucial for setting up the configuration of smart manufacturing ecosystems. These configurations are designed to map out the RAMI 4.0 Cube dimensions and to define the interactions between different microsystems within the ecosystem.

## RAMI 4.0 Cube Configuration

The following JSON structure represents the configuration of the RAMI 4.0 Cube which outlines the dimensions and coordinates of various microsystems.

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

## Microsystem Interaction Matrix Configuration
The JSON configuration below defines the interaction matrix between microsystems. It specifies the type of interactions, the direction of services, and descriptions of those services.


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

