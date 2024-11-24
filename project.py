import numpy as np 
import matplotlib.pyplot as plt 
 
# WR28 waveguide dimensions 
a = 0.007112  # Width in meters 
b = 0.003556  # Height in meters 
m = np.array([1, 2, 0, 1]) 
n = np.array([0, 0, 1, 1]) 
 
def TE01(): 
    # Implementation for TE01 mode 
    pass 
 
def TE11(): 
    # Implementation for TE11 mode 
    pass 
 
def TE20(): 
    # Implementation for TE20 mode 
    pass 
 
mur = 1 
epsilonr = 1 
mu = mur * 4 * np.pi * 1e-7  # Permeability of free space 
epsilon = epsilonr * 8.854e-12  # Permittivity of free space 
 
# Frequency range 
f = np.linspace(20e9, 50e9, 1000)  # Frequencies up to 1.2 
times the cutoff frequency 
 
fig, axes = plt.subplots(2, 2, figsize=(10, 8)) 
fig.subplots_adjust(hspace=0.5, wspace=0.3)  # Adjust 
spacing between subplots 
 
for j, ax in enumerate(axes.flat): 
    # Cutoff frequency calculation 
    fc = (1 / (2 * np.pi * np.sqrt(mu * epsilon))) * 
(np.sqrt(((m[j] * np.pi) / a) ** 2 + ((n[j] * np.pi) / b) ** 2))  # 
Cutoff frequency for TE10 
    # Calculate propagation constant for TE10 mode 
    omega = 2 * np.pi * f 
    beta = np.zeros_like(f, dtype=complex) 
    for i in range(1000): 
        beta[i] = omega[i] * np.sqrt(mu * epsilon) * np.sqrt(1 - 
((fc + 1j * 0.01) / (f[i] + 1j * 0.01)) ** 2) 
 
    ax.plot(f, np.real(beta), 'b', f, np.imag(beta), 'r') 
    ax.set_xlabel('Frequency (Hz)') 
    ax.set_ylabel('Propagation constant') 
    ax.legend(['Real', 'Imaginary']) 
    ax.set_title(f'Propagation Constant vs. Frequency (Mode 
{j+1})') 
 
plt.show() 
