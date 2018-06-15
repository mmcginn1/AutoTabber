from scipy.io import wavfile
import numpy

#Project Created

fs, data = wavfile.read('note.wav')
otp = numpy.fft.fft(data)
print(otp)

#def main():
#    print("This is a test")
