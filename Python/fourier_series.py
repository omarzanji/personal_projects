import numpy as np
import matplotlib.pyplot as plt

# Settings
A = 10.0  # Amplitude
N = 100
t = np.linspace(0,10,N)  # t (s)
wo = 1000.0  # freq 1kHz

# function
# x = (A/2.0) - (A/(np.pi*k)) * (np.sin(k*wo*t))


fig1 = plt.figure(1)
k_ = []
for k in range(1,N+1):
    k_.append(k)

print(k_)
x = (A/2.0) - (A/(np.pi*k)) * (np.sin(k*wo*t))
plt.plot(20*np.log10(x))
plt.xlabel('Time (t) seconds')
plt.ylabel('Amplitude (A)')
plt.show()
