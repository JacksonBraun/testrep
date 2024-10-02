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



    pNewtgood = cleanZeros(pNewt,iNewt)

    ynewt = np.abs(pNewtgood[1::]-xcritNewt)
    xnewt = np.abs(pNewtgood[0:-1]-xcritNewt)

 

    plt.plot(ynewt,xnewt)
    plt.xscale('log')
    plt.yscale('log')
    plt.title("Newton |x_k+1 - alpha| vs |x_k - alpha|")
    plt.show()


    pSecgood = cleanZeros(pSec,iSec)

    ySec = np.abs(pSecgood[2::]-xcritSec)
    xSec = np.abs(pSecgood[1:-1]-xcritSec)

 

    plt.plot(ySec,xSec)
    plt.xscale('log')
    plt.yscale('log')
    plt.title("Secant |x_k+1 - alpha| vs |x_k - alpha|")
    plt.show()

    return


def cleanZeros(p,i):
    p1 = np.zeros(i)
    for j in range(i):
        p1[j] = p[j]
    return p1


driver()