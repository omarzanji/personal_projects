'''
A beautiful logistical map visualizaion of the Bifurcation "fractal".

author: Omar Barazanji
date: 3/12/21

Python 3.7x

sources:
https://matplotlib.org/3.3.4/gallery/animation/simple_anim.html
https://isquared.digital/visualizations/2020-11-18-bufurcation-diagram/
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import matplotlib as mpl
mpl.rcParams['agg.path.chunksize'] = 10000

    

class Simulation:
    
    def __init__(self):
        self.r = np.random.uniform(0.0, 4.0, 1000000)
        self.x = np.random.uniform(0.0,1.0, 1000000)
        self.fig, self.ax = plt.subplots()


    def animate(self, i):
        for _ in range(i + 1):
            self.x = self.log_map(self.r, self.x)
        self.line, = self.ax.plot(self.r, self.x, ',b', alpha=0.5)
        self.ax.set_title(f"Bifurcation Diagram for $x^{{(r)}}_{{n + 1}} = rx^{{(r)}}_{{n}}(1 - x^{{(r)}}_{{n}})$ for $n=${i + 1}")
        self.ax.set_xlabel('r')
        self.ax.set_ylabel('$x^{(r)}_{n}$')
        return self.line,

    def log_map(self, r, x):
        return r*x*(1-x)

    def plot_ani(self):
        ani = animation.FuncAnimation(
            self.fig, self.animate, frames=50, interval=225, blit=True
        )



if __name__ == "__main__":
    sim = Simulation()
    sim.plot_ani()
    plt.title("Yes")
    plt.show()
