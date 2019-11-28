import numpy as np
from RungeKutta import RK4
import matplotlib.pyplot as plt

G = 6.674 * 10**-11 # gravitational constant(ish)
mEarth = 5.972 * 10**24 # mass of the earth
mMoon = 7.34767309 * 10**22 # mass of the moon

def ForceOnEarth(yEarth, yMoon):
    positionEarth = yEarth[0]
    x2 = yEarth[1]
    positionMoon = yMoon[0]

    dx1dt = x2
    dx2dt = 1 / mEarth * (G * mEarth * mMoon * (positionMoon - positionEarth))/(np.sqrt((positionMoon - positionEarth)**2)**3)

    return np.array([dx1dt, dx2dt])

def ForceOnMoon(yMoon, yEarth):
    positionMoon = yMoon[0]
    x2 = yMoon[1]
    positionEarth = yEarth[0]

    dx1dt = x2
    dx2dt = 1 / mMoon * (G * mMoon * mEarth * (positionEarth - positionMoon))/(np.sqrt((positionEarth - positionMoon)**2)**3)

    return np.array([dx1dt, dx2dt])

def EarthMoonSystem():
    def system(t,y):
        yEarth = y[:,0:2]
        yMoon = y[:,2:4]
        youtEarth = ForceOnEarth(yEarth, yMoon)
        youtMoon = ForceOnMoon(yMoon, yEarth)
        yout = np.append(youtEarth, youtMoon, axis=1)
        return yout

    return system

y0Earth = np.array([[0, 0], [0, 0]]) # initial position of earth is stationary at origin
y0Moon = np.array([[2, 2], [-1, -1]])
y0 = np.append(y0Earth, y0Moon, axis=1)

system = EarthMoonSystem()
tout, yout = RK4(system, 0.0001, np.array([0, 0.1]), y0)

EarthPositions = yout[:,0,:]
MoonPositions = yout[:,2,:]

plt.figure()
plt.plot(EarthPositions[0,:], EarthPositions[1,:])
plt.plot(MoonPositions[0,:], MoonPositions[1,:])
plt.xlim([-10, 10])
plt.ylim([-10, 10])
plt.show()
