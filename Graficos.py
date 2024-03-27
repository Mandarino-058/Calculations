import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def input_vector(prompt):
    values = input(prompt).split(',')
    return [float(value.strip()) for value in values]

u = input_vector("Ingrese los valores del vector u separados por comas (ejemplo: 0,0,0): ")
v = input_vector("Ingrese los valores del vector v separados por comas (ejemplo: 0,0,0): ")

u = np.array([0, 0, 0] + u)
v = np.array([0, 0, 0] + v)
u_plus_v = u + v

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.quiver(*u, color='r', label='u')
ax.quiver(*v, color='g', label='v')
ax.quiver(*u_plus_v, color='b', label='u + v')

ax.set_xlim([0, max(u_plus_v[3], u[3], v[3])])
ax.set_ylim([0, max(u_plus_v[4], u[4], v[4])])
ax.set_zlim([0, max(u_plus_v[5], u[5], v[5])])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
# comment
plt.show()

#importar todas las librerias antes de usarlo 