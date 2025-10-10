import matplotlib.pyplot as plt
import numpy as np

a_avg_only = [7,7,7,7]
a_avg_after_update = [138,132,131,142]
a_avg_after_insert = [91,97,95,98]

s_avg_only = [10,9,9,9]
s_avg_after_update = [85,88,88,91]
s_avg_after_insert = [70,69,65,70]

w = 0.35
x = np.arange(4)
xl=x-w/2
xr=x+w/2

fig, axs = plt.subplots(1,3, sharey=True, constrained_layout=True, figsize=(10,5))

bar01 = axs[0].bar(xl, a_avg_only, width=w, label="alone")
bar02 = axs[0].bar(xr, s_avg_only, width=w, label="sharded")

bar11 = axs[1].bar(xl, a_avg_after_update, width=w, label="alone")
bar12 = axs[1].bar(xr, s_avg_after_update, width=w, label="sharded")

bar21 = axs[2].bar(xl, a_avg_after_insert, width=w, label="alone")
bar22 = axs[2].bar(xr, s_avg_after_insert, width=w, label="sharded")

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

axs[0].set_title("average only")
axs[1].set_title("average after update")
axs[2].set_title("average after insert")

fig.supylabel("Duration / ms")
fig.supxlabel("Depth")
fig.savefig("./couch_figs/obj_avg.pdf", bbox_inches="tight")
