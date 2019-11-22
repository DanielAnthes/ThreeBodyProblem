import numpy as np

def RK4(f, h, interval, y0):
    ''' expects a function to be integrated (vector or scalar) as well as
    a stepsize that determines the distance between estimated points and
    an interval over which the system should be integrated and an
    initial state'''
    statelen = len(y0) # the length of each state
    t = np.arange(interval[0], interval[1], h) # time
    y = np.zeros((statelen, len(t))) # state at each timestep
    y[:,0] = y0

    for i in range(len(t)-1):
        k1 = h * f(t[i],y[:,i])
        k2 = h * f(t[i] + h/2, y[:,i] + k1/2)
        k3 = h * f(t[i] + h/2, y[:,i] + k2/2)
        k4 = h * f(t[i] + h, y[:,i] + k3)
        y[:,i+1] = y[:,i] + 1/6 * (k1 + 2*k2 + 2*k3 + k4)

    return t, y
