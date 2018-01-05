#coding:utf-8
import wave
from numpy import *
from pylab import *
import Play

wf = wave.open("output.wav", 'r')
Play.printWaveInfo(wf)

buffer = wf.readframes(wf.getnframes())
print len(buffer)

data = frombuffer(buffer, dtype="int16")

plot(data)
show()