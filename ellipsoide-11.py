import plotly.graph_objects as go
import numpy as np

def generate_ellipsoid(a, b, c, y_shift, colorscale_val, angle_deg):
    # Generate a grid of points
    theta = np.linspace(0, 2 * np.pi, 100)
    phi = np.linspace(0, np.pi, 100)
    theta, phi = np.meshgrid(theta, phi)
    X = a * np.sin(phi) * np.cos(theta)
    Y = b * np.sin(phi) * np.sin(theta)
    Z = c * np.cos(phi)

    # Rotation around the x-axis
    angle = np.radians(angle_deg)  # Convert angle from degrees to radians
    Z_rot = Z * np.cos(angle) - Y * np.sin(angle)
    Y_rot = Z * np.sin(angle) + Y * np.cos(angle)
    
    # Shift the ellipsoid along the y-axis
    Y_shifted = Y_rot + y_shift

    # Create a 3D surface plot using Plotly
    ellipsoid = go.Surface(
        x=Y_shifted, y=Y, z=Z_rot,
        colorscale=colorscale_val,
        showscale=False,
        opacity=1,
        lighting=dict(ambient=0.5, diffuse=0.5, roughness=0.1, specular=0.01, fresnel=0.01),
        lightposition=dict(x=200, y=200, z=200)
    )

    return ellipsoid

# Example usage:
a = 10  # Semi-major axis along the x-axis
b = 10  # Semi-major axis along the y-axis
c = 30  # Semi-minor axis along the z-axis
angle_deg = 45  # Angle to tilt the ellipsoid

# Define colorscales for visual distinction
subtle_red_colorscale = [[0, 'rgb(180, 0, 0)'], [1, 'rgb(220, 20, 20)']]
subtle_blue_colorscale = [[0, 'rgb(0, 0, 180)'], [1, 'rgb(20, 20, 220)']]
subtle_green_colorscale = [[0, 'rgb(0, 180, 0)'], [1, 'rgb(20, 220, 20)']]

# Shifts along the y-axis for each ellipsoid
y_shifts = [-15, 0, 15]

# Generate three ellipsoids with a rotation along the x-axis and different y-axis shifts
ellipsoid1 = generate_ellipsoid(a, b, c, y_shifts[0], subtle_blue_colorscale, angle_deg)
ellipsoid2 = generate_ellipsoid(a, b, c, y_shifts[1], subtle_green_colorscale, angle_deg)
ellipsoid3 = generate_ellipsoid(a, b, c, y_shifts[2], subtle_red_colorscale, angle_deg)

# Update the layout for a better view
fig = go.Figure(data=[ellipsoid1, ellipsoid2, ellipsoid3])
fig.update_layout(
    title='3D Ellipsoids with Subtle Shading and Tilt',
    scene=dict(
        xaxis_title='X Axis',
    yaxis_title='Y Axis',
    zaxis_title='Z Axis',
    #xaxis=dict(nticks=4, range=[-a, a]),
    #yaxis=dict(nticks=4, range=[min(y_shifts) - b, max(y_shifts) + b]),  # Adjust y-axis range to account for shifts
     xaxis=dict(nticks=4, range=[-50, 50]),
        yaxis=dict(nticks=4, range=[-50, 50]),  # Adjust y-axis range to account for shifts
    zaxis=dict(nticks=4, range=[-c, c]),
    aspectmode='manual',
    aspectratio=dict(x=1, y=1, z=c/a),  # Keep aspect ratio 1:1 for x and y for consistent shift spacing
    camera_eye=dict(x=2, y=2, z=2)  # Adjust camera position if needed
),
autosize=True,
margin=dict(l=0, r=0, b=0, t=30)
)
fig.show()      
