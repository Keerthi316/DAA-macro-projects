# ============================================================
# Project 1: All-Pairs Shortest Path — Floyd-Warshall Algorithm
# Prompt : Show iterative updates of distance matrix
# Outcome: Stepwise matrix visualization (saved as Visualization.png)
# ============================================================

import copy
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

INF = math.inf

# ── Graph Input ───────────────────────────────────────────────────────────────
# Weighted directed graph as adjacency matrix
# INF means no direct edge between the vertices

def get_sample_graph():
    """
    Sample 4-vertex weighted directed graph:
        0 --3--> 1
        0 --INF-> 2  (no direct edge)
        0 --7--> 3
        1 --2--> 2
        2 --1--> 3
        3 --1--> 1
    """
    I = INF
    return [
        [0, 3,   I, 7],
        [I, 0,   2, I],
        [I, I,   0, 1],
        [I, 1,   I, 0],
    ]


# ── Floyd-Warshall Core ───────────────────────────────────────────────────────

def floyd_warshall(graph):
    """
    Runs Floyd-Warshall and records the distance matrix after each
    intermediate vertex k.

    Returns:
        snapshots : list of (label, matrix) tuples — one per step + initial
        final_dist: final all-pairs shortest path matrix
    """
    n = len(graph)
    dist = [row[:] for row in graph]   # deep copy
    snapshots = [("Initial Matrix", [row[:] for row in dist])]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF:
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        label = f"After k = {k}  (intermediate vertex {k})"
        snapshots.append((label, [row[:] for row in dist]))

    # Negative cycle detection
    for i in range(n):
        if dist[i][i] < 0:
            print(f"⚠ Negative cycle detected involving vertex {i}")

    return snapshots, dist


# ── Console Print ─────────────────────────────────────────────────────────────

def print_matrix(label, matrix):
    n = len(matrix)
    print(f"\n{'='*50}")
    print(f"  {label}")
    print(f"{'='*50}")
    header = "      " + "  ".join(f"v{j}" for j in range(n))
    print(header)
    print("    " + "-" * (n * 4))
    for i, row in enumerate(matrix):
        vals = "  ".join("INF" if v == INF else f"{v:3}" for v in row)
        print(f"  v{i} | {vals}")


# ── Visualization ─────────────────────────────────────────────────────────────

def matrix_to_numpy(matrix):
    """Replace INF with NaN so heatmap renders nicely."""
    n = len(matrix)
    arr = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            arr[i][j] = np.nan if matrix[i][j] == INF else matrix[i][j]
    return arr


def plot_snapshots(snapshots, output_path="Visualization.png"):
    """
    Creates a grid of heatmaps — one per Floyd-Warshall step.
    Cells with INF are shown in light gray.
    """
    n_steps = len(snapshots)
    cols = 3
    rows = math.ceil(n_steps / cols)

    fig, axes = plt.subplots(rows, cols, figsize=(cols * 4, rows * 3.5))
    axes = axes.flatten()

    # Color map: viridis for finite values, gray for INF
    cmap = plt.cm.YlGnBu.copy()
    cmap.set_bad(color="#d3d3d3")   # light gray for NaN (INF)

    for idx, (label, matrix) in enumerate(snapshots):
        ax = axes[idx]
        arr = matrix_to_numpy(matrix)
        n = len(matrix)

        im = ax.imshow(arr, cmap=cmap, aspect="auto")

        # Annotate each cell
        for i in range(n):
            for j in range(n):
                val = matrix[i][j]
                text = "INF" if val == INF else str(int(val))
                color = "white" if (val != INF and val > 4) else "black"
                ax.text(j, i, text, ha="center", va="center",
                        fontsize=11, fontweight="bold", color=color)

        ax.set_title(label, fontsize=9, fontweight="bold", pad=6)
        ax.set_xticks(range(n))
        ax.set_yticks(range(n))
        ax.set_xticklabels([f"v{j}" for j in range(n)])
        ax.set_yticklabels([f"v{i}" for i in range(n)])
        ax.set_xlabel("To", fontsize=8)
        ax.set_ylabel("From", fontsize=8)

    # Hide unused subplots
    for idx in range(n_steps, len(axes)):
        axes[idx].set_visible(False)

    # Legend patch for INF
    inf_patch = mpatches.Patch(color="#d3d3d3", label="INF (no path)")
    fig.legend(handles=[inf_patch], loc="lower right", fontsize=9)

    fig.suptitle(
        "Floyd-Warshall: Stepwise Distance Matrix Updates\n"
        "All-Pairs Shortest Path Algorithm",
        fontsize=13, fontweight="bold", y=1.01
    )
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    print(f"\n✔ Visualization saved to '{output_path}'")
    plt.show()


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("Floyd-Warshall All-Pairs Shortest Path")
    print("=" * 50)

    graph = get_sample_graph()
    n = len(graph)
    print(f"Graph: {n} vertices, weighted directed")

    # Run algorithm and collect step-by-step snapshots
    snapshots, final_dist = floyd_warshall(graph)

    # Print each matrix step to console
    for label, matrix in snapshots:
        print_matrix(label, matrix)

    print("\n✔ Algorithm complete.")
    print(f"  Total intermediate steps: {n}")
    print(f"  Total matrix snapshots  : {len(snapshots)} (including initial)")

    # Generate and save visualization
    plot_snapshots(snapshots, output_path="Visualization.png")
