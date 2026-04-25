# from dataclasses import dataclass
# from ADSR import ADSR
#
# @dataclass(frozen=True)
# class ADSRParams:
#     attack: float
#     decay: float
#     sustain: float
#     release: float
#
#
#     def to_adsr(self, duration: float, sample_rate: int = 44100) -> ADSR:
#         return ADSR(duration, self.attack, self.decay, self.sustain, self.release, sample_rate)
#
# class EnvelopeStore:
#
#     PRESETS: dict[str, ADSRParams] = {
#         "piano": ADSRParams(attack=0.005, decay=0.30, sustain=0.30, release=0.50),
#         "acoustic_guitar": ADSRParams(attack=0.005, decay=0.25, sustain=0.15, release=0.30),
#         "bass_guitar": ADSRParams(attack=0.010, decay=0.35, sustain=0.40, release=0.40),
#         "electric_guitar": ADSRParams(attack=0.010, decay=0.20, sustain=0.70, release=0.35),
#         "guitar_synth": ADSRParams(attack=0.040, decay=0.10, sustain=0.80, release=0.60),
#         "violin": ADSRParams(attack=0.120, decay=0.05, sustain=0.85, release=0.25),
#         "flute": ADSRParams(attack=0.080, decay=0.05, sustain=0.75, release=0.18),
#         "whistle": ADSRParams(attack=0.020, decay=0.02, sustain=0.90, release=0.06),
#     }
#
#     @classmethod
#     def get(cls, instrument: str) -> ADSRParams:
#         key = instrument.lower().replace(" ", "_")
#         if key not in cls.PRESETS:
#             available = list(cls.PRESETS.keys())
#             raise ValueError(f"Unknown instrument '{instrument}'. Available: {available}")
#         return cls.PRESETS[key]
