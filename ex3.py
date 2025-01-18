<<<<<<< HEAD
import numpy as np
import matplotlib.pyplot as plt

"""
We define a set of points (point_coords) on a plane. The angle_from function calculates the angle between two points, and distance calculates the straight distance.

Graham's Scan:
    We find the point with the lowest y-coordinate to start.
    Then sort the points by polar angle and distance from the starting point.
    Then b uild the convex hull by adding points while ensuring only left turns are made.

Then we plot the points and the convex hull (the boundary enclosing the points).
"""


# given point_coords
point_coords = np.array([
    (4, 2),
    (7, -1),
    (3, -5),
    (-3, 6),
    (-4, 4),
    (-1, -1),
    (-2, -6)
])

def angle_from(p0, p1):
    # compute the polar angle from p0 to p1, p0 as origin.
    y = p1[1] - p0[1]
    x = p1[0] - p0[0]
    return np.arctan2(y, x)

def distance(p0, p1):
    # Euclidean distance between p0 and p1
    return np.sqrt((p1[0] - p0[0]) ** 2 + (p1[1] - p0[1]) ** 2)

def graham_scan(point_coords):
    # convex hull of a set of point_coords using Graham's scan algorithm
    # find  point with the lowest y-coordinate (and lowest x if tie)
    start = point_coords[np.argmin(point_coords, axis=0)[1]]
    if np.any(point_coords[:, 1] == start[1]):
        start = point_coords[np.sum(point_coords == start, axis=1).argmin()]

    # sort point_coords by polar angle with respect to the start point
    sorted_point_coords = sorted(point_coords, key=lambda p: (angle_from(start, p), distance(start, p)))

    # build the convex hull
    hull = [sorted_point_coords[0], sorted_point_coords[1]]
    for point in sorted_point_coords[2:]:
        while len(hull) > 1 and not is_left_turn(hull[-2], hull[-1], point):
            hull.pop()
        hull.append(point)

    return np.array(hull)

def is_left_turn(p0, p1, p2):
    # verify if the turn from p0 to p1 to p2 is a left turn
    return np.cross(p1 - p0, p2 - p0) > 0

hull = graham_scan(point_coords)

plt.figure(figsize=(8, 6))
plt.plot(point_coords[:, 0], point_coords[:, 1], 'bo', label='point_coords')
plt.plot(hull[:, 0], hull[:, 1], 'r-', label='Convex Hull', marker='o')

# close the convex hull by connecting the last point to the first
plt.plot([hull[-1, 0], hull[0, 0]], [hull[-1, 1], hull[0, 1]], 'r-')

plt.title('Convex Hull of given point_coords')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()

=======
import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

points = {'A': (11, 9), 'B': (5, 1), 'C': (15, 1.5), 'D': (8, 1), 'E': (12, 1.3)}

for point in points:
    G.add_node(point, pos=points[point])

edges = [('A', 'B'), ('B', 'C'), ('C', 'A'), ('A', 'D'), ('A', 'E')]
G.add_edges_from(edges)


node_colors = {'A': 'red', 'B': 'blue', 'C': 'green', 'D': 'green', 'E': 'blue'}

pos = nx.get_node_attributes(G, 'pos')

plt.figure(figsize=(6, 6))
nx.draw(G, pos, with_labels=True, node_size=500, node_color=[node_colors[node] for node in G.nodes], font_size=16, font_weight='bold', edge_color='black')

plt.title('Triangulation with 3 Triangles and 5 Edges')
plt.show()
>>>>>>> b0680c0 (Lab7)
