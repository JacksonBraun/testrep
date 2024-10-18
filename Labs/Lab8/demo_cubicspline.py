import matplotlib.pyplot as plt
import numpy as np
import math
from numpy.linalg import inv 
from numpy.linalg import norm


def driver():
    f = lambda x: 1/(1+(10*x)**2)
    a = -1
    b = 1
    """ create points you want to evaluate at"""
    Neval = 1000
    xeval = np.linspace(a,b,Neval)
    ''' number of intervals'''
    Nint = 4
    xint = np.linspace(a,b,Nint+1)
    yint = f(xint)

    ''' create points you want to evaluate at'''
    Neval = 100
    xeval =  np.linspace(xint[0],xint[Nint],Neval+1)

#   Create the coefficients for the natural spline    
    (M,C,D) = create_natural_spline(yint,xint,Nint)

#  evaluate the cubic spline     
    yeval = eval_cubic_spline(xeval,Neval,xint,Nint,M,C,D)
    
    
    ''' evaluate f at the evaluation points'''
    fex = f(xeval)
        
    nerr = norm(fex-yeval)
    print('nerr = ', nerr)
    
    plt.figure()    
    plt.plot(xeval,fex,label='exact function')
    plt.plot(xeval,yeval,label='natural spline') 
    plt.legend
    plt.show()
     
    err = abs(yeval-fex)
    plt.figure() 
    plt.semilogy(xeval,err,'ro--',label='absolute error')
    plt.legend()
    plt.show()
    
def create_natural_spline(yint,xint,N):
    #FORCE ALL h to be the same size, so equilaly spaced nodes

#    create the right  hand side for the linear system
    b = np.zeros(N-1)
#  vector values
    h = np.zeros(N+1)
    h[0] = xint[1] - xint[0]
    for i in range(1,N):
       h[i] = xint[i+1] - xint[i]
       if not(h[i] == h[i-1]):
            print("FUCK YOU MAN!!!!! YOU DONT NEED CHEBYSHEV NODES OR WHATEVER TF YOUR DOING")
            return
    

    for i in range(1,N-1):
        b[i] = (yint[i+2]-yint[i+1])/h[i] - (yint[i+1] - yint[i])/h[i]

#  create the matrix A so you can solve for the M values
    A = np.zeros((N,N))

    A[0, 0] =  4  # Natural spline boundary condition at the first point
    for i in range(1, N-2):
        A[i, i - 1] = 1
        A[i, i] = 4
        A[i, i + 1] = 1

    A[N-1, N - 2] = 1
    A[N-1, N-1] = 4

    A = 1/12 * A



#  Invert A    
    Ainv = inv(A)

# solver for M   
    M = np.zeros(N+1)
    M[0] = 0
    M[N] = 0
    M[1:-1]  = Ainv.dot(b)
    
#  Create the linear coefficients
    B = np.zeros(N)
    C = np.zeros(N)
    for i in range(N-1):
        B[i] = yint[i] - M[i]*(h[i]**2)/6
        C[i] = yint[i+1] - M[i+1]*(h[i]**2)/6
        return(M,B,C)
    
       
def eval_local_spline(xeval,xi,xip,Mi,Mip,B,C):
# Evaluates the local spline as defined in class
# xip = x_{i+1}; xi = x_i
# Mip = M_{i+1}; Mi = M_i

    hi = xip-xi

    yeval = (1/hi)*((Mi*(xip - xeval)**3)/(6*hi) + (Mip*(xi - xeval)**3)/(6*hi) + B*(xip - xeval) + C*(xeval - xi))
   
   
    return yeval 
    
    
def  eval_cubic_spline(xeval,Neval,xint,Nint,M,C,D):
    
    yeval = np.zeros(Neval+1)
    
    for j in range(Nint):
        '''find indices of xeval in interval (xint(jint),xint(jint+1))'''
        '''let ind denote the indices in the intervals'''
        atmp = xint[j]
        btmp= xint[j+1]
        
#   find indices of values of xeval in the interval
        ind= np.where((xeval >= atmp) & (xeval <= btmp))
        xloc = xeval[ind]

# evaluate the spline
        yloc = eval_local_spline(xloc,atmp,btmp,M[j],M[j+1],C[j],D[j])
#   copy into yeval
        yeval[ind] = yloc

    return(yeval)
           
driver()               


