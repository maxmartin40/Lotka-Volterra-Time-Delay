import numpy as np
import matplotlib.pyplot as plt
from ddeint import ddeint

# Define constants
alpha = 0.8
beta = 0.2
c = 0.5
d = 0.07
T = 1
# Equilibrium point as starting value
x_0, y_0 = c/d, alpha/beta

# Perturbation
eps = np.array([0.01, 0.0])

def model(Y, t):
    # Current values
    x_t, y_t = Y(t)
    # Delayed values
    x_tau, y_tau = Y(t - T)
    # System of equations
    dxdt = alpha*x_t -beta*x_t*y_tau
    dydt = -c*y_t - d*y_t*x_tau
    return np.array([dxdt, dydt])

def history(t):
    # System for before t=0
    return np.array([x_0, y_0]) + eps

# Evaluation period
t_eval = np.linspace(0, 5, 200)

# Solve the system
sol = ddeint(model, history, t_eval)

# Graph the system
plt.figure(figsize=(8,4))
plt.plot(t_eval, sol[:,0], label="x(t)")
plt.plot(t_eval, sol[:,1], label="y(t)")
plt.xlabel("t")
plt.ylabel("x(t), y(t)")
plt.title("Perturbed system near equilibrium")
plt.legend()
plt.grid(True)
plt.show()
