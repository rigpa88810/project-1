import pandas as pd
import numpy as np

df = pd.read_csv("Grocery_Inventory_and_Sales_Dataset.csv")

price = df["Unit_Price"].str.replace("$", "", regex=False).to_numpy(dtype=float)
stock = df["Stock_Quantity"].to_numpy(dtype=float)
sales = df["Sales_Volume"].to_numpy(dtype=float)

# (1) 每個商品的總庫存價值
df["Total_Inventory_Value"] = stock * price

# (2) 找出最暢銷商品
best_index = np.argmax(sales)
best_product = df.loc[best_index, ["Product_ID", "Product_Name", "Sales_Volume"]]

# (3) 計算 9 折後收入
df["Discount_Revenue"] = sales * price * 0.9

print(df[["Product_Name", "Total_Inventory_Value", "Discount_Revenue"]])
print("最暢銷商品：")
print(best_product)
print("9折後總收入：", df["Discount_Revenue"].sum())