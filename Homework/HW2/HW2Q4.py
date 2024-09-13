import numpy as np
import math as math
import matplotlib.pyplot as plt

def driver():
    #4.a
    t = np.linspace(0,np.pi,31)
    y = np.cos(t)

    S = 0
    (n,) = np.shape(t)
    print(y)

    for i in range(n):
        S = S + t[i]*y[i]

    print("The sum is: ", S)


    #4.b
#first part
    n =100
    theta = np.linspace(0, 2*np.pi,n)
    R = 1.2
    delta = .1
    f = 15
    p = 0


    [X1, Y1] = funcgenHW2(theta,R,delta, f, p)





    plt.plot(X1,Y1)
    plt.show()


    delta = .05
    X2 = np.ndarray((10,n))
    Y2 = np.ndarray((10,n))
    for i in range(10):
        R = i
        f = 2 + i
        p = np.random.uniform(0,2)

        [X2[i][:],Y2[i][:]]= funcgenHW2(theta,R,delta, f, p)
        
        plt.plot(X2[i][:],Y2[i][:])
        print("iteration: ", i)
    plt.show()








    return

#imputs:  theta(Vector), R(double), delta(double), f(double),p(double)
#return: X,Y
def funcgenHW2(theta, R, delta, f, p):

    X =  R*(1 + delta*np.sin(f*theta + p))*np.cos(theta)
    Y =  R*(1 + delta*np.sin(f*theta + p))*np.sin(theta)
    return [X, Y]

driver()