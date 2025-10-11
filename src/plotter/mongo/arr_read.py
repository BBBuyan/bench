import matplotlib.pyplot as plt
import numpy as np

a_read_wo_index = [22, 49, 198, 13312]
a_read_w_index = [4,7,14,871]

s_read_wo_index = [15,28,111,1628]
s_read_w_index = [2,3,5,134]

w = 0.35
x = np.arange(4)
xl=x-w/2
xr=x+w/2

fig, axs = plt.subplots(1,2, sharey=True, constrained_layout=True, figsize=(8,5))

bars01 = axs[0].bar(xl, a_read_wo_index, width=w, label="alone")
bars02 = axs[0].bar(xr, s_read_wo_index, width=w, label="sharded")

bars11 = axs[1].bar(xl, a_read_w_index, width=w, label="alone")
bars12 = axs[1].bar(xr, s_read_w_index, width=w, label="sharded")

for bar in list(bars01) + list(bars02):
    height = bar.get_height()
    axs[0].text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.0f}",
        ha="center", va="bottom", fontsize=8
    )

for bar in list(bars11) + list(bars12):
    height = bar.get_height()
    axs[1].text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.0f}",
        ha="center", va="bottom", fontsize=8
    )

axs[0].legend(loc="lower right", bbox_to_anchor=(0.2,1))
axs[0].set_yscale("log")

axs[0].set_title("no index")
axs[1].set_title("with index")

axs[0].set_xticks(x, [1,2,4,8])
axs[1].set_xticks(x, [1,2,4,8])

fig.supxlabel("Depth")
fig.supylabel("Duration / ms (log scale)")

fig.savefig("./mongo_figs/arr_read.pdf", bbox_inches="tight")
