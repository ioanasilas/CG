import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d, Delaunay
from matplotlib.animation import FuncAnimation

# define points
points = np.array([[3, 5], [6, 6], [6, 4], [9, 5], [9, 7]])

# create voronoi diagram
vor = Voronoi(points)

# perform delaunay triangulation
triang = Delaunay(points)

# plot diagram
fig, ax = plt.subplots(figsize=(8, 8))

# set plot limits and aesthetics
ax.set_xlim(0, 11)
ax.set_ylim(0, 10)
ax.set_aspect('equal', 'box')
ax.set_title("Voronoi Diagram with Delaunay Triangulation", fontsize=16)

# function to update the plot for animation
def update(frame):
    ax.clear()
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal', 'box')
    ax.set_title("Voronoi Diagram with Delaunay Triangulation", fontsize=16)

    # Step 1: Show Voronoi diagram
    if frame >= 1:
        voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors='gray', line_width=1, point_size=5)
    
    # Step 2: Plot points (appear after Voronoi diagram)
    if frame >= 2:
        ax.plot(points[:, 0], points[:, 1], 'ro')

        # label points
        for i, point in enumerate(points):
            ax.text(point[0] + 0.1, point[1] + 0.1, f'{chr(65 + i)}', fontsize=12, color='darkred')
    
    # Step 3: Plot Delaunay triangulation (appear after points)
    if frame >= 3:
        for simplex in triang.simplices:
            ax.plot(points[simplex, 0], points[simplex, 1], 'b-', lw=1.5)

        # to ensure edges between A-C and E-D are visible
        ac_edge = [0, 2]  # points A and C
        ed_edge = [3, 4]  # points E and D
        ax.plot(points[ac_edge, 0], points[ac_edge, 1], 'b-', lw=1.5)
        ax.plot(points[ed_edge, 0], points[ed_edge, 1], 'b-', lw=1.5)

# create animation
ani = FuncAnimation(fig, update, frames=4, interval=1000)

# show the animation
plt.show()
