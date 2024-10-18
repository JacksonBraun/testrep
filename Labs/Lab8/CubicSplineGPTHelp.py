import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import inv
from numpy.linalg import norm

def driver():
    f = lambda x: 1 / (1 + (10 * x) ** 2)
    a = -1
    b = 1
    Neval = 1000
    xeval = np.linspace(a, b, Neval)
    Nint = 17
    xint = np.linspace(a, b, Nint + 1)
    yint = f(xint)

    spline = CubicNaturalSpline(xint, yint)

    # Evaluate the spline
    yeval = spline.evaluate(xeval)


    # Evaluate f at the evaluation points
    fex = f(xeval)

    nerr = norm(fex - yeval)
    print('nerr = ', nerr)
    
    plt.figure()    
    plt.plot(xeval, fex, label='Exact Function')
    plt.plot(xeval, yeval, label='Natural Spline') 
    plt.legend()
    plt.show()
     
    err = abs(yeval - fex)
    plt.figure() 
    plt.semilogy(xeval, err, 'ro--', label='Absolute Error')
    plt.legend()
    plt.show()

class CubicNaturalSpline:
    def __init__(self, x, y):
        self.x = np.array(x)
        self.y = np.array(y)
        self.n = len(x)
        
        # Coefficients
        self.a = self.y.copy()
        self.b = np.zeros(self.n - 1)
        self.c = np.zeros(self.n)
        self.d = np.zeros(self.n - 1)
        
        # Set up the system of equations
        self._compute_coefficients()

    def _compute_coefficients(self):
        # Step 1: Compute the h values
        h = np.diff(self.x)

        # Step 2: Construct the matrix and solve for c
        A = np.zeros((self.n, self.n))
        A[0, 0] = 1
        A[-1, -1] = 1

        for i in range(1, self.n - 1):
            A[i, i - 1] = h[i - 1]
            A[i, i] = 2 * (h[i - 1] + h[i])
            A[i, i + 1] = h[i]

        # Step 3: Right-hand side vector
        rhs = np.zeros(self.n)
        for i in range(1, self.n - 1):
            rhs[i] = (3 / h[i]) * (self.a[i + 1] - self.a[i]) - (3 / h[i - 1]) * (self.a[i] - self.a[i - 1])

        # Solve for c
        self.c = np.linalg.solve(A, rhs)

        # Step 4: Compute b and d coefficients
        for i in range(self.n - 1):
            self.b[i] = (self.a[i + 1] - self.a[i]) / h[i] - h[i] * (2 * self.c[i] + self.c[i + 1]) / 3
            self.d[i] = (self.c[i + 1] - self.c[i]) / (3 * h[i])

    def evaluate(self, x_eval):
        x_eval = np.array(x_eval)
        y_eval = np.zeros_like(x_eval)

        for i in range(self.n - 1):
            mask = (x_eval >= self.x[i]) & (x_eval <= self.x[i + 1])
            if np.any(mask):
                dx = x_eval[mask] - self.x[i]
                y_eval[mask] = (self.a[i] + 
                                self.b[i] * dx + 
                                self.c[i] * dx**2 + 
                                self.d[i] * dx**3)

        return y_eval

driver()
