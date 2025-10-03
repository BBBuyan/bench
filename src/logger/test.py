import matplotlib.pyplot as plt
import numpy as np

shard_insert_small_no_index = [9946]
shard_insert_small_index = [10489]

shard_insert_big_no_index = [118653]
shard_insert_big_index = [119857]

alone_insert_small_no_index = [153]
alone_insert_small_index = [145]

alone_insert_big_no_index = [1337]
alone_insert_big_index = [1781]

w = 0.2
x = np.arange(2)

fig, axs = plt.subplots(1, 2, sharey=True, constrained_layout=True)

alone_small = [153, 145]
alone_big = [1337, 1781]

shard_small = [9946, 10489]
shard_big= [118653, 119857]

bars_a1 = axs[0].bar(x-w/2, alone_small, width=w, label="alone")
bars_a2 = axs[0].bar(x+w/2, shard_small, width=w, label="sharded")

bars_b1 = axs[1].bar(x-w/2, alone_big, width=w, label="alone")
bars_b2 = axs[1].bar(x+w/2, shard_big, width=w, label="sharded")

for bar in list(bars_a1) + list(bars_a2):
    height = bar.get_height()
    axs[0].text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.0f}",
        ha="center", va="bottom", fontsize=8
    )

for bar in list(bars_b1) + list(bars_b2):
    height = bar.get_height()
    axs[1].text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.0f}",
        ha="center", va="bottom", fontsize=8
    )

axs[0].legend(loc="lower right", bbox_to_anchor=(0.2,1))
axs[0].set_yscale("log")
axs[0].set_ylabel("Duration / ms (log scale)")

axs[0].set_xticks(x, ["no index", "with index"])
axs[1].set_xticks(x, ["no index", "with index"])

axs[0].set_title("insert small data")
axs[1].set_title("insert big data")

fig.savefig("./figs/insert.pdf", bbox_inches="tight")
