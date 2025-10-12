import matplotlib.pyplot as plt
import numpy as np

shard_avg_no_index =[81, 167, 561, 4764]
shard_avg_with_index = [106, 255, 989, 4895]

shard_group_no_index = [46, 94, 462, 8096]
shard_group_with_index =[48, 118, 468, 5131]

alone_avg_no_index = [149, 265, 1316, 32020]#[38, 93, 445, 22521]
alone_avg_with_index = [74, 218, 1293, 23623]#[41, 90, 461, 29055]

alone_group_no_index = [128, 253, 1186, 28897]#[82, 168, 898, 31421]
alone_group_with_index = [80, 174, 788, 28114]#[81, 177, 908, 31730]

w = 0.35
x = np.arange(4)
xl=x-w/2
xr=x+w/2

fig, axs = plt.subplots(1,4, constrained_layout=True, sharey=True, figsize=(8,4))

axs[0].bar(xl, alone_avg_no_index, width=w, label="alone")
axs[0].bar(xr, shard_avg_no_index, width=w, label="sharded")

axs[1].bar(xl, alone_avg_with_index, width=w, label="alone")
axs[1].bar(xr, shard_avg_with_index, width=w, label="sharded")

axs[2].bar(xl, alone_group_no_index, width=w, label="alone")
axs[2].bar(xr, shard_group_no_index, width=w, label="sharded")

axs[3].bar(xl, alone_group_with_index, width=w, label="alone")
axs[3].bar(xr, shard_group_with_index, width=w, label="sharded")

# for bar in list(a) + list(b):
#     height = bar.get_height()
#     axs[0].text(
#         bar.get_x() + bar.get_width() / 2,
#         height,
#         f"{height:.0f}",
#         ha="center", va="bottom", fontsize=8
#     )
#
# for bar in list(c) + list(d):
#     height = bar.get_height()
#     axs[1].text(
#         bar.get_x() + bar.get_width() / 2,
#         height,
#         f"{height:.0f}",
#         ha="center", va="bottom", fontsize=8
#     )

axs[0].set_xticks(x, [1,2,4,8])
axs[1].set_xticks(x, [1,2,4,8])
axs[2].set_xticks(x, [1,2,4,8])
axs[3].set_xticks(x, [1,2,4,8])

axs[0].set_xlabel("average")
axs[1].set_xlabel("average")
axs[2].set_xlabel("sort")
axs[3].set_xlabel("sort")

axs[0].set_title("no index")
axs[1].set_title("with index")
axs[2].set_title("no index")
axs[3].set_title("with index")

axs[0].set_ylabel("Duration / ms (log scale)")
axs[0].set_yscale("log")

axs[0].legend(loc="lower right", bbox_to_anchor=(0.2,1))

fig.savefig("./mongo_figs/arr_analytic.pdf", bbox_inches="tight")
