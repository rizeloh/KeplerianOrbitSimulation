import matplotlib.pyplot as plt
import numpy as np

# Constants
G = 6.67430e-11  # Gravitational constant, m^3 kg^-1 s^-2
M = 1.989e30  # Mass of the sun, kg
AU = 1.496e11  # Astronomical unit, meters

def kepler_orbit(a, e, num_points=1000):
    """
    Simulate a Keplerian orbit.

    Parameters:
    a (float): Semi-major axis in meters.
    e (float): Eccentricity of the orbit.
    num_points (int): Number of points to simulate.

    Returns:
    tuple: Arrays of x and y coordinates of the orbit.
    """
    theta = np.linspace(0, 2 * np.pi, num_points)
    r = (a * (1 - e**2)) / (1 + e * np.cos(theta))
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x, y

def plot_orbit(x, y, title='Keplerian Orbit'):
    """
    Plot the orbit.

    Parameters:
    x (array): X coordinates of the orbit.
    y (array): Y coordinates of the orbit.
    title (str): Title of the plot.

    Returns:
    None
    """
    plt.figure(figsize=(8, 8))
    plt.plot(x, y, label='Orbit')
    plt.plot(0, 0, 'yo', label='Star (Sun)')
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.axis('equal')
    plt.show()

if __name__ == "__main__":
    # Example usage
    a = AU  # Semi-major axis (1 AU)
    e = 0.0167  # Eccentricity (Earth's orbit)
    
    x, y = kepler_orbit(a, e)
    plot_orbit(x, y, title='Orbit of the Earth around the Sun')
