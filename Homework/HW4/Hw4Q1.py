import numpy as np
import scipy as scipy
import matplotlib.pyplot as plt
import scipy.special
from RootFind import bisection
from RootFind import Newton

def driver():

    Ti = 20
    Ts = -15
    alpha = .138e-6
    epsilon = 10**(-13)
    t = 60 * 24 *3600
    tol = 1e-10

    x = np.linspace(0,2,100)

    f = lambda x: (Ti - Ts)*(scipy.special.erf(x/(2*np.sqrt(alpha*t)))) + Ts
    df = lambda x: (Ti - Ts)*((2/np.sqrt(np.pi))*(1/(2*np.sqrt(alpha*t)))*np.exp(-(x**2)/(4*alpha*t)))

    a = 0
    b = 2

    plt.plot(x,f(x))
    plt.show()


    [xcrit,i,err] = bisection(f,a,b,52,tol)

    print("The first root found with bisection is: ", xcrit)
    print("Iterations needed: ", i)
    print("Error message (1 = worked, 0 = failed): ", err)

    x0 = .01
    n = 100

    [xcritNewt1,pNewt1,iNewt1,errNewt1] = Newton(f,df,x0,n,tol)

    print("The first root found with newton starting at x0 = .01 is: ", xcritNewt1)
    print("Iterations needed: ", iNewt1)
    print("Error message (1 = failed, 0 = worked): ", errNewt1)


    x0 = 2
    
    [xcritNewt2,pNewt2,iNewt2,errNewt2] = Newton(f,df,x0,n,tol)

    print("The first root found with newton starting at x0 = 2 is: ", xcritNewt2)
    print("Iterations needed: ", iNewt2)
    print("Error message (1 = failed, 0 = worked): ", errNewt2)


    return



driver()