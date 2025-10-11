import matplotlib.pyplot as plt
import numpy as np


fa_read_only = [37]
fa_read_after_update = [124]
fa_read_after_insert = [82]

fs_read_only = [31]
fs_read_after_update = [115]
fs_read_after_insert = [88]

a_read_only = fa_read_only + [38, 35, 34, 36]
a_read_after_update = fa_read_after_update + [127, 127, 131, 117]
a_read_after_insert = fa_read_after_insert + [91, 94, 88, 89]

s_read_only = fs_read_only + [29, 29, 32, 31]
s_read_after_update = fs_read_after_update + [101, 119, 105, 113]
s_read_after_insert = fs_read_after_insert + [86, 81, 81, 83]


w = 0.35
x = np.arange(5)
xl=x-w/2
xr=x+w/2

fig, axs = plt.subplots(1,3, sharey=True, constrained_layout=True, figsize=(10,5))

bar01 = axs[0].bar(xl, a_read_only, width=w, label="alone")
bar02 = axs[0].bar(xr, s_read_only, width=w, label="sharded")

bar11 = axs[1].bar(xl, a_read_after_update, width=w, label="alone")
bar12 = axs[1].bar(xr, s_read_after_update, width=w, label="sharded")

bar21 = axs[2].bar(xl, a_read_after_insert, width=w, label="alone")
bar22 = axs[2].bar(xr, s_read_after_insert, width=w, label="sharded")


# for bar in list(bar01) + list(bar02):
#     height = bar.get_height()
#     axs[0,0].text(
#         bar.get_x() + bar.get_width() / 2,
#         height,
#         f"{height:.0f}",
#         ha="center", va="bottom", fontsize=8
#     )
#
# for bar in list(bar11) + list(bar12):
#     height = bar.get_height()
#     axs[0,1].text(
#         bar.get_x() + bar.get_width() / 2,
#         height,
#         f"{height:.0f}",
#         ha="center", va="bottom", fontsize=8
#     )
# for bar in list(bar21) + list(bar22):
#     height = bar.get_height()
#     axs[0,2].text(
#         bar.get_x() + bar.get_width() / 2,
#         height,
#         f"{height:.0f}",
#         ha="center", va="bottom", fontsize=8
#     )


levels = ["flat","1","2","4","8"]
axs[0].legend(loc="lower right", bbox_to_anchor=(0.2,1))

axs[0].set_title("read only")
axs[1].set_title("read after update")
axs[2].set_title("read after insert")

axs[0].set_xticks(x, levels)
axs[1].set_xticks(x, levels)
axs[2].set_xticks(x, levels)

axs[0].set_ylabel("Duration / ms")

fig.supxlabel("Depth")

fig.savefig("./couch_figs/flat_obj_read.pdf", bbox_inches="tight")
