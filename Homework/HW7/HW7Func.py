import numpy as np


def lineinterpMon(x,y,N):
    V = VandConstruct(x,N)
    a = np.linalg.lstsq(V,y)

    return [a,V]

def VandConstruct(x,n):
    V = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            V[i][j] = x[i]**j

    return V