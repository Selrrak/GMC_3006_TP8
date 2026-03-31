import lvm.lvm as lvm
import analyse.graph as graph
import math
import numpy as np
import os
import pandas as pd


def get_data():
    zs = (0.0, 115.71, 227.05)
    lcp, lm = 830.25, 19.22
    cwd = os.getcwd()
    data_dir = os.path.join(cwd, "TP8_data")
    for filename in os.listdir(data_dir):
        print(f"parsing: {filename}")
        df = lvm.parse_lvm(os.path.join(data_dir, filename))
        df["X_Value"] = pd.to_numeric(df["X_Value"])
        df["Tension"] = pd.to_numeric(df["Tension"])
        graph.make_graph(df, filename)
        if "chutelibre" in filename:
            ts = find_sensor_times(6.0, df)
            g = g_fall(zs, ts)
            print(f"sensors passed at{ts}, resulting g: {round(g,3)}")
        else:
            T = find_pendulum_T(6.0, df)
            g = g_pendulum(lcp, lm, T)
            print(f"period of pendulum: {T}, resulting g: {round(g,3)}")
    return None


def find_sensor_times(base_V, df):
    below_thresh = df["Tension"] < base_V
    diff = np.diff(below_thresh.astype(int))
    falling_edges = np.where(diff == 1)[0]
    event_times = df["X_Value"].iloc[falling_edges].values
    return event_times


def find_pendulum_T(base_V, df):
    below_thresh = df["Tension"] < base_V
    diff = np.diff(below_thresh.astype(int))
    falling_edges = np.where(diff == 1)[0]
    event_times = df["X_Value"].iloc[falling_edges].values
    T = event_times[2] - event_times[0]
    return T


def g_pendulum(lcp, lm, T):
    return 4 * (math.pi**2) * (lcp + lm / 2) / (1000 * (T**2))


def g_fall(zs, ts):
    z1, z2, z3 = zs
    t1, t2, t3 = ts
    return (2 / (1000 * (t3 - t2))) * (
        ((z1 - z3) / (t1 - t3)) - ((z1 - z2) / (t1 - t2))
    )
