import wave_generator as waves
import sounddevice as sd
from note_creator import *
import numpy as np

SAMPLE = 44100
wave = waves.Wave(440,0.5,5, SAMPLE)

l= wave.sine()


note = Note(440,0.5,5, SAMPLE)
d = note.build(Wave.sine,3)

sd.play(l,SAMPLE)
sd.wait()

sd.play(d,SAMPLE)
sd.wait()
