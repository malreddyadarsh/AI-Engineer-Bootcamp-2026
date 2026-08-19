# Program 4 — Polynomial Features

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error


# --------------------------------------------------
# 1. Load Dataset
# --------------------------------------------------

df = pd.read_csv("day36/Program 4.csv")

print("Original Dataset:")
print(df.head())


# --------------------------------------------------
# 2. Create X and y
# --------------------------------------------------

X = df[["Study_Hours"]]
y = df["Marks"]


# --------------------------------------------------
# 3. Train/Test Split
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ==================================================
# MODEL 1 — ORIGINAL FEATURE
# ==================================================

# --------------------------------------------------
# 4. Train Linear Regression
# --------------------------------------------------

linear_model = LinearRegression()

linear_model.fit(X_train, y_train)


# --------------------------------------------------
# 5. Make Predictions
# --------------------------------------------------

linear_predictions = linear_model.predict(X_test)


# --------------------------------------------------
# 6. Evaluate Linear Regression
# --------------------------------------------------

linear_r2 = r2_score(y_test, linear_predictions)

linear_mse = mean_squared_error(
    y_test,
    linear_predictions
)


# ==================================================
# POLYNOMIAL FEATURES
# ==================================================

# --------------------------------------------------
# 7. Create Polynomial Features
# --------------------------------------------------

poly = PolynomialFeatures(
    degree=2
)

X_train_poly = poly.fit_transform(X_train)

X_test_poly = poly.transform(X_test)


# --------------------------------------------------
# 8. Print Polynomial Features
# --------------------------------------------------

print("\nOriginal Features:")
print(X_train.head())

print("\nPolynomial Features:")
print(X_train_poly[:5])


# --------------------------------------------------
# 9. Train Linear Regression
#    using Polynomial Features
# --------------------------------------------------

poly_model = LinearRegression()

poly_model.fit(
    X_train_poly,
    y_train
)


# --------------------------------------------------
# 10. Make Predictions
# --------------------------------------------------

poly_predictions = poly_model.predict(
    X_test_poly
)


# --------------------------------------------------
# 11. Evaluate Polynomial Model
# --------------------------------------------------

poly_r2 = r2_score(
    y_test,
    poly_predictions
)

poly_mse = mean_squared_error(
    y_test,
    poly_predictions
)


# ==================================================
# COMPARISON
# ==================================================

print("\n==============================")
print("MODEL COMPARISON")
print("==============================")

print("\nLinear Regression:")
print("R² Score:", linear_r2)
print("MSE:", linear_mse)

print("\nPolynomial Regression:")
print("R² Score:", poly_r2)
print("MSE:", poly_mse)