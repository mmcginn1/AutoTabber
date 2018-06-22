from scipy.io import wavfile
from fft import fft
from matplotlib import pyplot as plt
import numpy
#from scipy.signal import argrelmax
import numpy as np

#Project Created
fs, data = wavfile.read('note.wav')

a = data.T[0]  # this is a two channel soundtrack, I get the first track
b = [(ele/2**8.)*2-1 for ele in a]  # this is 8-bit track, b is now normalized on [-1,1)
otp = fft(b)  # calculate fourier transform (complex numbers list)
d = int(len(otp)/2)  # you only need half of the fft list (real signal symmetry)
e = abs(otp[:d])
freqs = np.fft.fftfreq(len(e))

freqlookup = dict(zip(e,freqs))

print(len(freqs))
print(len(e))

#def main():
#    print("This is a test")
