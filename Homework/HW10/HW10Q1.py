import numpy as np
import math as math
import matplotlib.pyplot as plt


def driver():

    f = lambda x: np.sin(x)
    M6 = lambda x:  x - (x**3)/(math.factorial(3)) + (x**5)/(math.factorial(5)) 
    P33 = lambda x: (x - (7/60)*x**3)/(1+(1/20)*x**2)
    P24 = lambda x: x/(1 + (1/6)*x**2 + (7/360)*x**4)
    P42 = lambda x: (x - (7/60)*x**3)/(1 + (1/20)*x**2)

    a = 0
    b = 5
    x = np.linspace(a,b,100)
    #plotting fun now. idk how many I should make, leaning towards quite a few

    plt.plot(x,f(x),label="f(x)")
    plt.plot(x,M6(x),label="6th deg McLauren")
    plt.plot(x,P33(x),label="Pade 3 deg num, 3 deg den")
    plt.plot(x,P24(x),label="Pade 2 deg num, 4 deg den")
    plt.plot(x,P42(x),label="Pade 4 deg num, 2 deg den")
    plt.title("All the approxes and the function on one")
    plt.legend()
    plt.show()


    plt.plot(x,M6(x)-f(x),label="6th deg McLauren")
    plt.plot(x,P33(x)-f(x),label="Pade 3 deg num, 3 deg den")
    plt.plot(x,P24(x)-f(x),label="Pade 2 deg num, 4 deg den")
    plt.plot(x,P42(x)-f(x),label="Pade 4 deg num, 2 deg den")
    plt.title("Error of Approximation")
    plt.legend()
    plt.show()



    return

driver()