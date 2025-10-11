import matplotlib.pyplot as plt
import numpy as np

a_sort_only = [48]
a_sort_after_update = [179]
a_sort_after_insert = [128]
alone_sort = a_sort_only + a_sort_after_update + a_sort_after_insert

s_sort_only = [30]
s_sort_after_update = [103]
s_sort_after_insert = [81]
sharded_sort = s_sort_only + s_sort_after_update + s_sort_after_insert

a_read_only = [37]
a_read_after_update = [124]
a_read_after_insert = [82]
alone = a_read_only + a_read_after_update + a_read_after_insert

s_read_only = [31]
s_read_after_update = [115]
s_read_after_insert = [88]
sharded = s_read_only + s_read_after_update + s_read_after_insert

w = 0.35
x = np.arange(3)
xl=x-w/2
xr=x+w/2

categories_sort = ["sort only", "after update", "after insert"]
categories = ["read only", "after update", "after insert"]

fig, axs = plt.subplots(1,2, sharey=True, constrained_layout=True, figsize=(8,5))

bar11 = axs[0].bar(xl, alone, width=w, label="alone")
bar12 = axs[0].bar(xr, sharded, width=w, label="sharded")

bar01 = axs[1].bar(xl, alone_sort, width=w, label="alone")
bar02 = axs[1].bar(xr, sharded_sort, width=w, label="sharded")

for bar in list(bar01) + list(bar02):
    height = bar.get_height()
    axs[1].text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.0f}",
        ha="center", va="bottom", fontsize=8
    )

for bar in list(bar11) + list(bar12):
    height = bar.get_height()
    axs[0].text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.0f}",
        ha="center", va="bottom", fontsize=8
    )

axs[0].legend(loc="lower right", bbox_to_anchor=(0.2,1))
axs[0].set_xticks(x,categories)
axs[1].set_xticks(x,categories_sort)

axs[0].set_title("read")
axs[1].set_title("sort")

fig.supylabel("Duration / ms")

fig.savefig("./couch_figs/flat_mango.pdf", bbox_inches="tight")
