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

def get_result(file_name: str):
    file_path = Path(__file__).parent.parent.parent/"result"/f"{file_name}.json"
    data = []
    with open(file_path, "r") as f:
        for line in f:
            tmp = loads(line)
            data.append(tmp)

    return data

def plot_es_flat(data: list[dict]):
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

def plot_es_nested(data:list[dict]):
    base_path = Path(__file__).parent.parent.parent/"result"/"figs"/"elastic"

    arr_result = [d for d in data if d["coll_type"] == "obj"]
    for arr in arr_result:
        operation = arr["operation"]
        depths = ["1","2","4","8"]
        durations = []
        for i in range(len(depths)):
            durations.append(arr[f"depth_{i}"])

        for i, v in enumerate(durations):
            plt.text(i, v + 0.5, str(v), ha='center', va='bottom')

        plt.bar(depths, durations)
        plt.title(f"obj_{operation}")
        plt.ylabel("Duration / ms")

        write_path=base_path/f"obj_{operation}.png"
        plt.savefig(write_path)
        plt.close()

def plot_flat(data: list[dict], coll_type: str, db_type: str):
    base_path = Path(__file__).parent.parent.parent/"result"/"figs"
    filtered = [d for d in data if d["coll_type"] == "flat"]

    durations = []
    operations = []

    for f in filtered:
        durations.append(f["depth_0"])
        operations.append(f["operation"])

    before = []
    after = []
    for i in durations:
        before.append(i[0])
        after.append(i[1])

    x = np.arange(len(operations))
    w = 0.25

    fig, ax = plt.subplots()

    bars1 = ax.bar(x-w/2, before, width=w, label="Before")
    bars2 = ax.bar(x+w/2, after, width=w, label="After")


    for bar in list(bars1) + list(bars2):
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{height:.0f}",
            ha="center", va="bottom", fontsize=8
        )
    # ax.set_yscale("log")
    ax.set_title("Flat")
    ax.set_xticks(x, operations)
    ax.set_ylabel("Duration / ms")

    write_path=base_path/f"{db_type}_{coll_type}_.png"
    fig.savefig(write_path)

def plot_nested(data:list[dict], coll_type: str, db_type: str):
    base_path = Path(__file__).parent.parent.parent/"result"/"figs"/f"{db_type}"
    filtered_ = [d for d in data if d["coll_type"] == coll_type]
    depths = ["1","2","4","8"]

    for f in filtered_:
        operation = f["operation"]
        durations = []

        for i in range(len(depths)):
            durations.append(f[f"depth_{i}"])

        before = []
        after = []

        for i in durations:
            before.append(i[0])
            after.append(i[1])

        fig, ax = plt.subplots()
        w = 0.35
        x = np.arange(len(depths))

        bars1 = ax.bar(x-w/2, before, width=w, label="Before")
        bars2 = ax.bar(x+w/2, after, width=w, label="After")

        for bar in list(bars1) + list(bars2):
            height = bar.get_height()
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                height,
                f"{height:.0f}",
                ha="center", va="bottom", fontsize=8
            )

        # ax.set_yscale("log")
        ax.set_title(operation)
        ax.set_xticks(x,depths)
        ax.set_ylabel("Duration / ms")
        ax.set_xlabel("Depth")

        write_path=base_path/f"{db_type}_{coll_type}_{operation}.png"
        fig.savefig(write_path)
        plt.close(fig)


def plot_result(before, after, name: str, depth, w):
    x = np.arange(len(depth))
    fig, ax = plt.subplots()

    ax.bar(x-w/2, before, width=w, label="Before")
    ax.bar(x+w/2, after, width=w, label="After")

    ax.set_title(name)
    ax.set_xticks(x)
    ax.set_xticklabels(depth)

    ax.set_ylabel("Duration / ms")
    ax.set_xlabel("Depth")

    ax.legend(loc="upper right", bbox_to_anchor=(1,-0.1))

    plt.tight_layout()
    # plt.show()

    file_name = get_file_name()
    fig.savefig(file_name)


