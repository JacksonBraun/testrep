import numpy as np
import matplotlib.pyplot as plt





def BarryEvalLagrange(xeval,xint,yint,Nint):
    w = np.zeros(Nint + 1)
    ptop = 0
    pbottom = 0
    for j in range(Nint):

        w[j] = weightj(xint,xint[j],Nint)
    
    for j in range(Nint):
        ptop = ptop + ((w[j])/(xeval - xint[j]))*yint[j]
        pbottom = pbottom + ((w[j])/(xeval - xint[j]))
    yeval = ptop/pbottom


    return yeval

def monomial(xeval,xint,yint,N):
    V = np.vander(xint)
    a = np.linalg.solve(V, yint)
    return np.polyval(a,xeval)


  

def weightj(x,xj,N):
    wjden = 1
    for i in range(N):
        if not (x[i] ==  xj):
            wjden = wjden*(xj - x[i])
    wj = 1/wjden
    return wj

def chebyshev_points(a,b,Nint):
    k = np.arange(Nint)
    chebyshev_pts = 0.5 * (b - a) * np.cos((2 * k + 1) * np.pi / (2 * Nint)) + 0.5 * (a + b)
    return chebyshev_pts


def driver():
    Neval = 1001
    a = -1
    b = 1
    xeval = np.linspace(a,b,Neval)

    f = lambda x: 1/(1+(10*x)**2)

    



    for N in range(2,100):

        xint = np.zeros(N+1)
        xint = chebyshev_points(a,b,N)
        yint = f(xint)
        fBaryLam = np.zeros(Neval)
        for i in range(Neval):
            fBaryLam[i] = BarryEvalLagrange(xeval[i],xint,yint,N)
        # if (N%3) == 0 :
        #     plt.plot(xint,yint,'o')
        #     plt.plot(xeval,fBaryLam)
        #     plt.plot(xeval,f(xeval))
        #     plt.title('Bary Lagrange Chebyshev with $N$ = {}'.format(N))
        #     plt.xlabel('$x$')
        #     plt.ylabel('$y$')
        #     plt.legend(['Data','Polynomial','$f(x)$'])
        #     plt.show()

        #Now do it with monomial
        
    for N in range(2,100):

        xint = np.zeros(N+1)
        xint = chebyshev_points(a,b,N)
        yint = f(xint)
        fMon = np.zeros(Neval)
        fMon = monomial(xeval,xint,yint,N)
        
        if np.max(fMon) >= 100:
            #this one is shit so plot it
            plt.plot(xint,yint,'o')
            plt.plot(xeval,fMon)
            plt.plot(xeval,f(xeval))
            plt.title('Monomial Chebyshev $N$ = {}'.format(N))
            plt.xlabel('$x$')
            plt.ylabel('$y$')
            plt.legend(['Data','Polynomial','$f(x)$'])
            plt.show()
        if (N%11) == 0 :
            plt.plot(xint,yint,'o')
            plt.plot(xeval,fMon)
            plt.plot(xeval,f(xeval))
            plt.title('Monomial Chebyshev $N$ = {}'.format(N))
            plt.xlabel('$x$')
            plt.ylabel('$y$')
            plt.legend(['Data','Polynomial','$f(x)$'])
            plt.show()


    
    return

driver()