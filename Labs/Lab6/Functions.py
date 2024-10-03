import numpy as np
import scipy as scipy



def findconvRate(p,pact):
    diff1 = np.abs(p[1::]-pact)
    diff2 = np.abs(p[0:-1]-pact)

    fit = np.polyfit(np.log(diff2.flatten()),np.log(diff1.flatten()),1)

    print("The convergence rate is")
    print('log(|p_{n+1}-p|) = log(lambda) + alpha*log(|p_n-p|) where')
    print('lambda = ' + str(np.exp(fit[1])))
    print('alpha = ' + str(fit[0]))

    return [fit,diff1,diff2]


def SlackerNewton(Jfunc,F,x0,n,tol):

    #p = np.zeros([n,l])
    #p[0] = x0


    totit = 0
    for j in range(n):
        J = Jfunc(x0)

        for i in range(5):
            p1 = x0 - np.linalg.solve(J, F(x0))
            #p[i] = p1
            if np.linalg.norm(p1 - x0) < tol :
                xcrit  = p1
                err = 0
                totit = totit + i
                return [xcrit,totit,err]
            
            if np.linalg.norm(p1 - x0) > 1e5:
                print("The solution has diverged, pick an x0 in the region of convergence or try a different method")
                err = 1
                xcrit = p1
                totit = totit + i
                return [xcrit,totit,err]
            x0 = p1
        totit = totit + i
        i = 0
    
    
    xcrit = p1
    err = 1
    return [xcrit,i,err]


def NewtonMultiVarJapprox(F,J,x0,n,tol,h):

    #p = np.zeros([n,l])
    #p[0] = x0

    for i in range(n):
        p1 = x0 - np.linalg.solve(J(x0,h), F(x0))
        #p[i] = p1
        if np.linalg.norm(p1 - x0) < tol :
            xcrit  = p1
            err = 0
            return [xcrit,i,err]
        
        if np.linalg.norm(p1 - x0) > 1e5:
            print("The solution has diverged, pick an x0 in the region of convergence or try a different method")
            err = 1
            xcrit = p1
            return [xcrit,i,err]
        x0 = p1
    
    xcrit = p1
    err = 1
    return [xcrit,i,err]