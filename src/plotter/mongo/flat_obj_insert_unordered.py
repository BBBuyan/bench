import matplotlib.pyplot as plt
import numpy as np

alone_flat_no_index_small = [108]
alone_flat_no_index_big = [1164]
alone_flat_with_index_small = [172]
alone_flat_with_index_big = [1573]

alone_obj_no_index_small = [109, 105, 100, 115]
alone_obj_no_index_big = [1180, 1141, 1296, 1499]
alone_obj_with_index_small = [152,183,208,230]
alone_obj_with_index_big = [1485, 1625, 1912,2020]

alone_arr_no_index_small = [2,3,7,235]
alone_arr_no_index_big = [27,41,87,1832]
alone_arr_with_index_small = [3,4,11,488]
alone_arr_with_index_big = [21,36,180,4220]

sharded_flat_no_index_small = [211]
sharded_flat_no_index_big = [2565]
sharded_flat_with_index_small = [226]
sharded_flat_with_index_big = [3179]

sharded_obj_no_index_small = [200,203,218,234]
sharded_obj_no_index_big = [2844,2433,2093,3585]
sharded_obj_with_index_small = [224,259,277,264]
sharded_obj_with_index_big = [3121,3055,3154,3371]

sharded_arr_no_index_small = [8,10,20,438]
sharded_arr_no_index_big = [36,55,259,4661]
sharded_arr_with_index_small = [8,10,24,528]
sharded_arr_with_index_big = [43,78,305,6034]

w = 0.35
x = np.arange(5)
xl=x-w/2
xr=x+w/2

a_no_index_small = alone_flat_no_index_small + alone_obj_no_index_small
s_no_index_small = sharded_flat_no_index_small + sharded_obj_no_index_small

a_index_small = alone_flat_with_index_small + alone_obj_with_index_small
s_index_small = sharded_flat_with_index_small + sharded_obj_with_index_small 

a_no_index_big = alone_flat_no_index_big + alone_obj_no_index_big
s_no_index_big = sharded_flat_no_index_big + sharded_obj_no_index_big

a_index_big = alone_flat_with_index_big + alone_obj_with_index_big
s_index_big = sharded_flat_with_index_big + sharded_obj_with_index_big 


fig, axs = plt.subplots(1,4, sharey=True, constrained_layout=True, figsize=(8,4))

bars01 = axs[0].bar(xl, a_no_index_small, width=w, label="alone")
bars02 = axs[0].bar(xr, s_no_index_small, width=w, label="sharded")

bars11 = axs[1].bar(xl, a_index_small, width=w, label="alone")
bars12 = axs[1].bar(xr, s_index_small, width=w, label="sharded")

bars21 = axs[2].bar(xl, a_no_index_big, width=w, label="alone")
bars22 = axs[2].bar(xr, s_no_index_big, width=w, label="sharded")

bars31 = axs[3].bar(xl, a_index_big, width=w, label="alone")
bars32 = axs[3].bar(xr, s_index_big, width=w, label="sharded")

levels = ["flat", 1,2,4,8]

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

axs[0].set_xticks(x, levels)
axs[1].set_xticks(x, levels)
axs[2].set_xticks(x, levels)
axs[3].set_xticks(x, levels)

fig.savefig("./mongo_figs/flat_obj_insert_unordered.pdf", bbox_inches="tight")
