import wave_generator as waves
import sounddevice as sd

SAMPLE = 44100
wave = waves.Wave(440,0.5,5, SAMPLE)
w= wave.sawtooth()
l= wave.sine()
d = wave.square()

sd.play(w,SAMPLE)
sd.wait()
# sd.play(l,SAMPLE)
# sd.wait()
# sd.play(d,SAMPLE)
# sd.wait()
