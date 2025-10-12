import matplotlib.pyplot as plt
import numpy as np

# a_no_index_b=[1621, 1119, 1483, 1714]
# a_no_index_s=[190, 125, 151, 152]
#
# a_w_index_b=[1747, 2011, 2053, 2057]
# a_w_index_s=[188, 178, 211, 205]

# a_no_index_s=[0.190, 0.125, 0.151, 0.152]
# a_w_index_s=[0.188, 0.178, 0.211, 0.205]

a_no_index_s=[0.19, 0.13, 0.15, 0.15]
a_w_index_s=[0.19, 0.18, 0.21, 0.21]

a_w_index_b=[1.747, 2.011, 2.053, 2.057]
a_no_index_b=[1.621, 1.119, 1.483, 1.714]

# s_no_index_b=[117631, 122962, 113479, 127302]
# s_w_index_b=[118685, 130749, 131521, 137839]
#

s_no_index_b=[118, 123, 113, 127]
s_w_index_b=[119, 131, 132, 138]

s_no_index_s = [10.7, 11.4, 11.8, 11.5]
s_w_index_s=[11.9, 12.7, 13.3, 12.1]

w = 0.35
x = np.arange(4)
xl=x-w/2
xr=x+w/2

fig, axs = plt.subplots(1,4, sharey=True, constrained_layout=True, figsize=(8,4))

a = axs[0].bar(xl, a_no_index_s, width=w, label="alone")
b = axs[0].bar(xr, s_no_index_s, width=w, label="sharded")

c = axs[1].bar(xl, a_w_index_s, width=w, label="alone")
d = axs[1].bar(xr, s_w_index_s, width=w, label="sharded")

e = axs[2].bar(xl, a_no_index_b, width=w, label="alone")
f = axs[2].bar(xr, s_no_index_b, width=w, label="sharded")

g = axs[3].bar(xl, a_w_index_b, width=w, label="alone")
h = axs[3].bar(xr, s_w_index_b, width=w, label="sharded")

for bar in list(a) + list(b):
    height = bar.get_height()
    axs[0].text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}",
        ha="center", va="bottom", fontsize=8
    )

for bar in list(c) + list(d):
    height = bar.get_height()
    axs[1].text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}",
        ha="center", va="bottom", fontsize=8
    )
for bar in list(e) + list(f):
    height = bar.get_height()
    axs[2].text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}",
        ha="center", va="bottom", fontsize=8
    )

for bar in list(g) + list(h):
    height = bar.get_height()
    axs[3].text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.2f}",
        ha="center", va="bottom", fontsize=8
    )

axs[0].set_xticks(x, [1,2,4,8])
axs[1].set_xticks(x, [1,2,4,8])
axs[2].set_xticks(x, [1,2,4,8])
axs[3].set_xticks(x, [1,2,4,8])

axs[0].set_ylabel("Duration / s")
axs[0].set_yscale("log")

axs[0].set_title("small data")
axs[1].set_title("small data")
axs[2].set_title("big data")
axs[3].set_title("big data")

# axs[0].set_ylabel("alone")
# axs[0].set_ylabel("sharded")
axs[0].legend(loc="lower right", bbox_to_anchor=(0.2,1))

fig.savefig("./mongo_figs/obj_insert_ordered.pdf", bbox_inches="tight")
