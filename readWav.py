from scipy.io import wavfile


def readWavFile(filename):
    fs, data = wavfile.read(filename)
    return data