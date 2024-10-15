import numpy as np
import matplotlib.pyplot as plt


def monomial(xeval,xint,yint,N):
    V = np.vander(xint)
    a = np.linalg.solve(V, yint)
    return np.polyval(a,xeval)

def driver():
    Neval = 1001
    a = -1
    b = 1
    xeval = np.linspace(a,b,Neval)

    f = lambda x: 1/(1+(10*x)**2)



    for N in range(2,21):
        xint = np.linspace(-1,1,N)
        yint = f(xint)
        fmon = monomial(xeval,xint,yint,N)
        if np.max(fmon) >= 100:
            #this one is shit so plot it
            plt.plot(xint,yint,'o')
            plt.plot(xeval,fmon)
            plt.plot(xeval,f(xeval))
            plt.title('$N$ = {}'.format(N))
            plt.xlabel('$x$')
            plt.ylabel('$y$')
            plt.legend(['Data','Polynomial','$f(x)$'])
            plt.show()
        if (N%3) == 0 :
            plt.plot(xint,yint,'o')
            plt.plot(xeval,fmon)
            plt.plot(xeval,f(xeval))
            plt.title('$N$ = {}'.format(N))
            plt.xlabel('$x$')
            plt.ylabel('$y$')
            plt.legend(['Data','Polynomial','$f(x)$'])
            plt.show()
        
    
    return

driver()