

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
    for x in range(0, len(Freqs)):
        if x < len(Freqs)-1:

            low = abs(Freqs[x] - FQ)
            high = abs(Freqs[x+1] - FQ)
            if low == min(low,high):
                note = Ref.get(Freqs[x])
            elif high == min(low,high):
                note = Ref.get(Freqs[x+1])

    return note



main(6843)
