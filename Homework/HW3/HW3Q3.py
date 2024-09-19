import numpy as np
import matplotlib.pyplot as plt
from RootFind import bisection
from RootFind import fixedpoint


def driver():
    a = 1
    b = 4
    f = lambda x: x**3 + x  - 4
    n = 52
    tol = 1e-3

    [xcrit,i,err] = bisection(f,a,b,n,tol)
    
    print("The found root for 3 is: ", xcrit)
    print("Iterations needed: ", i)
    print("Error message (1 = worked, 0 = failed): ", err)



    return

driver()