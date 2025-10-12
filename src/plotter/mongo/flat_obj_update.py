import matplotlib.pyplot as plt
import numpy as np

flat_a_no_index = [905]
flat_a_with_index = [92]
flat_a_indexed_field = [101]

flat_s_no_index = [395]
flat_s_with_index = [52]
flat_s_indexed_field = [53]
flat_s_by_shard_key = [81]

a_no_index= flat_a_no_index + [1162, 1038, 1126, 3262]
a_w_index=flat_a_with_index + [96, 104, 96, 90]
a_indexed= flat_a_indexed_field + [115, 112, 113, 122]

s_no_index=flat_s_no_index + [439, 409, 518, 637]
s_w_index=flat_s_with_index + [41, 50, 85, 38]
s_indexed= flat_s_indexed_field + [46, 49, 61, 51]
s_shard_key=flat_s_by_shard_key + [91, 83, 90, 90]

w = 0.35
x = np.arange(5)
xl=x-w/2
xr=x+w/2

fig, axs = plt.subplots(1,4, sharey=True, constrained_layout=True, figsize=(8,4))

bars01 = axs[0].bar(xl, a_no_index, width=w, label="alone")
bars02 = axs[0].bar(xr, s_no_index, width=w, label="sharded")

bars11 = axs[1].bar(xl, a_w_index, width=w, label="alone")
bars12 = axs[1].bar(xr, s_w_index, width=w, label="sharded")

bars21 = axs[2].bar(xl, a_indexed, width=w, label="alone")
bars22 = axs[2].bar(xr, s_indexed, width=w, label="sharded")

bars31 = axs[3].bar(x, s_shard_key, width=w, label="sharded", color="C1")

# for bar in list(bars01) + list(bars02):
#     height = bar.get_height()
#     axs[0].text(
#         bar.get_x() + bar.get_width() / 2,
#         height,
#         f"{height:.0f}",
#         ha="center", va="bottom", fontsize=8
#     )
#
# for bar in list(bars11) + list(bars12):
#     height = bar.get_height()
#     axs[1].text(
#         bar.get_x() + bar.get_width() / 2,
#         height,
#         f"{height:.0f}",
#         ha="center", va="bottom", fontsize=8
#     )
#
# for bar in list(bars21) + list(bars22):
#     height = bar.get_height()
#     axs[2].text(
#         bar.get_x() + bar.get_width() / 2,
#         height,
#         f"{height:.0f}",
#         ha="center", va="bottom", fontsize=8
#     )
#
# for bar in list(bars31):
#     height = bar.get_height()
#     axs[3].text(
#         bar.get_x() + bar.get_width() / 2,
#         height,
#         f"{height:.0f}",
#         ha="center", va="bottom", fontsize=8
#     )
#
levels = ["flat", 1,2,4,8]

axs[0].legend(loc="lower right", bbox_to_anchor=(0.2,1))
axs[0].set_yscale("log")

axs[0].set_title("no index")
axs[1].set_title("with index")
axs[2].set_title("update indexed")
axs[3].set_title("shard key")

axs[0].set_ylabel("Duration / ms (log scale)")

axs[0].set_xticks(x, levels)
axs[1].set_xticks(x, levels)
axs[2].set_xticks(x, levels)
axs[3].set_xticks(x, levels)

fig.supxlabel("Depth")

fig.savefig("./mongo_figs/flat_obj_update.pdf", bbox_inches="tight")
