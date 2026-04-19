import numpy as np

class Wave:
    """
    Oscillator class which is only responsible for generating raw periodic waveforms.

    This class intentionally does not handle musical concepts such as notes,
    envelopes, or mixing but only handles the foundational waveform, which are
    either derived from sine (harmonic) or phase (geometric) definitions.
    """
    def __init__(self, freq, amp, duration, sample_rate=44100):
        self.freq = freq
        self.amp = amp
        self.sample_rate = sample_rate
        self.duration = duration

    def make_t(self):
        num_samples = int(self.sample_rate * self.duration)
        return np.linspace(0, self.duration, num_samples, False)

    def sine(self):
        t = self.make_t()
        wave = (self.amp * np.sin(2 * np.pi * self.freq * t))
        return wave.astype(np.float32)

    def square(self):
        base = self.sine()
        wave = (self.amp * np.sign(base))
        return wave.astype(np.float32)

    def sawtooth(self):
        t = self.make_t()
        frac = (self.freq * t) % 1
        base = ((2 * frac) - 1)
        wave = self.amp * base
        return wave.astype(np.float32)

    def triangle(self):
        t = self.make_t()
        frac = (self.freq * t) % 1
        saw = ((2 * frac) - 1)
        base = 2 * np.abs(saw) - 1
        wave = self.amp * base
        return wave.astype(np.float32)