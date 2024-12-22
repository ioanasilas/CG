import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from scipy.spatial.distance import pdist, squareform
from matplotlib.animation import FuncAnimation

# static points
static_points = np.array([
    [1, 6], [1, 1], [-4, 7], [6, 7], [1, -1], [5, 3], [-2, 3]  # points A, B, C, D, E, F, P
])

# function to compute mst for a given lambda
def compute_mst_for_lambda(lambda_value):
    Q = np.array([lambda_value - 2, 3])  # define Q for this lambda
    points = np.vstack([static_points, Q])  # add Q to the static points
    distances = squareform(pdist(points))  # calculate pairs off distances

    G = nx.Graph()  # create a graph
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            G.add_edge(i, j, weight=distances[i, j])  # add edges with weights

    mst = nx.minimum_spanning_tree(G)  # compute mst
    mst_length = sum([mst[u][v]['weight'] for u, v in mst.edges()])  # get total mst length
    
    return points, mst, mst_length

# lambda values with 0.5 increments
lambda_values = np.arange(-5, 5.5, 0.5)

# create plot
fig, ax = plt.subplots(figsize=(10, 8))

# plot the static points
ax.scatter(static_points[:, 0], static_points[:, 1], color='red', label='points')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('mst animation for varying λ')

# set plot limits
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

# prepare line and text objects for animation
line, = ax.plot([], [], 'b-', lw=2)
text = ax.text(0.05, 0.95, '', transform=ax.transAxes, fontsize=12)

# initialize animation
def init():
    line.set_data([], [])
    text.set_text('')
    return line, text

# store mst lengths and find the minimum
mst_lengths = []
for lambda_value in lambda_values:
    _, _, mst_length = compute_mst_for_lambda(lambda_value)
    mst_lengths.append(mst_length)

# find the lambda with smallest mst length
min_mst_length = min(mst_lengths)
min_lambda = lambda_values[mst_lengths.index(min_mst_length)]

# update function for animation
def update(frame):
    lambda_value = lambda_values[frame]
    points, mst, mst_length = compute_mst_for_lambda(lambda_value)

    # update mst edges
    x_vals = []
    y_vals = []
    for u, v in mst.edges():
        x_vals.extend([points[u, 0], points[v, 0], np.nan])
        y_vals.extend([points[u, 1], points[v, 1], np.nan])
    
    line.set_data(x_vals, y_vals)

    # update text with lambda and mst length
    text.set_text(f'λ = {lambda_value:.1f}, mst length = {mst_length:.2f}')

    return line, text

# create animation
ani = FuncAnimation(fig, update, frames=len(lambda_values), init_func=init, blit=True, repeat=False, interval=1000)

# display animation
plt.grid(True)
plt.legend()
plt.show()

# output the result
print(f"the minimum spanning tree length is smallest when λ = {min_lambda:.1f} with a length of {min_mst_length:.2f}")
