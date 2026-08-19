# Student Performance Feature Engineering System
# 
# Create a dataset with:
# 
# Student_ID
# Age
# Study Hours
# Attendance
# Math
# Science
# English
# Assignments Completed
# Total Assignments
# 
# Create:
# 
# Average Marks
# Assignment Completion Rate
# Study Efficiency
# Study_Attendance
# 
# For example:
# 
# StudyEfficiency=
# StudyHours+1
# AverageMarks
	# ​
# 
# 
# Then perform:
# 
# Load Dataset
      # ↓
# EDA
      # ↓
# Feature Engineering
      # ↓
# Analyze Correlations
      # ↓
# Select Useful Features
      # ↓
# Train ML Model
      # ↓
# Evaluate
      # ↓
# Compare
# Your final report should answer:
# 1. Which features were created?
# 2. Why were they created?
# 3. Which features were most useful?
# 4. Were any features removed?
# 5. Did the engineered features improve performance?
# 
# That last question is especially important.
# 
# Feature engineering should be tested, not assumed to be useful.

# Mini Project — Student Performance Feature Engineering System

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# ==========================================================
# 1. LOAD DATASET
# ==========================================================

df = pd.read_csv("day36/student.csv")

print("\n================ DATASET ================")
print(df.head())

print("\n================ DATASET INFO ================")
print(df.info())

print("\n================ STATISTICS ================")
print(df.describe())


# ==========================================================
# 2. EDA
# ==========================================================

print("\n================ MISSING VALUES ================")
print(df.isnull().sum())

print("\n================ DATASET SHAPE ================")
print(df.shape)


# ==========================================================
# 3. FEATURE ENGINEERING
# ==========================================================

# Average Marks
df["Average_Marks"] = (
    df[["Math", "Science", "English"]].mean(axis=1)
)

# Assignment Completion Rate
df["Assignment_Completion_Rate"] = (
    df["Assignments_Completed"] /
    df["Total_Assignments"]
)

# Study Efficiency
df["Study_Efficiency"] = (
    df["Average_Marks"] /
    (df["Study_Hours"] + 1)
)

# Study Attendance
df["Study_Attendance"] = (
    df["Study_Hours"] *
    df["Attendance"]
)


print("\n================ ENGINEERED DATASET ================")
print(df.head())


# ==========================================================
# 4. ANALYZE CORRELATIONS
# ==========================================================

print("\n================ CORRELATION MATRIX ================")

correlation = df.corr(numeric_only=True)

print(correlation)


# Correlation Heatmap

plt.figure(figsize=(12, 8))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Feature Correlation Matrix")

plt.show()


# ==========================================================
# 5. SELECT TARGET
# ==========================================================

# We want to predict Average_Marks

y = df["Average_Marks"]


# ==========================================================
# MODEL 1
# ORIGINAL FEATURES ONLY
# ==========================================================

original_features = [
    "Age",
    "Study_Hours",
    "Attendance",
    "Math",
    "Science",
    "English",
    "Assignments_Completed",
    "Total_Assignments"
]

X_original = df[original_features]


# ==========================================================
# TRAIN / TEST SPLIT
# ==========================================================

X_train_original, X_test_original, y_train, y_test = train_test_split(
    X_original,
    y,
    test_size=0.2,
    random_state=42
)


# ==========================================================
# TRAIN MODEL 1
# ==========================================================

model_original = LinearRegression()

model_original.fit(
    X_train_original,
    y_train
)


# Predictions

predictions_original = model_original.predict(
    X_test_original
)


# Evaluation

original_r2 = r2_score(
    y_test,
    predictions_original
)

original_mse = mean_squared_error(
    y_test,
    predictions_original
)


print("\n========================================")
print("MODEL 1 — ORIGINAL FEATURES")
print("========================================")

print("R² Score :", original_r2)
print("MSE      :", original_mse)


# ==========================================================
# MODEL 2
# ORIGINAL + ENGINEERED FEATURES
# ==========================================================

engineered_features = [
    "Age",
    "Study_Hours",
    "Attendance",
    "Math",
    "Science",
    "English",
    "Assignments_Completed",
    "Total_Assignments",
    "Average_Marks",
    "Assignment_Completion_Rate",
    "Study_Efficiency",
    "Study_Attendance"
]

X_engineered = df[engineered_features]


# ==========================================================
# TRAIN / TEST SPLIT
# ==========================================================

X_train_engineered, X_test_engineered, y_train2, y_test2 = train_test_split(
    X_engineered,
    y,
    test_size=0.2,
    random_state=42
)


# ==========================================================
# TRAIN MODEL 2
# ==========================================================

model_engineered = LinearRegression()

model_engineered.fit(
    X_train_engineered,
    y_train2
)


# Predictions

predictions_engineered = model_engineered.predict(
    X_test_engineered
)


# Evaluation

engineered_r2 = r2_score(
    y_test2,
    predictions_engineered
)

engineered_mse = mean_squared_error(
    y_test2,
    predictions_engineered
)


print("\n========================================")
print("MODEL 2 — ENGINEERED FEATURES")
print("========================================")

print("R² Score :", engineered_r2)
print("MSE      :", engineered_mse)


# ==========================================================
# 6. MODEL COMPARISON
# ==========================================================

print("\n========================================")
print("MODEL COMPARISON")
print("========================================")

print("\nOriginal Features:")
print("R² Score :", original_r2)
print("MSE      :", original_mse)

print("\nEngineered Features:")
print("R² Score :", engineered_r2)
print("MSE      :", engineered_mse)


# ==========================================================
# 7. CHECK IMPROVEMENT
# ==========================================================

print("\n========================================")
print("FEATURE ENGINEERING RESULT")
print("========================================")

if engineered_r2 > original_r2:

    print("Feature engineering IMPROVED the R² score.")

elif engineered_r2 < original_r2:

    print("Feature engineering DECREASED the R² score.")

else:

    print("Feature engineering produced the SAME R² score.")


if engineered_mse < original_mse:

    print("Feature engineering REDUCED the MSE.")

elif engineered_mse > original_mse:

    print("Feature engineering INCREASED the MSE.")

else:

    print("Feature engineering produced the SAME MSE.")


# ==========================================================
# 8. DISPLAY FEATURE IMPORTANCE
# ==========================================================

print("\n========================================")
print("MODEL COEFFICIENTS")
print("========================================")

coefficients = pd.DataFrame({
    "Feature": engineered_features,
    "Coefficient": model_engineered.coef_
})

print(coefficients.sort_values(
    by="Coefficient",
    ascending=False
))