import numpy as np

def fixedpntIts(g,x0,n,tol):
    i = 0
    err = 0
    x1 = g(x0)
    p = np.zeros((n,1))
    while(i < n):
        if(abs(x1 - x0)<2*tol):
            xcrit = x1
            err  = 0 
            p[i] = x1
            return [xcrit,i,err,p]
        p[i] = x0
        x0 = x1
        x1 = g(x0)
        i = i + 1
    xcrit = x1
    err = 1
    return [xcrit,i,err,p]

def findconvRate(p,pact):
    diff1 = np.abs(p[1::]-pact)
    diff2 = np.abs(p[0:-1]-pact)

    fit = np.polyfit(np.log(diff2.flatten()),np.log(diff1.flatten()),1)

    print("The convergence rate is")
    print('log(|p_{n+1}-p|) = log(lambda) + alpha*log(|p_n-p|) where')
    print('lambda = ' + str(np.exp(fit[1])))
    print('alpha = ' + str(fit[0]))

    return [fit,diff1,diff2]

def cleanZeros(p,i):
    p1 = np.zeros(i)
    for j in range(i):
        p1[j] = p[j]
    return p1


def Newton(f,df,x0,n,tol):
    p = np.zeros(n+1)
    p[0] = x0
    
    for i in range(n):

        p1 = x0 - f(x0)/df(x0)
        p[i + 1] = p1
        if abs(p1 - x0) < tol:
            xcrit = p1
            err = 0
            return [xcrit,p,i,err]
        x0 = p1
    xcrit = p1
    err = 1
    return [xcrit,p,i,err]

def driver():

    g = lambda x: x-.5*x*np.cos(x)
    n = 100
    tol =1e-8

    f = lambda x: ((x-2)**2)*(x-4)*(x-5)
    df = lambda x: (x-2)*(4*x**2 - 31*x + 58)
    ddf = lambda x: 12*x**2 - 78*x +120
    x0 = .5

    [xcritog,pog,iog,errog]= Newton(f,df,x0,n,tol)

    print(xcritog)
    print(iog)

    pog1 = cleanZeros(pog,iog)
    [fit,diff1,diff2] = findconvRate(pog1,xcritog)

    [xcrit2,p2,i2,err2] = Newton(df,ddf,x0,n,tol)
    print(xcrit2)
    print(i2)
    p21 = cleanZeros(p2,i2)
    [fit,diff1,diff2] = findconvRate(p21,xcrit2)






    # [xcrit,i,err,p] = fixedpntIts(g,x0,n,tol)

    # print(xcrit)
    # print(i)
    # print(err)
    # p1 = cleanZeros(p,i)

    # [fit,diff1,diff2] = findconvRate(p1,xcrit)

    return


driver()
