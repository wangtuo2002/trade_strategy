import numpy as np
import matplotlib.pyplot as plt
import math

X = 10
k = 10

a_values = np.arange(0.1, 1.1, 0.1)
Y_values = np.arange(100, 1100, 100)

Y_fixed = 50
n_a = np.zeros_like(a_values)
m_a = np.zeros_like(a_values)
for i, a in enumerate(a_values):
    n_a[i] = math.ceil((Y_fixed / X + (1 + a) * (k+1)) / a)
    m_a[i] = math.ceil((n_a[i] + Y_fixed / X) / (1 + a))

a_fixed = 0.25
n_Y = np.zeros_like(Y_values)
m_Y = np.zeros_like(Y_values)
for i, Y in enumerate(Y_values):
    n_Y[i] = math.ceil((Y / X + (1 + a_fixed) * k) / a_fixed)
    m_Y[i] = math.ceil((n_Y[i] + Y / X) / (1 + a_fixed))

plt.figure(figsize=(10, 8))

plt.subplot(2, 1, 1)
plt.plot(a_values, n_a, '-o', linewidth=2, label='Buy n')
plt.plot(a_values, m_a, '-s', linewidth=2, label='Sell m')
plt.xlabel('Increase a')
plt.ylabel('Shares')
plt.title(f'Reserve k={k} shares, fixed profit Y={Y_fixed}, n and m vs a')
plt.grid(True)
plt.legend(loc='upper left')

plt.subplot(2, 1, 2)
plt.plot(Y_values, n_Y, '-o', linewidth=2, label='Buy n')
plt.plot(Y_values, m_Y, '-s', linewidth=2, label='Sell m')
plt.xlabel('Profit Y')
plt.ylabel('Shares')
plt.title(f'Reserve k={k} shares, fixed increase a={a_fixed:.2f}, n and m vs Y')
plt.grid(True)
plt.legend(loc='upper left')

plt.tight_layout()
plt.show()
