import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x = np.array([1, 2, 4, 7, 10])
y = np.array([2, 7 , 6, 1, 3])

x_1 = np.array([0.36, -4.36, 15.56, -9.56])
x_2 = np.array([0.36, -4.36, 15.56, -9.56])
x_3 = np.array([0.046296, -0.5833, 0.445, 10.593])
x_4 = np.array([0.046296, -0.5833, 0.445, 10.593])
x_t = np.array([x_1, x_2, x_3, x_4])

for i in range(len(x)-1):
    xi = np.linspace(x[i], x[i+1], 30)
    yi = np.array([])
    for j in xi:
        y_temp = x_t[i][0]*(j**3) + x_t[i][1]*(j**2) + x_t[i][2]*(j) + x_t[i][3]
        yi = np.append(yi, y_temp)
    plt.scatter(xi, yi)

plt.plot(x, y, 'ro')
plt.show()