import numpy as np
import math
import matplotlib.pyplot as plt
from numpy.linalg import inv 
from numpy.linalg import norm
from HW8Funct import create_clamed_spline
from HW8Funct import eval_local_spline
from HW8Funct import eval_cubic_spline

def driver():

    a = 0
    b = 2*np.pi
    Neval = 1000
    xeval = np.linspace(a,b,Neval+1)
    f = lambda x: np.sin(10*x)
    fp = lambda x: 10*np.cos(10*x)
    Nint = 30
    xint = np.linspace(a,b,Nint+1)
    yint = f(xint)
    ypint=fp(xint)
    (MClamp,CClamp,DClamp) = create_clamed_spline(yint,xint,ypint[Nint],ypint[Nint],Nint)
    yClamped = eval_cubic_spline(xeval,Neval,xint,Nint,MClamp,CClamp,DClamp)

    plt.plot(xeval,f(xeval),label='Actual Function')
    plt.plot(xeval,yClamped,label='Clamped Spline')
    plt.plot(xint,yint,'o')
    plt.title('Clamped Spline with $N$ = {}'.format(Nint))
    plt.legend
    plt.show()
    return

driver()