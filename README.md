# Smart Trash Collector: Intelligent Route Optimization System 🚛♻️

## 📌 Project Overview
Urban waste collection often suffers from inefficiencies due to static, fixed routes that lead to wasted fuel, time, and human effort. [cite_start]Our team developed the **Smart Trash Collector**, an intelligent route-planning system that dynamically optimizes collection paths based on real-time coordinates[cite: 662]. [cite_start]By minimizing travel distance, we aim to reduce operational costs and carbon emissions, contributing to a cleaner and more sustainable urban environment[cite: 677].

## 🚀 Key Features
* [cite_start]**Dynamic Path Planning:** Replaces traditional manual routing with automated algorithmic solutions[cite: 663].
* [cite_start]**Algorithmic Comparison:** Provides a rigorous evaluation between local (Nearest Neighbor) and global (Genetic Algorithm) optimization methods[cite: 664].
* [cite_start]**Scalability Testing:** Performance verified across datasets ranging from 5 to 1,000 collection points[cite: 1021].
* [cite_start]**Performance Visualization:** Includes execution time graphs and route distance analysis using Matplotlib[cite: 666].

## 🛠️ Tech Stack
* [cite_start]**Language:** Python[cite: 666].
* [cite_start]**Libraries:** NumPy for data processing, Pandas for data manipulation, and Matplotlib for visualization[cite: 666].
* [cite_start]**Optimization Techniques:** Genetic Algorithms (GA) and Nearest Neighbor (NN)[cite: 664].

## 🧠 Algorithmic Implementation
Our team compared two distinct approaches:

### 1. Simple Algorithm: Nearest Neighbor (NN)
* [cite_start]**Logic:** A greedy approach that always selects the closest unvisited point[cite: 757].
* [cite_start]**Complexity:** Time complexity of O(n^2) and Space complexity of O(n)[cite: 785, 816].
* [cite_start]**Best For:** Small-scale problems where speed is the primary concern[cite: 1156].

### 2. Optimized Algorithm: Genetic Algorithm (GA)
* [cite_start]**Logic:** An evolutionary technique utilizing selection, crossover, and mutation to explore a global search space[cite: 846].
* [cite_start]**Evolutionary Operations:** Custom-built functions to merge parent routes (Crossover) and apply random swap mutations to prevent local optima stagnation[cite: 867, 870].
* [cite_start]**Complexity:** Time complexity of O(G * P * n * log P) and Space complexity of O(P * n)[cite: 954, 1002].

## 📊 Empirical Results
* [cite_start]**Accuracy:** The Genetic Algorithm consistently produced shorter, more optimized routes compared to the Nearest Neighbor as the number of points increased[cite: 1168].
* [cite_start]**Efficiency:** While Nearest Neighbor remains faster in execution time, the Genetic Algorithm's accuracy makes it the superior choice for real-world logistics[cite: 1157, 1204].

## 👥 Contributors (Team Members)
* [cite_start]Ghadah Almutairi [cite: 649]
* [cite_start]Aknan Alshubrumi [cite: 649]
* [cite_start]Tala Albishri [cite: 649]
* [cite_start]Jawaher Alharbi [cite: 649]

---
