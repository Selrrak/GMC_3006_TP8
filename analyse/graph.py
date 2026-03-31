import matplotlib.pyplot as plt
import pandas as pd
import os
import numpy as np


def make_graph(df, name):
    cwd = os.getcwd()
    graph_dir = os.path.join(cwd, "graphs")
    graph_file = os.path.join(graph_dir, f"{name}.png")
    X = df["X_Value"]
    Y = df["Tension"]
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(X, Y)
    plt.title(f"{name}")
    fig.tight_layout
    fig.savefig(graph_file, dpi=300, bbox_inches="tight")
    return None
