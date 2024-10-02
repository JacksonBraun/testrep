import numpy as np


#F: funct array, J: Jacobian Matrix (both are functions because I dont know another way), n: max number of iterations, tol: precision desired, l: number of variables in the question
def NewtonMultiVar(F,J,x0,n,tol,l):

    #p = np.zeros([n,l])
    #p[0] = x0

    for i in range(n):
        p1 = x0 - np.linalg.solve(J(x0),F(x0))
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


