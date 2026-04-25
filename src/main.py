import wave_generator as waves
import sounddevice as sd
from note_creator import *
import numpy as np

SAMPLE = 44100

a = Note(440, 0.5, 1.0, SAMPLE).build(Wave.sine, "piano", 3)
c = Note(523, 0.5, 1.0, SAMPLE).build(Wave.sine, "piano", 3)
e = Note(659, 0.5, 1.0, SAMPLE).build(Wave.sine, "piano", 3)

piece = np.concatenate([a, c, e])

sd.play(piece, SAMPLE)
sd.wait()