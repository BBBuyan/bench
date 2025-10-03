import matplotlib.pyplot as plt
import numpy as np

# a_no_index_b=[1621, 1119, 1483, 1714]
# a_no_index_l=[190, 125, 151, 152]
#
# a_w_index_b=[1747, 2011, 2053, 2057]
# a_w_index_l=[188, 178, 211, 205]

a_no_index_l=[0.190, 0.125, 0.151, 0.152]
a_w_index_l=[0.188, 0.178, 0.211, 0.205]

a_w_index_b=[1.747, 2.011, 2.053, 2.057]
a_no_index_b=[1.621, 1.119, 1.483, 1.714]

# s_no_index_b=[117631, 122962, 113479, 127302]
# s_w_index_b=[118685, 130749, 131521, 137839]
#

s_no_index_b=[118, 123, 113, 127]
s_w_index_b=[119, 131, 132, 138]

s_no_index_l=[10.7, 11.4, 11.8, 11.5]
s_w_index_l=[11.9, 12.7, 13.3, 12.1]

w = 0.35
x = np.arange(4)
xl=x-w/2
xr=x+w/2

fig, axs = plt.subplots(2,2, constrained_layout=True, figsize=(12,6))

a = axs[0,0].bar(xl, a_no_index_l, width=w, label="no index")
b = axs[0,0].bar(xr, a_w_index_l, width=w, label="with index")

c= axs[1,0].bar(xl, s_no_index_l, width=w, label="no index")
d= axs[1,0].bar(xr, s_w_index_l, width=w, label="with index")

e= axs[0,1].bar(xl, a_no_index_b, width=w, label="no index")
f= axs[0,1].bar(xr, a_w_index_b, width=w, label="with index")

g= axs[1,1].bar(xl, s_no_index_b, width=w, label="no index")
h= axs[1,1].bar(xr, s_w_index_b, width=w, label="with index")


for bar in list(a) + list(b):
    height = bar.get_height()
    axs[0,0].text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}",
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
        f"{height:.2f}",
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

axs[0,0].set_title("little data")
axs[0,1].set_title("big data")

axs[0,0].set_ylabel("alone")
axs[1,0].set_ylabel("sharded")
axs[0,0].legend(loc="lower right", bbox_to_anchor=(0.2,1))

fig.supylabel("Duration / s")

fig.savefig("./figs/obj_insert.pdf", bbox_inches="tight")
