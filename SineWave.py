import struct
import wave
from pylab import *

def createSineWave(A, f0, fs, length):
    data =[]
    for n in arange(length * fs):
        s = A * np.sin(2 * np.pi * f0 * n / fs)
        if s > 1.0: 
            s = 1.0
        if s < -1.0:
            s = -1.0
        data.append(s)
    data = [int(x * 32767.0) for x in data]
    data = struct.pack("h" * len(data), * data)
    return data

def play (data, fs, bit):
    import pyaudio
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
            channels=1,
            rate=int(fs),
            output=True)
    chunk = 1024
    sp = 0
    buffer = data[sp:sp+chunk]
    while buffer != '':
        stream.write(buffer)
        sp = sp + chunk
        buffer = data[sp:sp+chunk]
    stream.close()
    p.terminate()

# freqList = [262, 294, 330, 349, 392, 440, 494, 523]
# for f in freqList:
#     data = createSineWave(1.0, f, 8000.0, 1.0)
#     play(data, 8000, 16)

if __name__ == "__main__" :
    allData = ""
    freqList = [262, 294, 330, 349, 392, 440, 494, 523] 
    for f in freqList:
        data = createSineWave(1.0, f, 8000.0, 1.0)
        play(data, 8000, 16)
        allData += data
    wf = wave.open("output.wav", "r")
    wf.setnchannels(1)
    wf.setsampwidth(16 / 8)
    wf.setframerate(8000)
    wf.writeframes(allData)
    wf.close()
