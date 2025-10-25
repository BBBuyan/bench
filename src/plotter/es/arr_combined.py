import matplotlib.pyplot as plt
import numpy as np
from resources import *

width = 0.15 
x = np.arange(4)

x1 = x-2*width
x2 = x-width
x3 = x
x4 = x+width
x5 = x+2*width

levels = ["1", "2", "4", "8"]

fig, axs = plt.subplots(1,3, constrained_layout=True, sharey=True, figsize=(8,4))

axs[0].bar(x - 2*width, alone_arr_read, width, label='alone')
axs[0].bar(x - width,   s1_arr_read, width, label='s = 1')
axs[0].bar(x,           s3_arr_read, width, label='s = 3')
axs[0].bar(x + width,   s5_arr_read, width, label='s = 5')
axs[0].bar(x + 2*width, s8_arr_read, width, label='s = 8')

axs[1].bar(x - 2*width, alone_arr_avg, width)
axs[1].bar(x - width,   s1_arr_avg, width)
axs[1].bar(x,           s3_arr_avg, width)
axs[1].bar(x + width,   s5_arr_avg, width)
axs[1].bar(x + 2*width, s8_arr_avg, width)

axs[2].bar(x - 2*width, alone_arr_group, width)
axs[2].bar(x - width,   s1_arr_group, width)
axs[2].bar(x,           s3_arr_group, width)
axs[2].bar(x + width,   s5_arr_group, width)
axs[2].bar(x + 2*width, s8_arr_group, width)


axs[0].set_ylabel("Duration / ms (log scale)")
axs[0].set_yscale("log")

axs[0].set_title("read")
axs[1].set_title("average")
axs[2].set_title("sort")

axs[0].set_xticks(x, levels)
axs[1].set_xticks(x, levels)
axs[2].set_xticks(x, levels)

fig.legend(ncol=5,loc="lower left", bbox_to_anchor=(0,1))

fig.savefig("./es_figs/arr_combined.pdf", bbox_inches="tight")
