import numpy as np
import matplotlib.pyplot as plt
from Functions import findconvRate

def forwardDiff(f,s,h):
    df = (f(s + h) - f(s))/h
    return df

def midDiff(f,s,h):
    df = (f(s + h) - f(s-h))/(2*h)
    return df

def driver():
    f = lambda x: np.cos(x)
    s = np.pi/2
    h = .01 * 2.**(-np.arange(0,10))

    dfFor = forwardDiff(f,s,h)
    dfMid = midDiff(f,s,h)

    [dfForFit,diff1,diff2] = findconvRate(dfFor,-1)




    [dfMidFit,diff1,diff2] = findconvRate(dfMid,-1)

    

    



    return


driver()