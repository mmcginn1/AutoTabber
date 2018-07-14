from scipy.io import wavfile
from fft import fft
#from matplotlib import pyplot as plt
from scipy.signal import argrelmax
import numpy as np
from NoteIdentifier import findnote
from math import log2

#Project Created
fs, data = wavfile.read('Note3.wav')                                    #reading file

print(data)
lst = list()
bufferlength = 2**14                                                    #buffer to find freq changes



for i in range(int(len(data)/bufferlength)):
    lst.append(data[bufferlength*i:bufferlength*(i+1)])

freqs = list()
e = list()

for x in lst:
    a = x.T[0]                                          # this is a two channel soundtrack, I get the first track
    b = [(ele/2**8.)*2-1 for ele in a]                  # this is 8-bit track, b is now normalized on [-1,1)
    for i in range(int((2 ** (log2(len(data) + 1)) - len(data)) / 2)):
        b.append(0)  # zero padding at start and end of data
        b.insert(0, 0)
    otp = fft(b)                                        # calculate fourier transform (complex numbers list)
    d = int(len(otp)/2)                                 # you only need half of the fft list (real signal symmetry)
    e.append(abs(otp[:d]))
for y in e:
        freqs.append(np.fft.fftfreq(len(y)))
for i in range(0,len(freqs)):
    freqlookup = dict(zip(e[i], freqs[i]))

    #plt.plot(e, 'r')
    #plt.show()
    mx = argrelmax(e[i])
    print(freqlookup.get(e[i].mx())*fs)
    print(findnote(freqlookup.get(e[i].mx())*fs))

#def main():
#print("This is a test")