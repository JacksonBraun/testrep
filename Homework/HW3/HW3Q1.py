import numpy as np
import math as math
import matplotlib.pyplot as plt
from RootFind import bisection

def driver():
    x = np.linspace(-10, 10, 100)
    f = lambda x: 2*x - 1 - np.sin(x)
    a = 0
    b = np.pi
    n = 52
    tol = 1e-8

    plt.plot(x,f(x))

    [xcrit, i, err] = bisection(f,a,b,n,tol)
    

    print("The found root for 1 is: ", xcrit)
    print("Iterations needed: ", i)
    print("Error message (1 = worked, 0 = failed): ", err)


    plt.plot(x,0*x)
    plt.scatter(xcrit,f(xcrit),s=15,c='r',marker='o')
    plt.show()

    return

driver()