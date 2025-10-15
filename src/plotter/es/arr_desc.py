import matplotlib.pyplot as plt
import numpy as np
from resources import *

width = 0.15 
x = np.arange(4)
categories = ["1", "2", "4", "8"]

# Plot bars side-by-side
plt.bar(x - 2*width, alone_arr_description, width, label='alone')
plt.bar(x - width,   s1_arr_description, width, label='s = 1')
plt.bar(x,           s3_arr_description, width, label='s = 3')
plt.bar(x + width,   s5_arr_description, width, label='s = 5')
plt.bar(x + 2*width, s8_arr_description, width, label='s = 8')

plt.xticks(x, categories)
plt.title("Search long text")
plt.xlabel("Depth")
plt.ylabel("Duration / ms")
plt.legend()
plt.tight_layout()
plt.savefig("es_figs/arr_desc.pdf")
