import numpy as np

Vcc = 12
B = 100

re = 13e3
ib = 1.66e-6
ic = .166e-3
ie = (B+1)*ib

gm = .007
rpi = 14.3e3
rc = 43000
rl = 43000
rb = 75000
ri = 1000


out = ( 1.0 / ( (1/rc) + (1/rl) ) )
inp = ( (1.0 /( (1/rb) + (1/rpi) )) / ((1 /( (1/rb) + (1/rpi) )) + ri ) )

Av = -gm*out*inp
print("Gain: %f" % Av)
print("Gain (dB): %d" % (20*np.log10(np.abs(Av))))

Rin = (1.0 /( (1/rb) + (1/rpi) ))
print("Rin: %d" % Rin)

# Rout = ( 1.0 / ( (1/ro) + (1/rc) ) )
# print("Rout: %d" % Rout)

vi_max_small_signal = (5e-3) / (inp)
print("Vi,max avoid small signal limit: %f" % vi_max_small_signal)

VE = ie*re
VC = ic*rc
vo_max = Vcc - VE - 0.2 - VC
vi_max_clipping = vo_max / Av
print("Vi,max avoid clipping: %f" % vi_max_clipping)
