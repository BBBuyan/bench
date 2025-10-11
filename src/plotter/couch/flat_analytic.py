import matplotlib.pyplot as plt
import numpy as np

a_sort_only = [48]
a_sort_after_update = [179]
a_sort_after_insert = [128]
alone_sort = a_sort_only + a_sort_after_update + a_sort_after_insert

a_avg_only = [8]
a_avg_after_update = [137]
a_avg_after_insert = [94]
alone_avg = a_avg_only + a_avg_after_update + a_avg_after_insert

s_sort_only = [30]
s_sort_after_update = [103]
s_sort_after_insert = [81]

sharded_sort = s_sort_only + s_sort_after_update + s_sort_after_insert

s_avg_only = [10]
s_avg_after_update = [84]
s_avg_after_insert = [71]

sharded_avg = s_avg_only + s_avg_after_update + s_avg_after_insert

w = 0.35
x = np.arange(3)
xl=x-w/2
xr=x+w/2

categories_sort = ["sort only", "after update", "after insert"]
categories_average = ["average only", "after update", "after insert"]

fig, axs = plt.subplots(1,2, sharey=True, constrained_layout=True, figsize=(10,5))

bar01 = axs[0].bar(xl, alone_sort, width=w, label="alone")
bar02 = axs[0].bar(xr, sharded_sort, width=w, label="sharded")

bar11 = axs[1].bar(xl, alone_avg, width=w, label="alone")
bar12 = axs[1].bar(xr, sharded_avg, width=w, label="sharded")

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

axs[0].legend(loc="lower right", bbox_to_anchor=(0.2,1))
axs[0].set_xticks(x,categories_sort)
axs[1].set_xticks(x,categories_average)

axs[0].set_title("sort")
axs[1].set_title("average")

fig.supylabel("Duration / ms")

fig.savefig("./couch_figs/flat_analytics.pdf", bbox_inches="tight")

