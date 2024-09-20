import numpy as np
import math as math
import matplotlib.pyplot as plt
from RootFind import fixedpoint

def driver():
    #For the plotting  of the normal function to find the zeros
    x = np.linspace(-10,10,100)
    f = lambda x: x - 4*np.sin(2*x) -3

    plt.plot(x,f(x))
    plt.plot(x,0*x)
    plt.show()


    #rearrange the equation for fixed point solver to work
    g = lambda x: - np.sin(2*x) + (5*x/4) - 3/4
    tol  = 1e-10
    n = 100


    x01 = -.9
    x02 = -.5
    x03 = 1.5
    x04 = 3
    x05 = 4.5

    [xcrit1, i1, err1] = fixedpoint(g,x01,n,tol)

    [xcrit2, i2, err2] = fixedpoint(g,x02,n,tol)

    [xcrit3, i3, err3] = fixedpoint(g,x03,n,tol)

    [xcrit4, i4, err4] = fixedpoint(g,x04,n,tol)

    [xcrit5, i5, err5] = fixedpoint(g,x05,n,tol)

    print("The first root found for 5 is: ", xcrit1)
    print("Iterations needed: ", i1)
    print("Error message (1 = worked, 0 = failed): ", err1)

    print("The second root found for 5 is: ", xcrit2)
    print("Iterations needed: ", i2)
    print("Error message (1 = worked, 0 = failed): ", err2)

    print("The third root found for 5 is: ", xcrit3)
    print("Iterations needed: ", i3)
    print("Error message (1 = worked, 0 = failed): ", err3)

    print("The forth root found for 5 is: ", xcrit4)
    print("Iterations needed: ", i4)
    print("Error message (1 = worked, 0 = failed): ", err4)

    print("The fith root found for 5 is: ", xcrit5)
    print("Iterations needed: ", i5)
    print("Error message (1 = worked, 0 = failed): ", err5)

    #the first fixed point is unstable meaning that we just keep moving away from it. Either to -infinity to or to the next critical point. The third and the fith are also unstable and will typically converge to one of the other two.
    #the second and fourth are very stable and they will be converged to in most regions




    return


driver()