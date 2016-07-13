# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 22:28:13 2016

@author: SMALLON
"""

#Plot Wiener Process

import scipy

N = 1000
T = 1
Delta = T/N

#Vector initialization for approximating Weiner process

W = scipy.zeros(N+1)

t = scipy.linspace(0, T, N+1)
W[1:N+1] = scipy.cumsum(scipy.sqrt(Delta)*scipy.random.standard_normal(N))

print("Simulation of the Wiener Process:\n",W)

#Brownain Motion Plot
from scipy.stats import norm

#Process parameters
delta = 0.25
dt = 0.1

#Initial condition
x = 0.0

#Number of iterations to compute
n = 20

#Iterate to compute steps of Brownian motion
for k in range(n):
    x = x + norm.rvs(scale = delta ** 2 * dt)
    print (x)
    


#2D Brownian Motion Plot

import numpy
from pylab import plot, show, grid, axis, xlabel, ylabel, title
from brownian import brownian

def main():
    #Weiner process parameter
    delta = 0.25
    #Total time
    T = 10.0
    #Number of steps
    N = 500
    #Time step size
    dt = T/N
    #Initial values of x
    x = numpy.empty((2, N+1))
    x[:,0] = 0.0

    brownian(x[:,0], N, dt, delta, out=x[:,1:])    
    
    #Plot 2D trajectory
    plot(x[0], x[1])
    
    #Mark start and end points
    plot(x[0,0], x[1,0], 'go')
    plot(x[0,-1], x[1,-1], 'ro')
    
    #Decorate plot
    title("2D Brownian Motion")
    xlabel('x', fontsize = 16)
    ylabel('y', fontsize = 16)
    axis('equal')
    grid('TRUE')
    show()
    
if __name__ == "__main__":
    main()