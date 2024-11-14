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
    return [xcrit,i,err,p]


def findconvRate(p,pact):
    diff1 = np.abs(p[1::]-pact)
    diff2 = np.abs(p[0:-1]-pact)

    fit = np.polyfit(np.log(diff2.flatten()),np.log(diff1.flatten()),1)

    print("The convergence rate is")
    print('log(|p_{n+1}-p|) = log(lambda) + alpha*log(|p_n-p|) where')
    print('lambda = ' + str(np.exp(fit[1])))
    print('alpha = ' + str(fit[0]))

    return [fit,diff1,diff2]

def AitkenDelSq(g,x0,n,tol):
    i = 0
    x1 = g(x0)
    p = np.zeros((n,1))
    phat = np.zeros(len(p)-2)
    # if converges in first 3, same as fixed point, then goes into aitkens meth which is when err = 2. Checks the phat deferences to insure that 
    while(i<n):
        if i<=2:
            if(abs(x1 - x0)<2*tol):
                xcrit = x1
                err  =1
                p[i] = x1
                return [xcrit,i,err,p]
            x0 = x1
            
        elif i>2:
            phat[i-2] = p[i-2] - ((p[i-1] - p[i-2])**2)/(p[i] -2*p[i-1]+p[i-2])
            if(abs(phat[i-2] - phat[i-3]) < tol):
                xcrit = phat[i-2]
                err = 2
                return[xcrit,i-2,err,phat]
            x0 = phat[i-2]
            
        x1 = g(x0)
        i = i + 1
    if(abs(phat[i-2] - phat[i-3]) < tol):
        xcrit = phat[i-2]
        err = 2
        return[xcrit,i-2,err,phat]
    else:
        xcrit = phat[i-2]
        err = 0
        return[xcrit,i-2,err,phat]





def steffensons(g,x0,n,tol):
    i = 0
    p = np.zeros((n,1))
    p[0] = x0
    while(i<n):
        a = p[i]
        b = g(a)
        c = g(b)
        p[i+1] = a - ((b-a)**2)/(c - 2*b + a)
        if (abs(p[i+1]-p[i]) < tol):
            xcrit = p[i+1]
            err =1
            return[xcrit,i+1,err,p]
        i = i+1
    if(abs(p[i+1]-p[i]) < tol):
        xcrit = p[i+1]
        err =1
        return[xcrit,i+1,err,p]
    else:
        xcrit = p[i+1]
        err = 0 
        return[xcrit,i+1,err,p]


        







