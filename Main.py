from scipy.io import wavfile
from scipy.fftpack import fft
from matplotlib import pyplot as plt
#import numpy

#Project Created

fs, data = wavfile.read('note.wav')

a = data.T[0]  # this is a two channel soundtrack, I get the first track
b = [(ele/2**8.)*2-1 for ele in a]  # this is 8-bit track, b is now normalized on [-1,1)
otp = fft(b)  # calculate fourier transform (complex numbers list)
d = len(otp)/2  # you only need half of the fft list (real signal symmetry)
plt.plot(abs(otp), 'r')
plt.show()


#def main():
#    print("This is a test")
