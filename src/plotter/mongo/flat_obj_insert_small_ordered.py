import matplotlib.pyplot as plt
import numpy as np

alone_flat_no_index_ordered = [153]
alone_flat_with_index_ordered = [150]

sharded_flat_no_index_ordered = [9946]
sharded_flat_with_index_ordered = [10489]

alone_obj_no_index_ordered = [190, 125, 151, 152]
alone_obj_with_index_ordered = [188, 178, 211, 205]

sharded_obj_no_index_ordered = [10747, 11411,11865,11531]
sharded_obj_with_index_ordered = [11903,12677,13319,12198]

alone_no_index = alone_flat_no_index_ordered + alone_obj_no_index_ordered
alone_with_index = alone_flat_with_index_ordered + alone_obj_with_index_ordered

sharded_no_index = sharded_flat_no_index_ordered + sharded_obj_no_index_ordered
sharded_with_index = sharded_flat_with_index_ordered + sharded_obj_with_index_ordered

w = 0.35
x = np.arange(5)
xl=x-w/2
xr=x+w/2


fig, axs = plt.subplots(
    1
    , 2
    , sharey=True
    , constrained_layout=True
    , figsize=(8,4)
)

a = axs[0].bar(xl, alone_no_index, width=w, label="alone")
b = axs[0].bar(xr, sharded_no_index, width=w, label="sharded")

c = axs[1].bar(xl, alone_with_index, width=w, label="alone")
d = axs[1].bar(xr, sharded_with_index, width=w, label="sharded")

levels = ["flat",1,2,4,8]

axs[0].set_xticks(x, levels)
axs[1].set_xticks(x, levels)

axs[0].set_title("no index")
axs[1].set_title("with index")

axs[0].set_ylabel("Duration / ms")
axs[0].legend(loc="lower right", bbox_to_anchor=(0.2,1))

fig.supxlabel("Ordered Insert")

fig.savefig("./mongo_figs/flat_obj_insert_small_ordered.pdf", bbox_inches="tight")
