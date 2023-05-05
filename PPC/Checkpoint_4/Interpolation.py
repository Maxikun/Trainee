import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp



x = np.array([1, 2, 4, 7, 10])
y = np.array([2, 7 , 8, 1, 3])

# x = np.array([1, 2, 3, 4])
# y = np.array([2, 7 , 6, 1])

f = sp.interpolate.CubicSpline(x, y)
x_new = np.linspace(x[0], x[-1], 100)
y_new = f(x_new)

f_dash = f.derivative()
y_derivative = f_dash(x_new)

f_dash_dash = f_dash.derivative()
y2_derivative = f_dash_dash(x_new)

plt.subplot(1, 2, 1)
plt.plot(x, y, 'ro')
plt.plot(x_new, y_new, 'black')
plt.plot(x_new, y_derivative, 'blue')
plt.plot(x_new, y2_derivative, 'red')
plt.legend(['Data', 'Cubic Spline', 'First Derivative', 'Second Derivative'])



radius = np.array([])
for x in x_new:
    r = (1 + (f_dash(x))**2)**(3/2) / abs(f_dash_dash(x))
    radius = np.append(radius, r)

plt.subplot(1, 2, 2)
plt.plot(x_new, radius, 'green')
plt.legend(['Radius of Curvature'])
plt.show()