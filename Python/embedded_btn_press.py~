# Cleaner plot of a button press oscope screen capture
#
# Author: Omar Barazanji
# Date: 3/18/20

import numpy as np
import matplotlib.pyplot as plt

x_delta = 48.5 # ms
x_end = 242.5 + x_delta # ms
x = np.arange(-242.5, x_end, x_delta) # ms
x_fall = -x_delta/2  # ms
x = np.insert(x,5,x_fall)

y =  np.arange(1.0,7.0,1.0)
y.fill(2.5)  # V
zero_pad = np.zeros(6)
y = np.append(y, zero_pad)  # V

y_axes = np.arange(-2.5,2.5+0.5,0.5)

figA = plt.figure(1)
bottom, top = plt.ylim()  # return the current ylim

plt.xlabel('time (ms)')
plt.ylabel('Volta (V)')
plt.title('Voltage Over Time')
plt.plot(x, y, linewidth=3)
plt.grid()
plt.show()
