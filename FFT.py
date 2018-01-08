import wave
import scipy.fftpack
from pylab import *

def myFFT(bufferArray, frameRate):
    X = scipy.fftpack.fft(bufferArray)
    freqList = scipy.fftpack.fftfreq(len(bufferArray    ), d=1.0 / frameRate)
    amplitudeSpectrum = [np.sqrt(c.real ** 2 + c.imag ** 2) for c in X]
    phaseSpectrum = [np.arctan2(int(c.imag), int(c.real)) for c in X]
    return freqList, amplitudeSpectrum, phaseSpectrum

def plotFFT(bufferArray, freqList, amplitudeSpectrum, phaseSpectrum, frameRate):
    subplot(311)
    plot(bufferArray)
    axis([0, len(bufferArray), -1.0, 1.0])
    xlabel("time [sample]")
    ylabel("amplitude")

    subplot(312)
    plot(freqList, amplitudeSpectrum, marker= 'o', linestyle='-')
    axis([0, frameRate / 2, 0, 50])
    xlabel("frequency [Hz]")
    ylabel("amplitude spectrum")

    subplot(313)
    plot(freqList, phaseSpectrum, marker= 'o', linestyle='-')
    axis([0, frameRate / 2, -np.pi, np.pi])
    xlabel("frequency [Hz]")
    ylabel("phase spectrum")

    show()

if __name__ == "__main__" :
    wav = wave.open("output.wav", "r")
    frameRate = wav.getframerate()
    buffer = wav.readframes(wav.getnframes())
    bufferArray = frombuffer(buffer, dtype= "int16") / 32768.0
    wav.close()
    freqList, amplitudeSpectrum, phaseSpectrum = myFFT(bufferArray, frameRate)
    plotFFT( bufferArray, freqList, amplitudeSpectrum, phaseSpectrum, frameRate)

