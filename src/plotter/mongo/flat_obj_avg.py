import matplotlib.pyplot as plt
import numpy as np

f_a_avg_no_index = [992]
f_a_avg_with_index = [75]

f_s_avg_no_index = [365]
f_s_avg_with_index = [44]

shard_avg_no_index = f_s_avg_no_index + [725, 776, 2028, 905]
shard_avg_with_index = f_s_avg_with_index + [33, 26, 25, 15]

alone_avg_no_index = f_a_avg_no_index + [778, 1400, 1310, 2997]
alone_avg_with_index = f_a_avg_with_index + [67, 40, 52, 69]

w = 0.35
x = np.arange(5)
xl=x-w/2
xr=x+w/2

fig, axs = plt.subplots(1,2, constrained_layout=True, sharey=True, figsize=(10,5))

a = axs[0].bar(xl, alone_avg_no_index, width=w, label="alone")
b = axs[0].bar(xr, shard_avg_no_index, width=w, label="sharded")

c = axs[1].bar(xl, alone_avg_with_index,width=w, label="alone")
d = axs[1].bar(xr, shard_avg_with_index, width=w, label="sharded")

for bar in list(a) + list(b):
    height = bar.get_height()
    axs[0].text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.0f}",
        ha="center", va="bottom", fontsize=8
    )

for bar in list(c) + list(d):
    height = bar.get_height()
    axs[1].text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.0f}",
        ha="center", va="bottom", fontsize=8
    )

levels = ["flat", 1,2,4,8]
axs[0].set_xticks(x, levels)
axs[1].set_xticks(x, levels)

axs[0].set_title("no index")
axs[1].set_title("with index")

axs[0].set_ylabel("Duration / ms (log scale)")

axs[0].set_yscale("log")
axs[0].legend(loc="lower right", bbox_to_anchor=(0.2,1))

fig.supxlabel("Depth")

fig.savefig("./mongo_figs/flat_obj_avg.pdf", bbox_inches="tight")
