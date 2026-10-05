# Project 1 — Floyd-Warshall: All-Pairs Shortest Path

## Prompt
> "Show iterative updates of the distance matrix in the Floyd-Warshall algorithm."

## Outcome
Stepwise matrix visualization — heatmap snapshots of the distance matrix
at every intermediate vertex step (k = 0 to n−1), saved as `Visualization.png`.

---

## Problem Statement

Given a weighted directed graph with `n` vertices, find the shortest path
between **every pair of vertices** using the **Floyd-Warshall algorithm**.

The algorithm works by progressively improving the distance estimate between
all pairs (i, j) by checking if routing through an intermediate vertex `k`
yields a shorter path:

```
dist[i][j] = min(dist[i][j],  dist[i][k] + dist[k][j])
```

This is repeated for every intermediate vertex k = 0, 1, ..., n−1.

---

## Project Structure

```
Project1_FloydWarshall/
├── Project1_FloydWarshall.py   ← Main algorithm + visualization
├── Prompt.txt                  ← Problem statement & prompt
├── Visualization.png           ← Generated heatmap (run .py to create)
└── README.md                   ← This file
```

---

## Algorithm Details

| Property         | Value                          |
|------------------|-------------------------------|
| Algorithm        | Floyd-Warshall                |
| Problem Type     | All-Pairs Shortest Path (APSP)|
| Time Complexity  | O(n³)                         |
| Space Complexity | O(n²)                         |
| Graph Type       | Weighted Directed Graph       |
| Handles          | Negative weights              |
| Detects          | Negative cycles               |

---

## Sample Graph (Built-in)

```
Vertices: 0, 1, 2, 3

Edges:
  0 → 1  (weight 3)
  0 → 3  (weight 7)
  1 → 2  (weight 2)
  2 → 3  (weight 1)
  3 → 1  (weight 1)
```

Adjacency Matrix:

```
     v0   v1   v2   v3
v0 [  0,   3, INF,   7 ]
v1 [INF,   0,   2, INF ]
v2 [INF, INF,   0,   1 ]
v3 [INF,   1, INF,   0 ]
```

---

## How to Run

1. Install dependency (if not already installed):
   ```bash
   pip install matplotlib numpy
   ```

2. Run the script:
   ```bash
   python Project1_FloydWarshall.py
   ```

3. What happens:
   - The distance matrix is printed to the console at each step k
   - A grid of heatmaps is displayed and saved as `Visualization.png`

---

## Visualization

`Visualization.png` shows **n+1 heatmap snapshots**:
- **Initial Matrix** — direct edge weights (INF where no edge)
- **After k=0, k=1, ... k=n−1** — matrix after each intermediate vertex

Cells with no path (INF) are shown in **light gray**.
Shorter distances appear in lighter blue; longer in darker blue.

---

## Console Output (Example)

```
==================================================
  Initial Matrix
==================================================
      v0  v1  v2  v3
    ----------------
  v0 |  0   3 INF   7
  v1 |INF   0   2 INF
  v2 |INF INF   0   1
  v3 |INF   1 INF   0

==================================================
  After k = 0  (intermediate vertex 0)
==================================================
...
```

---

## References

- Cormen, T. H. et al. — *Introduction to Algorithms* (CLRS), Chapter 25
- Floyd (1962), Warshall (1962) — original publications
