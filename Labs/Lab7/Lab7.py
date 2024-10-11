import numpy as np
import matplotlib.pyplot as plt
from Lab7Func import VandConstruct
from Lab7Func import polyconstruct
from interp import eval_lagrange
from interp import dividedDiffTable
from interp import evalDDpoly


def driver():
    f = lambda x: 1/(1+(10*x)**2)
    x = np.linspace(-1,1,1000)


    y=np.zeros(1000)
    y=f(x)
    V=np.vander(x,1000)

    A = np.linalg.solve(V,y)


    #plt.scatter(x,y)
    #plt.plot(x,np.polyfit(a,x))
 


    a = -1
    b = 1
    N = 10
   
   
    ''' create equispaced interpolation nodes'''
    xint = np.linspace(a,b,N+1)
    
    ''' create interpolation data'''
    yint = f(xint)
    
    ''' create points for evaluating the Lagrange interpolating polynomial'''
    Neval = 1000
    xeval = np.linspace(a,b,Neval+1)
    yeval_l= np.zeros(Neval+1)
    yeval_dd = np.zeros(Neval+1)
  
    '''Initialize and populate the first columns of the 
     divided difference matrix. We will pass the x vector'''
    y = np.zeros( (N+1, N+1) )
     
    for j in range(N+1):
       y[j][0]  = yint[j]

    y = dividedDiffTable(xint, y, N+1)
    ''' evaluate lagrange poly '''
    for kk in range(Neval+1):
       yeval_l[kk] = eval_lagrange(xeval[kk],xint,yint,N)
       yeval_dd[kk] = evalDDpoly(xeval[kk],xint,y,N)

    plt.plot(xeval,yeval_l)
    plt.show()


    
    plt.plot(xeval,yeval_dd)
    plt.show()







    


    return


driver()