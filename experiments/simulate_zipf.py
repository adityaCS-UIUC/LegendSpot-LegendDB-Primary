import numpy as np
from hotspot_fusiondb.hotspot_detector import HotSpotPredictor

def simulate_zipf(theta=1.2, size=100000, keyspace=1000):
    keys = np.random.zipf(theta, size) % keyspace
    hsp = HotSpotPredictor()

    for k in keys:
        hsp.record(int(k))

    hot = hsp.detect_hot()
    np.save("/mnt/data/hot_keys.npy", np.array(hot))
    print("Detected hot keys:", hot[:10])

if __name__ == "__main__":
    simulate_zipf()