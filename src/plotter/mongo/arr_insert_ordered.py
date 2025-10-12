import matplotlib.pyplot as plt
import numpy as np

# a_no_index_s=[2,3,19,216]
# a_no_index_b=[11,24,168,3363]
#
# a_w_index_s=[3,4,24,422]
# a_w_index_b=[34,31,352,3926]
#
# s_no_index_s=[7,9,20,478]
# s_no_index_b=[36,67,293,4514]
#
# s_w_index_s=[8,9,24,683]
# s_w_index_b=[38,79,335,6198]

alone_no_index_small = [2,3,19,216]
shard_no_index_small = [7,9,20,478]

alone_with_index_small = [3,4,24,422]
shard_with_index_small = [8,9,25,683]

alone_no_index_big = [11,24,168,3363]
shard_no_index_big = [36,67,293,4514]


alone_with_index_big = [34,31,352,3926]
shard_with_index_big = [38,79,335,6198]

w = 0.35
x = np.arange(4)
xl=x-w/2
xr=x+w/2

fig, axs = plt.subplots(1,4,sharey=True, constrained_layout=True, figsize=(8,4))

a = axs[0].bar(xl, alone_no_index_small, width=w, label="alone")
b = axs[0].bar(xr, shard_no_index_small, width=w, label="sharded")

c = axs[1].bar(xl, alone_with_index_small, width=w, label="alone")
d = axs[1].bar(xr, shard_with_index_small, width=w, label="sharded")

e = axs[2].bar(xl, alone_no_index_big, width=w, label="alone")
f = axs[2].bar(xr, shard_no_index_big, width=w, label="sharded")

g = axs[3].bar(xl, alone_with_index_big, width=w, label="alone")
h = axs[3].bar(xr, shard_with_index_big, width=w, label="sharded")

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
# for bar in list(e) + list(f):
#     height = bar.get_height()
#     axs[2].text(
#         bar.get_x() + bar.get_width() / 2,
#         height,
#         f"{height:.0f}",
#         ha="center", va="bottom", fontsize=8
#     )
#
# for bar in list(g) + list(h):
#     height = bar.get_height()
#     axs[3].text(
#         bar.get_x() + bar.get_width() / 2,
#         height,
#         f"{height:.0f}",
#         ha="center", va="bottom", fontsize=8
#     )

axs[0].set_xticks(x, [1,2,4,8])
axs[1].set_xticks(x, [1,2,4,8])
axs[2].set_xticks(x, [1,2,4,8])
axs[3].set_xticks(x, [1,2,4,8])

axs[0].set_yscale("log")

axs[0].set_title("no index")
axs[1].set_title("with index")
axs[2].set_title("no index")
axs[3].set_title("with index")

axs[0].set_xlabel("small data")
axs[1].set_xlabel("small data")
axs[2].set_xlabel("big data")
axs[3].set_xlabel("big data")

axs[0].set_ylabel("Duration / ms (log scale)")

axs[0].legend(loc="lower right", bbox_to_anchor=(0.2,1))

fig.savefig("./mongo_figs/arr_insert_ordered.pdf", bbox_inches="tight")
