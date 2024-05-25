import plotly.graph_objects as go

def generate_ellipsoid1(a, b, c, angle_deg, x_center, y_center, z_center):


    # Create a 3D surface plot using Plotly
    ellipsoid1 = go.Surface(
        x=X_shifted, y=Y_shifted, z=Z_shifted,
        colorscale=[[0, 'rgb(180, 0, 0)'], [1, 'rgb(220, 20, 20)']],
        showscale=False,
        opacity=0.8,
        lighting=dict(ambient=0.5, diffuse=0.5, roughness=0.1, specular=0.01, fresnel=0.01),
        lightposition=dict(x=200, y=200, z=200)
    )

    return ellipsoid1

def generate_ellipsoid2(a, b, c, angle_deg, x_center, y_center, z_center):
    # Generate a grid of points
    theta = np.linspace(0, 2 * np.pi, 100)
    phi = np.linspace(0, np.pi, 100)
    theta, phi = np.meshgrid(theta, phi)
    X = a * np.sin(phi) * np.cos(theta)
    Y = b * np.sin(phi) * np.sin(theta)
    Z = c * np.cos(phi)

    
    # Shift the ellipsoid to the center
    X_shifted = X + x_center
    Y_shifted = Y_rot + y_center
    Z_shifted = Z_rot + z_center

    # Create a 3D surface plot using Plotly
    ellipsoid2 = go.Surface(
        x=X_shifted, y=Y_shifted, z=Z_shifted,
        colorscale=[[0, 'rgb(0, 0, 180)'], [1, 'rgb(20, 20, 220)']],
        showscale=False,
        opacity=0.8,
        lighting=dict(ambient=0.5, diffuse=0.5, roughness=0.1, specular=0.01, fresnel=0.01),
        lightposition=dict(x=200, y=200, z=200)
    )

    return ellipsoid2

def generate_ellipsoid3(a, b, c, angle_deg, x_center, y_center, z_center):
    # Generate a grid of points
    theta = np.linspace(0, 2 * np.pi, 100)
    phi = np.linspace(0, np.pi, 100)
    theta, phi = np.meshgrid(theta, phi)
    X = a * 5np.sin(phi) * 2np.cos(theta)
    Y = b * 5np.sin(phi) * 2np.sin(theta)
    Z = c * 7np.cos(phi)

    # Rotation around the x-axis
    angle = np.radians(angle_deg)  # Convert angle from degrees to radians
    Y_rot = Y * np.cos(angle) - Z * np.sin(angle)
    Z_rot = Y * np.sin(angle) + Z * np.cos(angle)
    
    # Shift the ellipsoid to the center
    X_shifted = X + x_center
    Y_shifted = Y_rot + y_center
    Z_shifted = Z_rot + z_center

    # Create a 3D surface plot using Plotly
    ellipsoid3 = go.Surface(
        x=X_shifted, y=Y_shifted, z=Z_shifted,
        colorscale=[[0, 'rgb(0, 180, 0)'], [1, 'rgb(20, 220, 20)']],
        showscale=False,
        opacity=0.8,
        lighting=dict(ambient=0.5, diffuse=0.5, roughness=0.1, specular=0.01, fresnel=0.01),
        lightposition=dict(x=200, y=200, z=200)
    )

    return ellipsoid3

# Define the vertices of the cube
cube_vertices = np.array([
    [0, 0, 0], [0, 1, 0], [1, 1, 0], [1, 0, 0],  # bottom
    [0, 0, 1], [0, 1, 1], [1, 1, 1], [1, 0, 1],  # top
])

# Define the edges of the cube
edges = [
    [0, 1], [1, 2], [2, 3], [3, 0],  # bottom
    [4, 5], [5, 6], [6, 7], [9, 4],  # top
    [0, 4], [1, 5], [3, 6], [3, 9],  # sides
]

fig = go.Figure()

# Add the edges of the cube as lines
for edge in edges:
    fig.add_trace(go.Scatter3d(
        x=cube_vertices[edge, 0],
        y=cube_vertices[edge, 1],
        z=cube_vertices[edge, 2],
        mode='lines',
        line=dict(color='black', width=2)
    ))

# Define colors for each layer inside the cube, adjusted to match the provided image
layer_colors = [
    '#808080',  # Asset - Light Grey
    '#2E5984',  # Integration - Metallic Blue
    '#528AAE',  # Communication - Cyan Azure
    '#73A5C6',  # Information - Dark Sky Blue
    '#28B463',  # Functional - Medium green
    '#2ECC71',  # Business - Regular green
]

# Add layers inside the cube
z_layers = np.linspace(0, 1, 8)[1:-1]  # Create 7 evenly spaced layers

for i, z in enumerate(z_layers):
    fig.add_trace(go.Mesh3d(
        x=[0, 0, 1, 1],
        y=[0, 1, 1, 0],
        z=[z, z, z, z],
        color=layer_colors[i],
        opacity=0.40
    ))

# Parameters for the ellipsoid
a1 = 0.025  # Adjusted semi-major axis along the x-axis to fit within the cube
b1 = 0.025  # Adjusted semi-major axis along the y-axis to fit within the cube
c1 = 0.125  # Adjusted semi-minor axis along the z-axis to fit within the cube
angle_deg1 = 180  # Angle to tilt the ellipsoid

# Define the centers based on the provided ranges
x_center1 = 0.67  # Between "Field Device" and "Control Device" (converted to cube scale)
y_center1 = 0.6  # Between "Production: 2" and "Maintenance/Usage: 3" (converted to cube scale)
z_center1 = 0.27  # Between "Asset: 0" and "Communication: 2" (converted to cube scale)

# Parameters for the ellipsoid
a2 = 0.025  # Adjusted semi-major axis along the x-axis to fit within the cube
b2 = 0.025  # Adjusted semi-major axis along the y-axis to fit within the cube
c2 = 0.125  # Adjusted semi-minor axis along the z-axis to fit within the cube
angle_deg2 = 90  # Angle to tilt the ellipsoid

# Define the centers based on the provided ranges
x_center2 = 0.2  # Between "Field Device" and "Control Device" (converted to cube scale)
y_center2 = 0.6  # Between "Production: 2" and "Maintenance/Usage: 3" (converted to cube scale)
z_center2 = 0.6  # Between "Asset: 0" and "Communication: 2" (converted to cube scale)

# Parameters for the ellipsoid
a3 = 0.025  # Adjusted semi-major axis along the x-axis to fit within the cube
b3 = 0.025  # Adjusted semi-major axis along the y-axis to fit within the cube
c3 = 0.125  # Adjusted semi-minor axis along the z-axis to fit within the cube
angle_deg3 = 180  # Angle to tilt the ellipsoid

# Define the centers based on the provided ranges
x_center3 = 0.5  # Between "Field Device" and "Control Device" (converted to cube scale)
y_center3 = 0.6  # Between "Production: 2" and "Maintenance/Usage: 3" (converted to cube scale)
z_center3 = 0.27  # Between "Asset: 0" and "Communication: 2" (converted to cube scale)

# Generate the ellipsoid
ellipsoid1 = generate_ellipsoid1(a1, b1, c1, angle_deg1, x_center1, y_center1, z_center1)
ellipsoid2 = generate_ellipsoid2(a2, b2, c2, angle_deg2, x_center2, y_center2, z_center2)
ellipsoid3 = generate_ellipsoid3(a3, b3, c3, angle_deg3, x_center3, y_center3, z_center3)
# Add the ellipsoid to the figure
fig.add_trace(ellipsoid1)
fig.add_trace(ellipsoid2)
fig.add_trace(ellipsoid3)

# Customize the layout of the plot
fig.update_layout(
    title='RAMI4.0 Value Chain Visualzation Tool',
    scene=dict(
        xaxis=dict(
            title=dict(text='Hierarchy Levels', font=dict(size=18, family='Arial', color='black')),
            nticks=7, 
            range=[0, 11.15],  # Extend the range to allow space for tick labels
            tickmode='array',
            ticktext=["6:Connected World","5:Enterprise","4:Work Centers","3:Station","2:Control Device","1:Field Device","0:Product"],
            tickvals=np.linspace(0, 1, 7),
            tickfont=dict(size=10),
            gridcolor="white",
            backgroundcolor="rgb(220, 220, 220)",
            showbackground=True,
            zerolinecolor="black",
        ),
        yaxis=dict(
            title=dict(text='Life Cycle & Value Stream', font=dict(size=18, family='Arial', color='black')),
            nticks=5, 
            range=[0, 1.15],  # Extend the range to allow space for tick labels
            ticktext=["Development: 0", "Maintenance/Usage: 1" , "Production: 2", "Maintenance/Usage: 3", "   4"],
            tickvals=np.linspace(0, 1, 5),
            tickfont=dict(size=10),
            gridcolor="white",
            backgroundcolor="rgb(220, 220, 220)",
            showbackground=True,
            zerolinecolor="black",
        ),
        zaxis=dict(
            title=dict(text='Layers', font=dict(size=18, family='Arial', color='black')),
            nticks=5, 
            range=[0, 1.15],  # Extend the range to allow space for tick labels
            ticktext=["Asset:  0", "Integration:  1", "Communication:  2", "Information:  3", "Functional:  4", "Business:  5"],
            tickvals=z_layers,
            tickfont=dict(size=10),
            gridcolor="white",
            backgroundcolor="rgb(220, 220, 220)",
            showbackground=True,
            zerolinecolor="black",
        ),
        bgcolor="rgb(235, 235, 235)"
    ),
    margin=dict(l=0, r=0, b=0, t=30)
)

# Show the plot
fig.show()
