import numpy as np
from ADSR import ADSR
from wave_generator import Wave

class Note:
    def __init__(self, freq, amp, duration, sample_rate=44100):
        self.freq = freq
        self.amp = amp
        self.sample_rate = sample_rate
        self.duration = duration

    def build(self, wave_type,N):
        samples = np.zeros(int(self.sample_rate * self.duration))
        for n in range(1,N+1):
            harmonic = Wave(self.freq * n, self.amp,self.duration,self.sample_rate)
            samples += wave_type(harmonic).astype(np.float32) * (1/n)

        max_val = np.max(np.abs(samples))
        if max_val > 0:
            samples /= max_val

        adsr = ADSR(self.duration, 0.02,0.05,0.7,0.2)
        env = adsr.envelope()

        samples = samples[:len(env)] * env

        return samples.astype(np.float32)





