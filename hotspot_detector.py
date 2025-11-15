import numpy as np

class HotSpotPredictor:
    def __init__(self, window=1000, threshold=2.0):
        self.window = window
        self.threshold = threshold
        self.history = {}

    def record(self, key):
        self.history[key] = self.history.get(key, 0) + 1

    def detect_hot(self):
        avg = np.mean(list(self.history.values()))
        return [k for k, v in self.history.items() if v > avg * self.threshold]