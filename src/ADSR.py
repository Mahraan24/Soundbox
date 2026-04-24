import numpy as np

class ADSR:
    def __init__(
            self,
            duration: float,
            attack: float,
            decay: float,
            sustain: float,
            release: float,
            sample_rate=44100,
    ):
        self.duration = duration
        self.attack = attack
        self.decay = decay
        self.sustain = sustain
        self.release = release
        self.sample_rate = sample_rate

        self.N = int(sample_rate * duration)

        self.attack_samples = min(int(attack * sample_rate), self.N)
        remaining = self.N - self.attack_samples
        self.decay_samples = min(int(decay * sample_rate), remaining)
        remaining -= self.decay_samples
        self.release_samples = min(int(release * sample_rate), remaining)
        remaining -= self.release_samples
        self.sustain_samples = remaining

    def attack_state(self) -> np.ndarray:
        return np.linspace(0.0,1.0,self.attack_samples, endpoint=False)

    def decay_state(self) -> np.ndarray:
        return np.linspace(1.0, self.sustain, self.decay_samples, endpoint=False)

    def sustain_state(self) -> np.ndarray:
        return np.full(self.sustain_samples, self.sustain)

    def release_state(self) -> np.ndarray:
        return np.linspace(self.sustain, 0.0, self.release_samples)

    def envelope(self) -> np.ndarray:
        return np.concatenate([
            self.attack_state(),
            self.decay_state(),
            self.sustain_state(),
            self.release_state()
        ])