import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay, Voronoi, voronoi_plot_2d

# define the first set of points
points1 = np.array([[0, 1], [2, 3], [4, 5], [10, 6], [8, 4], [8, 2]])

# define the second set of points
points2 = np.array([[-4, 2], [-4, 6], [-6, 2], [-2, 6], [-8, 4], [-6, 6], [-8, 2]])

# perform delaunay triangulation
tri1 = Delaunay(points1)
tri2 = Delaunay(points2)

# function to count unique edges
def count_edges(tri):
    edges = set()
    for simplex in tri.simplices:
        edges.update([tuple(sorted([simplex[i], simplex[j]])) for i in range(3) for j in range(i + 1, 3)])
    return len(edges)

# count edges for each triangulation
edges1 = count_edges(tri1)
edges2 = count_edges(tri2)

# function to count half-lines (infinite edges)
def count_half_lines(vor):
    half_lines = 0
    for ridge in vor.ridge_vertices:
        if -1 in ridge:
            half_lines += 1
    return half_lines

# generate Voronoi diagrams
vor1 = Voronoi(points1)
vor2 = Voronoi(points2)

# count half-lines for each Voronoi diagram
half_lines1 = count_half_lines(vor1)
half_lines2 = count_half_lines(vor2)

# plotting
plt.figure(figsize=(12, 6))

# plot first set of points and triangulation
plt.subplot(1, 2, 1)
plt.triplot(points1[:, 0], points1[:, 1], tri1.simplices, color='blue', lw=1)
plt.plot(points1[:, 0], points1[:, 1], 'ro')
voronoi_plot_2d(vor1, ax=plt.gca(), show_vertices=False, line_colors='orange', line_width=1)
plt.title('Triangulation and Voronoi of points1')
plt.xlabel('x')
plt.ylabel('y')

# plot second set of points and triangulation
plt.subplot(1, 2, 2)
plt.triplot(points2[:, 0], points2[:, 1], tri2.simplices, color='green', lw=1)
plt.plot(points2[:, 0], points2[:, 1], 'bo')
voronoi_plot_2d(vor2, ax=plt.gca(), show_vertices=False, line_colors='purple', line_width=1)
plt.title('Triangulation and Voronoi of points2')
plt.xlabel('x')
plt.ylabel('y')

# show the plot
plt.tight_layout()
plt.show()

# output the number of edges for each triangulation and half-lines in the Voronoi diagram
print(f"Number of edges in points1 triangulation: {edges1}")
print(f"Number of edges in points2 triangulation: {edges2}")
print(f"Number of half-lines in points1 Voronoi diagram: {half_lines1}")
print(f"Number of half-lines in points2 Voronoi diagram: {half_lines2}")
