from readWav import readWavFile
from fft import fft

#driver function
def main():
    filename = input("Input filename: ")
    data = readWavFile(filename)
    freqData = fft(data)
    for x in range(0, 100):
        print(freqData[x])

main()