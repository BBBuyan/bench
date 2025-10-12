import matplotlib.pyplot as plt
import numpy as np

alone_arr_no_index_small = [2,3,7,235]
sharded_arr_no_index_small = [8,10,20,438]

alone_arr_with_index_small = [3,4,11,350]
sharded_arr_with_index_small = [8,10,24,528]

alone_arr_no_index_big = [27,41,87,1832]
sharded_arr_no_index_big = [36,55,259,4661]

alone_arr_with_index_big = [21,36,180,4220]
sharded_arr_with_index_big = [43,78,305,6034]

w = 0.35
x = np.arange(4)
xl=x-w/2
xr=x+w/2

fig, axs = plt.subplots(1,4, sharey=True, constrained_layout=True, figsize=(8,4))

bar01 = axs[0].bar(xl, alone_arr_no_index_small, width=w, label="alone")
bar02 = axs[0].bar(xr, sharded_arr_no_index_small, width=w, label="sharded")

bar11 = axs[1].bar(xl, alone_arr_with_index_small, width=w, label="alone")
bar12 = axs[1].bar(xr, sharded_arr_with_index_small, width=w, label="sharded")

bar21 = axs[2].bar(xl, alone_arr_no_index_big, width=w, label="alone")
bar22 = axs[2].bar(xr, sharded_arr_no_index_big, width=w, label="sharded")

bar31 = axs[3].bar(xl, alone_arr_with_index_big, width=w, label="alone")
bar32 = axs[3].bar(xr, sharded_arr_with_index_big, width=w, label="sharded")

# for bar in list(bar01) + list(bar02):
#     height = bar.get_height()
#     axs[0].text(
#         bar.get_x() + bar.get_width() / 2,
#         height,
#         f"{height:.0f}",
#         ha="center", va="bottom", fontsize=5
#     )
#
# for bar in list(bar11) + list(bar12):
#     height = bar.get_height()
#     axs[1].text(
#         bar.get_x() + bar.get_width() / 2,
#         height,
#         f"{height:.0f}",
#         ha="center", va="bottom", fontsize=5
#     )
# for bar in list(bar21) + list(bar22):
#     height = bar.get_height()
#     axs[2].text(
#         bar.get_x() + bar.get_width() / 2,
#         height,
#         f"{height:.0f}",
#         ha="center", va="bottom", fontsize=5
#     )
# for bar in list(bar31) + list(bar32):
#     height = bar.get_height()
#     axs[3].text(
#         bar.get_x() + bar.get_width() / 2,
#         height,
#         f"{height:.0f}",
#         ha="center", va="bottom", fontsize=5
#     )

levels = [1,2,4,8]

axs[0].legend(loc="lower right", bbox_to_anchor=(0.2,1))
axs[0].set_yscale("log")

axs[0].set_title("no index")
axs[1].set_title("with index")
axs[2].set_title("no index")
axs[3].set_title("with index")

axs[0].set_ylabel("Duration / ms (log scale)")

axs[0].set_xlabel("small data")
axs[1].set_xlabel("small data")
axs[2].set_xlabel("big data")
axs[3].set_xlabel("big data")

axs[0].set_title("no index")
axs[1].set_title("with index")
axs[2].set_title("no index")
axs[3].set_title("with index")

axs[0].set_xticks(x, levels)
axs[1].set_xticks(x, levels)
axs[2].set_xticks(x, levels)
axs[3].set_xticks(x, levels)

fig.savefig("./mongo_figs/arr_insert_unordered.pdf", bbox_inches="tight")
