import pandas as pd

data_dict = {
    "Product": ["Apple", "Banana", "Orange", "Mango", "Grape", "Guava"],
    "Price": [30, 20, 25, 60, 45, 35],
    "Sales": [100, 150, 80, 60, 90, 54]
}

df1 = pd.DataFrame(data_dict)

print(df1.head())
print(df1.tail())
print(df1.shape)
print(df1.columns)
print(df1.dtypes)
print(df1.count())

stock = df1.describe().round(2)

print(stock)

stock.to_csv("0520_stock2.csv")