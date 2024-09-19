import numpy as np
import math as math

def fixedpntIts(g,x0,n,tol):
    i = 0
    err = 0
    x1 = g(x0)
    p = np.zeros((n,1))
    while(i < n):
        if(abs(x1 - x0)<2*tol):
            xcrit = x1
            err  =1
            p[i] = x1
            return [xcrit,i,err,p]
        p[i] = x0
        x0 = x1
        x1 = g(x0)
        i = i + 1
    xcrit = x1
    err = 1
    return [xcrit,i,err]


def findconvRate(p,pact):
    diff1 = np.abs(p[1::]-pact)
    diff2 = np.abs(p[0:-1]-pact)

    fit = np.polyfit(np.log(diff2.flatten()),np.log(diff1.flatten()),1)

    print("The convergence rate is")
    print('log(|p_{n+1}-p|) = log(lambda) + alpha*log(|p_n-p|) where')
    print('lambda = ' + str(np.exp(fit[1])))
    print('alpha = ' + str(fit[0]))

    return [fit,diff1,diff2]

def AitkenDelSq(p):
    i = 0
    phat = np.zeros(len(p)-2)
    for i in range(len(p)-2):
        phat[i] = p[i] - (((p[i+1]-p[i])**2)/(p[i+2] -p[i+1]+p[i]))
    return phat






