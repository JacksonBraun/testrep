import numpy as np
import math as math
import scipy as scipy
import matplotlib.pyplot as plt
import scipy.integrate

# Function section: Trap, simpson, maybe a select between the two

def trap(f, xint, n):
    w = np.ones(np.shape(xint))
    w[0] = .5
    w[n] = .5
    yint = f(xint)
    total = ((xint[n] - xint[0])/n)*np.sum(w*yint)
    return total

def simpsons(f,xint, k):
    n = 2*k
    if not(n%2 ==0):
        print("Hey idiot, the xint vect needs to have n sections where n = 2k, please try again")
        return 0
    w = np.ones(np.shape(xint))
    yint = f(xint)
    for i in range(1,n-1):
        if (i%2 == 0):
            w[i] = 4
        else:
            w[i] =2
   
    total = (1/3)*((xint[n] - xint[0])/n)*np.sum(w*yint)
    return total

# how would I tell the difference? what makes each better? calc end error first

def driver():


    a = -5
    b = 5
    k = 1000
    N = 2*k
    x = np.linspace(a,b,N+1)
    f = lambda x: 1/(1+x**2)

    trapInt = trap(f,x,N)

    simpint = simpsons(f,x,k)

    quad = scipy.integrate.quad(f,a,b)


    print("Trapizoidal Method: ", trapInt)
    print("Simpson's Method: ", simpint)
    print("Scipy : ", quad)



    return


driver()