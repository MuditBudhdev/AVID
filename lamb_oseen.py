# what is a lamb oseen?
# great question
# basically a mathematical equation that can be used to generate velocity fields that model a vortex
# this will effectively provide me with training data 


import numpy as np
import matplotlib.pyplot as plt

def lamb_oseen_vortex(grid_size=128, gamma=5.0, r_core=10.0):
    x = np.linspace(-64, 64, grid_size)
    y = np.linspace(-64, 64, grid_size)
    X, Y = np.meshgrid(x, y)
    r = np.sqrt(X**2 + Y**2) + 1e-8  

    v_theta = (gamma / (2 * np.pi * r)) * (1 - np.exp(-(r**2 / r_core**2)))
    vx = -v_theta * (Y / r)
    vy =  v_theta * (X / r)

    return vx, vy

vx, vy = lamb_oseen_vortex()
speed = np.sqrt(vx**2 + vy**2)

plt.imshow(speed, cmap='plasma')
plt.colorbar(label='Velocity magnitude')
plt.title('Lamb–Oseen vortex')
plt.show()