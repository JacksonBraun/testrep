import numpy as np
import math
from numpy.linalg import inv 
from numpy.linalg import norm


def eval_hermite(xeval,xint,yint,ypint,N):

    ''' Evaluate all Lagrange polynomials'''

    lj = np.ones(N+1)
    for count in range(N+1):
       for jj in range(N+1):
           if (jj != count):
              lj[count] = lj[count]*(xeval - xint[jj])/(xint[count]-xint[jj])

    ''' Construct the l_j'(x_j)'''
    lpj = np.zeros(N+1)
#    lpj2 = np.ones(N+1)
    for count in range(N+1):
       for jj in range(N+1):
           if (jj != count):
#              lpj2[count] = lpj2[count]*(xint[count] - xint[jj])
              lpj[count] = lpj[count]+ 1./(xint[count] - xint[jj])
              

    yeval = 0.
    
    for jj in range(N+1):
       Qj = (1.-2.*(xeval-xint[jj])*lpj[jj])*lj[jj]**2
       Rj = (xeval-xint[jj])*lj[jj]**2
#       if (jj == 0):
#         print(Qj)
         
#         print(Rj)
#         print(Qj)
#         print(xeval)
 #        return
       yeval = yeval + yint[jj]*Qj+ypint[jj]*Rj
       
    return(yeval)

def LagrangeEval(xeval,xint,yint,N):
    lj = np.ones(N+1)
    for count in range(N+1):
      for j in range(N):
         if not(j == count):
            lj[count] = lj[count]*(xeval-xint[count])/(xint[j]-xint[count])
    
    yeval = 0.
    
    for j in range(N+1):
       yeval = yeval + yint[j]*lj[j]
  
    return(yeval)

def eval_lagrange(xeval,xint,yint,N):

    lj = np.ones(N+1)
    
    for count in range(N+1):
       for jj in range(N+1):
           if (jj != count):
              lj[count] = lj[count]*(xeval - xint[jj])/(xint[count]-xint[jj])

    yeval = 0.
    
    for jj in range(N+1):
       yeval = yeval + yint[jj]*lj[jj]
  
    return(yeval)
  

def create_natural_spline(yint,xint,N):
 

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

    #print(A)

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
    yeval = (Mi*(xip-xeval)**3 +(xeval-xi)**3*Mip)/(6*hi) + C*(xip-xeval) + D*(xeval-xi)
   
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
   

def create_clamed_spline(yint,xint,fp0,fpn,N):

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
    b[0] = fp0
    b[N] = fpn
    # print(b)
    

#  create the matrix A so you can solve for the M values
    A = np.zeros((N+1,N+1))

    A[0][0] =  1  # Natural spline boundary condition at the first point
    for i in range(1, N):
        A[i][i - 1] = h[i-1]/6
        A[i][i] = (h[i]+h[i-1])/3
        A[i][i + 1] = h[i+1]/6
    A[N][N] = 1
    
    #print(A)

#  Invert A    
    Ainv = inv(A)

# solver for M   
  
    M = Ainv.dot(b)
    print(M)
    
#  Create the linear coefficients
    C = np.zeros(N)
    D = np.zeros(N)


    for i in range(N):
        C[i] = yint[i]/h[i] - M[i]*(h[i])/6
        D[i] = yint[i+1]/h[i] - M[i+1]*(h[i])/6

    return(M,C,D)


def chebyshev_points(a,b,Nint):
    #This only works when centered at zero I think. Please try and find a actually good organizing alg in the future, idiot!
    k = np.arange(Nint)
    chebyshev_pts = -0.5 * (b - a) * np.cos((2 * k + 1) * np.pi / (2 * Nint)) + 0.5 * (a + b)
    return chebyshev_pts

