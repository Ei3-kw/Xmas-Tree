import numpy as np
import matplotlib.pyplot as plt

sigma = 12
rho = 23
beta = 23/12

dt = 0.01
t = np.arange(0, 100, dt)

# initialize the Lorenz system
x, y, z = [-20], [-20], [-20]

# iterate thru the time steps 
for i in range(len(t) - 1):
    dx = sigma * (y[-1] - x[-1]) * dt
    dy = (x[-1] * (rho - z[-1]) - y[-1]) * dt
    dz = (x[-1] * y[-1] - beta * z[-1]) * dt
    x.append(x[-1] + dx)
    y.append(y[-1] + dy)
    z.append(z[-1] + dz)

x = np.array(x)
y = np.array(y)
z = np.array(z)

# scale to fit
x *= 0.1
y *= 0.1
z *= 0.1

graph = plt.figure().add_subplot(111, projection='3d')

graph.plot(x, y, z, 'g')

# a star at the top
graph.scatter(0, 0, 1, c='darkorange', marker='*', s=200)

# set limits
graph.set_xlim(-1, 1)
graph.set_ylim(-1, 1)
graph.set_zlim(-1, 1)

plt.show()
