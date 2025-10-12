import matplotlib.pyplot as plt
import numpy as np


# a_no_index_s=[190, 125, 151, 152]
# a_w_index_s=[188, 178, 211, 205]

# a_no_index_b=[1621, 1119, 1483, 1714]
# a_w_index_b=[1747, 2011, 2053, 2057]

# s_no_index_b=[117631, 122962, 113479, 127302]
# s_w_index_b=[118685, 130749, 131521, 137839]

alone_flat_no_index_small = [153]
alone_flat_with_index_small = [150]

sharded_flat_no_index_small = [9946]
sharded_flat_with_index_small = [10489]

alone_obj_no_index_small = [153] +[190, 125, 151, 152]
alone_obj_with_index_small = [150] + [188, 178, 211, 205]

sharded_obj_no_index_small = [9946] + [10747, 11411,11865,11531]
sharded_obj_with_index_small = [10489] + [11903,12677,13319,12198]

##big data
alone_flat_no_index_big = [1330]
alone_flat_with_index_big = [1780]

sharded_flat_no_index_big = [118653]
sharded_flat_with_index_big = [119857]

alone_obj_no_index_big = [1330] + [1621, 1119, 1483, 1714]
alone_obj_with_index_big = [1780] + [1747,2011,1053,2057]

sharded_obj_no_index_big = [118653] + [117631, 122962, 113479, 127302]
sharded_obj_with_index_big =[119857] + [118685, 130749, 131521, 137839]

###

# a_flat_no_index_s=[0.15]
# a_flat_with_index_s= [0.15]
#
# a_flat_no_index_b = [1.33]
# a_flat_w_index_b = [1.78]
#
# s_flat_no_index_small = [9.946]
# s_flat_no_index_big = [118]
#
# s_flat_index_small = [10.4]
# s_flat_index_big = [119]
#
# a_no_index_s= a_flat_no_index_s + [0.19, 0.13, 0.15, 0.15]
# a_w_index_s= a_flat_with_index_s + [0.19, 0.18, 0.21, 0.21]
#
# a_no_index_b= a_flat_no_index_b + [1.621, 1.119, 1.483, 1.714]
# a_w_index_b= a_flat_w_index_b + [1.747, 2.011, 2.053, 2.057]
#
# s_no_index_s = s_flat_no_index_small + [10.7, 11.4, 11.8, 11.5]
# s_w_index_s= s_flat_index_small + [11.9, 12.7, 13.3, 12.1]
#
# s_no_index_b= s_flat_no_index_big + [118, 123, 113, 127]
# s_w_index_b= s_flat_index_big + [119, 131, 132, 138]

w = 0.35
x = np.arange(5)
xl=x-w/2
xr=x+w/2

fig, axs = plt.subplots(1,4, sharey=True, constrained_layout=True, figsize=(8,4))

a = axs[0].bar(xl, alone_obj_no_index_small, width=w, label="alone")
b = axs[0].bar(xr, sharded_obj_no_index_small, width=w, label="sharded")

c = axs[1].bar(xl, alone_obj_with_index_small, width=w, label="alone")
d = axs[1].bar(xr, sharded_obj_with_index_small, width=w, label="sharded")

e = axs[2].bar(xl, alone_obj_no_index_big, width=w, label="alone")
f = axs[2].bar(xr, sharded_obj_no_index_big, width=w, label="sharded")

g = axs[3].bar(xl, alone_obj_no_index_big, width=w, label="alone")
h = axs[3].bar(xr, sharded_obj_with_index_big, width=w, label="sharded")

# for bar in list(a) + list(b):
#     height = bar.get_height()
#     axs[0].text(
#         bar.get_x() + bar.get_width() / 2,
#         height,
#         f"{height:.2f}",
#         ha="center", va="bottom", fontsize=8
#     )
#
# for bar in list(c) + list(d):
#     height = bar.get_height()
#     axs[1].text(
#         bar.get_x() + bar.get_width() / 2,
#         height,
#         f"{height:.2f}",
#         ha="center", va="bottom", fontsize=8
#     )
# for bar in list(e) + list(f):
#     height = bar.get_height()
#     axs[2].text(
#         bar.get_x() + bar.get_width() / 2,
#         height,
#         f"{height:.2f}",
#         ha="center", va="bottom", fontsize=8
#     )
#
# for bar in list(g) + list(h):
#     height = bar.get_height()
#     axs[3].text(
#         bar.get_x() + bar.get_width() / 2,
#         height,
#         f"{height:.2f}",
#         ha="center", va="bottom", fontsize=8
#     )

levels = ["flat",1,2,4,8]

axs[0].set_xticks(x, levels)
axs[1].set_xticks(x, levels)
axs[2].set_xticks(x, levels)
axs[3].set_xticks(x, levels)

axs[0].set_ylabel("Duration / ms (log scale)")
axs[0].set_yscale("log")

axs[0].set_xlabel("small data")
axs[1].set_xlabel("small data")
axs[2].set_xlabel("big data")
axs[3].set_xlabel("big data")

axs[0].set_title("no index")
axs[1].set_title("with index")
axs[2].set_title("no index")
axs[3].set_title("with index")

axs[0].legend(loc="lower right", bbox_to_anchor=(0.2,1))

fig.savefig("./mongo_figs/flat_obj_insert_ordered.pdf", bbox_inches="tight")
