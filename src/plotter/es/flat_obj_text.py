import matplotlib.pyplot as plt
import numpy as np
from resources import *

width = 0.15 
x = np.arange(5)

x1 = x-2*width
x2 = x-width
x3 = x
x4 = x+width
x5 = x+2*width

levels = ["flat","1", "2", "4", "8"]

fig, axs = plt.subplots(1,2, constrained_layout=True, sharey=True, figsize=(6,4))

axs[0].bar(x - 2*width, alone_obj_info, width, label='alone')
axs[0].bar(x - width,   s1_obj_info, width, label='s = 1')
axs[0].bar(x,           s3_obj_info, width, label='s = 3')
axs[0].bar(x + width,   s5_obj_info, width, label='s = 5')
axs[0].bar(x + 2*width, s8_obj_info, width, label='s = 8')

axs[1].bar(x - 2*width, alone_obj_description, width)
axs[1].bar(x - width,   s1_obj_description, width)
axs[1].bar(x,           s3_obj_description, width)
axs[1].bar(x + width,   s5_obj_description, width)
axs[1].bar(x + 2*width, s8_obj_description, width)

axs[0].set_ylabel("Duration / ms")

axs[0].set_title("info")
axs[1].set_title("description")

axs[0].set_xticks(x, levels)
axs[1].set_xticks(x, levels)

fig.legend(ncol=5,loc="lower left", bbox_to_anchor=(0,1))

fig.savefig("./es_figs/obj_text.pdf", bbox_inches="tight")


