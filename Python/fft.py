# This program will demonstrate the basics of using an FFT in Python.
#
# Author: Omar Barazanji
# Python Version: 2.7

import numpy as np
import matplotlib.pyplot as plt


def generate_signal():
    # Time axis
    t = np.linspace(0, 2*np.pi, 1000, endpoint=True)

    # Frequency in Hz
    freq = 3.0

    # Amplitude in units
    amplitude = 100.0

    # Signal (basically the graph of "100sin(2*pi*3*t)"
    s = amplitude * np.sin(2*np.pi*freq*t)

    plt.plot(t, s)
    plt.show()

    return s


def plot_fft(s):
    # FFT on function (or signal) s
    sf = np.fft.fft(s)

    plt.plot(sf)
    plt.show()

    return sf


def plot_fft_real(fft_signal):
    # This will be where the graph stops - eliminating the mirrored effect.
    n = int(len(fft_signal)/2 + 1)

    # This will graph with absolute value - eliminating the imaginary numbers and displaying the "real" values.
    sf_real = np.abs(fft_signal[:n])

    plt.plot(sf_real)
    plt.show()

    return sf_real


if __name__ == '__main__':
    # This will graph the sine function defined in the function generate_signal().
    signal = generate_signal()

    # This will graph the FFT of the sine function. Notice that the graph mirrors... We have to fix this.
    signal_fft = plot_fft(signal)

    # This is the real FFT with imaginary and mirrored values eliminated
    real_fft = plot_fft_real(signal_fft)
