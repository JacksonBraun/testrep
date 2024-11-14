import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

def driver():

    a = 0
    b = 2*np.pi
    Neval = 1000
    xeval = np.linspace(a,b,Neval+1)
    f = lambda x: np.sin(10*x)
    fp = lambda x: 10*np.cos(10*x)
    Nint = 15
    xint = np.linspace(a,b,Nint+1)
    yint = f(xint)
    ypint=fp(xint)
    (MClamp,CClamp,DClamp) = create_periodic_spline(yint,xint,Nint)
    yClamped = eval_cubic_spline(xeval,Neval,xint,Nint,MClamp,CClamp,DClamp)

    plt.plot(xeval,f(xeval),label='Actual Function')
    plt.plot(xeval,yClamped,label='Clamped Spline')
    plt.plot(xint,yint,'o')
    plt.title('Clamped Spline with $N$ = {}'.format(Nint))
    plt.legend
    plt.show()
    return






def create_periodic_spline(yint, xint, N):
    """
    Create a periodic cubic spline given the values at the nodes, 
    the number of nodes N, and the periodic boundary conditions.
    
    Parameters:
    yint  : Array of function values at the interpolation nodes
    xint  : Array of interpolation nodes (x values)
    N     : Number of interpolation nodes
    
    Returns:
    M, C, D : Coefficients for the cubic spline
    """
    # Create the right-hand side for the linear system
    b = np.zeros(N + 1)
    h = np.zeros(N + 1)
    
    # Compute the h values (differences between x values)
    for i in range(1, N):
        hi = xint[i] - xint[i-1]
        hip = xint[i+1] - xint[i]
        b[i] = (yint[i+1] - yint[i])/hip - (yint[i] - yint[i-1])/hi
        h[i-1] = hi
        h[i] = hip
    
    # Create the matrix A for the linear system
    A = np.zeros((N + 1, N + 1))
    
    # Periodic boundary conditions
    # First and last node second derivatives must match
    A[0][0] = 1
    A[N][N] = 1
    b[0] = (yint[1] - yint[0]) / h[0]  # f'(x_0) = f'(x_N)
    b[N] = (yint[N] - yint[N-1]) / h[N-1]  # f'(x_N) = f'(x_0)
    
    # Fill the matrix A for the interior points
    for i in range(1, N):
        A[i][i-1] = h[i-1] / 6
        A[i][i] = (h[i] + h[i-1]) / 3
        A[i][i+1] = h[i] / 6
    
    # Periodic boundary conditions for the second derivative at the endpoints
    A[0][N-1] = h[N-1] / 6
    A[N][1] = h[0] / 6
    
    # Solve for the second derivatives M
    Ainv = inv(A)
    M = Ainv.dot(b)
    
    # Create the linear coefficients C and D
    C = np.zeros(N)
    D = np.zeros(N)
    
    for i in range(N):
        C[i] = yint[i] / h[i] - M[i] * h[i] / 6
        D[i] = yint[i+1] / h[i] - M[i+1] * h[i] / 6
    
    return M, C, D

def eval_local_spline(xeval, xi, xip, Mi, Mip, C, D):
    """
    Evaluate the cubic spline at a given point xeval within the interval [xi, xip]
    
    Parameters:
    xeval  : The point at which to evaluate the spline
    xi     : The left endpoint of the interval
    xip    : The right endpoint of the interval
    Mi     : The second derivative at xi
    Mip    : The second derivative at xip
    C      : The coefficient for the linear term
    D      : The coefficient for the constant term
    
    Returns:
    yeval  : The evaluated spline at xeval
    """
    hi = xip - xi
    yeval = (Mi * (xip - xeval)**3 + (xeval - xi)**3 * Mip) / (6 * hi) + C * (xip - xeval) + D * (xeval - xi)
    return yeval

def eval_cubic_spline(xeval, Neval, xint, Nint, M, C, D):
    """
    Evaluate the cubic spline at multiple points.
    
    Parameters:
    xeval  : Array of points where the spline is to be evaluated
    Neval  : Number of points in xeval
    xint   : Array of interpolation nodes (x values)
    Nint   : Number of interpolation nodes
    M      : Array of second derivatives
    C      : Array of linear coefficients
    D      : Array of constant coefficients
    
    Returns:
    yeval  : Array of evaluated spline values
    """
    yeval = np.zeros(Neval + 1)
    
    for j in range(Nint):
        # Find the indices of xeval within the interval [xint(j), xint(j+1)]
        atmp = xint[j]
        btmp = xint[j+1]
        
        # Find the indices of values of xeval in the interval
        ind = np.where((xeval >= atmp) & (xeval <= btmp))
        xloc = xeval[ind]
        
        # Evaluate the spline at the local points
        yloc = eval_local_spline(xloc, atmp, btmp, M[j], M[j+1], C[j], D[j])
        
        # Copy into yeval
        yeval[ind] = yloc
    
    return yeval


driver()