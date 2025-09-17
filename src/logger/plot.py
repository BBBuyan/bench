import matplotlib.pyplot as plt
import numpy as np
import os
from pathlib import Path
from json import loads
from pprint import pprint

def get_file_name():
    i = 1
    while os.path.exists(f"img_{i}.png"):
        i+=1

    return f"img_{i}.png"

def plot(
    before: list[float]
    , after: list[float]
    , name: str
    , depth: list[int]
    , w):

    x = np.arange(len(depth))
    fig, ax = plt.subplots()

    ax.bar(x-w/2, before, width=w, label="Before")
    ax.bar(x+w/2, after, width=w, label="After")

    ax.set_title(name)
    ax.set_xticks(x)

    ax.set_ylabel("Duration / ms")
    ax.set_xlabel("Depth")

    ax.legend(loc="upper right", bbox_to_anchor=(1,-0.1))

    plt.tight_layout()

    file_name = get_file_name()
    fig.savefig(file_name)

def get_es_result():
    file_path = Path(__file__).parent.parent.parent/"result"/"es_result.json"
    data = []
    with open(file_path, "r") as f:
        for line in f:
            tmp = loads(line)
            data.append(tmp)

    return data

def plot_es_flat():
    data = get_es_result()
    write_path = Path(__file__).parent.parent.parent/"result"/"es_figs"/"flat.png"

    flat_result = [d for d in data if d["coll_type"] == "flat"]
    durations = []
    operations = []

    for r in flat_result:
        durations.append(r["depth_0"])
        operations.append(r["operation"])

    plt.bar(operations, durations)

    for i, v in enumerate(durations):
        plt.text(i, v + 0.5, str(v), ha='center', va='bottom')

    plt.title("Flat")
    plt.ylabel("Duration / ms")

    plt.savefig(write_path)
    plt.close()



def plot_es_nested():
    data = get_es_result()
    base_path = Path(__file__).parent.parent.parent/"result"/"es_figs"
    arr_result = [d for d in data if d["coll_type"] == "arr"]
    for arr in arr_result:
        operation = arr["operation"]
        depths = ["1","2","4","8"]
        durations = []
        for i in range(len(depths)):
            durations.append(arr[f"depth_{i}"])

        for i, v in enumerate(durations):
            plt.text(i, v + 0.5, str(v), ha='center', va='bottom')

        plt.bar(depths, durations)
        plt.title(f"arr_{operation}")
        plt.ylabel("Duration / ms")

        write_path=base_path/f"arr_{operation}.png"
        plt.savefig(write_path)
        plt.close()



