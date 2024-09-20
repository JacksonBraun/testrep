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



def bisectionClass(f,a,b,tol):
    
#    Inputs:
#     f,a,b       - function and endpoints of initial interval
#      tol  - bisection stops when interval length < tol

#    Returns:
#      astar - approximation of root
#      ier   - error message
#            - ier = 1 => Failed
#            - ier = 0 == success

#     first verify there is a root we can find in the interval 

    fa = f(a)
    fb = f(b)
    if (fa*fb>0):
       ier = 1
       astar = a
       return [astar, 0, ier]

#   verify end points are not a root 
    if (fa == 0):
      astar = a
      ier =0
      return [astar, 0, ier]

    if (fb ==0):
      astar = b
      ier = 0
      return [astar, 0, ier]

    count = 0
    d = 0.5*(a+b)
    while (abs(d-a)> tol):
      fd = f(d)
      if (fd ==0):
        astar = d
        ier = 0
        return [astar, count, ier]
      if (fa*fd<0):
         b = d
      else: 
        a = d
        fa = fd
      d = 0.5*(a+b)
      count = count +1
#      print('abs(d-a) = ', abs(d-a))
      
    astar = d
    ier = 0
    return [astar, count, ier]