import matplotlib.pyplot as plt
import numpy as np

w = 0.35
x = np.arange(5)
xl=x-w/2
xr=x+w/2

a_flat_read_no_index = [871]
a_flat_read_with_index = [86]

s_flat_read_no_index = [355]
s_flat_read_with_index = [49]
s_flat_read_with_shard_key = [73]

a_obj_read_no_index = [1010, 1067, 1840, 2657]
a_obj_read_with_index = [79,86,73,65]

s_obj_read_no_index = [294,316,354,378]
s_obj_read_with_index = [40,43,39,31]
s_obj_read_with_shard_key = [77,73,69,65]

a_no_index = a_flat_read_no_index + a_obj_read_no_index
a_with_index = a_flat_read_with_index + a_obj_read_with_index

s_no_index = s_flat_read_no_index + s_obj_read_no_index
s_with_index = s_flat_read_with_index + s_obj_read_with_index

shard_key = s_flat_read_with_shard_key + s_obj_read_with_shard_key

fig, axs = plt.subplots(1,3, sharey=True, constrained_layout=True, figsize=(10,5))

bar01 = axs[0].bar(xl, a_no_index, width=w, label="alone")
bar02 = axs[0].bar(xr, s_no_index, width=w, label="sharded")

bar11 = axs[1].bar(xl, a_with_index, width=w, label="alone")
bar12 = axs[1].bar(xr, s_with_index, width=w, label="sharded")

bar21 = axs[2].bar(x, shard_key, width=w, label="alone", color="C1")


for bar in list(bar01) + list(bar02):
    height = bar.get_height()
    axs[0].text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.0f}",
        ha="center", va="bottom", fontsize=8
    )

for bar in list(bar11) + list(bar12):
    height = bar.get_height()
    axs[1].text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.0f}",
        ha="center", va="bottom", fontsize=8
    )
for bar in list(bar21):
    height = bar.get_height()
    axs[2].text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.0f}",
        ha="center", va="bottom", fontsize=8
    )


levels = ["flat","1","2","4","8"]
axs[0].legend(loc="lower right", bbox_to_anchor=(0.2,1))

axs[0].set_yscale("log")

axs[0].set_title("no index")
axs[1].set_title("with index")
axs[2].set_title("by shard key")

axs[0].set_xticks(x, levels)
axs[1].set_xticks(x, levels)
axs[2].set_xticks(x, levels)

axs[0].set_ylabel("Duration / ms (log scale)")

fig.supxlabel("Depth")

fig.savefig("./mongo_figs/flat_obj_read.pdf", bbox_inches="tight")
