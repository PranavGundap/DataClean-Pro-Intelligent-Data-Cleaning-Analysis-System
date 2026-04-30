import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load raw (before cleaning) data
raw_df = pd.read_csv(r"D:\All Projects\DataClean Pro Intelligent Data Cleaning & Analysis System\data\dirty_cafe_sales.csv")

# Load cleaned data
df = pd.read_csv("cleaned_data/cleaned.csv")


print("First 5 rows of cleaned data:")
print(df.head())


# Print comparison in terminal
print("\nData Cleaning Comparison:")
print("Before cleaning (rows, columns):", raw_df.shape)
print("After cleaning (rows, columns):", df.shape)


# Correlation Heatmap
plt.figure(figsize=(6,4))
sns.heatmap(
    df.select_dtypes(include=['number']).corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()


# Item sales count
plt.figure(figsize=(6,4))
df["Item"].value_counts().plot(kind='bar')
plt.title("Items Sold")
plt.xlabel("Item")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Payment method distribution
plt.figure(figsize=(6,4))
df["Payment Method"].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Payment Method Distribution")
plt.ylabel("")  #
plt.tight_layout()
plt.show()


# Data cleaning impact (Before vs After)
before_rows = raw_df.shape[0]
after_rows = df.shape[0]

labels = ["Before Cleaning", "After Cleaning"]
values = [before_rows, after_rows]

plt.figure(figsize=(5,4))
bars = plt.bar(labels, values)

# Add values on top of bars
for i, v in enumerate(values):
    plt.text(i, v + 10, str(v), ha='center')

plt.title("Data Cleaning Impact")
plt.xlabel("Stage")
plt.ylabel("Number of Rows")
plt.tight_layout()
plt.show()
