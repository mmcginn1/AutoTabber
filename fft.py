import numpy

def fft(data):
    freqData = numpy.fft.fft(data)
    return freqData