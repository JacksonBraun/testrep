#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 11:32:07 2024

@author: jacksonbraun
"""



import numpy as np
import numpy.linalg as la
import math
def driver():
    n = 100
    x = np.linspace(0,np.pi,n)
    # this is a function handle. You can use it to define
    # functions instead of using a subroutine like you
    # have to in a true low level language.
    f = lambda x: x**2 + 4*x + 2*np.exp(x)
    g = lambda x: 6*x**3 + 2*np.sin(x)
    y = f(x)
    w = g(x)
    # evaluate the dot product of y and w
    dp = dotProduct(y,w,n)
    # print the output
    print("the dot product is : ", dp)
    
    
    
    # New vectors, keeping it simple for now.
    
    h = np.array([1, 0, 0]);
    i = np.array([0, 1, 1]);
    n2 = np.size(h);
    print("length of h: ", n2)
    dp2 = dotProduct(h, i, n2);
    
    print("the dot product of orthogonal vectors h and i is ",dp2)
    
    
    
    A = np.ndarray(shape=(2,2))
    A[0][0] = 1
    A[1][0] = 0
    A[0][1] = 0
    A[1][1] = 1
    
    B = np.ndarray(shape=(2,2))
    B[0][0] = 1
    B[1][0] = 1
    B[0][1] = 0
    B[1][1] = 0

    (n,m) = np.shape(A)
    (o,p) = np.shape(B)


    C = matMult(A,B,n,m,o,p)

    
    print("matrix mult of A and B is ", C)
    
    
    #try some other matricies to see if it work
    #maybe also use command window for inputs, could make testing easier
    

    Mat1rows = input("How many rows do you want matrix A to have? ")
    Mat1colomn = input("How many columns do you want matrix A to have? ")
    A = np.ndarray(shape=(Mat1rows,Mat1colomn))
    for i in range(Mat1rows):
        for j in range(Mat1colomn):
            A[i][j] = input("What value for position " ,i, ",", j,"? ")

    
    
    return


def dotProduct(x,y,n):
    # Computes the dot product of the n x 1 vectors x and y
    dp = 0.
    for j in range(n):
        dp = dp + x[j]*y[j]
    return dp


def matMult(x, y, m,n,o,p):
    matrix = np.ndarray(shape=(m,p))
    if n == o:
        for i in range(m):
            j=0
            for j in range(p):
                mat = 0
                k=0
                for k in range(n):
                    mat = mat + x[i][k]*y[k][j]
                    matrix[i][j] = mat    
                
        return matrix
    else:
        print("matrix sizes are not compatable")
        return
driver()