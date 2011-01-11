# Wow! What a nice little bit about fft in Python
# http://macdevcenter.com/pub/a/python/2001/01/31/numerically.html

import numpy as np
import numpy.fft
import matplotlib
import matplotlib.pyplot as plt

x = np.arange(256.0)
sig = np.sin(2*np.pi*(1250.0/10000.0)*x) + np.sin(2*np.pi*(625.0/10000.0)*x)

plt.plot(x[0:129], 10*np.log10(abs(np.fft.rfft(sig))))
plt.show()