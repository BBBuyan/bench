import matplotlib.pyplot as plt
import numpy as np

a_avg_only = [8]
a_avg_after_update = [137]
a_avg_after_insert = [94]
alone_avg = a_avg_only + a_avg_after_update + a_avg_after_insert

s_avg_only = [10]
s_avg_after_update = [84]
s_avg_after_insert = [71]
sharded_avg = s_avg_only + s_avg_after_update + s_avg_after_insert

w = 0.35
x = np.arange(3)
xl=x-w/2
xr=x+w/2

categories_average = ["average only", "after update", "after insert"]
# plt.figure(figsize=(10,5))

bar01 = plt.bar(xl, alone_avg, width=w, label="alone")
bar02 = plt.bar(xr, sharded_avg, width=w, label="sharded")

for bar in list(bar01) + list(bar02):
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"{height:.0f}",
        ha="center", va="bottom", fontsize=8
    )

plt.xticks(x,categories_average)

plt.tight_layout()
plt.ylabel("Duration / ms")
plt.legend(loc="lower right", bbox_to_anchor=(0.2,1))
plt.savefig("./couch_figs/flat_avg.pdf", bbox_inches="tight")
