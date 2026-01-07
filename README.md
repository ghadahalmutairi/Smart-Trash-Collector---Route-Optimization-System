# Smart Trash Collector: Intelligent Route Optimization System 🚛♻️

## 📌 Project Overview
Urban waste collection often suffers from inefficiencies due to static, fixed routes that lead to wasted fuel, time, and human effort. Our team developed the **Smart Trash Collector**, an intelligent route-planning system that dynamically optimizes collection paths based on real-time coordinates. By minimizing travel distance, we aim to reduce operational costs and carbon emissions, contributing to a cleaner and more sustainable urban environment.

## 🚀 Key Features
* **Dynamic Path Planning:** Replaces traditional manual routing with automated algorithmic solutions.
* **Algorithmic Comparison:** Provides a rigorous evaluation between local (Nearest Neighbor) and global (Genetic Algorithm) optimization methods.
* **Scalability Testing:** Performance verified across datasets ranging from 5 to 1,000 collection points.
* **Performance Visualization:** Includes execution time graphs and route distance analysis using Matplotlib.

## 🛠️ Tech Stack
* **Language:** Python
* **Libraries:** NumPy for data processing, Pandas for data manipulation, and Matplotlib for visualization.
* **Optimization Techniques:** Genetic Algorithms (GA) and Nearest Neighbor (NN).

## 🧠 Algorithmic Implementation
Our team compared two distinct approaches:

### 1. Simple Algorithm: Nearest Neighbor (NN)
* **Logic:** A greedy approach that always selects the closest unvisited point.
* **Complexity:** Time complexity of O(n^2) and Space complexity of O(n).
* **Best For:** Small-scale problems where speed is the primary concern.

### 2. Optimized Algorithm: Genetic Algorithm (GA)
* **Logic:** An evolutionary technique utilizing selection, crossover, and mutation to explore a global search space.
* **Evolutionary Operations:** Custom-built functions to merge parent routes (Crossover) and apply random swap mutations to prevent local optima stagnation.
* **Complexity:** Time complexity of O(G * P * n * log P) and Space complexity of O(P * n).

## 📊 Empirical Results
* **Accuracy:** The Genetic Algorithm consistently produced shorter, more optimized routes compared to the Nearest Neighbor as the number of points increased.
* **Efficiency:** While Nearest Neighbor remains faster in execution time, the Genetic Algorithm's accuracy makes it the superior choice for real-world logistics.

## 👥 Contributors (Team Members)
* Ghadah Almutairi
* Aknan Alshubrumi
* Tala Albishri
* Jawaher Alharbi
