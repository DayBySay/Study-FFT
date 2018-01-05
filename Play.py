#coding: utf-8
import wave
import pyaudio

def printWaveInfo(wf):
    print "チャネル数:", wf.getnchannels()

if __name__ ==  '__main__':
    wf = wave.open("output.wav", "r")
    printWaveInfo(wf)
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True)
    chunk = 1024
    data = wf.readframes(chunk)
    while data != '':
        stream.write(data)
        data = wf.readframes(chunk)
    stream.close()
    p.terminate()
