import matplotlib.pyplot as plt
import numpy as np

a_update_no_index=[26,47,210,14920]
a_update_w_index=[3,2,20,1532]
a_update_indexed_field=[3,6,27,1833]

s_update_no_index=[16,28,109,1409]
s_update_w_index=[4,5,12,457]
s_update_indexed_field=[6,5,19,606]

update_by_shard_key=[17,33,127,1769]

w = 0.35
x = np.arange(4)
xl=x-w/2
xr=x+w/2

fig, axs = plt.subplots(1,4, sharey=True, constrained_layout=True, figsize=(12,6))

bars01 = axs[0].bar(xl, a_update_no_index, width=w, label="alone")
bars02 = axs[0].bar(xr, s_update_no_index, width=w, label="sharded")

bars11 = axs[1].bar(xl, a_update_w_index, width=w, label="alone")
bars12 = axs[1].bar(xr, s_update_w_index, width=w, label="sharded")

bars21 = axs[2].bar(xl, a_update_indexed_field, width=w, label="alone")
bars22 = axs[2].bar(xr, s_update_indexed_field, width=w, label="sharded")

bars31 = axs[3].bar(x, update_by_shard_key, width=w, label="sharded", color="C1")

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

for bar in list(bars21) + list(bars22):
    height = bar.get_height()
    axs[2].text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.0f}",
        ha="center", va="bottom", fontsize=8
    )

for bar in list(bars31):
    height = bar.get_height()
    axs[3].text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.0f}",
        ha="center", va="bottom", fontsize=8
    )

axs[0].legend(loc="lower right", bbox_to_anchor=(0.2,1))
axs[0].set_yscale("log")

axs[0].set_title("no index")
axs[1].set_title("with index")
axs[2].set_title("update indexed")
axs[3].set_title("shard key")

axs[0].set_xticks(x, [1,2,4,8])
axs[1].set_xticks(x, [1,2,4,8])
axs[2].set_xticks(x, [1,2,4,8])
axs[3].set_xticks(x, [1,2,4,8])

fig.supxlabel("Depth")
fig.supylabel("Duration / ms (log scale)")

fig.savefig("./figs/arr_update.pdf", bbox_inches="tight")
