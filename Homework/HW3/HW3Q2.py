import numpy as np
import math as math
import matplotlib.pyplot as plt
from RootFind import fixedpoint
from RootFind import bisection

def driver():

    a = 4.82
    b = 5.2
    n = 52
    tol = 1e-4

    f1 = lambda x: (x-5)**9
    f2 = lambda x: x**9 - 45 * (x**8) + 900 * (x**7) -10500 * (x**6) + 78750 * (x**5) - 393750*(x**4) + 1312500 * (x**3) - 2812500* (x**2) + 3515625 * x - 1953125

    [xcrit1, i1, err1] = bisection(f1,a,b,n,tol)

    print("The found root for 1a is: ", xcrit1)
    print("Iterations needed: ", i1)
    print("Error message (1 = worked, 0 = failed): ", err1)

    [xcrit2, i2, err2] = bisection(f2,a,b,n,tol)

    print("The found root for 1a is: ", xcrit2)
    print("Iterations needed: ", i2)
    print("Error message (1 = worked, 0 = failed): ", err2)

    return

driver()
