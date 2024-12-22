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
