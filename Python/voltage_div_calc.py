import matplotlib.pyplot as plt
import numpy as np


class Circuit:

    def __init__(self, Vin, R1, R2):
        self.vin = float(Vin)
        self.R1 = float(R1)
        self.R2 = float(R2)
        self.vout = Vin * (self.R2 / (self.R1 + self.R2))


    def __repr__(self):
        return 'Output Voltage = %1.2E' % self.vout


    def plot_relationship(self):
        R2_arr = np.linspace(1.0, self.R2, 50.0)
        vout_arr = []
        curr_arr = []
        for ndx, R2 in enumerate(R2_arr):
            vout_arr.append(Circuit(self.vin, self.R1, R2).vout)
            curr_arr.append(100000*(vout_arr[ndx]/R2))
        x = R2_arr
        y1 = np.array(vout_arr)
        y2 = np.array(curr_arr)

        fig, ax1 = plt.subplots()
        ax1.set_xlabel('R2 (Ohms)')
        ax1.set_ylabel('Vout (V)', color='tab:red')
        ax1.plot(x, y1, color='tab:red')
        ax1.tick_params(axis='y', labelcolor='tab:red')

        ax2 = ax1.twinx()
        ax2.set_ylabel('Iout (uA)', color='tab:blue')
        ax2.plot(x, y2, color='tab:blue')
        ax2.tick_params(axis='y', labelcolor='tab:blue')

        fig.tight_layout()
        plt.title('Voltage Divider with Vin: %1.2e, R1: %1.2e' % (self.vin, self.R1))
        plt.show()
