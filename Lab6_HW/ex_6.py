import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations
from matplotlib.animation import FuncAnimation

# compute the circumcenter of a triangle
def circumcenter(A, B, C):
    D = 2 * (A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1]))
    ux = ((A[0]**2 + A[1]**2) * (B[1] - C[1]) + (B[0]**2 + B[1]**2) * (C[1] - A[1]) + (C[0]**2 + C[1]**2) * (A[1] - B[1])) / D
    uy = ((A[0]**2 + A[1]**2) * (C[0] - B[0]) + (B[0]**2 + B[1]**2) * (A[0] - C[0]) + (C[0]**2 + C[1]**2) * (B[0] - A[0])) / D
    return np.array([ux, uy])

# compute the squared distance from a point to the circumcenter
def dist_sq(P, center):
    return np.sum((P - center) ** 2)

# check if point P is inside the circumcircle of triangle ABC
def is_point_inside_circumcircle(A, B, C, P):
    center = circumcenter(A, B, C)
    radius_sq = dist_sq(A, center)
    return dist_sq(P, center) < radius_sq

# generate all triangles and check the Delaunay condition
def delaunay_triangulation(points):
    triangles = []
    edges = set()
    
    # all possible triangles
    for comb in combinations(range(len(points)), 3):
        i, j, k = comb
        A, B, C = points[i], points[j], points[k]
        
        # check if any point is inside the circumcircle of the triangle
        valid_triangle = True
        for p in range(len(points)):
            if p != i and p != j and p != k:
                P = points[p]
                if is_point_inside_circumcircle(A, B, C, P):
                    valid_triangle = False
                    break
        
        if valid_triangle:
            # add valid triangle to the list
            triangles.append([A, B, C])
            
            # add edges to the edge set (order the edges to avoid duplicates)
            edges.update([tuple(sorted([i, j])) for i, j in [(i, j), (j, k), (k, i)]])
    
    return triangles, edges

#  count unique edges
def count_edges(edges):
    return len(edges)

#  count the number of triangles
def count_triangles(triangles):
    return len(triangles)

# main function to compute the triangulation, number of triangles and edges
def triangulation_and_counts(lambda_val):
    # define the points A, B, C, D, E, M
    points = np.array([[1, -1], [-1, 1], [2, -1], [1, 1], [0, 2], [1, lambda_val]])
    
    # delaunay triangulation
    triangles, edges = delaunay_triangulation(points)
    
    # count the number of triangles and edges
    num_triangles = count_triangles(triangles)
    num_edges = count_edges(edges)
    
    return triangles, points

# figure and axis for plotting
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_title("Delaunay Triangulation Animation")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid(True)

# plotting function for the animation
def update(lambda_val):
    ax.clear()
    
    # get the triangulation for the current lambda value
    triangles, points = triangulation_and_counts(lambda_val)
    
    # plot the triangles
    for triangle in triangles:
        triangle = np.array(triangle)
        ax.plot([triangle[0, 0], triangle[1, 0]], [triangle[0, 1], triangle[1, 1]], 'b-')
        ax.plot([triangle[1, 0], triangle[2, 0]], [triangle[1, 1], triangle[2, 1]], 'b-')
        ax.plot([triangle[2, 0], triangle[0, 0]], [triangle[2, 1], triangle[0, 1]], 'b-')
    
    # plot the points
    ax.plot(points[:, 0], points[:, 1], 'ro')
    
    ax.set_xlim(-2, 3)
    ax.set_ylim(-2, 3)
    
    ax.set_title(f'Delaunay Triangulation for λ = {lambda_val:.2f}')
    return ax,

# animation with a range of lambda values
lambda_values = np.linspace(0.1, 1.5, 30)
ani = FuncAnimation(fig, update, frames=lambda_values, repeat=True, interval=300)


plt.show()
