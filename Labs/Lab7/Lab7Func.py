
import numpy as np
import math
from numpy.linalg import inv

# def eval_lin_spline(xeval,Neval,a,b,f,Nint):
#     '''create the intervals for piecewise approximations'''
#     xint = np.linspace(a,b,Nint+1)
#     '''create vector to store the evaluation of the linear splines'''
#     yeval = np.zeros(Neval)
#     for jint in range(Nint):
#         '''find indices of xeval in interval (xint(jint),xint(jint+1))'''
#         '''let ind denote the indices in the intervals'''
#         '''let n denote the length of ind'''
#         '''temporarily store your info for creating a line in the interval of
#         interest'''
#         a1= xint(jint)
#         fa1 = f(a1)
#         b1 = xint(jint+1)
#         fb1 = f(b1)
#         for kk in range(n):
#             '''use your line evaluator to evaluate the lines at each of the points
#             in the interval'''
#             '''yeval(ind(kk)) = call your line evaluator at xeval(ind(kk)) with
#             the points (a1,fa1) and (b1,fb1)'''
#             if __name__ == '__main__':
#                 # run the drivers only if this is called from the command line
#                 driver()


def VandConstruct(x,n):
    V = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            V[i][j] = x[i]**j

    return V


def polyconstruct(a,n,x):
    p = 0
    for i in range(n):
        p = p+a[i]*x**i
    return p