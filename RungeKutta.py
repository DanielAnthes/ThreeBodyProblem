import numpy as np

def RK4(func, stepsize, interval, y0):
    ''' expects a function to be integrated (vector or scalar) as well as
    a stepsize that determines the distance between estimated points and
    an interval over which the system should be integrated and an
    initial state'''
    statelen = len(y0) # the length of each state
    t_vector = np.arange(interval[0], interval[1], h) # time
    y_vector = np.zeros((statelen, len(t_vector))) # state at each timestep
    y_vector[:,0] = y0

    for i in range(length(t_vector)-1):
