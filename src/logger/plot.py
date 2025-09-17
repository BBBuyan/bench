import matplotlib.pyplot as plt
import numpy as np
import os


def get_file_name():
    i = 1
    while os.path.exists(f"img_{i}.png"):
        i+=1

    return f"img_{i}.png"

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

    file_name = get_file_name()
    fig.savefig(file_name)
