import matplotlib.pyplot as plt
import numpy as np

width = 0.15 
x = np.arange(4)
categories = ["1", "2", "4", "8"]
xl=x-width
xr=x+width

read_no                = [58, 137, 478, 11503]
sort_no                = [59, 226, 3120, 81250]
avg_no                 = [147, 451, 3085, 81478]
update_no              = [142, 342, 1888, 38144]
insert_no              = [15, 14, 64, 979]

read_index                = [6, 16, 89, 8713]
sort_index                = [62, 239, 2214, 79970]
avg_index                 = [136, 471, 3228, 78128]
update_index              = [145, 349, 2477, 41073]
insert_index              = [10, 19, 75, 1851]

read_path                = [3, 6, 31, 1157]
sort_path                = [60, 226, 1769, 82572]
avg_path                 = [149, 443, 3151, 84345]

fig, axs = plt.subplots(1,3,sharey=True, constrained_layout=True, figsize=(8,4))

axs[0].bar(xl, read_no, width=width, label="no index")
axs[0].bar(x, read_index, width=width)
axs[0].bar(xr,read_path , width=width)

axs[1].bar(xl, avg_no, width=width)
axs[1].bar(x, avg_index , width=width, label = "with GIN")
axs[1].bar(xr, avg_path, width=width, label="with jsonb_path_ops")

axs[2].bar(xl, sort_no, width=width)
axs[2].bar(x, sort_index, width=width)
axs[2].bar(xr, sort_path, width=width)

axs[0].set_xticks(x, [1,2,4,8])
axs[1].set_xticks(x, [1,2,4,8])
axs[2].set_xticks(x, [1,2,4,8])

axs[0].set_yscale("log")
axs[0].set_ylabel("Duration / ms (log scale)")

axs[0].set_title("read")
axs[1].set_title("average")
axs[2].set_title("sort")

fig.supxlabel("Depth")

fig.legend(loc="outside upper right", ncol=4)
fig.savefig("./post_figs/arr_read_sort_avg.pdf")
