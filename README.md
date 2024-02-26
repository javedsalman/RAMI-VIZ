# RAMI4.0-VIZ
RAMI4.0 Visualizations

**Example Configuration Template (JSON)
**
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
  },
  
}




**Microsystem Interaction Matrix Configuration Template (JSON)
**
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
      },
      // Additional microsystems and their interactions
    ]
  }
}
![image](https://github.com/javedsalman/RAMI4.0-VIZ/assets/71730474/55710cfc-dac2-409d-b87c-b83bd7ade797)
