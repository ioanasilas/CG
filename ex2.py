<<<<<<< HEAD
from scipy.spatial import ConvexHull

import matplotlib.pyplot as plt

def points_on_border(A, B, C, D, M):
    """
    Computes the number of points on the border of the convex hull for the set {A, B, C, D, M}.
    Returns the number of points on the convex hull.
    """
    # points
    points = [A, B, C, D, M]

    # Graham's scan implementation (same as ex. 1)
    def graham_scan(points):
        points = sorted(points, key=lambda p: (p[1], p[0]))

        def cross_product(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

        lower_hull = []
        for p in points:
            while len(lower_hull) >= 2 and cross_product(lower_hull[-2], lower_hull[-1], p) <= 0:
                lower_hull.pop()
            lower_hull.append(p)

        upper_hull = []
        for p in reversed(points):
            while len(upper_hull) >= 2 and cross_product(upper_hull[-2], upper_hull[-1], p) <= 0:
                upper_hull.pop()
            upper_hull.append(p)

        return lower_hull[:-1] + upper_hull[:-1]

    # compute the convex hull
    convex_hull = graham_scan(points)

    # return the number of points on the border
    return len(convex_hull)


# static points
A = (3, -3)
B = (3, 3)
C = (-3, -3)
D = (-3, 3)

# choose lambda as 0 but we can change it
# from -0.9 to -0.1 and from 5.1 to 5.9 we get 5 vertices, otherwise we get 4
λ = 5.9
M = (-2 + λ, 3 - λ)

points_count = points_on_border(A, B, C, D, M)
print(points_count)
=======
import matplotlib.pyplot as plt
import numpy as np

def plot_polygon_one_camera():

    vertices = [
        (0, 5), (-1, -2), (3, -2),  (3, 0),  (3, 2), (1, 2)
    ]


    x, y = zip(*vertices)

    x = list(x) + [x[0]]
    y = list(y) + [y[0]]


    camera_start_x, camera_start_y = vertices[5]  # P5
    camera_end_x, camera_end_y = 1.5, 1  # arbitrary point inside the polygon


    plt.figure(figsize=(10, 8))
    plt.plot(x, y, label="Polygon", color="brown")
    plt.fill(x, y, color="lightcoral", alpha=0.4)
    plt.scatter(camera_end_x, camera_end_y, color="green", label="Camera Target", s=100, zorder=5)

    for vx, vy in vertices:
        if (min(x) <= vx <= max(x)) and (min(y) <= vy <= max(y)):
            plt.plot([camera_start_x, vx], [camera_start_y, vy], color="green", alpha=0.6, linewidth=2)


    plt.plot([camera_start_x, camera_end_x], [camera_start_y, camera_end_y], color="green", alpha=0.8, label="Ray from P5")


    plt.title("Art Gallery Theorem: One Camera Placement with Rays from P5")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.axis("equal")
    plt.show()

def plot_polygon_two_cameras():
    vertices = [
        (0, 5), (-1, -2), (3, -2),  (3, 0),  (3, 2), (1, 2)
    ]

    x, y = zip(*vertices)

    x = list(x) + [x[0]]
    y = list(y) + [y[0]]

    camera1_x, camera1_y = vertices[4]  # P6
    camera2_x, camera2_y = vertices[0]  # P1

    plt.figure(figsize=(10, 8))
    plt.plot(x, y, label="Polygon", color="brown")
    plt.fill(x, y, color="lightcoral", alpha=0.4)
    plt.scatter(camera1_x, camera1_y, color="blue", label="Camera at P6", s=100, zorder=5)
    plt.scatter(camera2_x, camera2_y, color="purple", label="Camera at P1", s=100, zorder=5)

    for vx, vy in vertices:
        if (min(x) <= vx <= max(x)) and (min(y) <= vy <= max(y)):
            if (vx, vy) not in [vertices[4], vertices[3], vertices[2]]:  # Exclude P6, P4, and P2
                plt.plot([camera2_x, vx], [camera2_y, vy], color="black", alpha=0.6, linewidth=2)
            if (vx, vy) not in [vertices[0]]:
                plt.plot([camera1_x, vx], [camera1_y, vy], color="blue", alpha=0.6, linewidth=2)


    plt.title("Art Gallery Theorem: Two Cameras Placement")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.axis("equal")
    plt.show()

plot_polygon_one_camera()
plot_polygon_two_cameras()
>>>>>>> b0680c0 (Lab7)
