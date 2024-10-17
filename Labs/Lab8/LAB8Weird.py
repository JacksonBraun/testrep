import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.linalg import inv
from Lab8 import PRELAB
def driver():
    f = lambda x: np.exp(x)
    a = 0
    b = 1
    """ create points you want to evaluate at"""
    Neval = 100
    xeval = np.linspace(a,b,Neval)
    """ number of intervals"""
    Nint = 10

    yeval = eval_lin_spline(xeval,Neval,a,b,f,Nint)
    fex = f(xeval)
    plt.figure()
    plt.plot(xeval,fex,'ro-')
    plt.plot(xeval,yeval,'bs-')
    plt.legend()
    plt.show()
    err = abs(yeval-fex)
    plt.figure()
    plt.plot(xeval,err,'ro-')
    plt.show()
def eval_lin_spline(xeval,Neval,a,b,f,Nint):

    xint = np.linspace(a,b,Nint+1)
    
    yeval = np.zeros(Neval)
    for j in range(Nint):

        atmp = xint[j]
        btmp= xint[j+1]
        # find indices of values of xeval in the interval
        ind= np.where((xeval >= atmp) & (xeval <= btmp))
        xloc = xeval[ind]
        n = len(xloc)
        fa = f(atmp)
        fb = f(btmp)
        yloc = np.zeros(len(xloc))
        for kk in range(n):
            #use your line evaluator to evaluate the spline at each location
            yloc[kk] = PRELAB(atmp,btmp,f,xloc[kk])#Call your line evaluator with points (atmp,fa) and (btmp,fb)
            # Copy yloc into the final vector
        yeval[ind] = yloc
    
    return yeval
driver()