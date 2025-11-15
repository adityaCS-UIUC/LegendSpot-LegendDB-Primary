import numpy as np
import matplotlib.pyplot as plt

# Simulated skew levels
skew = np.array([0.2, 0.6, 1.0, 1.2, 1.5])

# Simulated throughput values (example numbers)
polar = np.array([15000, 12000, 7000, 4000, 2000])        # PolarDB-MP baseline
fusion = np.array([16000, 15000, 14000, 13000, 12500])    # HotSpot-FusionDB

plt.figure(figsize=(8,5))
plt.plot(skew, polar, marker="o", label="PolarDB-MP")
plt.plot(skew, fusion, marker="o", label="HotSpot-FusionDB")

plt.xlabel("Zipf Skew (α)")
plt.ylabel("Throughput (TPS)")
plt.title("Performance Under Skewed Workloads")
plt.legend()
plt.grid(True)

plt.savefig("hotspot_results.png", dpi=300)
plt.show()
