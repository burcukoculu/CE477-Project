import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

data=pd.read_csv("media prediction and its cost.csv",encoding="latin-1")
o_h = data[["food_department"]].value_counts()
ohe = pd.get_dummies(data=o_h)
o_h.head(15)
ohe.shape

with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', 3,
                       ):
    print(ohe)

