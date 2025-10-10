import matplotlib.pyplot as plt
import numpy as np

a_sort_only = [53,50,52,49]
a_sort_after_update = [171,176,179,176]
a_sort_after_insert = [121,123,123,126]

s_sort_only = [29,31,30,30]
s_sort_after_update = [99,100,103,101]
s_sort_after_insert = [82,82,81,79]

w = 0.35
x = np.arange(4)
xl=x-w/2
xr=x+w/2

categories_sort = ["sort only", "sort after update", "sort after insert"]
categories_average = ["average only", "average after update", "average after insert"]

fig, axs = plt.subplots(1,3, sharey=True, constrained_layout=True, figsize=(10,5))

bar01 = axs[0].bar(xl, a_sort_only, width=w, label="alone")
bar02 = axs[0].bar(xr, s_sort_only, width=w, label="sharded")

bar11 = axs[1].bar(xl, a_sort_after_update, width=w, label="alone")
bar12 = axs[1].bar(xr, s_sort_after_update, width=w, label="sharded")

bar21 = axs[2].bar(xl, a_sort_after_insert, width=w, label="alone")
bar22 = axs[2].bar(xr, s_sort_after_insert, width=w, label="sharded")

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
    
for bar in list(bar21) + list(bar22):
    height = bar.get_height()
    axs[2].text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.0f}",
        ha="center", va="bottom", fontsize=8
    )

levels = [1,2,4,8]

axs[0].legend(loc="lower right", bbox_to_anchor=(0.2,1))
axs[0].set_xticks(x,levels)
axs[1].set_xticks(x,levels)
axs[2].set_xticks(x,levels)

axs[0].set_title("sort only")
axs[1].set_title("sort after update")
axs[2].set_title("sort after insert")

fig.supylabel("Duration / ms")
fig.supxlabel("Depth")
fig.savefig("./couch_figs/obj_sort.pdf", bbox_inches="tight")
