# DAA Macro Projects – Algorithm Visualization Lab

A collection of interactive and visualization-based projects developed for the **Design and Analysis of Algorithms (DAA)** laboratory.

The repository demonstrates important algorithmic techniques such as **sorting, greedy methods, dynamic programming, backtracking, branch and bound, and graph algorithms** through implementations, step-by-step visualizations, state-space trees, and algorithm analysis.

The main objective of these projects is to make classical DAA algorithms easier to understand by combining **algorithm implementation with visual learning**.

---

## 📚 Projects Overview

| Unit | Project | Algorithm / Technique | Visualization |
|------|---------|------------------------|---------------|
| Unit I | Sorting Lab Pro | Bubble, Selection, Insertion, Merge & Quick Sort | Interactive Web Visualizer |
| Unit III | Optimal Merge Pattern | Greedy Method | Weighted Binary Merge Tree |
| Unit III | Floyd-Warshall | Dynamic Programming | Distance Matrix Heatmaps |
| Unit IV | N-Queens | Backtracking | State Space Tree & Flow |
| Unit V | 0/1 Knapsack | Branch and Bound | State Space Tree |

---

# 🔹 Unit I – Sorting Lab Pro

An interactive web-based laboratory for understanding and comparing fundamental sorting algorithms.

### Algorithms

- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort

### Features

- Generate random arrays
- Enter custom elements
- Adjustable array size
- Adjustable animation speed
- Animated comparisons and swaps
- Live comparison count
- Live swap/move count
- Progress percentage
- Runtime display
- Time complexity display
- Quick Sort pivot visualization
- Sorted-position visualization
- Algorithm explanations
- Best/Average/Worst complexity comparison
- Responsive dark glassmorphism interface

### Technologies

- HTML
- CSS
- JavaScript

### Running the Project

Open:

```text
Sorting_Algorithm_Visualizer.html
```

The project runs directly in a browser and requires **no backend**.

---

# 🔹 Unit III – Optimal Merge Pattern

An interactive visualization of the **Optimal Merge Pattern** using the Greedy Method.

The objective is to merge a collection of files with minimum total merge cost.

### Example

For file sizes:

```text
10, 20, 30, 40
```

The optimal sequence is:

```text
10 + 20 = 30    → Cost = 30
30 + 30 = 60    → Cost = 60
40 + 60 = 100   → Cost = 100
```

Therefore:

```text
Minimum Total Cost = 30 + 60 + 100 = 190
```

### Features

- Weighted binary merge tree
- Step-by-step merge visualization
- Custom file sizes
- Next Merge operation
- Auto Play
- Reset
- Animation speed control
- Live sorted working list
- Merge step log
- Total cost calculation
- Comparison with largest-first merging
- Algorithm explanation
- Complexity analysis
- Responsive dark interface

### Running the Project

Open:

```text
Optimal_Merge_Pattern_Visualizer.html
```

The project runs directly in Chrome or Edge and requires **no backend**.

---

# 🔹 Unit III – Floyd-Warshall Algorithm

A visualization-based implementation of the **Floyd-Warshall All-Pairs Shortest Path algorithm**.

The algorithm finds the shortest path between every pair of vertices in a weighted directed graph.

### Core Formula

```text
dist[i][j] = min(dist[i][j],
                 dist[i][k] + dist[k][j])
```

The algorithm progressively considers every vertex as an intermediate vertex.

### Example Graph

```text
Vertices: 0, 1, 2, 3

Edges:

0 → 1  (3)
0 → 3  (7)
1 → 2  (2)
2 → 3  (1)
3 → 1  (1)
```

### Features

- Initial distance matrix
- Step-by-step matrix updates
- Intermediate vertex visualization
- Heatmap snapshots
- Detection of unreachable vertices
- Negative-weight support
- Negative-cycle detection

### Complexity

```text
Time Complexity  : O(n³)
Space Complexity : O(n²)
```

### Project Structure

```text
Project1_FloydWarshall/
│
├── Project1_FloydWarshall.py
├── Prompt.txt
├── Visualization.png
└── README.md
```

### Running the Project

Install the required libraries:

```bash
pip install matplotlib numpy
```

Run:

```bash
python Project1_FloydWarshall.py
```

The program prints the distance matrix after every intermediate vertex and generates:

```text
Visualization.png
```

---

# 🔹 Unit IV – N-Queens

A Java implementation of the classic **N-Queens problem** using recursive backtracking.

The objective is to place `N` queens on an `N × N` chessboard such that no two queens attack each other.

For:

```text
N = 4
```

there are exactly **2 valid solutions**.

### Techniques Used

- Recursion
- Backtracking
- Depth-First Search
- State Space Tree
- Pruning

### Features

- Row-by-row queen placement
- Safety checking
- Early pruning of invalid branches
- Console output of solutions
- State-space tree visualization
- Backtracking flow visualization
- Safe, invalid and solution node identification

### Sample Solution

```text
. Q . .
. . . Q
Q . . .
. . Q .
```

Another solution is:

```text
. . Q .
Q . . .
. . . Q
. Q . .
```

### Complexity

```text
Time Complexity  : O(N!)
Space Complexity : O(N)
```

### Project Structure

```text
N-Queens/
│
├── NQueens.java
├── README.md
├── state-space-tree.png
└── backtracking-flow.png
```

### Running the Project

Compile:

```bash
javac NQueens.java
```

Run:

```bash
java NQueens
```

The board size can be changed by modifying the `N` value in the Java program.

---

# 🔹 Unit V – 0/1 Knapsack using Branch and Bound

An implementation and visualization of the **0/1 Knapsack problem using Branch and Bound**.

The objective is to maximize total profit without exceeding the given knapsack capacity.

### Input

```text
Weights : [2, 3, 4, 5]
Profits : [40, 50, 65, 70]

Capacity = 7
```

### Result

```text
Maximum Profit = 115
Total Weight   = 7
```

The optimal selection is:

```text
Item 2 + Item 3
```

with:

```text
Total Weight = 3 + 4 = 7
Total Profit = 50 + 65 = 115
```

### Branch and Bound Approach

1. Calculate profit/weight ratios.
2. Sort items according to their ratios.
3. Create the root node.
4. Calculate the upper bound.
5. Generate include and exclude branches.
6. Calculate bounds for child nodes.
7. Select the node with the highest bound.
8. Prune nodes that cannot improve the current solution.
9. Continue processing promising nodes.
10. Return the maximum profit.

### Visualization

The state-space tree displays:

- Item inclusion/exclusion
- Node weight
- Node profit
- Upper bound
- Pruned branches
- Optimal solution path

### Project Structure

```text
Project13_Knapsack_BnB/
│
├── Project13_Knapsack_BnB.py
├── Prompt.txt
├── Visualization.png
└── README.md
```

---

# 🧠 Algorithms and Techniques Covered

This repository covers several important DAA paradigms:

### Divide and Conquer

- Merge Sort
- Quick Sort

### Greedy Method

- Optimal Merge Pattern

### Dynamic Programming

- Floyd-Warshall

### Backtracking

- N-Queens

### Branch and Bound

- 0/1 Knapsack

### Basic Sorting Techniques

- Bubble Sort
- Selection Sort
- Insertion Sort

---

# 📊 Complexity Summary

| Algorithm | Technique | Best Case | Average Case | Worst Case | Space |
|-----------|-----------|-----------|--------------|------------|-------|
| Bubble Sort | Sorting | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | Sorting | O(n²) | O(n²) | O(n²) | O(1) |
| Insertion Sort | Sorting | O(n) | O(n²) | O(n²) | O(1) |
| Merge Sort | Divide & Conquer | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | Divide & Conquer | O(n log n) | O(n log n) | O(n²) | O(log n)* |
| Floyd-Warshall | Dynamic Programming | O(n³) | O(n³) | O(n³) | O(n²) |
| N-Queens | Backtracking | — | — | O(N!) | O(N) |
| Optimal Merge Pattern | Greedy | O(n log n) | O(n log n) | O(n log n) | O(n) |
| 0/1 Knapsack | Branch & Bound | — | — | O(2ⁿ) | O(n) |

`*` Quick Sort space complexity depends on the recursion depth and implementation.

---

# 🛠️ Technologies Used

The projects use different technologies depending on the algorithm:

- **Java**
- **Python**
- **HTML**
- **CSS**
- **JavaScript**
- **NumPy**
- **Matplotlib**

No database or backend server is required for the visualization-based projects.

---

# 📁 Repository Structure

```text
DAA-macro-projects/
│
├── Unit 1 Sorting/
│   └── Sorting_Algorithm_Visualizer.html
│
├── Unit 3 Optimal Merge Pattern/
│   ├── Optimal_Merge_Pattern_Visualizer.html
│   ├── Prompt.txt
│   └── README.md
│
├── Project1_FloydWarshall/
│   ├── Project1_FloydWarshall.py
│   ├── Prompt.txt
│   ├── Visualization.png
│   └── README.md
│
├── Unit 4 N-Queens/
│   ├── NQueens.java
│   ├── README.md
│   ├── state-space-tree.png
│   └── backtracking-flow.png
│
├── Unit 5 Knapsack/
│   ├── Project13_Knapsack_BnB.py
│   ├── Prompt.txt
│   ├── Visualization.png
│   └── README.md
│
└── README.md
```

> Folder names may vary depending on the final repository organization.

---

# 🎯 Objectives

The main objectives of this project are:

- To implement important DAA algorithms.
- To understand different algorithm design paradigms.
- To analyze time and space complexity.
- To visualize algorithm execution step by step.
- To understand state-space trees and pruning techniques.
- To compare algorithmic approaches.
- To make DAA concepts easier to understand through interactive demonstrations.
- To create presentation-ready visualizations for laboratory evaluation.

---

# 📚 Learning Outcomes

After completing these projects, the learner will be able to:

- Analyze algorithms using asymptotic complexity.
- Implement fundamental sorting algorithms.
- Understand Divide and Conquer techniques.
- Apply the Greedy Method to optimization problems.
- Implement Dynamic Programming algorithms.
- Understand recursive backtracking.
- Construct and interpret state-space trees.
- Apply Branch and Bound to optimization problems.
- Visualize intermediate algorithmic states.
- Compare different algorithmic strategies based on efficiency.

---

# ▶️ How to Use This Repository

1. Clone or download the repository.

```bash
git clone <repository-url>
```

2. Open the required unit/project folder.

3. Follow the `README.md` inside the project for specific instructions.

4. Run the corresponding program or open the HTML visualization.

5. Explore the algorithm step by step using the provided visualizations.

---

# 🌐 Browser-Based Projects

The following projects can be opened directly in a modern browser:

- Sorting Algorithm Visualizer
- Optimal Merge Pattern Visualizer

Recommended browsers:

- Google Chrome
- Microsoft Edge

No backend server is required.

---

# 👩‍💻 Academic Project

**Project:** DAA Macro Project  
**Subject:** Design and Analysis of Algorithms  
**Focus:** Algorithm Implementation, Analysis & Visualization

This repository demonstrates how theoretical DAA concepts can be transformed into **interactive and visual learning tools**.

---

## ⭐ Conclusion

The **DAA Macro Projects – Algorithm Visualization Lab** brings together multiple classical algorithms from different algorithm design paradigms.

Instead of only implementing the algorithms, the projects provide **visual representations of sorting operations, shortest-path matrix updates, greedy merging, backtracking search, and Branch and Bound pruning**.

This makes the repository useful for **learning, experimentation, laboratory demonstrations, and academic presentations**.
