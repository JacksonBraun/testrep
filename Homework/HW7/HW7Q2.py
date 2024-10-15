import numpy as np
import matplotlib.pyplot as plt


def BaryLagrange(xeval,xint,yint,Nint,Neval):
    p = np.zeros(Neval)
    w = np.zeros(Nint)
    print(Nint)
    for j in range(Nint):
        w[j] = weightj(xint,xint[j],Nint)
        print(w[j])

    for i in range(Neval):
        p1 = 0
        for j in range(Nint):
            if not (xeval[i] == xint[j]):
                p1 = p1 + ((w[j]/(xeval[i] - xint[j]))*yint[j])/(w[j]/(xeval[i]-xint[j]))
        p[i] = p1
    
    return p


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


  

def weightj(x,xj,N):
    wjden = 1
    for i in range(N):
        if not (x[i] ==  xj):
            wjden = wjden*(xj - x[i])
    wj = 1/wjden
    return wj


def driver():
    Neval = 1001
    a = -1
    b = 1
    xeval = np.linspace(a,b,Neval)

    f = lambda x: 1/(1+(10*x)**2)

    



    for N in range(2,30):
        xint = np.linspace(-1,1,N)
        yint = f(xint)
        fBaryLam = np.zeros(Neval)
        for i in range(Neval):
            fBaryLam[i] = BarryEvalLagrange(xeval[i],xint,yint,N)
        if np.max(fBaryLam) >= 100:
            #this one is shit so plot it
            plt.plot(xint,yint,'o')
            plt.plot(xeval,fBaryLam)
            plt.plot(xeval,f(xeval))
            plt.title('$N$ = {}'.format(N))
            plt.xlabel('$x$')
            plt.ylabel('$y$')
            plt.legend(['Data','Polynomial','$f(x)$'])
            plt.show()
        if (N%3) == 0 :
            plt.plot(xint,yint,'o')
            plt.plot(xeval,fBaryLam)
            plt.plot(xeval,f(xeval))
            plt.title('$N$ = {}'.format(N))
            plt.xlabel('$x$')
            plt.ylabel('$y$')
            plt.legend(['Data','Polynomial','$f(x)$'])
            plt.show()
        
    
    return

driver()