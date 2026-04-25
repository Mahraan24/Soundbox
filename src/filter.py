import numpy as np


class Filter:

    def __init__(self, a=0.5):
        self.a = a

    def low_pass(self, samples: np.ndarray):
        output = np.zeros_like(samples)
        output[0] = samples[0]
        for i in range(1,len(samples)):
            output[i] = (1 - self.a) * samples[i] + self.a * output[i - 1]

        return output