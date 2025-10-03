import matplotlib.pyplot as plt
import numpy as np

a_no_index_s=[2,3,19,216]
a_w_index_s=[3,4,24,422]

a_no_index_b=[11,24,168,3363]
a_w_index_b=[34,31,352,3926]


s_no_index_s=[8,12,52,590]
s_w_index_s=[26,11,26,657]

s_no_index_b=[34,47,281,5742]
s_w_index_b=[47,76,392,6913]


w = 0.35
x = np.arange(4)
xl=x-w/2
xr=x+w/2

fig, axs = plt.subplots(2,2, constrained_layout=True, figsize=(12,6))

a = axs[0,0].bar(xl, a_no_index_s, width=w, label="no index")
b = axs[0,0].bar(xr, a_w_index_s, width=w, label="with index")

c= axs[1,0].bar(xl, s_no_index_s, width=w, label="no index")
d= axs[1,0].bar(xr, s_w_index_s, width=w, label="with index")

e= axs[0,1].bar(xl, a_no_index_b, width=w, label="no index")
f= axs[0,1].bar(xr, a_w_index_b, width=w, label="with index")

g= axs[1,1].bar(xl, s_no_index_b, width=w, label="no index")
h= axs[1,1].bar(xr, s_w_index_b, width=w, label="with index")


for bar in list(a) + list(b):
    height = bar.get_height()
    axs[0,0].text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.0f}",
        ha="center", va="bottom", fontsize=8
    )

for bar in list(c) + list(d):
    height = bar.get_height()
    axs[1,0].text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.0f}",
        ha="center", va="bottom", fontsize=8
    )
for bar in list(e) + list(f):
    height = bar.get_height()
    axs[0,1].text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.0f}",
        ha="center", va="bottom", fontsize=8
    )

for bar in list(g) + list(h):
    height = bar.get_height()
    axs[1,1].text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.0f}",
        ha="center", va="bottom", fontsize=8
    )

axs[0,0].set_xticks(x, [1,2,4,8])
axs[0,1].set_xticks(x, [1,2,4,8])
axs[1,0].set_xticks(x, [1,2,4,8])
axs[1,1].set_xticks(x, [1,2,4,8])

axs[0,0].sharey(axs[0,1])
axs[1,0].sharey(axs[1,1])

axs[0,0].set_yscale("log")
axs[1,0].set_yscale("log")

axs[0,0].set_title("little data")
axs[0,1].set_title("big data")

axs[0,0].set_ylabel("alone")
axs[1,0].set_ylabel("sharded")
axs[0,0].legend(loc="lower right", bbox_to_anchor=(0.2,1))

fig.supylabel("Duration / ms")

fig.savefig("./figs/arr_insert.pdf", bbox_inches="tight")
