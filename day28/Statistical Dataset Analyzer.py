# Mini Project
# Statistical Dataset Analyzer
# 
# Build a reusable program that accepts a CSV file and produces:
# 
# Dataset information
# Number of rows
# Number of columns
# Data types
# Missing values
# Statistics
# Mean
# Median
# Standard deviation
# Quartiles
# IQR
# Analysis
# Outliers
# Correlation
# Highest/lowest values
# Output
# 
# Generate a text report:
# 
# STATISTICAL ANALYSIS REPORT
# ===========================
# 
# Dataset:
# Rows:
# Columns:
# 
# Mean:
# Median:
# Standard Deviation:
# 
# Outliers:
# 
# Strongest Correlation:
# 
# Key Insights:
# 1.
# 2.
# 3.
# 
# This is a much better portfolio project than another simple calculator.


import pandas as pd
import numpy as np 

df=pd.read_csv("day28/dataset.csv")

# Dataset information
print("\nDataset information :\n")
df.info()

# Number of rows
print("\nNumber of rows :",df.shape[0])

# Number of columns
print("\nNumber of columns :",df.shape[1])

# Data types
print("\nData types are :\n",df.dtypes)

# Missing values
print("\nMissing values are :",df.isnull().sum().sum())

numeric_columns = df.select_dtypes(include=np.number).columns

print("\nNumeric Columns:")
print(list(numeric_columns))


print("\n==========================================")
print("              STATISTICS")
print("==========================================")

print("\nMean:")
print(df[numeric_columns].mean())

print("\nMedian:")
print(df[numeric_columns].median())

print("\nStandard Deviation:")
print(df[numeric_columns].std())

print("\nQ1 — 25th Percentile:")
print(df[numeric_columns].quantile(0.25))

print("\nQ2 — 50th Percentile:")
print(df[numeric_columns].quantile(0.50))

print("\nQ3 — 75th Percentile:")
print(df[numeric_columns].quantile(0.75))

# ==========================================
# 5. IQR
# ==========================================

Q1 = df[numeric_columns].quantile(0.25)
Q3 = df[numeric_columns].quantile(0.75)

IQR = Q3 - Q1

print("\nIQR:")
print(IQR)


# ==========================================
# 6. OUTLIER DETECTION
# ==========================================

print("\n==========================================")
print("              OUTLIERS")
print("==========================================")

lower_bound = Q1 - (1.5 * IQR)
upper_bound = Q3 + (1.5 * IQR)

for column in numeric_columns:

    outliers = df[
        (df[column] < lower_bound[column]) |
        (df[column] > upper_bound[column])
    ]

    if len(outliers) > 0:
        print(f"\n{column} Outliers:")

        for value in outliers[column]:
            print(value)

    else:
        print(f"\n{column}: No outliers")


# ==========================================
# 7. HIGHEST AND LOWEST VALUES
# ==========================================

print("\n==========================================")
print("        HIGHEST / LOWEST VALUES")
print("==========================================")

for column in numeric_columns:

    highest = df[column].max()
    lowest = df[column].min()

    print(f"\n{column}")
    print("Highest :", highest)
    print("Lowest  :", lowest)


# ==========================================
# 8. CORRELATION
# ==========================================

print("\n==========================================")
print("              CORRELATION")
print("==========================================")

correlation = df[numeric_columns].corr()

print(correlation)


# ==========================================
# 9. FIND STRONGEST CORRELATION
# ==========================================

correlation_matrix = correlation.copy()

# Remove self-correlations
np.fill_diagonal(correlation_matrix.values, np.nan)

# Find strongest absolute correlation
strongest_pair = correlation_matrix.abs().stack().idxmax()

column1 = strongest_pair[0]
column2 = strongest_pair[1]

strongest_value = correlation.loc[column1, column2]

print("\nStrongest Correlation:")
print(column1, "<->", column2)
print("Correlation :", strongest_value)


# ==========================================
# 10. KEY INSIGHTS
# ==========================================

print("\n==========================================")
print("              KEY INSIGHTS")
print("==========================================")

# Highest mean
highest_mean_column = df[numeric_columns].mean().idxmax()

# Lowest mean
lowest_mean_column = df[numeric_columns].mean().idxmin()

# Most variable column
highest_std_column = df[numeric_columns].std().idxmax()

print("1. Highest average value is in :", highest_mean_column)

print("2. Lowest average value is in  :", lowest_mean_column)

print("3. Highest variation is in     :", highest_std_column)

print("\n==========================================")
print("              ANALYSIS COMPLETE")
print("==========================================")