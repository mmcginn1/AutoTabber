from scipy.io import wavfile
from fft import fft
from matplotlib import pyplot as plt
#from scipy.signal import argrelmax
import numpy as np
from NoteIdentifier import findnote
import threading

#Project Created
fs, data = wavfile.read('note.wav')
lst = list()
bufferlength = 2**12
for i in range(int(len(data)/bufferlength)):
    lst.append(data[bufferlength*i:bufferlength*(i+1)])

freqs = list()
e = list()

for x in lst:
    a = x.T[0]  # this is a two channel soundtrack, I get the first track
    b = [(ele/2**8.)*2-1 for ele in a]  # this is 8-bit track, b is now normalized on [-1,1)
    otp = fft(b)  # calculate fourier transform (complex numbers list)
    d = int(len(otp)/2)  # you only need half of the fft list (real signal symmetry)
    e.append(abs(otp[:d]))
for y in e:
        freqs.append(np.fft.fftfreq(len(y)))
for i in range(0,len(freqs)):
    freqlookup = dict(zip(e[i], freqs[i]))

    #plt.plot(e, 'r')
    #plt.show()
    max = e[i].argmax()
    print(freqlookup.get(e[i].max())*fs)
    print(findnote(freqlookup.get(e[i].max())*fs))


#     #def main():
#     #    print("This is a test")
