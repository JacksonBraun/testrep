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
    Nint = 9
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
    plt.plot(xint,yint,"o")
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
 #    create the right  hand side for the linear system
    b = np.zeros(N+1)
#  vector values
    h = np.zeros(N+1)  
    for i in range(1,N):
       hi = xint[i]-xint[i-1]
       hip = xint[i+1] - xint[i]
       b[i] = (yint[i+1]-yint[i])/hip - (yint[i]-yint[i-1])/hi
       h[i-1] = hi
       h[i] = hip

#  create the matrix A so you can solve for the M values
    A = np.zeros((N+1,N+1))

    A[0][0] =  1  # Natural spline boundary condition at the first point
    for i in range(1, N):
        A[i][i - 1] = h[i-1]/6
        A[i][i] = (h[i]+h[i-1])/3
        A[i][i + 1] = h[i+1]/6
    A[N][N] = 1

    print(A)





#  Invert A    
    Ainv = inv(A)

# solver for M   
  
    M = Ainv.dot(b)
    
#  Create the linear coefficients
    C = np.zeros(N)
    D = np.zeros(N)


    for i in range(N):
        C[i] = yint[i]/h[i] - M[i]*(h[i])/6
        D[i] = yint[i+1]/h[i] - M[i+1]*(h[i])/6

    return(M,C,D)
    
       
def eval_local_spline(xeval,xi,xip,Mi,Mip,C,D):
# Evaluates the local spline as defined in class
# xip = x_{i+1}; xi = x_i
# Mip = M_{i+1}; Mi = M_i

    # hi = xip-xi

    # yeval = ((Mi*(xip - xeval)**3)/(6*hi) + (Mip*(xeval-xi)**3)/(6*hi) + C*(xip - xeval) + D*(xeval - xi))

    hi = xip-xi
    yeval = (Mi*(xip-xeval)**3 +(xeval-xi)**3*Mip)/(6*hi) \
    + C*(xip-xeval) + D*(xeval-xi)
   
   
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


