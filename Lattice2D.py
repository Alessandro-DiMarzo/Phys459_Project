import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi

# Function to generate lattice points based on the basis vectors
def generate_lattice(basis_vectors, num_points):
    points = []
    for i in range(-num_points, num_points + 1):
        for j in range(-num_points, num_points + 1):
            point = i * basis_vectors[0] + j * basis_vectors[1]
            points.append(point)
    
    return np.array(points)

# Function to plot the Wigner-Seitz cell using the Voronoi method
def plot_wigner_seitz(points):
    vor = Voronoi(points)
    
    # Plot the Voronoi regions
    for region in vor.regions:
        if not -1 in region and region:  # Skip invalid regions
            polygon = [vor.vertices[i] for i in region]
            plt.fill(*zip(*polygon), alpha=0.3, color='yellow', edgecolor='black')

# Function to plot the lattice and Wigner-Seitz cell
def plot_lattice_with_wigner_seitz(basis_vectors, num_points=5):
    points = generate_lattice(basis_vectors, num_points)
    
    # Plot the lattice points
    plt.scatter(points[:, 0], points[:, 1], color='blue', marker='o')
    
    # Plot the basis vectors
    origin = np.array([[0, 0], [0, 0]])  # Origin point for the arrows
    plt.quiver(*origin, [basis_vectors[0][0], basis_vectors[1][0]], 
                        [basis_vectors[0][1], basis_vectors[1][1]], 
                        color=['r', 'g'], scale=1, scale_units='xy', angles='xy')
    
    # Plot Wigner-Seitz cell
    plot_wigner_seitz(points)
    
    # Set equal scaling and grid
    plt.gca().set_aspect('equal', adjustable='box')
    plt.grid(True)
    
    plt.title('2D Lattice')
    plt.show()



basis_vectors = np.array([[1,0], [1/2,np.sqrt(3)/2]])  # Example for hexagonal lattice
    
# Plot the lattice with specified number of points around origin
plot_lattice_with_wigner_seitz(basis_vectors, num_points=3)
