import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("media prediction and its cost.csv",encoding="latin-1")
numeric_data = data[["cost"]]


fig = plt.figure(figsize =(5, 5))
ax = fig.add_subplot(111)
ax.set_xticklabels(["cost"])
mean_shape = dict(markerfacecolor ="blue", marker = "D", markeredgecolor = "green")
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
bp = ax.boxplot(numeric_data, showmeans = True, meanprops = mean_shape)

plt.show()