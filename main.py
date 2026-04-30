import pandas as pd 
import os


# Here we have load a dataset
df = pd.read_csv(r"D:\All Projects\DataClean Pro Intelligent Data Cleaning & Analysis System\data\dirty_cafe_sales.csv")
print(df.head())

# Now we can handle missing values 

# Here we Check missing values
print(df.isnull().sum())


# And here we will convert numeric columns first (important step)
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Price Per Unit"] = pd.to_numeric(df["Price Per Unit"], errors="coerce")
df["Total Spent"] = pd.to_numeric(df["Total Spent"], errors="coerce")

# And we can Replace UNKNOWN values with NA
df.replace("UNKNOWN", pd.NA, inplace=True)


# Now Fill missing values (after cleaning)
# Fill numeric columns with mean
df.fillna(df.mean(numeric_only=True), inplace=True)

# Fill categorical columns with mode
df.fillna(df.mode().iloc[0], inplace=True)


# Now we will Remove duplicates 
df.drop_duplicates(inplace=True)


# Here We have handle outliers 

# Using IQR method only on numeric columns
numeric_df = df.select_dtypes(include=['number'])

Q1 = numeric_df.quantile(0.25)
Q3 = numeric_df.quantile(0.75)
IQR = Q3 - Q1

df = df[~((numeric_df < (Q1 - 1.5 * IQR)) | (numeric_df > (Q3 + 1.5 * IQR))).any(axis=1)]


# here we do Basic analysis 
print(df.describe())

# Correlation only on numeric data
print(df.select_dtypes(include=['number']).corr())


# Here we create folder for saving cleaned data
os.makedirs("cleaned_data", exist_ok=True)

# Save cleaned dataset
df.to_csv("cleaned_data/cleaned.csv", index=False)

print("\nCleaned data saved successfully!")

