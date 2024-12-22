import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
from matplotlib.animation import FuncAnimation

'''
Initially we have 4 half lines already, we want to keep this number
For a point inside the convex hull, its Voronoi region is bounded because it is surrounded by the regions of other points.
So, points inside the convex hull only create bounded edges in the Voronoi diagram.
'''

# points
points = np.array([
    [5, 1],  # A1
    [7, -1],  # A2
    [9, -1],  # A3
    [7, 3],  # A4
    [11, 1],  # A5
    [9, 3],  # A6
    [7, 2],  # A7 (new point we chose)
    [9, 2]   # A8 (new point we chose)
])

# plot
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(4, 12)
ax.set_ylim(-2, 4)
ax.set_title("Voronoi Diagram with Points A1 to A8")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.grid(True)

#function to plot Voronoi diagram
def plot_voronoi(points):
    vor = Voronoi(points)
    ax.clear()
    voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_width=2, line_colors='purple')
    ax.scatter(points[:, 0], points[:, 1], color='red', zorder=5)
    for i, point in enumerate(points):
        ax.text(point[0] + 0.1, point[1] + 0.1, f"A{i+1}", fontsize=12, color='blue')

#  the first set of points (A1 to A6)
def update(frame):
    # add points up to the current frame
    plot_voronoi(points[:frame])

ani = FuncAnimation(fig, update, frames=range(6, len(points) + 1), interval=1000, repeat=False)

plt.show()
