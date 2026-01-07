# Smart Trash Collector: Intelligent Route Optimization System 🚛♻️

## 📌 Project Overview
[cite_start]Urban waste collection often suffers from inefficiencies due to static, fixed routes that lead to wasted fuel, time, and human effort[cite: 661, 662]. [cite_start]Our team developed the **Smart Trash Collector**, an intelligent route-planning system that dynamically optimizes collection paths based on real-time coordinates[cite: 662, 663]. [cite_start]By minimizing travel distance, we aim to reduce operational costs and carbon emissions, contributing to a cleaner and more sustainable urban environment[cite: 673, 677].

## 🚀 Key Features
* [cite_start]**Dynamic Path Planning:** Replaces traditional manual routing with automated algorithmic solutions[cite: 662, 674].
* [cite_start]**Algorithmic Comparison:** Provides a rigorous evaluation between local (Nearest Neighbor) and global (Genetic Algorithm) optimization methods[cite: 664, 1200].
* [cite_start]**Scalability Testing:** Performance verified across datasets ranging from 5 to 1,000 collection points[cite: 1021, 1025].
* [cite_start]**Performance Visualization:** Includes execution time graphs and route distance analysis using **Matplotlib**[cite: 666, 1028].

## 🛠️ Tech Stack
* [cite_start]**Language:** Python[cite: 666].
* [cite_start]**Libraries:** NumPy (Data Processing), Pandas (Data Manipulation), Matplotlib (Visualization)[cite: 666].
* [cite_start]**Optimization Techniques:** Genetic Algorithms (GA) and Nearest Neighbor (NN)[cite: 664].

## 🧠 Algorithmic Implementation
Our team compared two distinct approaches:

### 1. Simple Algorithm: Nearest Neighbor (NN)
* [cite_start]**Logic:** A greedy approach that always selects the closest unvisited point[cite: 757, 839].
* [cite_start]**Complexity:** Time complexity of $O(n^2)$ and Space complexity of $O(n)$[cite: 785, 816].
* [cite_start]**Best For:** Small-scale problems where speed is the primary concern[cite: 1156].

### 2. Optimized Algorithm: Genetic Algorithm (GA)
* [cite_start]**Logic:** An evolutionary technique utilizing selection, crossover, and mutation to explore a global search space[cite: 845, 846].
* **Crossover & Mutation:** Custom-built functions to merge parent routes and apply random swap mutations to prevent local optima stagnation.
* [cite_start]**Complexity:** Time complexity of $O(G \times P \times n \times \log P)$ and Space complexity of $O(P \times n)$[cite: 954, 1002].

## 📊 Empirical Results
* [cite_start]**Accuracy:** The Genetic Algorithm consistently produced shorter, more optimized routes compared to the Nearest Neighbor as the number of points increased[cite: 1101, 1204].
* [cite_start]**Efficiency:** While Nearest Neighbor remains faster in execution time, the Genetic Algorithm's accuracy makes it the superior choice for real-world logistics[cite: 1157, 1203].

## 👥 Contributors (Team Members)
* Ghadah Almutairi
* Aknan Alshubrumi
* Tala Albishri
* Jawaher Alharbi

---
