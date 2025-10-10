import matplotlib.pyplot as plt
import numpy as np

a_read_only = [37]
a_read_after_update = [124]
a_read_after_insert = [82]

alone = a_read_only + a_read_after_update + a_read_after_insert

s_read_only = [31]
s_read_after_update = [115]
s_read_after_insert = [88]

sharded = s_read_only + s_read_after_update + s_read_after_insert

w = 0.35
x = np.arange(3)
xl=x-w/2
xr=x+w/2

categories = ["read", "read after update", "read after insert"]
bar01 = plt.bar(xl, alone, width=w, label="alone")
bar02 = plt.bar(xr, sharded, width=w, label="sharded")

for bar in list(bar01) + list(bar02):
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.0f}",
        ha="center", va="bottom", fontsize=8
    )

plt.xticks(x,categories)
plt.ylabel("Duration / ms")

plt.legend(loc="lower right", bbox_to_anchor=(0.2,1))

plt.savefig("./couch_figs/flat.pdf", bbox_inches="tight")

