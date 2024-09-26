import numpy as np
import math as math

def bisection(f,a,b,n,tol):
    fa = f(a)
    fb = f(b)
    err = 0
    if fa*fb < 0:
        i =0
        while(i < n ):
            xn = (b+a)/2
            fx = f(xn)
            if fx*fa < 0:
                b = xn
                fb = fx
            elif fx*fa > 0:
                a = xn
                fa = fx
            else:
                x = xn
                err = 1
                return [x,i,err]
            i = i+1
            if (abs(a - b) < tol):
                x = xn
                err = 1
                return [x,i,err]
        x =xn
        err = 1

    elif fa*fb > 0:
        err = 0
        x = a
        i = 0
    elif fa ==0:
        x = a
        err = 1
        i=0
    else:
        x = b
        err  = 1
        i=0
    return [x, i, err]

def fixedpoint(g,x0,n,tol):
    i = 0
    err = 0
    x1 = g(x0)
    while(i < n):
        if(abs(x1 - x0)<2*tol):
            xcrit = x1
            err  =1
            return [xcrit,i,err]
        x0 = x1
        x1 = g(x0)
        i = i + 1
    xcrit = x1
    if(abs(x1 - x0)<2*tol):
        err = 1
    else:
       err = 0
    return [xcrit,i,err]

def Newton(f,df,x0,n,tol):
    p = np.zeros(n+1)
    p[0] = x0
    
    for i in range(n):

        p1 = x0 - f(x0)/df(x0)
        p[i + 1] = p1
        if abs(p1 - x0) < tol:
            xcrit = p1
            err = 0
            return [xcrit,p,i,err]
        x0 = p1
    xcrit = p1
    err = 1
    return [xcrit,p,i,err]


def findconvRate(p,pact):
    diff1 = np.abs(p[1::]-pact)
    diff2 = np.abs(p[0:-1]-pact)

    fit = np.polyfit(np.log(diff2.flatten()),np.log(diff1.flatten()),1)

    print("The convergence rate is")
    print('log(|p_{n+1}-p|) = log(lambda) + alpha*log(|p_n-p|) where')
    print('lambda = ' + str(np.exp(fit[1])))
    print('alpha = ' + str(fit[0]))

    return [fit,diff1,diff2]


def fixedpntIts(g,x0,n,tol):
    i = 0
    err = 0
    x1 = g(x0)
    p = np.zeros((n,1))
    while(i < n):
        if(abs(x1 - x0)<2*tol):
            xcrit = x1
            err  = 0 
            p[i] = x1
            return [xcrit,i,err,p]
        p[i] = x0
        x0 = x1
        x1 = g(x0)
        i = i + 1
    xcrit = x1
    err = 1
    return [xcrit,i,err,p]

def secant(f,a,b,n,tol):
    x0 = a
    x1 = b
    p = np.zeros(n)
    p[0] = x0
    p[1] = x1
    for i in range(n-2):
        x2 = x0 - f(x1)*(x1-x0)/(f(x1) - f(x0))
        p[i+2] = x2
        if abs(x2-x1) < tol:
            xcrit = x2
            err = 0
            return [xcrit,p,i,err]
        x0 = x1
        x1 = x2
    xcrit  = x2
    err = 1
    return [xcrit,p,i,err]