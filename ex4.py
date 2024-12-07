import matplotlib.pyplot as plt

"""
Leftmost:
First test: Identify the leftmost point, which is P2=(1,3).
Second test: From P2, we find the next point M. For each point Pj​, compute the orientation with respect to P2. 
The candidate that results in a counterclockwise turn becomes the next point.
Third test: After selecting M, we repeat the process to find M's successor, comparing all other points to find the next counterclockwise turn.
"""

"""
Lowest:
First test: Identify the lowest point, which is P1=(2,-1).
Second test: From P1, we find the next point M. For each point Pj, compute the orientation with respect to P1. 
The candidate that results in a counterclockwise turn becomes the next point.
Third test: After selecting M, we repeat the process to find M's successor, comparing all other points to find the next counterclockwise turn.
"""

# orientation test function
def orientation(p, q, r):
    # using the determinant formula
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # collinear
    elif val > 0:
        return 1  # counterclockwise
    else:
        return 2  # clockwise

# jarvis March algorithm
def jarvis_march(points):
    n = len(points)
    if n < 3:
        return []  # convex hull is not possible with fewer than 3 points

    # start from the leftmost point
    leftmost = min(points, key=lambda p: p[0])
    hull = []
    p = leftmost

    while True:
        hull.append(p)
        q = None
        for r in points:
            if r == p:
                continue
            # find the next point in the convex hull by checking the orientation
            if q is None or orientation(p, q, r) == 2:  # clockwise (to find the rightmost counterclockwise turn)
                q = r
        p = q

        # while we return to the starting point, stop
        if p == leftmost:
            break
    
    return hull

# points P1 to P5
points = [(2, -1), (1, 3), (4, 0), (4, 3), (5, 2)]

# find the convex hull
convex_hull = jarvis_march(points)
print("Convex Hull:", convex_hull)


# Extract x and y coordinates for plotting
x_points, y_points = zip(*points)
x_hull, y_hull = zip(*convex_hull)

# Plot the points
plt.scatter(x_points, y_points, color='blue', label='Points')

# Plot the convex hull
x_hull += (x_hull[0],)  # to make the polygon close by adding the first point at the end
y_hull += (y_hull[0],)
plt.plot(x_hull, y_hull, color='red', label='Convex Hull')

# Adding labels and legend
plt.title('Convex Hull using Jarvis March')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

# Show the plot
plt.show()