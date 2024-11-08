import numpy as np
import math as math
import matplotlib.pyplot as plt

# Function section: Trap, simpson, maybe a select between the two

def trap(f, xint, n):
    w = np.ones(np.shape(xint))
    w[0] = .5
    w[n] = .5
    print("w = ",w)
    yint = f(xint)
    total = ((xint[0] - xint[n])/n)*np.sum(w*yint)
    return total

def simpsons(f,xint, k):
    n = 2*k
    if not(xint%2 ==0):
        print("Hey idiot, the xint vect needs to have n sections where n = 2k, please try again")
        return 0
    w = np.ones(np.shape(xint))
    yint = f(xint)
    for i in range(1,n-1):
        if (i%2 == 0):
            w[i] = 4
        else:
            w[i] =2
    total = ((xint[0] - xint[n])/n)*np.sum(w*yint)
    return total

# how would I tell the difference? what makes each better? calc end error first? 