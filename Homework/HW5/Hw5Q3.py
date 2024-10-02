import numpy as np

f = lambda x,y,z: x**2 + 4*y**2 + 4*z**2 - 16
fx = lambda x: 2*x
fy = lambda y: 8*y
fz = lambda z: 8*z

x0 = 1
y0 = 1
z0 = 1
tol =  1e-6

x = {}
y = {}
z = {}

x[0] = x0
y[0] = y0
z[0] = z0

i =1


while np.abs(f(x0,y0,z0)) > tol:
    x1 = x0 - (f(x0,y0,z0)/(fx(x0)**2 + fy(y0)**2 + fz(z0)**2))*fx(x0)
    y1 = y0 - (f(x0,y0,z0)/(fx(x0)**2 + fy(y0)**2 + fz(z0)**2))*fy(y0)
    z1 = z0 - (f(x0,y0,z0)/(fx(x0)**2 + fy(y0)**2 + fz(z0)**2))*fz(z0)

    x0 = x1
    y0 = y1
    z0 = z1

    x[i] = x1
    y[i] = y1
    z[i] = z1
    i = i + 1

print(x)
print(y)
print(z)

print(f(x0,y0,z0))