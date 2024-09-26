import numpy as np
import matplotlib.pyplot as plt
from RootFindingBetter import bisection
from RootFindingBetter import Newton
from RootFindingBetter import Bisect2Newt

def driver():
    f = lambda x: np.exp((x**2)+7*x-30) - 1
    df = lambda x: (2*x+7)*np.exp((x**2)+7*x-30)
    ddf = lambda x: ((2*x+7)**2)*np.exp((x**2)+7*x-30) + 2*np.exp((x**2)+7*x-30)


    a = 2
    b = 4.5
    x0 = 4.5
    n =60
    tol = 1e-16

    [xBi,iBi,errBi] = bisection(f,a,b,n,tol)

    print("The root found with bisection is: ", xBi)
    print("Iterations needed: ", iBi)
    print("Error message (1 = failed, 0 = worked): ", errBi)

    [xNewt,pNewt,iNewt,errNewt] = Newton(f,df,x0,n,tol)

    print("The root found with Newton is: ", xNewt)
    print("Iterations needed: ", iNewt)
    print("Error message (1 = failed, 0 = worked): ", errNewt)

    [xComb,pComb,iComb,errComb] = Bisect2Newt(f,df,ddf,a,b,n,tol)

    print("The root found with the combined method is: ", xComb)
    print("Iterations needed: ", iComb)
    print("Error message (1 = failed, 0 = worked): ", errComb)

    return

driver()