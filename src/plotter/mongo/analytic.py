import matplotlib.pyplot as plt
import numpy as np

avg_alone = [992, 75]
group_alone = [632, 73]

avg_shard = [365, 44]
group_shard = [389, 52]

w = 0.2
x = np.arange(2)

fig, axs = plt.subplots(1, 2, sharey=True, constrained_layout=True)

bars_a1 = axs[0].bar(x-w/2, avg_alone, width=w, label="alone")
bars_a2 = axs[0].bar(x+w/2, avg_shard, width=w, label="sharded")

bars_b1 = axs[1].bar(x-w/2, group_alone, width=w, label="alone")
bars_b2 = axs[1].bar(x+w/2, group_shard, width=w, label="sharded")

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

axs[0].set_title("average")
axs[1].set_title("sort")

fig.savefig("./figs/analytic.pdf", bbox_inches="tight")
