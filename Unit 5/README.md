# 0/1 Knapsack using Branch and Bound

## Description

This project implements the 0/1 Knapsack problem using the
Branch and Bound technique.

Branch and Bound explores possible item selections using a
state-space tree. An upper bound is calculated at every node
to determine whether the node can produce a better solution.

Branches that cannot improve the current best solution are
pruned.

## Problem

Given a set of items with weights and profits, maximize the
total profit without exceeding the knapsack capacity.

## Input

Weights: [2, 3, 4, 5]

Profits: [40, 50, 65, 70]

Capacity: 7

## Algorithm

1. Calculate the profit/weight ratio of each item.
2. Sort items according to their ratio.
3. Create the root node.
4. Calculate its upper bound.
5. Generate include and exclude branches.
6. Calculate the bound of each child node.
7. Select the node having the highest bound.
8. Prune nodes whose bound is not greater than the current
   maximum profit.
9. Continue until all promising nodes are processed.
10. Return the maximum profit.

## Pseudocode

Include the Branch and Bound pseudocode here.

## Visualization

The state-space tree shows:
- Item inclusion/exclusion
- Node weight
- Node profit
- Upper bound
- Pruned branches
- Optimal solution path

## Result

For the given example:

Maximum Profit = 115

The optimal selection is Item 2 and Item 3.

Total Weight = 7

Total Profit = 115

## Learning Outcomes

- Understand the 0/1 Knapsack problem.
- Understand Branch and Bound.
- Learn how upper bounds are calculated.
- Understand pruning of non-promising nodes.
- Visualize a state-space search tree.
- Understand how Branch and Bound reduces unnecessary
  exploration.

## Files

- `Project13_Knapsack_BnB.py`
- `Prompt.txt`
- `Visualization.png`
- `README.md`