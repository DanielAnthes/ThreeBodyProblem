import numpy as np
from RungeKutta import RK4
import matplotlib.pyplot as plt

def LotkaVolterra(a, b, delta, gamma):
# the LotkaVolterra equations for predator prey relationship. Can handle vector
#input for x and y, but only if arguments are given as numpy arrays
        def system(t,y):
                x = y[0]
                y = y[1]
                dxdt = a * x - b * x * y
                dydt = delta * x * y - gamma * y
                return np.array([dxdt, dydt])

        return system

a = 0.08
b = 0.005
delta = 0.2
gamma = 0.1
y0 = np.array([10,10]).T # initial populations

system = LotkaVolterra(a,b,delta,gamma)
tout, yout = RK4(system, 0.1, [0, 100], y0)

plt.figure()
plt.plot(yout[0,:], yout[1,:])
plt.show()
