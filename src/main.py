import numpy as np
import sounddevice as sd
from note_creator import Note

SAMPLE = 44100

# Frequencies for each note
notes = {
    "E4": 329.63, "Eb4": 311.13, "D4": 293.66,
    "B3": 246.94, "G3": 196.00, "C4": 261.63,
    "A3": 220.00, "F3": 174.61, "E3": 164.81,
    "C3": 130.81, "F4": 349.23,
}

def make_note(freq, duration, instrument="piano"):
    return Note(freq, 0.5, duration, SAMPLE).build(instrument)

def rest(duration):
    return np.zeros(int(SAMPLE * duration), dtype=np.float32)

# Für Elise note sequence transcribed with claude.ai assistance
sequence = [
    # Theme A (first time)
    ("E4", 0.25), ("Eb4", 0.25), ("E4", 0.25), ("Eb4", 0.25),
    ("E4", 0.25), ("B3", 0.25), ("D4", 0.25), ("C4", 0.25),
    ("A3", 0.50), (None, 0.25),
    ("C3", 0.25), ("E3", 0.25), ("A3", 0.25),
    ("B3", 0.50), (None, 0.25),
    ("E3", 0.25), ("G3", 0.25), ("B3", 0.25),
    ("C4", 0.50), (None, 0.25),
    ("E3", 0.25), ("E4", 0.25), ("Eb4", 0.25),
    ("E4", 0.25), ("Eb4", 0.25), ("E4", 0.25),
    ("B3", 0.25), ("D4", 0.25), ("C4", 0.25),
    ("A3", 0.50), (None, 0.25),

    # Bridge section
    ("C3", 0.25), ("E3", 0.25), ("A3", 0.25),
    ("B3", 0.50), (None, 0.25),
    ("E3", 0.25), ("G3", 0.25), ("B3", 0.25),
    ("C4", 0.50), (None, 0.25),

    # Theme B
    ("B3", 0.25), ("C4", 0.25), ("D4", 0.25),
    ("E4", 0.50), (None, 0.25),
    ("G3", 0.25), ("F4", 0.25), ("E4", 0.25),
    ("D4", 0.50), (None, 0.25),
    ("F3", 0.25), ("E4", 0.25), ("D4", 0.25),
    ("C4", 0.50), (None, 0.25),
    ("E3", 0.25), ("D4", 0.25), ("C4", 0.25),
    ("B3", 0.50), (None, 0.25),

    # Theme A repeat
    ("E4", 0.25), ("Eb4", 0.25), ("E4", 0.25), ("Eb4", 0.25),
    ("E4", 0.25), ("B3", 0.25), ("D4", 0.25), ("C4", 0.25),
    ("A3", 0.50), (None, 0.25),
    ("C3", 0.25), ("E3", 0.25), ("A3", 0.25),
    ("B3", 0.50), (None, 0.25),
    ("E3", 0.25), ("G3", 0.25), ("B3", 0.25),
    ("C4", 0.50), (None, 0.25),
    ("E3", 0.25), ("E4", 0.25), ("Eb4", 0.25),
    ("E4", 0.25), ("Eb4", 0.25), ("E4", 0.25),
    ("B3", 0.25), ("D4", 0.25), ("C4", 0.25),
    ("A3", 1.00),
]

def main():
    piece = []
    for name, dur in sequence:
        if name is None:
            piece.append(rest(dur))
        else:
            piece.append(make_note(notes[name], dur, "piano"))

    output = np.concatenate(piece)
    sd.play(output, SAMPLE)
    sd.wait()

if __name__ == "__main__":
    main()