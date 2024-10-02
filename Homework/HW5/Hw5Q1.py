import numpy as np
import matplotlib.pyplot as plt
from HighOrderRootFind import NewtonMultiVar


def driver():
    f  = lambda x : 3*x[0]**2 - x[1]**2
    g = lambda x : 3*x[0]*x[1]**2 - x[0]**3 -1


    J = np.array([[1/6, 1/18],[0, 1/6]])

    print(J)

    x0 = np.array([1,1])
    x1 = np.zeros((2, 1))
    tol = 1e-6
    i = 0
    n = 50

    print(x0)
    print(x1)

    print(np.shape(J))





    [x1,i,err] = MultiWeird(x0,J,n,tol)
        

    print(x1)
    print(i)
    l = 2

    [xNewt,iNewt,errNewt] = NewtonMultiVar(Ffunc,JFunc,x0,n,tol,l)

    print("Newtons Method:")
    print("xcrit: ", xNewt)
    print("iterations: ", iNewt)

    return

def MultiWeird(x0,J,n,tol):
    x1 = np.zeros(np.shape(x0))
    for i in range(n):

        F = Ffunc(x0)
        x1 = x0 - (J @ F)
        if np.linalg.norm(x1-x0) < tol:
            err = 0
            return [x1,i,err]
        x0 = x1
        
    err = 1
    return [x1,i,err]

def Ffunc(x):
    f  =  3*x[0]**2 - x[1]**2
    g = 3*x[0]*x[1]**2 - x[0]**3 -1
    F = np.array([f,g])

    return F

def JFunc(x):
    J11 = 6*x[0]
    J12 = -2*x[1]
    J21  =3*x[1]**2
    J22 = 6*x[0]*x[1]
    J = np.array([[J11,J12],[J21,J22]])
    return J


  
driver()