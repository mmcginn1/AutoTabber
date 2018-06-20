

def main(freq):

    # Consider putting this in a different function that doesn't initialize the dict every time you call it. It's fine for now
    # but for optimization, just initialize these values at start up
    BaseNotes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    BaseFreqs = [16.35, 17.32, 18.35, 19.45, 20.60, 21.83, 23.12, 24.50, 25.96, 27.50, 29.14, 30.87,]

    Freqs = []
    Notes = []
    for x in range(0,9):
        for y in BaseFreqs:
            Freqs.append(y * 2**x)

    for x in range(0,9):
        for y in BaseNotes:
            Notes.append(y + str(x))


    Ref = dict(zip(Freqs, Notes))
    note = ""
    threshold = 2.5/100
    for x in Freqs:
            if x * (1-threshold) < freq < x * (1+threshold):
                note = Ref.get(x)

    print(note)
    return note



main(100)
