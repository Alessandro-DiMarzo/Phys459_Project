import numpy as np
import matplotlib.pyplot as plt


# Function to generate lattice points based on the basis vectors
def generate_lattice_3d(basis_vectors, num_points):
    points = []

    for i in range(-num_points, num_points + 1):
        for j in range(-num_points, num_points + 1):
            for k in range(-num_points, num_points + 1):
                point = i * basis_vectors[0] + j * basis_vectors[1] + k * basis_vectors[2]
                points.append(point)

    return np.array(points)

# Function to plot the 3D lattice
def plot_lattice_3d(basis_vectors, num_points=5):
    points = generate_lattice_3d(basis_vectors, num_points)

    # Create a 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the lattice points
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], color='blue', marker='o')

    # Plot the basis vectors
    origin = np.zeros((3, 3))  # Origin points for the arrows
    ax.quiver(
        origin[:, 0], origin[:, 1], origin[:, 2],
        [basis_vectors[0][0], basis_vectors[1][0], basis_vectors[2][0]],
        [basis_vectors[0][1], basis_vectors[1][1], basis_vectors[2][1]],
        [basis_vectors[0][2], basis_vectors[1][2], basis_vectors[2][2]],
        color=['r', 'g', 'b']
    )

    # Set labels and grid
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    l = 2 #bounds for plot
    ax.set_xlim(-l,l)
    ax.set_ylim(-l,l)
    ax.set_zlim(-l,l)
    ax.grid(True)
    plt.title('3D Lattice Structure')
    plt.show()
    
basis_vectors = np.array([
        [1, 0, 0],  # x-direction
        [0, 1, 0],  # y-direction
        [0, 0, 1]   # z-direction
    ])

# Plot the lattice with specified number of points around the origin
plot_lattice_3d(basis_vectors, num_points=2)
