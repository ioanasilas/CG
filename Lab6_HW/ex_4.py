import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d

# define the points ai, bi, ci
A = [(1 + i, i - 1) for i in range(6)]
B = [(-i, i) for i in range(6)]
C = [(0, i) for i in range(6)]

# combine all points into one list
points = np.array(A + B + C)

# compute the voronoi diagram
vor = Voronoi(points)

# function to count the number of half-lines (unbounded edges)
def count_half_lines(vor):
    half_lines_count = 0
    # iterate over the voronoi regions
    for ridge in vor.ridge_vertices:
        # check if the ridge is unbounded
        if -1 in ridge:
            half_lines_count += 1
    return half_lines_count

# count the number of half-lines
half_lines = count_half_lines(vor)
print(f"number of half-lines in the voronoi diagram: {half_lines}")

# plot the points
plt.figure(figsize=(8, 8))
plt.scatter(*zip(*A), color='r', label='a points')
plt.scatter(*zip(*B), color='g', label='b points')
plt.scatter(*zip(*C), color='b', label='c points')

# add labels to the points
for i, (x, y) in enumerate(A):
    plt.text(x, y, f'a{i}', fontsize=12, color='r')
for i, (x, y) in enumerate(B):
    plt.text(x, y, f'b{i}', fontsize=12, color='g')
for i, (x, y) in enumerate(C):
    plt.text(x, y, f'c{i}', fontsize=12, color='b')

# plot the voronoi diagram over the points
voronoi_plot_2d(vor, ax=plt.gca(), show_vertices=False, line_width=1, line_colors='black')

plt.xlim(-8, 8)
plt.ylim(-8, 8) 

plt.title("plot of points a, b, and c with voronoi diagram")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()

# show the plot
plt.grid(True)
plt.show()
