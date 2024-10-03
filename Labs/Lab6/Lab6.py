import numpy as np
import scipy as sp
from Functions import SlackerNewton
from Functions import NewtonMultiVarJapprox

def driver():
    x0 = [1,0]
    n = 50
    tol = 1e-10

    [xcrit,i,err] = SlackerNewton(Jfunc,Ffunc,x0,n,tol)

    print(xcrit)
    print(i)

    h = .01 * 2.**(-10)
    [xcrit,i,err] = NewtonMultiVarJapprox(Ffunc,JpertFind,x0,n,tol,h)
    print(xcrit)
    print(i)



    return

def Ffunc(x0):
    F = [4* x0[0]**2 + x0[1]**2 - 4, x0[0] + x0[1] -np.sin(x0[0]-x0[1])]
    return F

def Jfunc(x0):
    J  = [[8*x0[0],2*x0[1]],[1-np.cos(x0[0]-x0[1]),1+np.cos(x0[0]-x0[1])]]
    return J

def forwardDiff(f,s,h):
    df = (f(s + h) - f(s))/h
    return df

def JpertFind(x0,h):
    J = [[((4* (x0[0]+h)**2 + x0[1]**2 - 4)-(4* x0[0]**2 + x0[1]**2 - 4))/h, ((4* x0[0]**2 + (x0[1]+h)**2 - 4)-(4* x0[0]**2 + x0[1]**2 - 4))/h ],[(((x0[0]+h) + x0[1] -np.sin((x0[0]+h)-x0[1]))-(x0[0] + x0[1] -np.sin(x0[0]-x0[1])))/h, ((x0[0] + (x0[1]+h) -np.sin(x0[0]-(x0[1]+h)))-(x0[0] + x0[1] -np.sin(x0[0]-x0[1])))/h]]
    return J




driver()