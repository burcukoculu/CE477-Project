import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


def drop_nonnumericals(df):
    non_floats = []
    for col in df:
        if df[col].dtypes != "float64":
            non_floats.append(col)
    dff = df.drop(columns=non_floats)
    return dff


def list_numeric_attributes(df):
    numeric_attributes = df.select_dtypes(include=np.number).columns.tolist()
    return numeric_attributes


def report_missed_value(df):
    print(df.isnull().sum())
    print(f'Total : {df.isnull().sum().sum()}')


def scatter_plot(x, y, size, marker, color, label):
    plt.scatter(x, y,
                s=size,
                marker=marker,
                color=color,
                label=label)
    plt.legend(title='Factors')


def apply_pca_visualization(dff):
    df = drop_nonnumericals(dff)
    scale = StandardScaler()
    scale.fit(df)
    scaled_data = scale.transform(df)
    pca = PCA(n_components=2)
    pca.fit(scaled_data)
    x_pca = pca.fit_transform(scaled_data)
    plt.figure(figsize=(8, 6))
    plt.scatter(x_pca[:, 0], x_pca[:, 1], c=df['cost'], s=3, marker='.', cmap='rainbow')
    plt.xlabel('First PCA')
    plt.ylabel('Second PCA')
    b = plt.colorbar()
    b.set_label('Cost Prediction on acquiring Customers')
    plt.show()


def hist_equal_width(arr, nbin):
    n, bins, patches = plt.hist(arr, nbin, edgecolor='black')
    plt.xticks(bins)
    plt.show()


def hist_equal_freq(arr, nbin):
    nlen = len(arr)
    print(nlen)
    x = np.interp(np.linspace(0, nlen, nbin + 1),
                  np.arange(nlen),
                  np.sort(arr))
    n, bins, patches = plt.hist(arr, x, 5,
                                edgecolor='black')
    print(bins)
    print(n)
    plt.xticks(bins)
    plt.show()


def apply_discretization(data, str):
    arr = data[str]
    plt.hist(arr, 100, edgecolor='black')
    plt.show()
    hist_equal_width(arr, 10)
    hist_equal_width(arr, 5)
    hist_equal_freq(arr, 5)


def draw_scatter_plots():
    common_factor = data.promotion_name == 'Weekend Markdown'

    factor1 = data.sales_country == 'USA'
    factor2 = data.sales_country == 'Mexico'

    x = data['store_cost(in millions)'][common_factor]
    y = data['store_sales(in millions)'][common_factor]
    plt.xlabel('Store Cost')
    plt.ylabel('Store Sales')

    scatter_plot(x[factor1], y[factor1], 20, 'D', 'red', 'Supermarket')
    scatter_plot(x[factor2], y[factor2], 20, 'D', 'green', 'Small Grocery')
    plt.show()

    common_factor = data.food_category == 'Bread'

    factor1 = data.store_type == 'Supermarket'
    factor2 = data.store_type == 'Small Grocery'
    factor3 = data.store_type == 'Deluxe Supermarket'

    x = data['SRP'][common_factor]
    y = data['store_sales(in millions)'][common_factor]
    plt.xlabel('SRP/MRP')
    plt.ylabel('Store Sales')

    scatter_plot(x[factor1], y[factor1], 10, 'o', 'red', 'Supermarket')
    scatter_plot(x[factor2], y[factor2], 10, 'o', 'green', 'Small Grocery')
    scatter_plot(x[factor3], y[factor3], 10, 'o', 'blue', 'Deluxe Supermarket')
    plt.show()

    common_factor = data.food_category == "Jams and Jellies"
    factor1 = data.marital_status == 'M'
    factor2 = data.marital_status == 'S'

    x = data['store_sales(in millions)']
    y = data['total_children']
    plt.xlabel('Store Sales ')
    plt.ylabel('Total Children in Home')
    plt.xlim(13, 20)
    plt.ylim(-0.2, 4.5)
    scatter_plot(x[factor1], y[factor1], 5, '.', 'red', 'Married')
    plt.show()


# print(data.shape[0])  -- num of row == .count()
# print(data.food_category.unique())

data = pd.read_csv("media prediction and its cost.csv", encoding="latin-1")

# Data Set Description
report_missed_value(data)
draw_scatter_plots()

# Preprocessing
apply_discretization(data, 'cost')
apply_pca_visualization(data)
# Apply Data Augmentation

quit()
