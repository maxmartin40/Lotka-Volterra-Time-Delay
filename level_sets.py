import numpy as np
import matplotlib.pyplot as plt
import sympy as smp

alpha = 0.8
beta = 0.2
c = 0.5
d = 0.07
T = 1
x_0 = c/d
y_0 = alpha/beta

def real(a,b):
    return a*2 - b**2 - a*(alpha-beta*y_0) + a*(c+d*x_0) - (c+d*x_0)*(alpha-beta*y_0) - beta*d*x_0*y_0*np.exp(-2*T*a)*np.cos(2*T*b)

def imaginary(a,b):
    return a*b + b*(alpha-beta*y_0) + b*(c+d*x_0) + beta*d*x_0*y_0*np.exp(-2*T*a)*np.sin(2*T*b)

a = np.linspace(-2,2,100)
b = np.linspace(-2,2,100)
A, B = np.meshgrid(a, b)
REAL = real(A,B)
IMAGINARY = imaginary(A,B)

plt.contour(A, B, REAL, levels=[0], colors='b',)
plt.contour(A, B, IMAGINARY, levels=[0], colors='r',)

plt.axhline(0, color='gray', linestyle='--')
plt.axvline(0, color='gray', linestyle='--')
plt.xlabel("a")
plt.ylabel("b")
plt.title("Level sets")
plt.grid(True)
plt.show()
