"""TSP Branch-and-Bound Search Tree (Project 14)
Unit V – Branch and Bound

Problem: Find the minimum cost Hamiltonian cycle (shortest route visiting
all 4 cities exactly once and returning to start) using branch-and-bound.

Algorithm (in comments):
-----------
1. Define cost matrix: cost[i][j] = cost to travel from city i to city j
2. Use a node structure with: level (city index), path so far, 
   cumulative cost, lower bound
3. Compute lower bound for each node:
   - For each unvisited city i, find the minimum cost edge from i to any
     other unvisited city or back to start
   - Sum these minimum edges and add to current path cost
   - Divide by 2 (since each edge is counted twice in a cycle)
4. Branch: create child nodes by adding each unvisited city to the path
5. Prune: if node's lower bound >= best solution found so far, discard
6. Use a priority queue (min-heap) to explore nodes with lowest bound first
7. When all cities visited, add cost to return to start city
8. Update best solution if current path cost < best cost
9. Output the optimal tour and minimum cost

Time Complexity: O(n!) worst case, but pruning greatly reduces exploration
Space Complexity: O(n) for recursion stack and path tracking

Uses Python's heapq for priority queue branch exploration.
"""

import heapq
import math


class TSPNode:
    """Node in branch-and-bound search tree for TSP."""
    
    def __init__(self, level, path, cost, bound, cost_matrix):
        self.level = level          # current city index (depth)
        self.path = path            # list of cities visited so far
        self.cost = cost            # cumulative cost from start to this node
        self.bound = bound          # lower bound on total cost from this node
        self.cost_matrix = cost_matrix
        
    def __lt__(self, other):
        """Compare nodes by bound for min-heap priority queue."""
        return self.bound < other.bound


def compute_lower_bound(cost, level, n, cost_matrix, visited):
    """Compute lower bound for TSP node using reduced cost matrix."""
    c = cost
    
    # For each unvisited city, find minimum outgoing edge to unvisited
    for i in range(n):
        if i not in visited and i != level:
            unvisited_j = [j for j in range(n) if i != j and j not in visited]
            if unvisited_j:
                min_edge = min(cost_matrix[i][j] for j in unvisited_j)
                c += min_edge
    
    # Add cost from current city back to start conceptually
    # Divide by 2 for double-counting adjustment in cycle
    bound = math.ceil(c / 2)
    return bound


def tsp_branch_and_bound(cost_matrix):
    """Solve TSP using branch-and-bound."""
    n = len(cost_matrix)
    
    # Start from city 0, compute initial lower bound
    visited = set([0])
    initial_cost = 0
    
    # Add minimum outgoing edges from city 0 to unvisited cities
    for j in range(n):
        if j != 0 and j not in visited:
            initial_cost += min(cost_matrix[0][k] for k in range(n) 
                               if k != 0 and k not in visited)
    
    # Add minimum outgoing edges from other cities
    for i in range(1, n):
        if i not in visited:
            min_edge = min(cost_matrix[i][j] for j in range(n) 
                          if i != j and j not in visited)
            initial_cost += min_edge
    
    initial_bound = math.ceil(initial_cost / 2)
    
    # Start from city 0
    start_node = TSPNode(level=0, path=[0], cost=0, 
                         bound=initial_bound, 
                         cost_matrix=cost_matrix)
    
    # Priority queue: (bound, counter, node)
    pq = [(start_node.bound, 0, start_node)]
    counter = 1
    
    best_cost = math.inf
    best_path = None
    
    while pq:
        bound, _, node = heapq.heappop(pq)
        
        # Prune if bound >= best known solution
        if bound >= best_cost:
            continue
        
        # If all cities visited, complete the tour
        if node.level == n - 1:
            # Add cost to return to start
            last_city = node.path[-1]
            total_cost = node.cost + cost_matrix[last_city][0]
            if total_cost < best_cost:
                best_cost = total_cost
                best_path = node.path + [0]
            continue
        
        # Branch: try adding each unvisited next city
        current_city = node.path[-1]
        for next_city in range(n):
            if next_city not in node.path:
                new_cost = node.cost + cost_matrix[current_city][next_city]
                new_path = node.path + [next_city]
                new_visited = set(new_path)
                
                # Compute bound for new node
                new_bound = compute_lower_bound(new_cost, next_city, 
                                                  n, cost_matrix, new_visited)
                
                if new_bound < best_cost:
                    new_node = TSPNode(level=node.level + 1, 
                                        path=new_path, 
                                        cost=new_cost, 
                                        bound=new_bound,
                                        cost_matrix=cost_matrix)
                    heapq.heappush(pq, (new_bound, counter, new_node))
                    counter += 1
    
    return best_path, best_cost


def compute_lower_bound_type2(cost, current_city, n, cost_matrix, visited):
    """Compute lower bound for TSP node - version 2."""
    total = cost
    
    # For each unvisited city, find minimum outgoing edge to unvisited
    for i in range(n):
        if i not in visited:
            min_edge = min(cost_matrix[i][j] for j in range(n) 
                          if i != j and j not in visited)
            total += min_edge
    
    # Add cost from current city back to start (conceptually)
    # Divide by 2 for double-counting adjustment
    bound = math.ceil((total + cost_matrix[current_city][0]) / 2)
    return bound


# --------------------
# Driver code for Project 14
# --------------------
# TSP with 4 cities as specified in the project
# Cost matrix: cost_matrix[i][j] = cost to travel from city i to city j
cost_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0],
]

print(f"TSP Branch-and-Bound Problem: {len(cost_matrix)} cities")
print("Cost matrix (city i to city j):")
for row in cost_matrix:
    print(" ".join(f"{c:3}" for c in row))

best_path, best_cost = tsp_branch_and_bound(cost_matrix)

print(f"\nOptimal Tour: {best_path}")
print(f"Minimum Cost: {best_cost}")
print(f"\nRoute: {' -> '.join(str(c) for c in best_path[:-1])} -> 0")