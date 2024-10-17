import numpy as np
import matplotlib.pyplot as plt
#from demo_cubicspline import eval_cubic_spline

def PRELAB(x0,x1,f,xeval):
    m = (f(x1)-f(x0))/(x1-x0)
    yint = f(x0) - m*x0
    y = m * xeval +yint
    return y


def eval_lin_spline(xeval,Neval,a,b,f,Nint):

    xint = np.linspace(a,b,Nint+1)
    
    yeval = np.zeros(Neval)
    for j in range(Nint):

        atmp = xint[j]
        btmp= xint[j+1]
        # find indices of values of xeval in the interval
        ind= np.where((xeval >= atmp) & (xeval <= btmp))
        xloc = xeval[ind]
        n = len(xloc)
        fa = f(atmp)
        fb = f(btmp)
        yloc = np.zeros(len(xloc))
        for kk in range(n):
            #use your line evaluator to evaluate the spline at each location
            yloc[kk] = PRELAB(atmp,btmp,f,xloc[kk])#Call your line evaluator with points (atmp,fa) and (btmp,fb)
            # Copy yloc into the final vector
        yeval[ind] = yloc
    
    return yeval


def driver():

    f = lambda x: 1/(1+(10*x)**2)
    a = -1
    b = 1
    """ create points you want to evaluate at"""
    Neval = 1000
    xeval = np.linspace(a,b,Neval)

    for N in range(2,30):
        yeval = eval_lin_spline(xeval,Neval,a,b,f,N)
        #this one is shit so plot it
  
        plt.plot(xeval,yeval)
        plt.plot(xeval,f(xeval))
        plt.title('$N$ = {}'.format(N))
        plt.xlabel('$x$')
        plt.ylabel('$y$')
        plt.legend(['Data','Polynomial','$f(x)$'])
        plt.show()
    if (N%3) == 0 :

        plt.plot(xeval,yeval)
        plt.plot(xeval,f(xeval))
        plt.title('$N$ = {}'.format(N))
        plt.xlabel('$x$')
        plt.ylabel('$y$')
        plt.legend(['Data','Polynomial','$f(x)$'])
        plt.show()



    return


driver()