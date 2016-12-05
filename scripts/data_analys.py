import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq
from mpl_toolkits.mplot3d import Axes3D

if __name__ == "__main__":

    dataset = np.load("dataset1.npy")

    din, dout = np.hsplit(dataset, 2)
    y = np.array([d[0][:256:1] for d in din], np.float32)
    """
    dout = np.array([d[0] for d in dout], dtype=np.float32)

    arrlen = len(din)
    for i in xrange(arrlen-1):
        dout[arrlen-2-i] = min(1, dout[arrlen-2-i] +dout[arrlen-1-i]*0.995)
    """

    N = 256
    dt = 0.01/320

    yf = fft(y[10000])/(N/2)
    yf[0] = yf[0]/2

    freq = fftfreq(N, dt)

    plt.figure(1)
    plt.subplot(211)
    plt.plot(freq[1:N/2], np.abs(yf)[1:N/2])
    plt.axis('tight')
    plt.ylabel("amplitude")
    plt.subplot(212)
    plt.plot(freq[1:N/2], np.angle(yf)[1:N/2]*180/np.pi)
    plt.axis('tight')
    plt.ylim(-180, 180)
    plt.xlabel("frequency[Hz]")
    plt.ylabel("phase[deg]")
    
    plt.figure(2)
    plt.subplot(211)
    plt.loglog(freq[1:N/2], np.abs(yf)[1:N/2])
    plt.axis('tight')
    plt.ylabel("amplitude")
    plt.subplot(212)
    plt.semilogx(freq[1:N/2], np.degrees(np.angle(yf)[1:N/2]))
    plt.axis('tight')
    plt.ylim(-180, 180)
    plt.xlabel("frequency[Hz]")
    plt.ylabel("phase[deg]")
    plt.show()
