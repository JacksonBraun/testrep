import numpy as np
import math as math
import matplotlib.pyplot as plt
from RootFindWIterations import fixedpntIts
from RootFindWIterations import findconvRate
from RootFindWIterations import AitkenDelSq

def driver():
    #2.1

    g = lambda x: (10/(x+4))**.5

    x0 = 1.5
    n = 100
    tol =1e-10

    [xcrit,i,err,p] = fixedpntIts(g,x0,n,tol)

    print("The crit point is: ", xcrit)
    print("Iterations taken: ",i)
    print("Error Message Reads: ", err)

    n = np.linspace(0,i,i)
    p1 = np.zeros(i)
    print(p1)
    ptrue = 1.3652300134140976
    for k in range(i):
        p1[k] = p[k]

    plt.scatter(n,np.log(abs(ptrue-p1)))
    plt.show()

    [fit,diff1,diff2] = findconvRate(p1,ptrue)

    phat = AitkenDelSq(p1)

    [fit2,diff12,diff22] = findconvRate(phat,ptrue)











    return

driver()