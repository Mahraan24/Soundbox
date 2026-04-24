import numpy as np

class Wave:
    """
    Oscillator class which is only responsible for generating raw periodic waveforms.

    This class intentionally does not handle musical concepts such as notes,
    envelopes, or mixing but only handles the foundational waveform, which are
    either derived from sine (harmonic) or phase (geometric) definitions.
    """
    def __init__(self, freq: float, amp: float, duration: float, sample_rate: int=44100):
        self.freq = freq
        self.amp = amp
        self.sample_rate = sample_rate
        self.duration = duration

    def make_t(self) -> np.ndarray:
        num_samples = int(self.sample_rate * self.duration)
        return np.linspace(0, self.duration, num_samples, False)

    def sine(self) -> np.ndarray:
        t = self.make_t()
        wave = (self.amp * np.sin(2 * np.pi * self.freq * t))
        return wave.astype(np.float32)

    def square(self) -> np.ndarray:
        base = self.sine()
        wave = (self.amp * np.sign(base))
        return wave.astype(np.float32)

    def sawtooth(self) -> np.ndarray:
        t = self.make_t()
        frac = (self.freq * t) % 1
        base = ((2 * frac) - 1)
        wave = self.amp * base
        return wave.astype(np.float32)

    def triangle(self) -> np.ndarray:
        t = self.make_t()
        frac = (self.freq * t) % 1
        saw = ((2 * frac) - 1)
        base = 2 * np.abs(saw) - 1
        wave = self.amp * base
        return wave.astype(np.float32)