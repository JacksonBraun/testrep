import numpy as np
import math as math


def Bisect2Newt(f,df,ddf,a,b,n,tol):
    #will produce an x in the basin of covergence as long as two points where f(x) is on either side of zero is provided.
    fa = f(a)
    fb = f(b)
    err = 0
    if fa*fb < 0:
        i =0
        while(i < n):
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
            if (abs((f(xn)*ddf(xn))/df(xn)) <1):
                x = xn
                err = 1
                return Newton(f,df,x,n,tol)
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