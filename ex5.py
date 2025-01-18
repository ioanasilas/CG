import matplotlib.pyplot as plt
<<<<<<< HEAD
import time

"""
Andrew's variant sorts the points by x-coordinate, and in case of ties, by the y-coordinate.
It then constructs the lower and upper hulls separately by iterating through the sorted points, 
checking for counterclockwise turns, and adding/removing points based on this.
Then  the algorithm concatenates the lower and upper hulls to get the convex hull."""

# orientation test function
def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # collinear
    elif val > 0:
        return 1  # counterclockwise
    else:
        return 2  # clockwise

# Andrew's variant of Graham's scan to find the convex hull
def convex_hull(points):
    points = sorted(points)

    lower = []
    # Plot initial points
    plt.scatter(*zip(*points), color='blue', label='Points')
    plt.title('Convex Hull using Andrew\'s Variant of Graham\'s Scan')
    plt.xlabel('X')
    plt.ylabel('Y')

    for p in points:
        while len(lower) >= 2 and orientation(lower[-2], lower[-1], p) != 1:
            lower.pop()
        lower.append(p)
        
        # plot the current state of the lower hull
        x_lower, y_lower = zip(*lower)
        plt.plot(x_lower, y_lower, color='green', label='Lower Hull')
        
        plt.draw()
        plt.pause(0.5)  # pause to visualize the intermediate step
        plt.cla()  # clear the current plot

        # replot the points and the current lower hull
        plt.scatter(*zip(*points), color='blue', label='Points')
        plt.plot(x_lower, y_lower, color='green', label='Lower Hull')

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and orientation(upper[-2], upper[-1], p) != 1:
            upper.pop()
        upper.append(p)
        
        # plot the current state of the upper hull
        x_upper, y_upper = zip(*upper)
        plt.plot(x_upper, y_upper, color='purple', label='Upper Hull')
        
        plt.draw()
        plt.pause(0.5)  # pause to visualize the intermediate step
        plt.cla()  # clear the current plot

        # replot the points, lower hull, and the current upper hull
        plt.scatter(*zip(*points), color='blue', label='Points')
        plt.plot(x_lower, y_lower, color='green', label='Lower Hull')
        plt.plot(x_upper, y_upper, color='purple', label='Upper Hull')

    return lower[:-1] + upper[:-1]

# points
points = [(1, 10), (-2, 7), (3, 8), (4, 10), (5, 7), (6, 7), (7, 11)]

# find the convex hull
hull = convex_hull(points)
print("Convex Hull:", hull)

x_points, y_points = zip(*points)
x_hull, y_hull = zip(*hull)

# plot the final convex hull
x_hull += (x_hull[0],)  # close the polygon by adding the first point at the end
y_hull += (y_hull[0],)
plt.plot(x_hull, y_hull, color='red', label='Convex Hull')

plt.legend()
=======


points = {
    'A': (-14, 9),
    'B': (-15, 4),
    'C': (-9, 4),
    'D': (-3, 6),
    'E': (-10, 6),
    'F': (-11, 4)
}

black_edges = [('A', 'B'), ('A', 'E'), ('B', 'E'), ('E', 'D'), ('D', 'C'), ('C', 'F'), ('F', 'E'), ('A', 'D')]
green_edges = [('B', 'F'), ('F', 'C'), ('C', 'E'), ('E', 'B')]

plt.figure(figsize=(8, 6))

for edge in black_edges:
    x_coords = [points[edge[0]][0], points[edge[1]][0]]
    y_coords = [points[edge[0]][1], points[edge[1]][1]]
    plt.plot(x_coords, y_coords, color='black')

for edge in green_edges:
    x_coords = [points[edge[0]][0], points[edge[1]][0]]
    y_coords = [points[edge[0]][1], points[edge[1]][1]]
    plt.plot(x_coords, y_coords, color='green')

for point, coord in points.items():
    plt.scatter(*coord, color='blue')
    plt.text(coord[0] + 0.3, coord[1], point, fontsize=12, color='blue')

plt.xlim(-16, -2)
plt.ylim(1, 10)
plt.grid(True, linestyle='--', alpha=0.6)
plt.gca().set_aspect('equal', adjustable='box')
>>>>>>> b0680c0 (Lab7)
plt.show()
