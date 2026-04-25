from dataclasses import dataclass
from ADSR import ADSR
from wave_generator import Wave

@dataclass(frozen=True)
class InstrumentPreset:
    attack: float
    decay: float
    sustain: float
    release: float
    wave_type: Wave
    harmonic: int
    filter_a: float

    def to_adsr(self, duration: float, sample_rate: int = 44100) -> ADSR:
        return ADSR(duration, self.attack, self.decay, self.sustain, self.release, sample_rate)


class InstrumentStore:

    PRESETS: dict[str, InstrumentPreset] = {
        "piano": InstrumentPreset(
            attack=0.005,
            decay=1.50,
            sustain=0.00,
            release=0.10,
            wave_type=Wave.triangle,
            harmonic=8,
            filter_a=0.80
        ),

        "acoustic_guitar": InstrumentPreset(
            attack=0.01,
            decay=1.20,
            sustain=0.00,
            release=0.10,
            wave_type=Wave.sawtooth,
            harmonic=6,
            filter_a=0.60
        ),

        "violin": InstrumentPreset(
            attack=0.15,
            decay=0.10,
            sustain=0.90,
            release=0.15,
            wave_type=Wave.sawtooth,
            harmonic=15,
            filter_a=0.5
        ),

        "flute": InstrumentPreset(
            attack=0.10,
            decay=0.20,
            sustain=0.80,
            release=0.10,
            wave_type=Wave.sine,
            harmonic=3,
            filter_a=0.35
        ),
    }

    @classmethod
    def get(cls, instrument: str) -> InstrumentPreset:
        key = instrument.lower().replace(" ", "_")
        if key not in cls.PRESETS:
            available = list(cls.PRESETS.keys())
            raise ValueError(f"Unknown instrument '{instrument}'. Available: {available}")
        return cls.PRESETS[key]
