# shows a set of notes in a chord via fft.
#
# Author: Omar Barazanji
# Date: 8/27/18

import numpy as np
import matplotlib.pyplot as plt

# every note's mid frequencies (4th octave)
Ab_hz = 415.30
A_hz = 440.00
Bb_hz = 466.16
B_hz = 493.88
C_hz = 261.63
Db_hz = 277.18
D_hz = 293.66
Eb_hz = 311.13
E_hz = 329.63
F_hz = 349.23
Gb_hz = 369.99
G_hz = 392.00

# sample freq
fs = 1.0e4

# Period
Ts = 1.0/fs

# sample size
sample_size = 1024

# 1 - sample_size (n)
n = np.arange(sample_size)

# sample freq domain
f = np.arange(sample_size) * (fs/sample_size)
f_shift = (np.arange(sample_size) - sample_size/2.0) * (fs/sample_size)

# time domain per note
t = n*Ts

# every note's signal
Ab = np.cos(2*np.pi*Ab_hz*t)
A = np.cos(2*np.pi*A_hz*t)
Bb = np.cos(2*np.pi*Bb_hz*t)
B = np.cos(2*np.pi*B_hz*t)
C = np.cos(2*np.pi*C_hz*t)
Db = np.cos(2*np.pi*Db_hz*t)
D = np.cos(2*np.pi*D_hz*t)
Eb = np.cos(2*np.pi*Eb_hz*t)
E = np.cos(2*np.pi*E_hz*t)
F = np.cos(2*np.pi*F_hz*t)
Gb = np.cos(2*np.pi*Gb_hz*t)
G = np.cos(2*np.pi*G_hz*t)

# Plotting
figA = plt.figure(1)

# Notes in chord (add as many as you want!)
s = C + D + E + B # This is C Major

plt.plot(np.linspace(0, 1.0/fs, len(s)), s)

figB = plt.figure(2)
sf = np.fft.fft(s)
sf_mag = np.sqrt(sf.real**2 + sf.imag**2)
plt.plot(f, sf_mag)

figC = plt.figure(3)
sf_shift = np.fft.fftshift(sf)
sf_shift_mag = np.sqrt(sf_shift.real**2 + sf_shift.imag**2)
plt.plot(f_shift, sf_shift_mag)

plt.show()

