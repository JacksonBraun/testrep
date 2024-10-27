import numpy as np
import math
import matplotlib.pyplot as plt
from numpy.linalg import inv 
from numpy.linalg import norm
from HW8Funct import eval_hermite
from HW8Funct import LagrangeEval
from HW8Funct import eval_cubic_spline
from HW8Funct import eval_local_spline
from HW8Funct import create_natural_spline
from HW8Funct import create_clamed_spline
from HW8Funct import eval_local_spline
from HW8Funct import eval_lagrange

def driver():
    Neval = 1001
    a = -5
    b = 5
    xeval = np.linspace(a,b,Neval+1)

    f = lambda x: 1/(1+(x)**2)
    fp  = lambda x: -2*x/((1+(x)**2)**2)



    for N in range(1,5):
        Nint = 5*N
        xint = np.linspace(a,b,Nint+1)

        yint = f(xint)
        ypint = fp(xint)
        yLag = np.zeros(Neval+1)
        yHerm = np.zeros(Neval+1)
        for i in range(Neval+1):
            yLag[i] = eval_lagrange(xeval[i],xint,yint,Nint)
            yHerm[i] = eval_hermite(xeval[i],xint,yint,ypint,Nint)
        (Mnat,CNat,DNat) = create_natural_spline(yint,xint,Nint)
        (MClamp,CClamp,DClamp) = create_clamed_spline(yint,xint,ypint[0],ypint[Nint],Nint)
        yNat = eval_cubic_spline(xeval,Neval,xint,Nint,Mnat,CNat,DNat)
        yClamped = eval_cubic_spline(xeval,Neval,xint,Nint,MClamp,CClamp,DClamp)

        #PLOT TIME!!!
        plt.plot(xeval,f(xeval),label='Actual Function')
        plt.plot(xeval,yLag,label='Lagrange Interp')
        plt.plot(xint,yint,'o')
        plt.title('Lagrange with $N$ = {}'.format(Nint))
        plt.legend
        plt.show()

        plt.plot(xeval,f(xeval),label='Actual Function')
        plt.plot(xeval,yHerm,label='Hermite Interp')
        plt.plot(xint,yint,'o')
        plt.title('Hermite with $N$ = {}'.format(Nint))
        plt.legend
        plt.show()

        plt.plot(xeval,f(xeval),label='Actual Function')
        plt.plot(xeval,yNat,label='Natural Spline')
        plt.plot(xint,yint,'o')
        plt.title('Natural Spline with $N$ = {}'.format(Nint))
        plt.legend
        plt.show()

        plt.plot(xeval,f(xeval),label='Actual Function')
        plt.plot(xeval,yClamped,label='Clamped Spline')
        plt.plot(xint,yint,'o')
        plt.title('Clamped Spline with $N$ = {}'.format(Nint))
        plt.legend
        plt.show()
    return

driver()




