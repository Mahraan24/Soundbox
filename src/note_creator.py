import numpy as np
from ADSR import ADSR
from envelope_store import EnvelopeStore, ADSRParams
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

    def build(self, wave_type=Wave.sine, instrument="piano", harmonic=3) -> np.ndarray:
        samples = np.zeros(int(self.sample_rate*self.duration))
        for n in range(1,harmonic + 1):
            wave = Wave(self.freq * n, self.amp, self.duration, self.sample_rate)
            samples += wave_type(wave) * (1/n)

        if instrument is None:
            adsr = ADSR(self.duration, 0.05, 0.20, 0.60, 0.20, self.sample_rate)
        elif isinstance(instrument, str):
            adsr = EnvelopeStore.get(instrument).to_adsr(self.duration, self.sample_rate)
        elif isinstance(instrument, ADSRParams):
            adsr = instrument.to_adsr(self.duration, self.sample_rate)
        else:
            raise TypeError(f"instrument must be str or ADSRParams, got {type(instrument)}")

        env = adsr.envelope()

        max_val = np.max(np.abs(samples))
        if max_val > 0:
            samples = samples / max_val

        samples = samples[:len(env)] * env
        return samples.astype(np.float32)




