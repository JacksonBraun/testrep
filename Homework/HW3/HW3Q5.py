import numpy as np
import math as math
import matplotlib.pyplot as plt
from RootFind import fixedpoint

def driver():
    x = np.linspace(-10,10,100)
    f = lambda x: x - 4*np.sin(2*x) -3

    plt.plot(x,f(x))
    plt.plot(x,0*x)
    plt.show()





    return


driver()