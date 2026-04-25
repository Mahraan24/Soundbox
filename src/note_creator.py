import numpy as np
from ADSR import ADSR
from envelope_store import EnvelopeStore, ADSRParams
from wave_generator import Wave

# Harmonic count presets — how many overtones each waveform type needs
# before it sounds "right" without adding obvious aliasing at high freqs.
HARMONIC_DEFAULTS: dict[str, int] = {
    "sine":     1,   # sine is already a single harmonic
    "square":   8,   # odd harmonics only, converges fast
    "sawtooth": 10,  # all harmonics, needs more
    "triangle": 6,   # odd harmonics, falls off as 1/n², converges faster
}

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

    def build(
        self,
        wave_type=None,
        harmonics: int | None = None,
        instrument: str | ADSRParams | None = None,
    ) -> np.ndarray:
        if wave_type is None:
            wave_type = Wave.sine

        if harmonics is None:
            method_name = wave_type.__name__ if hasattr(wave_type, "__name__") else "sine"
            harmonics = HARMONIC_DEFAULTS.get(method_name,6)
        samples = np.zeros(int(self.sample_rate * self.duration), dtype=np.float64)
        for n in range(1, harmonics + 1):
            harmonic = Wave(self.freq * n, self.amp,self.duration,self.sample_rate)
            samples += wave_type(harmonic).astype(np.float64) * (1.0/n)

        max_val = np.max(np.abs(samples))
        if max_val > 0:
            samples /= max_val

        if instrument is None:
            adsr = ADSR(self.duration, 0.05,0.20,0.60,0.20, self.sample_rate)
        elif isinstance(instrument, str):
            adsr = EnvelopeStore.get(instrument).to_adsr(self.duration, self.sample_rate)
        elif isinstance(instrument, ADSRParams):
            adsr = instrument.to_adsr(self.duration, self.sample_rate)
        else:
            raise TypeError(f"instrument must be str or ADSRParams, got {type(instrument)}")

        env = adsr.envelope()

        samples = samples[:len(env)] * env

        return samples.astype(np.float32)




