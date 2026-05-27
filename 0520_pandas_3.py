import pandas as pd

file_path = "SuperMarket Analysis.csv"

df = pd.read_csv(file_path)

# 清除欄位名稱前後空白
df.columns = df.columns.str.strip()

# 檢查欄位
print("欄位名稱：")
print(df.columns)

# 如果沒有 Total 欄位，就自己建立
if "Total" not in df.columns:
    df["Total"] = df["Unit price"] * df["Quantity"] * 1.05

print("資料大小：", df.shape)

print("\n前五筆資料：")
print(df.head())

filter_df = df[
    (df["Branch"].astype(str).str.startswith("A")) &
    (df["Customer type"] == "Member")
]

print("\n篩選後資料筆數：", filter_df.shape[0])

product_summary = (
    filter_df
    .groupby("Product line")
    .agg(
        Total_Sales=("Total", "sum"),
        Avg_Rating=("Rating", "mean")
    )
    .round(2)
    .reset_index()
)

print("\n各產品線分析：")
print(product_summary)

city_gender_summary = (
    filter_df
    .groupby(["City", "Gender"])
    .agg(
        Avg_Sales=("Total", "mean"),
        Transaction_Count=("Invoice ID", "count")
    )
    .round(2)
    .reset_index()
)

print("\nCity 與 Gender 分組分析：")
print(city_gender_summary)

top_product = product_summary.loc[
    product_summary["Total_Sales"].idxmax()
]

print("\n總銷售額最高產品線：")
print(top_product)

output_file = "0520_pandas_3OK.csv"

product_summary.to_csv(
    output_file,
    index=False,
    encoding="utf-8-sig"
)

print(f"\n已輸出檔案：{output_file}")