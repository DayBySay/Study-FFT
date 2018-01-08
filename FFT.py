import wave
import scipy.fftpack
from pylab import *

if __name__ == "__main__" :
    wf = wave.open("output.wav", "r" )
    fs = wf.getframerate()
    x = wf.readframes(wf.getnframes())
    x = frombuffer(x, dtype= "int16") / 32768.0
    wf.close()

    start = 0
    N = len(x) - start

    X = scipy.fftpack.fft(x[start:start+N])
    freqList = scipy.fftpack.fftfreq(N, d=1.0/ fs)

    amplitudeSpectrum = [np.sqrt(c.real ** 2 + c.imag ** 2) for c in X]
    phaseSpectrum = [np.arctan2(int(c.imag), int(c.real)) for c in X]

    subplot(311)
    plot(range(start, start+N), x[start:start+N])
    axis([start, start+N, -1.0, 1.0])
    xlabel("time [sample]")
    ylabel("amplitude")

    subplot(312)
    plot(freqList, amplitudeSpectrum, marker= 'o', linestyle='-')
    axis([0, fs/2, 0, 50])
    xlabel("frequency [Hz]")
    ylabel("amplitude spectrum")

    subplot(313)
    plot(freqList, phaseSpectrum, marker= 'o', linestyle='-')
    axis([0, fs/2, -np.pi, np.pi])
    xlabel("frequency [Hz]")
    ylabel("phase spectrum")

    show()