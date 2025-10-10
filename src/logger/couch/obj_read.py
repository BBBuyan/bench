import matplotlib.pyplot as plt
import numpy as np

a_read_only = [38, 35, 34, 36]
a_read_after_update = [127, 127, 131, 117]
a_read_after_insert = [91, 94, 88, 89]

alone = a_read_only + a_read_after_update + a_read_after_insert

s_read_only = [29, 29, 32, 31]
s_read_after_update = [101, 119, 105, 113]
s_read_after_insert = [86, 81, 81, 83]

sharded = s_read_only + s_read_after_update + s_read_after_insert

w = 0.35
x = np.arange(4)
xl=x-w/2
xr=x+w/2

categories = ["read", "read after update", "read after insert"]
levels = ["1","2","4","8"]

fig, axs = plt.subplots(1,3, sharey=True, constrained_layout=True, figsize=(10,5))

bar01 = axs[0].bar(xl, a_read_only, width=w, label="alone")
bar02 = axs[0].bar(xr, s_read_only, width=w, label="sharded")

bar11 = axs[1].bar(xl, a_read_after_update, width=w, label="alone")
bar12 = axs[1].bar(xr, s_read_after_update, width=w, label="sharded")

bar21 = axs[2].bar(xl, a_read_after_insert, width=w, label="alone")
bar22 = axs[2].bar(xr, s_read_after_insert, width=w, label="sharded")

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

axs[0].legend(loc="lower right", bbox_to_anchor=(0.2,1))

axs[0].set_title("read only")
axs[1].set_title("read after update")
axs[2].set_title("read after insert")

axs[0].set_xticks(x, levels)
axs[1].set_xticks(x, levels)
axs[2].set_xticks(x, levels)

fig.supxlabel("Depth")
fig.supylabel("Duration / ms")

fig.savefig("./couch_figs/obj_read.pdf", bbox_inches="tight")

