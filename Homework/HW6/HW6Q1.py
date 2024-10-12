import numpy as np
import time
from HW6Func import newtonND
from HW6Func import Broyden
from HW6Func import LazyNewton


def driver():

    ## Question 1

    x01 = [1,1]
    x02 = [1,-1]
    x03 = [0,0]
    tol = 1e-8
    n = 50

    TimeNewt1 = time.perf_counter()
    [X, Xstar, info, i] = newtonND(Ffunc,JFunc,x01,tol,n)

    print("The root from x0 = [1,1] using Newtons method is: ", Xstar)
    print("Took i iterations: ", i)

    [X, Xstar, info, i] = newtonND(Ffunc,JFunc,x02,tol,n)

    print("The root from x0 = [1,-1] using Newtons method is: ", Xstar)
    print("Took i iterations: ", i)

    # [X, Xstar, info, i] = newtonND(Ffunc,JFunc,x03,tol,n)

    print("The root from x0 = [0,0] fails as it is the Jacobian at x0 is singular")
    print("Took i iterations: NA")


    TimeNewt2 = time.perf_counter()

    print("total runtime for all Newton: ", TimeNewt2-TimeNewt1)



    TimeBroy1 = time.perf_counter()

    [X, Xstar, info, i] = Broyden(Ffunc,JFunc(x01),x01,tol,n)

    print("The root from x0 = [1,1] using Broyden method is: ", Xstar)
    print("Took i iterations: ", i)

    [X, Xstar, info, i] = Broyden(Ffunc,JFunc(x02),x02,tol,n)

    print("The root from x0 = [1,-1] using Broyden method is: ", Xstar)
    print("Took i iterations: ", i)

    [X, Xstar, info, i] = Broyden(Ffunc,[[1,0],[0,1]],x03,tol,n)

    print("The root from x0 = [0,0] using Broyden method with B0 = I is: ", Xstar)
    print("Took i iterations: ", i)


    TimeBroy2 = time.perf_counter()

    print("Total time Broyden method took: ", TimeBroy2-TimeBroy1)


    TimeLazy1 = time.perf_counter()


    [X, Xstar, info, i] = LazyNewton(Ffunc,JFunc,x01,tol,n)

    print("The root from x0 = [1,1] using Lazy Newton method is: ", Xstar)
    print("Took i iterations: ", i)

    [X, Xstar, info, i] = LazyNewton(Ffunc,JFunc,x02,tol,n)

    print("The root from x0 = [1,-1] using Lazy Newton method is: ", Xstar)
    print("Took i iterations: ", i)

    #[X, Xstar, info, i] = LazyNewton(Ffunc,JFunc,x03,tol,n)

    print("The root from x0 = [0,0] using Lazy Newton fails as J0 is singular ")
    # print("Took i iterations: ", i)


    TimeLazy2 = time.perf_counter()

    print("Total time for Lazy Newton is: ",TimeLazy2-TimeLazy1)



    return

def Ffunc(x):
    f  = x[0]**2 + x[1]**2 - 4
    g = np.exp(x[0]) + x[1] - 1
    F = np.array([f,g])

    return F

def JFunc(x):
    J11 = 2*x[0]
    J12 = 2*x[1]
    J21  = np.exp(x[0])
    J22 = 1
    J = np.array([[J11,J12],[J21,J22]])
    return J


driver()