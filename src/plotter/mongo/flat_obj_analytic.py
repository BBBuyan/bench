import matplotlib.pyplot as plt
import numpy as np

f_a_avg_no_index = [992]
f_a_avg_with_index = [75]

f_s_avg_no_index = [365]
f_s_avg_with_index = [44]

f_a_group_no_index = [632]
f_a_group_with_index = [75]

f_s_group_no_index = [389]
f_s_group_with_index = [52]

alone_group_no_index = f_a_group_no_index + [1186, 1292, 1412, 2000]
shard_group_no_index = f_s_group_no_index + [548, 731, 1130, 1768]

alone_group_with_index = f_a_group_with_index + [62, 48, 67, 60]
shard_group_with_index = f_s_group_with_index + [27, 26, 26, 16]

alone_avg_no_index = f_a_avg_no_index + [778, 1400, 1310, 2997]
shard_avg_no_index = f_s_avg_no_index + [725, 776, 896, 905]

shard_avg_with_index = f_s_avg_with_index + [35,30,34,22]
alone_avg_with_index = f_a_avg_with_index + [67, 40, 52, 69]

w = 0.35
x = np.arange(5)
xl=x-w/2
xr=x+w/2

fig, axs = plt.subplots(1,4, constrained_layout=True, sharey=True, figsize=(8,4))

a = axs[0].bar(xl, alone_avg_no_index, width=w, label="alone")
b = axs[0].bar(xr, shard_avg_no_index, width=w, label="sharded")

c = axs[1].bar(xl, alone_avg_with_index,width=w, label="alone")
d = axs[1].bar(xr, shard_avg_with_index, width=w, label="sharded")

e = axs[2].bar(xl, alone_group_no_index, width=w, label="alone")
f = axs[2].bar(xr, shard_group_no_index, width=w, label="sharded")

g = axs[3].bar(xl, alone_group_with_index,width=w, label="alone")
h = axs[3].bar(xr, shard_group_with_index, width=w, label="sharded")

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

levels = ["flat", 1,2,4,8]
axs[0].set_xticks(x, levels)
axs[1].set_xticks(x, levels)
axs[2].set_xticks(x, levels)
axs[3].set_xticks(x, levels)

axs[0].set_title("no index")
axs[1].set_title("with index")
axs[2].set_title("no index")
axs[3].set_title("with index")

axs[0].set_xlabel("average")
axs[1].set_xlabel("average")
axs[2].set_xlabel("sort")
axs[3].set_xlabel("sort")

axs[0].set_ylabel("Duration / ms (log scale)")

axs[0].set_yscale("log")
axs[0].legend(loc="lower right", bbox_to_anchor=(0.2,1))

fig.savefig("./mongo_figs/flat_obj_analytic.pdf", bbox_inches="tight")
