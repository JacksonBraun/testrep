import numpy as np

# Newton's method
# (X,Xstar,info,it) = newtonND(F,J_F,X0, tol, Nmax)
# print('The approximate root is', Xstar)
# print('The error message reads:', '%d' % info)
# print('Number of iterations:', '%d' % it)
def newtonND(F,J_F,X0, tol, Nmax):
  """
  Newton N-Dimensional iteration.
  
  Inputs:
    F,J_F - Vector containing system of non-linear equations and Jacobian
    X0   - initial guess for root
    tol  - iteration stops when X_n,X_{n+1} are within tol
    Nmax - max number of iterations
  Returns:
    X     - an array of the iterates
    Xstar - the last iterate
    info  - success message
          - 0 if we met tol
          - 1 if we hit Nmax iterations (fail)
    it    - number of iterations
     
  """
  X = []
  X.append(X0)
  for it in range(Nmax):
      Y0 = np.linalg.solve(J_F(X0), -F(X0))
      X1 = X0 + Y0
      X.append(X1)
      if (np.linalg.norm(Y0,2) < tol):
          Xstar = X1
          info = 0
          return [np.array(X),Xstar,info,it+1]
      X0 = X1
  Xstar = X1
  info = 1
  return [np.array(X),Xstar,info,it+1]

def LazyNewton(F, J, x0, tol, Nmax):
  ''' Lazy Newton = use only the inverse of the Jacobian for initial guess'''
  ''' inputs: x0 = initial guess, tol = tolerance, Nmax = max its'''
  ''' Outputs: xstar= approx root, ier = error message, its = num its'''
  X = []
  X.append(x0)
  J0 = J(x0)
  J0inv = np.linalg.inv(J0)
  for its in range(Nmax):
    x1 = x0 - J0inv @ F(x0)
    X.append(x1)
    if (np.linalg.norm(x1-x0) < tol):
      xstar = x1
      ier =0
      return[np.array(X),xstar, ier,its]
    x0 = x1
  xstar = x1
  ier = 1
  return[np.array(X),xstar,ier,its]

def Broyden(F, A0, x0, tol, Nmax):
  '''tol = desired accuracy
  Nmax = max number of iterations'''
  '''Sherman-Morrison
  (A+xy^T)^{-1} = A^{-1}-1/p*(A^{-1}xy^TA^{-1})
  where p = 1+y^TA^{-1}Ax'''
  '''In Newton
  x_k+1 = xk -(G(x_k))^{-1}*F(x_k)'''
  '''In Broyden
  x = [F(xk)-F(xk-1)-\hat{G}_k-1(xk-xk-1)
  y = x_k-x_k-1/||x_k-x_k-1||^2'''
  ''' implemented as in equation (10.16) on page 650 of text'''
  '''initialize with 1 newton step'''
  v = F(x0)
  A = np.linalg.inv(A0)
  s = -A.dot(v)
  xk = x0+s
  X = []
  X.append(x0)
  for its in range(Nmax):
    '''(save v from previous step)'''
    w = v
    ''' create new v'''
    v = F(xk)
    '''y_k = F(xk)-F(xk-1)'''
    y = v-w
    '''-A_{k-1}^{-1}y_k'''
    z = -A.dot(y)
    ''' p = s_k^tA_{k-1}^{-1}y_k'''
    p = -np.dot(s,z)
    u = np.dot(s,A)
    ''' A = A_k^{-1} via Morrison formula'''
    tmp = s+z
    tmp2 = np.outer(tmp,u)
    A = A+1./p*tmp2
    ''' -A_k^{-1}F(x_k)'''
    s = -A.dot(v)
    xk = xk+s
    X.append(xk)
    if (np.linalg.norm(s) < tol):
      alpha = xk
      ier = 0
      return[np.array(X),alpha,ier,its]
  alpha = xk
  ier = 1
  return[np.array(X),alpha,ier,its]


###############################
### steepest descent code

def SteepestDescent(F, J, x,tol,Nmax):
    
    X = []
    X.append(x)
    for its in range(Nmax):
        g1 = evalg(x, F)
        z = eval_gradg(x, F, J)
        z0 = np.linalg.norm(z)

        if z0 == 0:
            print("zero gradient")
        z = z/z0
        alpha1 = 0
        alpha3 = 1
        dif_vec = x - alpha3*z
        g3 = evalg(dif_vec, F)

        while g3>=g1:
            alpha3 = alpha3/2
            dif_vec = x - alpha3*z
            g3 = evalg(dif_vec, F)
            
        if alpha3<tol:
            print("no likely improvement")
            ier = 0
            return [np.array(X),x,ier,its+1]
        
        alpha2 = alpha3/2
        dif_vec = x - alpha2*z
        g2 = evalg(dif_vec, F)

        h1 = (g2 - g1)/alpha2
        h2 = (g3-g2)/(alpha3-alpha2)
        h3 = (h2-h1)/alpha3

        alpha0 = 0.5*(alpha2 - h1/h3)
        dif_vec = x - alpha0*z
        g0 = evalg(dif_vec, F)

        if g0<=g3:
            alpha = alpha0
            gval = g0

        else:
            alpha = alpha3
            gval =g3

        x = x - alpha*z
        X.append(x)

        if abs(gval - g1)<tol:
            ier = 0
            return [np.array(X),x,ier,its+1]

    print('max iterations exceeded')    
    ier = 1        
    return [np.array(X),x,ier,its+1]

def evalg(x,F):

  F = F(x)
  g = F[0]**2 + F[1]**2 + F[2]**2
  return g

def eval_gradg(x,F,J):
    F = F(x)
    J = J(x)
    
    gradg = np.transpose(J).dot(F)
    return gradg