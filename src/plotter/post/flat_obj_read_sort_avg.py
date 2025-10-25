import matplotlib.pyplot as plt
import numpy as np

width = 0.15 
x = np.arange(5)
categories = ["flat","1", "2", "4", "8"]

f_read_no                = [451]
f_sort_no                = [444]
f_avg_no                 = [451]

f_read_arrow                = [30]
f_sort_arrow                = [20]
f_avg_arrow                 = [32]

f_read_index                = [102]
f_sort_index                = [149]
f_avg_index                 = [155]

f_read_path                = [46]
f_sort_path                = [46]
f_avg_path                 = [47]

read_no                =f_read_no  +[489, 7461, 9225, 10284]
sort_no                =f_sort_no  +[483, 7426, 3267, 10207]
avg_no                 =f_avg_no   +[4167, 8529, 2314, 10227]

read_index                =f_read_index  + [193, 265, 376, 709]
sort_index                =f_sort_index  + [219, 328, 340, 213]
avg_index                 =f_avg_index   + [260, 312, 311, 522]

read_arrow                =f_read_arrow  + [7, 18, 39, 39]
sort_arrow                =f_sort_arrow  + [12, 15, 23, 23]
avg_arrow                 =f_avg_arrow   + [5, 15, 39, 39]

read_path                = f_read_path + [62, 65, 65, 59]
sort_path                = f_sort_path + [60, 64, 32, 31]
avg_path                 = f_avg_path  + [65, 60, 62, 58]

fig, axs = plt.subplots(1,3,sharey=True, constrained_layout=True, figsize=(8,4))

axs[0].bar(x - 1.5*width , read_no, width, label='no index')
axs[0].bar(x - 0.5*width , read_index, width)
axs[0].bar(x + 0.5*width , read_path, width)
axs[0].bar(x + 1.5*width , read_arrow, width)

axs[1].bar(x - 1.5*width , avg_no, width)
axs[1].bar(x - 0.5*width , avg_index, width, label='with GIN')
axs[1].bar(x + 0.5*width , avg_path, width,)
axs[1].bar(x + 1.5*width , avg_arrow, width)

axs[2].bar(x - 1.5*width , sort_no, width)
axs[2].bar(x - 0.5*width , sort_index, width)
axs[2].bar(x + 0.5*width , sort_path, width, label='with jsonb_path_ops')
axs[2].bar(x + 1.5*width , sort_arrow, width, label='with BTREE')

axs[0].set_xticks(x, categories)
axs[1].set_xticks(x, categories)
axs[2].set_xticks(x, categories)

axs[0].set_title("read")
axs[1].set_title("average")
axs[2].set_title("sort")

axs[0].set_yscale("log")
axs[0].set_ylabel("Duration / ms (log scale)")
fig.supxlabel("Depth")

fig.legend(loc="outside upper right", ncol=4)
fig.savefig("./post_figs/flat_obj_read_sort_avg.pdf")
