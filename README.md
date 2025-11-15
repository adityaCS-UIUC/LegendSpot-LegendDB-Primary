* HotSpot-FusionDB — Research Prototype & Simulation Toolkit

- * A hybrid LSM-augmented, multi-primary RDMA OLTP architecture for mitigating hot-spot contention in cloud databases.

* Overview

- * HotSpot-FusionDB is a research prototype accompanying the CS411 project proposal “HotSpot-FusionDB: Bridging LSM Write Optimization and Multi-Primary RDMA Concurrency Control.”

- * This repository provides:
	•	A simulation of skew-induced contention in multi-primary systems
	•	Synthetic models of ownership churn, throughput decay, and EMA-based hot-spot prediction
	•	A graph demonstrating expected performance improvements of HotSpot-FusionDB over PolarDB-MP
	•	Well-structured prototype modules (LSM buffer, hot-spot detector)

- * This is not a production database system — it is a research model illustrating how LSM write buffering and RDMA ownership consolidation can reduce contention under highly skewed OLTP workloads.
