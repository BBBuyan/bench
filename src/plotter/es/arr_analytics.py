import matplotlib.pyplot as plt
import numpy as np
from resources import *

width = 0.10 
x = np.arange(4)

x1 = x-2*width
x2 = x-width
x3 = x
x4 = x+width
x5 = x+2*width

levels = ["1", "2", "4", "8"]

# Plot bars side-by-side
#
# plt.xticks(x, categories)
# plt.title("Sort Nested Arrays")
# plt.xlabel("Depth")
# plt.ylabel("Duration / ms")
# plt.legend()
# plt.tight_layout()
# plt.savefig("es_figs/arr_sort.pdf")
#

fig, axs = plt.subplots(1,2, constrained_layout=True, sharey=True)

axs[0].bar(x - 2*width, alone_arr_group, width, label='alone')
axs[0].bar(x - width,   s1_arr_group, width, label='s = 1')
axs[0].bar(x,           s3_arr_group, width, label='s = 3')
axs[0].bar(x + width,   s5_arr_group, width, label='s = 5')
axs[0].bar(x + 2*width, s8_arr_group, width, label='s = 8')

axs[1].bar(x - 2*width, alone_arr_avg, width, label='alone')
axs[1].bar(x - width,   s1_arr_avg, width, label='s = 1')
axs[1].bar(x,           s3_arr_avg, width, label='s = 3')
axs[1].bar(x + width,   s5_arr_avg, width, label='s = 5')
axs[1].bar(x + 2*width, s8_arr_avg, width, label='s = 8')

axs[0].legend()

axs[0].set_ylabel("Duration / ms (log scale)")
axs[0].set_yscale("log")

axs[0].set_title("Sort")
axs[1].set_title("Average")

axs[0].set_xticks(x, levels)
axs[1].set_xticks(x, levels)

fig.savefig("./es_figs/arr_analytics.pdf", bbox_inches="tight")
