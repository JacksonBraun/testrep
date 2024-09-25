import numpy as np
import matplotlib.pyplot as plt
from RootFind import Newton
from RootFind import fixedpntIts
from RootFind import findconvRate


def driver():
    a = 3
    b = 5

    m =2

    x = np.linspace(a,b,100)
    n = 50
    tol = 1e-16
    x0 = 4


    f = lambda x: np.exp(3*x) - (27 * x**6) +(27 * (x**4) * np.exp(x)) - (9*(x**2)*np.exp(2*x))
    df = lambda x: 3*np.exp(3*x) - 162*x**5 + (108*(x**3)*np.exp(x)) + (27 * (x**4) * np.exp(x)) - (18 * (x**2)*np.exp(2*x)) - (18 * x *np.exp(2*x))


    g1 = lambda x: f(x)/df(x)
    g2 = lambda x: x-m*f(x)/df(x)


    plt.plot(x,f(x))
    plt.show()


    [xcritNewt,pNewt,iNewt,errNewt] = Newton(f,df,x0,n,tol)

    pNewtGood = cleanZeros(pNewt,iNewt)



    print("The first root found with newton starting at x0 = 4 is: ", xcritNewt)
    print("Iterations needed: ", iNewt)
    print("Error message (1 = failed, 0 = worked): ", errNewt)

    [fitNewt,diff1Newt,diff2Newt] = findconvRate(pNewtGood,xcritNewt)



    [xcritNewtClass,iNewtClass,errNewtClass,pNewtClass] = Newton(g1,x0,n,tol)

    pNewtClassGood = cleanZeros(pNewtClass,iNewtClass)

    print("The first root found with modified newton from class starting at x0 = 4 is: ", xcritNewtClass)
    print("Iterations needed: ", iNewtClass)
    print("Error message (1 = failed, 0 = worked): ", errNewtClass)

    [fitNewtClass,diff1NewtClass,diff2NewtClass] = findconvRate(pNewtClassGood,xcritNewt)


    [xcritNewt2,iNewt2,errNewt2,pNewt2] = fixedpntIts(g2,x0,n,tol)

    pNewt2Good = cleanZeros(pNewt2,iNewt2)

    print("The first root found with modified newton from Q2 starting at x0 = 4 is: ", xcritNewt2)
    print("Iterations needed: ", iNewt2)
    print("Error message (1 = failed, 0 = worked): ", errNewt2)

    [fitNewt2,diff1Newt2,diff2Newt2] = findconvRate(pNewt2Good,xcritNewt2)


    return

def cleanZeros(p,i):
    p1 = np.zeros(i)
    for j in range(i):
        p1[j] = p[j]
    return p1


driver()