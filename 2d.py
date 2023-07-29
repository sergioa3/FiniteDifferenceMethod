import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

max_t = 1000
k = 2
dx = 1
delta_t = (dx**2)/(4 * k)
gamma = (k * delta_t) / (dx**2)


# 
ang = np.linspace(0,2*np.pi, 1000)
r = 30
x = np.around(r*np.cos(ang))+r+2
y = np.around(r*np.sin(ang))+r+2
plt.scatter(x,y)
plt.show()

txy = lambda x,y: np.sqrt(x**2 + y**2)

L = 2*r+3
u = np.empty((max_t, L, L))

# 
u.fill(-10)
rs = np.linspace(0,r,100)
for j in rs:
    x = (j*np.cos(ang))+r
    y = (j*np.sin(ang))+r
    for i in range(len(x)):
        if j == r:
            u[:,int(x[i]), int(y[i])] = txy(x[i],y[i])
        else:
            u[:,int(x[i]), int(y[i])] = -5


# Set the boundary conditions


def calculate(u):
    for k in range(0, max_t-1, 1):
        for i in range(0, L, dx):
            for j in range(0, L, dx):
                if u[k+1, i, j] == -5:
                    u[k + 1, i, j] = gamma *(u[k][i+1][j] + u[k][i-1][j] + u[k][i][j+1] + u[k][i][j-1] - 4*u[k][i][j]) + u[k][i][j]

    return u

def plotheatmap(u_k, k):
    # Clear the current plot figure
    plt.clf()

    plt.title(f"Temperature at t = {k*delta_t:.3f} unit time")
    plt.xlabel("x")
    plt.ylabel("y")

    # This is to plot u_k (u at time-step k)
    plt.pcolormesh(u_k, cmap=plt.cm.jet, vmin=-10, vmax=100)
    plt.colorbar()
    plt.show()

    return plt

# Do the calculation here
u = calculate(u)

def animate(k):
    plotheatmap(u[k], k)

anim = animation.FuncAnimation(plt.figure(), animate, interval=1, frames=max_t, repeat=False)
plt.show()