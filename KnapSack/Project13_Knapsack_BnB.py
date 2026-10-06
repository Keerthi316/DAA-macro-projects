from queue import PriorityQueue


class Node:
    def __init__(self, level, profit, weight, bound):
        self.level = level
        self.profit = profit
        self.weight = weight
        self.bound = bound

    def __lt__(self, other):
        return self.bound > other.bound


def calculate_bound(node, n, capacity, weights, profits):

    if node.weight >= capacity:
        return 0

    profit_bound = node.profit
    total_weight = node.weight
    j = node.level + 1

    # Add complete items
    while j < n and total_weight + weights[j] <= capacity:
        total_weight += weights[j]
        profit_bound += profits[j]
        j += 1

    # Add fraction of next item for upper bound
    if j < n:
        profit_bound += (
            (capacity - total_weight)
            * profits[j]
            / weights[j]
        )

    return profit_bound


def knapsack_branch_and_bound(weights, profits, capacity):

    n = len(weights)

    # Sort according to profit/weight ratio
    items = list(zip(weights, profits))

    items.sort(
        key=lambda x: x[1] / x[0],
        reverse=True
    )

    weights = [item[0] for item in items]
    profits = [item[1] for item in items]

    pq = PriorityQueue()

    root = Node(-1, 0, 0, 0)

    root.bound = calculate_bound(
        root,
        n,
        capacity,
        weights,
        profits
    )

    pq.put(root)

    max_profit = 0

    while not pq.empty():

        node = pq.get()

        if node.bound <= max_profit:
            continue

        next_level = node.level + 1

        if next_level >= n:
            continue

        # Include current item
        include_weight = (
            node.weight + weights[next_level]
        )

        include_profit = (
            node.profit + profits[next_level]
        )

        if include_weight <= capacity:

            include_node = Node(
                next_level,
                include_profit,
                include_weight,
                0
            )

            if include_node.profit > max_profit:
                max_profit = include_node.profit

            include_node.bound = calculate_bound(
                include_node,
                n,
                capacity,
                weights,
                profits
            )

            if include_node.bound > max_profit:
                pq.put(include_node)

        # Exclude current item
        exclude_node = Node(
            next_level,
            node.profit,
            node.weight,
            0
        )

        exclude_node.bound = calculate_bound(
            exclude_node,
            n,
            capacity,
            weights,
            profits
        )

        if exclude_node.bound > max_profit:
            pq.put(exclude_node)

    return max_profit


# Example
weights = [2, 3, 4, 5]
profits = [40, 50, 65, 70]
capacity = 7

result = knapsack_branch_and_bound(
    weights,
    profits,
    capacity
)

print("Maximum Profit:", result)