import numpy as np
import matplotlib.pyplot as plt
import math as math
from fixedpt_example import fixedpt
from bisection_example import bisection



def driver():
    #4.1
    f1 = lambda x: (x**2) * (x -1)
    a = .5
    b = 2
    print("4.1 a-c")

    [xcrit, errmes] = bisection(f1,a,b, 1e-7)

    if errmes == 0:
        print("The root is: ", xcrit)
    else:
        print("Unable to find root")

    a = -1
    b = .5
    
    [xcrit, errmes] = bisection(f1, a,b, 1e-7)

    if errmes == 0:
        print("The root is: ", xcrit)
    else:
        print("Unable to find root")
    
    a = -1
    b = 2

    [xcrit, errmes] = bisection(f1,a,b, 1e-7)

    if errmes == 0:
        print("The root is: ", xcrit)
    else:
        print("Unable to find root")




    ## 4.2

    print("4.2 a-c")

    tol  = 1e-5

    f2 = lambda x: (x -1)*(x-3)*(x-5)
    a = 0
    b = 2.4

    [xcrit, errmes] = bisection(f2,a,b, tol)

    if errmes == 0:
        print("The root is: ", xcrit)
    else:
        print("Unable to find root")

    f3 = lambda x:((x -1)**2)*(x-3)
    a = 0
    b = 2

    [xcrit, errmes] = bisection(f3,a,b, tol)

    if errmes == 0:
        print("The root is: ", xcrit)
    else:
        print("Unable to find root")

    
    f4  = lambda x: np.sin(x)
    a = 0
    b = .1

    [xcrit, errmes] = bisection(f4,a,b, tol)

    if errmes == 0:
        print("The root is: ", xcrit)
    else:
        print("Unable to find root")

    a = .5
    b = 3*np.pi/4
    [xcrit, errmes] = bisection(f4,a,b, tol)

    if errmes == 0:
        print("The root is: ", xcrit)
    else:
        print("Unable to find root")




    # 4.3 

    print("4.3 a-d")

    Nmax = 1000
    tol = 1e-10
    x0 =1


    # the first two funcitons fail for this method

#     f5  = lambda x: x*(1 + ((7-x**5)/(x**2))**3)

# # # test f5 '''
#     [xstar,ier] = fixedpt(f5,x0,tol,Nmax)
#     print('the approximate fixed point is:',xstar)
#     print('f5(xstar):',f5(xstar))
#     print('Error message reads:',ier)



#     f6  = lambda x: x - (((x**5)-7)/(x**2))

# # # test f6 '''
#     [xstar,ier] = fixedpt(f6,x0,tol,Nmax)
#     print('the approximate fixed point is:',xstar)
#     print('f6(xstar):',f6(xstar))
#     print('Error message reads:',ier)


    f7  = lambda x: x - (((x**5)-7)/(5*x**4))

# # test f7 '''

    [xstar,ier] = fixedpt(f7,x0,tol,Nmax)
    print('the approximate fixed point is:',xstar)
    print('f7(xstar):',f7(xstar))
    print('Error message reads:',ier)



    
    f8  = lambda x: x - (((x**5)-7)/(12))

# # test f7 '''

    [xstar,ier] = fixedpt(f8,x0,tol,Nmax)
    print('the approximate fixed point is:',xstar)
    print('f8(xstar):',f8(xstar))
    print('Error message reads:',ier)







    return


## Bisection method code
#imputs: a(start),b(end),f (function), n (max num iterations), tol (acceptable error)
#outputs x (val where f(x) = 0 within tolarence), error message
# def bisection(a,b,f,n,tol):
    

#     fa = f(a)
#     fb = f(b)
#     if fa*fb < 0:
#         i = 0
#         while(i<n & abs(a-b)>2*tol):
#             xn = (a - b)/2
#             fxn = f(xn)
#             if fa*fxn < 0:
#                 #there is a change in sign between a and xn 
#                 b = xn
#                 fb = f(b)
#             elif fa*fxn > 0:
#                 #there not a change in sign which means it must be on the other side
#                 a = xn
#                 fa = f(a)
#             else:
#                 #f(xn) = 0 so this is our root
#                 x = xn
#                 a = xn
#                 b = xn
#                 errmes = 1

#             i = i +1
#         x = xn
#         errmes = 1   
#     elif fa*fb>0:
#         #there is no swap in signs Bisection wont work
#         errmes = 0
#         x = a

#     else:
#         if fa == 0:
#             # a is the root
#             x = a
#             errmes  =1
#         else:
#             # b is the root
#             x = b 
#             errmes =1
    
#     return [x, errmes]




# def fixedpoint():





#     return

driver()