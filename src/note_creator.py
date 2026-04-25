import numpy as np
from filter import Filter
from instrument_store import InstrumentStore
from wave_generator import Wave

class Note:
    def __init__(
        self,
        freq: float,
        amp: float,
        duration: float,
        sample_rate: int=44100,
    ):
        self.freq = freq
        self.amp = amp
        self.sample_rate = sample_rate
        self.duration = duration

    def build(self, instrument="piano") -> np.ndarray:
        preset = InstrumentStore.get(instrument)

        samples = np.zeros(int(self.sample_rate * self.duration))
        for n in range(1, preset.harmonic + 1):
            wave = Wave(self.freq * n, self.amp, self.duration, self.sample_rate)
            samples += preset.wave_type(wave) * (1/n)

        max_val = np.max(np.abs(samples))
        if max_val > 0:
            samples = samples / max_val

        samples = Filter(preset.filter_a).low_pass(samples)

        env = preset.to_adsr(self.duration, self.sample_rate).envelope()
        samples = samples[:len(env)] * env

        return samples.astype(np.float32)




