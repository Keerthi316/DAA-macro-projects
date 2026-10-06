# Project 14: TSP Branch-and-Bound Search Tree

## Description
This project implements the Traveling Salesperson Problem (TSP) using branch-and-bound search. Given a 4-city problem with a cost matrix, the goal is to find the minimum-cost Hamiltonian cycle (shortest route visiting all cities exactly once and returning to the start city). Branch-and-bound is used to systematically explore possible tours while pruning suboptimal branches using lower-bound estimates.

## Algorithm
The branch-and-bound algorithm for TSP works as follows:

1. **Initialization**: Start from city 0 with zero cumulative cost and compute initial lower bound
2. **Node Selection**: Use a min-priority queue (heapq) to always expand the node with the lowest lower bound first
3. **Lower Bound Computation**: For each node, compute a lower bound on the total tour cost by:
   - Adding minimum cost edges from each unvisited city to other unvisited cities
   - Summing these minimum edges and dividing by 2 (since each edge is counted twice in a complete cycle)
4. **Branching**: Create child nodes by extending the partial tour with each unvisited city
5. **Pruning**: If a node's lower bound >= the best known solution cost, discard that branch (prune)
6. **Solution Update**: When all cities are visited, add the cost to return to the start city; update the best solution if the new tour is cheaper
7. **Termination**: Continue until the priority queue is exhausted; the remaining best solution is optimal

Key data structure: `TSPNode` tracks level (city index), path so far, cumulative cost, and lower bound.

Time Complexity: O(n!) worst case, but branch-and-bound pruning dramatically reduces the number of nodes explored compared to brute force.
Space Complexity: O(n) for the priority queue and node tracking.

## Prompt Used
"Draw a search tree showing bounding and pruning for TSP with 4 cities. Outcome: Hierarchical tree showing cost bounds."

## Output
The program prints the optimal tour and minimum cost found:

```
Optimal Tour: [0, 1, 3, 2, 0]
Minimum Cost: 80

Route: 0 -> 1 -> 3 -> 2 -> 0
```

The search tree explores nodes in order of increasing lower bound, pruning branches that cannot possibly improve upon the current best solution. The number of nodes explored depends on the cost matrix structure and how effectively the lower bound prunes the search space.

## Learning Outcome
- Understood branch-and-bound paradigm for optimization problems
- Learned lower-bound computation techniques for TSP
- Practiced priority queue-based search tree exploration
- Gained experience with GitHub repository structure and README documentation
- Developed algorithmic thinking for combinatorial optimization problems