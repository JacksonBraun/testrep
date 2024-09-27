import numpy as np
import matplotlib.pyplot as plt
from RootFind import Newton
from RootFind import secant

def driver():

    f = lambda x: x**6 - x - 1
    df = lambda x: 6*x**5 - 1

    x0 = 2
    x1 = 1

    tol = 1e-10
    n =50

    [xcritNewt,pNewt,iNewt,errNewt] =Newton(f,df,x0,n,tol)

    print("The root found with Newton is: ", xcritNewt)
    print("Iterations needed: ", iNewt)
    print("Error message (1 = failed, 0 = worked): ", errNewt)

    print("Iteration #| P(i)     |p(i)-xcrit")
    for j in range(iNewt):
        print(j,"    |    ", pNewt[j],"    |  ",abs(xcritNewt-pNewt[j]))

    [xcritSec,pSec,iSec,errSec] = secant(f,x1,x0,n,tol)

    print("The root found with Newton is: ", xcritSec)
    print("Iterations needed: ", iSec)
    print("Error message (1 = failed, 0 = worked): ", errSec)

    print("Iteration #| P(i)     |p(i)-xcrit")
    for j in range(iSec):
        print(j,"    |    ", pSec[j],"    |  ",abs(xcritSec-pSec[j]))

    return



driver()