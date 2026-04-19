import numpy as np

class ADSR:
    def __init__(self, duration, attack, decay, sustain, release,sample_rate=44100):
        self.duration = duration
        self.attack = attack
        self.decay = decay
        self.sustain = sustain
        self.release = release
        self.sample_rate = sample_rate

        self.N = int(sample_rate * duration)
        self.attack_samples = int(self.attack * self.sample_rate)
        self.decay_samples = int(self.decay * self.sample_rate)
        self.release_samples = int(self.release * self.sample_rate)

        used = self.attack_samples + self.decay_samples + self.release_samples
        self.sustain_samples = max(0, self.N - used)

    def attack_state(self):
        return np.linspace(0.0,1.0,self.attack_samples, endpoint=False)

    def decay_state(self):
        return np.linspace(1.0, self.sustain, self.decay_samples, endpoint=False)

    def sustain_state(self):
        return np.full(self.sustain_samples, self.sustain)

    def release_state(self):
        return np.linspace(self.sustain, 0.0, self.release_samples)

    def envelope(self):
        return np.concatenate([
            self.attack_state(),
            self.decay_state(),
            self.sustain_state(),
            self.release_state()
        ])