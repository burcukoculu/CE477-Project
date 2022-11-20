import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder



data=pd.read_csv("media prediction and its cost.csv",encoding="latin-1")



numeric_data1 = data[["store_sales(in millions)","store_cost(in millions)","unit_sales(in millions)"]]
fig = plt.figure(figsize =(5, 5))
ax = fig.add_subplot(111)
ax.set_xticklabels(["store_sales(in millions)","store_cost(in millions)","unit_sales(in millions)"])
mean_shape = dict(markerfacecolor ="blue", marker = "D", markeredgecolor = "green")
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
bp = ax.boxplot(numeric_data1, showmeans = True, meanprops = mean_shape)






numeric_data2 = data[["cost"]]
fig = plt.figure(figsize =(5, 5))
ax = fig.add_subplot(111)
ax.set_xticklabels(["cost"])
mean_shape = dict(markerfacecolor ="blue", marker = "D", markeredgecolor = "green")
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
bp = ax.boxplot(numeric_data2, showmeans = True, meanprops = mean_shape)







numeric_data3 = data[["gross_weight","net_weight"]]
fig = plt.figure(figsize =(5, 5))
ax = fig.add_subplot(111)
ax.set_xticklabels(["gross_weight","net_weight"])
mean_shape = dict(markerfacecolor ="blue", marker = "D", markeredgecolor = "green")
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()
bp = ax.boxplot(numeric_data3, showmeans = True, meanprops = mean_shape)

plt.show()









o_h = data[["food_department"]].value_counts()
ohe = pd.get_dummies(data=o_h)
o_h.head(15)
ohe.shape

with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', 3,
                       ):
    print(ohe)
