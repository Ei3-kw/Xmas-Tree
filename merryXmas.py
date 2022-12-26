import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors

graph = plt.figure().add_subplot(111, projection='3d')

# starting point
x, y, z = 0, 0, -5

num_turns = 23
radius = 3
num_points = 100
angle_step = num_turns * 3.5 * np.pi / num_points

xs, ys, zs = [x], [y], [z]

for i in range(num_points):
    # increasing angle while decreasing radius
    angle = angle_step * i
    radius = radius - 0.02

    # new point of the spiral
    x = radius * np.cos(angle)
    y = radius * np.sin(angle)
    z = z + 0.1

    xs.append(x)
    ys.append(y)
    zs.append(z)

xs = np.array(xs)
ys = np.array(ys)
zs = np.array(zs)

# scale to fit
xs *= 0.2
ys *= 0.2
zs *= 0.2

# limits of the graphis
graph.set_xlim(-1, 1)
graph.set_ylim(-1, 1)
graph.set_zlim(-1, 1)
graph.plot(xs, ys, zs, color='g')

# a star at the top
graph.scatter(0, 0, 1, c='darkorange', marker='*', s=200)

# 13 gifts on the ground
colors = list(mcolors.CSS4_COLORS.keys())
for i in range(13):
    x = np.random.uniform(-1, 1)
    y = np.random.uniform(-1, 1)
    size = np.random.uniform(50, 200)
    c1 = colors[int(np.random.uniform(0, len(colors)))]
    c2 = colors[int(np.random.uniform(0, len(colors)))]
    graph.scatter(x, y, -1, c=c1, marker='s', s=size)
    graph.scatter(x, y, -1, c=c2, marker='+', s=size)

plt.title('Merry Turtle Sponge Xmas')
plt.show()
