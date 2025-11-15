import numpy as np
import matplotlib.pyplot as plt

hot = np.load("/mnt/data/hot_keys.npy")

plt.figure(figsize=(6,4))
plt.hist(hot, bins=50)
plt.title("Detected Hot Keys Distribution")
plt.xlabel("Key")
plt.ylabel("Frequency")
plt.savefig("/mnt/data/hotspot_distribution.png", dpi=200)
print("Saved plot to /mnt/data/hotspot_distribution.png")