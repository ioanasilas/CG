<<<<<<< HEAD
from scipy.spatial import ConvexHull

import matplotlib.pyplot as plt


def graham_scan(points):
    """
    This is a Graham's Scan algorithm  implementationto find the convex hull of a given set of points.
    """
    # first we sort points by y-coordinate; if we have ties, we break by x-coordinate
    points = sorted(points, key=lambda p: (p[1], p[0]))

    # function to calculate cross product of vectors
    def cross_product(o, a, b):
        # Vector OA x OB = (Ax - Ox)(By - Oy) - (Ay - Oy)(Bx - Ox)
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    # build the lower hull
    lower_hull = []
    for p in points:
        while len(lower_hull) >= 2 and cross_product(lower_hull[-2], lower_hull[-1], p) <= 0:
            lower_hull.pop()
        lower_hull.append(p)

    # build the upper hull
    upper_hull = []
    for p in reversed(points):
        while len(upper_hull) >= 2 and cross_product(upper_hull[-2], upper_hull[-1], p) <= 0:
            upper_hull.pop()
        upper_hull.append(p)

    # combine lower and upper hulls
    return lower_hull[:-1] + upper_hull[:-1]

# points from ex. 1
points = [
    (30, 60), (15, 25), (0, 30), (70, 30),
    (50, 40), (50, 10), (20, 0), (55, 20)
]

# compute convex hull using Graham's Scan
convex_hull = graham_scan(points)

# plot the points and the convex hull
plt.figure(figsize=(8, 6))
for point in points:
    plt.plot(point[0], point[1], 'o', color='blue')

# plot the convex hull
hull_path = convex_hull + [convex_hull[0]]  # close the hull
for i in range(len(hull_path) - 1):
    plt.plot(
        [hull_path[i][0], hull_path[i + 1][0]],
        [hull_path[i][1], hull_path[i + 1][1]],
        'k-',
        lw=2
    )

plt.title("Convex Hull (Graham's Scan)")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid()
plt.show()

convex_hull
=======
import matplotlib.pyplot as plt
import numpy as np

def plot_polygon_with_camera():
    vertices = [
         (-5, 6),(-7, 4), (-7, -4),  (-5, -6),(4, -4),   (6, -4), (9, -6), (11, -6),
        (11, 6),(9, 6),  (6, 4),  (4, 4)
    ]

    x, y = zip(*vertices)

    x = list(x) + [x[0]]
    y = list(y) + [y[0]]

    camera_x = 0
    camera_y = 0

    plt.figure(figsize=(10, 8))
    plt.plot(x, y, label="Polygon", color="brown")
    plt.fill(x, y, color="lightcoral", alpha=0.4)
    plt.axhline(0, color="blue", linestyle="--", label="Symmetry Axis")
    plt.scatter(camera_x, camera_y, color="green", label="Camera", s=100, zorder=5)

    for vx, vy in vertices:
        plt.plot([camera_x, vx], [camera_y, vy], color="green", linestyle="dotted", alpha=0.6)

    plt.title("Art Gallery Theorem: 1 Camera Placement")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.axis("equal")
    plt.show()

#the visualization
plot_polygon_with_camera()
>>>>>>> b0680c0 (Lab7)
