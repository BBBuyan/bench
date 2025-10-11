import matplotlib.pyplot as plt
import numpy as np

shard_avg_no_index = [725, 776, 2028, 905]
shard_avg_with_index = [33, 26, 25, 15]

shard_group_no_index = [548, 731, 1130, 1768]
shard_group_with_index =[27, 26, 26, 16]

alone_avg_no_index = [778, 1400, 1310, 2997]
alone_avg_with_index = [67, 40, 52, 69]

alone_group_no_index = [1186, 1292, 1412, 2000]
alone_group_with_index = [62, 48, 67, 60]

w = 0.35
x = np.arange(4)
xl=x-w/2
xr=x+w/2


fig, axs = plt.subplots(2,2, constrained_layout=True, figsize=(12,6))

a = axs[0,0].bar(xl, alone_avg_no_index, width=w, label="no index")
b = axs[0,0].bar(xr, alone_avg_with_index, width=w, label="with index")

c= axs[1,0].bar(xl, shard_avg_no_index,width=w, label="no index")
d= axs[1,0].bar(xr, shard_avg_with_index, width=w, label="with index")

e= axs[0,1].bar(xl, alone_group_no_index, width=w, label="no index")
f= axs[0,1].bar(xr, alone_group_with_index, width=w, label="with index")

g= axs[1,1].bar(xl, shard_group_no_index, width=w, label="no index")
h= axs[1,1].bar(xr, shard_group_with_index, width=w, label="with index")

for bar in list(a) + list(b):
    height = bar.get_height()
    axs[0,0].text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.0f}",
        ha="center", va="bottom", fontsize=8
    )

for bar in list(c) + list(d):
    height = bar.get_height()
    axs[1,0].text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.0f}",
        ha="center", va="bottom", fontsize=8
    )
for bar in list(e) + list(f):
    height = bar.get_height()
    axs[0,1].text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.0f}",
        ha="center", va="bottom", fontsize=8
    )

for bar in list(g) + list(h):
    height = bar.get_height()
    axs[1,1].text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.0f}",
        ha="center", va="bottom", fontsize=8
    )

axs[0,0].set_xticks(x, [1,2,4,8])
axs[0,1].set_xticks(x, [1,2,4,8])
axs[1,0].set_xticks(x, [1,2,4,8])
axs[1,1].set_xticks(x, [1,2,4,8])

axs[0,0].set_title("average")
axs[0,1].set_title("group")

axs[0,0].sharey(axs[0,1])
axs[1,0].sharey(axs[1,1])

axs[0,0].set_ylabel("alone")
axs[1,0].set_ylabel("sharded")

axs[0,0].set_yscale("log")
axs[1,0].set_yscale("log")

axs[0,0].legend(loc="lower right", bbox_to_anchor=(0.2,1))

fig.supylabel("Duration / ms")

fig.savefig("./figs/obj_analytic.pdf", bbox_inches="tight")
