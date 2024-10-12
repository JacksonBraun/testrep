import numpy as np
import time
from HW6Func import SteepestDescent
from HW6Func import newtonND

def driver():
    x0 = [0,0,0]
    tol = 1e-6
    n = 100
    print("x0 for all will be [0,0,0]")


    TimeNewt1 = time.perf_counter()
    [X,Xcrit,info,i] = newtonND(Ffunc,Jfunc,x0,tol,n)
    print("Newton Method coverges to: ", Xcrit)
    print("Iterations taken: ", i)
    TimeNewt2 = time.perf_counter()
    print("Time taken for Newton: ", TimeNewt2-TimeNewt1)



    TimeSteep1 = time.perf_counter()
    [X,Xcrit,info,i] = SteepestDescent(Ffunc,Jfunc,x0,tol,n)
    print("Steepest Descent converges to: ", Xcrit)
    print("Iterations taken: ", i)
    TimeSteep2 = time.perf_counter()
    print("Time taken for Steepest Descent: ", TimeSteep2-TimeSteep1)

    TimeComb1= time.perf_counter()
    [X,Xcrit,info,i1] = SteepestDescent(Ffunc,Jfunc,x0,5e-2,n)
    [X,Xcrit,info,i2] = newtonND(Ffunc,Jfunc,Xcrit,tol,n-i1)
    print("The combined Method converges to: ", Xcrit)
    print("Iterations taken: ", i1+i2)
    TimeComb2 = time.perf_counter()
    print("Time taken for Steepest Descent: ", TimeComb2-TimeComb1)






    return

def Ffunc(x):
    f = x[0] + np.cos(x[0]*x[1]*x[2])
    g = (1-x[0])**.25 + x[1] + .05*x[2] - .15*x[2] - 1
    h = -x[0]**2 -.1*x[1]**2 + .01*x[1] + x[2] - 1
    F = np.array([f,g,h])

    return F

def Jfunc(x):
    J11 = 1 - x[1]*x[2]*np.sin(x[0]*x[1]*x[2])
    J12 = - x[0]*x[2]*np.sin(x[0]*x[1]*x[2])
    J13 = - x[0]*x[1]*np.sin(x[0]*x[1]*x[2])
    J21 = -1/(4*(1-x[0])**(.75))
    J22 = 1
    J23 = .1*x[2] - .15
    J31 = -2*x[0]
    J32 = -.2*x[1] + .01
    J33 = 1
    J = np.array([[J11, J12, J13],[J21,J22,J23],[J31,J32,J33]])
    return J



driver()