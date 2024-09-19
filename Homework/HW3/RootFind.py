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
    err = 1
    return [xcrit,i,err]