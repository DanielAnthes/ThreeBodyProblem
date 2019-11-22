import numpy as np
from RungeKutta import RK4
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def Pendulum(g, L):
# with g the gravitational constant
# L the length of the pendulum
    def system(t,y):
        x = y[0]
        y = y[1]
        dfdx = y
        dfdy = - g/L * np.sin(x)
        return np.array([dfdx, dfdy])

    return system


def DampedPendulum(g, L, b):
# with g the gravitational constant
# L the length of the pendulum
# b the dampening factor
    def system(t,y):
        x = y[0]
        y = y[1]
        dfdx = y
        dfdy = - g/L * np.sin(x) - b * y
        return np.array([dfdx, dfdy])

    return system


system = DampedPendulum(9.81, 1, 0.1)
y0 = np.array([np.pi*0.9,0])
tout, yout = RK4(system, 0.01, [0, 100], y0)

# animate pendulum
time = tout
angle = yout[0,:]
acceleration = yout[1,:]

# rotate angles by 90° so that at angle zero the pendulum points down
angle = angle - 0.5*np.pi
x_coordinates = np.cos(angle)
y_coordinates = np.sin(angle)

x_coordinates_vel = x_coordinates + (np.cos(angle + 0.5*np.pi) * acceleration * 0.1)
y_coordinates_vel = y_coordinates + (np.sin(angle + 0.5*np.pi) * acceleration * 0.1)

fig, ax = plt.subplots()
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
line, = ax.plot([0, x_coordinates[0], x_coordinates_vel[0]], [0, y_coordinates[0], y_coordinates_vel[0]])

def init():  # only required for blitting to give a clean slate.
    line.set_ydata([np.nan] * 3)
    return line,


def animate(i):
    line.set_data([0, x_coordinates[i], x_coordinates_vel[i]], [0, y_coordinates[i], y_coordinates_vel[i]])  # update the data.
    return line,


ani = animation.FuncAnimation(
    fig, animate, init_func=init, interval=2, blit=True, save_count=50)
plt.show()
