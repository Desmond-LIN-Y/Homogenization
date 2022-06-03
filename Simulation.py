import numpy as np
from copy import deepcopy
from matplotlib import pyplot as plt


a = np.array([[[1,2],[2,1]],[[2,1],[1,2]]])
u = np.zeros(shape=(101,101))
v = np.zeros(shape=(101,101))
u[50,50] = 10
for n in range(1000):
    for i in range(1,100):
        for j in range(1,100):
            p=a[(i + j) % 2]
            v[i,j] = (p[0, 0] * (u[i+1, j] + u[i-1,j]) +
                     (p[0, 1] + p[1, 0]) / 4 * (u[i+1, j+1] + u[i-1,j-1] - u[i+1,j-1] - u[i-1,j+1]) +
                      p[1, 1] * (u[i,j+1] + u[i,j-1])) / (2*(p[0,0]+p[1,1]))
    u = deepcopy(v)
    u[50,50] = 10

#Plots
x_values = np.linspace(0,10,100)
y_values = np.linspace(0,10,100)
x, y = np.meshgrid(x_values, y_values)
plt.imshow(u)

np.random.seed(1)
a = np.array([[[1,2],[2,1]],[[2,1],[1,2]]])
u = np.zeros(shape=(101,101))
v = np.zeros(shape=(101,101))
u[50,50] = 10
for n in range(1000):
    for i in range(1,100):
        for j in range(1,100):
            k = np.random.randint(0,2)
            v[i,j] = (a[k][0, 0] * (u[i+1, j] + u[i-1,j]) +
                     (a[k][0, 1] + a[k][1, 0]) / 4 * (u[i+1, j+1] + u[i-1,j-1] -u[i+1,j-1]-u[i-1,j+1]) +
                      a[k][1, 1] * (u[i,j+1] + u[i,j-1])) / (2*(a[k][0,0]+a[k][1,1]))
    u = deepcopy(v)
    u[50,50] = 10

#Plots
x_values = np.linspace(0,10,100)
y_values = np.linspace(0,10,100)
x, y = np.meshgrid(x_values, y_values)
plt.imshow(u)
