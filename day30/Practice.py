# import pandas as pd
# 
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# 
# # Dataset
# data = {
    # "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    # "Marks": [40, 45, 50, 60, 65, 70, 78, 85, 90, 95]
# }
# 
# df = pd.DataFrame(data)
# 
# print("Dataset:")
# print(df)
# 
# # Features
# X = df[["Study_Hours"]]
# 
# # Target
# y = df["Marks"]
# 
# print("\nFeatures (X):")
# print(X)
# 
# print("\nTarget (y):")
# print(y)
# 
# # Split data
# X_train, X_test, y_train, y_test = train_test_split(
    # X,
    # y,
    # test_size=0.2,
    # random_state=42
# )
# 
# print("\nTraining samples:")
# print(X_train)
# 
# print("\nTesting samples:")
# print(X_test)
# 
# # Create model
# model = LinearRegression()
# 
# # Train model
# model.fit(X_train, y_train)
# 
# # Predictions
# predictions = model.predict(X_test)
# 
# print("\nActual values:")
# print(y_test.values)
# 
# print("\nPredicted values:")
# print(predictions)
# 
# # Compare actual vs predicted
# comparison = pd.DataFrame({
    # "Actual": y_test.values,
    # "Predicted": predictions
# })
# 
# print("\nComparison:")
# print(comparison)


# # Program 2 — Train/Test Split

# # Take a dataset and perform:

# # train_test_split()

# # Display:

# # Number of training samples.
# # Number of testing samples.

# # Understand exactly why the split happens.

# import pandas as pd
# from sklearn.model_selection import train_test_split

# data={
    # "Study_Hours":[1,2,3,4,5,6,7,8,9,10],
    # "Marks":[40,45,50,55,60,65,70,75,80,90]
# }

# df=pd.DataFrame(data)

# X=df[["Study_Hours"]]

# y=df["Marks"]

# X_train, X_test, y_train, y_test= train_test_split (
    # X,y,test_size=0.2,random_state=42
# )

# print("Training Samples :")
# print(X_train)
# print("No.of Training Samples :",len(X_train))

# print("Testing Samples :")
# print(X_test)
# print("Number of testing samples :",len(X_test))


# # Program 3 — Prediction

# # Train a simple model and ask:

# # "If a student studies 7.5 hours, what marks might the model predict?"

# # This teaches you the difference between:

# # training examples and new/unseen data.

# import pandas as pd

# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression

# data = {
    # "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    # "Marks": [40, 45, 50, 60, 65, 70, 78, 85, 90, 95]
# }

# df = pd.DataFrame(data)

# X = df[["Study_Hours"]]
# y = df["Marks"]

# X_train, X_test, y_train, y_test = train_test_split(
    # X,
    # y,
    # test_size=0.2,
    # random_state=42
# )

# model = LinearRegression()

# model.fit(X_train, y_train)

# # New unseen student
# new_student = pd.DataFrame({
    # "Study_Hours": [7.5]
# })

# prediction = model.predict(new_student)

# print("Study Hours:", 7.5)
# print("Predicted Marks:", prediction[0])



# # Program 4 — Overfitting Demonstration
# 
# # Use a small dataset and compare:
# 
# # A simple model.
# # A more complex model.
# 
# # Don't worry about sophisticated algorithms.
# 
# # The goal is to observe that a model can fit training data extremely well but perform poorly on unseen data.
# 
# import numpy as np
# 
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.preprocessing import PolynomialFeatures
# from sklearn.pipeline import make_pipeline
# from sklearn.metrics import mean_squared_error
# 
# # Dataset
# X = np.array([
    # [1], [2], [3], [4], [5],
    # [6], [7], [8], [9], [10],
    # [11], [12], [13], [14], [15]
# ])
# 
# y = np.array([
    # 3, 5, 8, 9, 12,
    # 13, 15, 18, 19, 20,
    # 22, 25, 24, 28, 30
# ])
# 
# # Split
# X_train, X_test, y_train, y_test = train_test_split(
    # X,
    # y,
    # test_size=0.3,
    # random_state=42
# )
# 
# # Simple model
# simple_model = make_pipeline(
    # PolynomialFeatures(degree=1),
    # LinearRegression()
# )
# 
# # Complex model
# complex_model = make_pipeline(
    # PolynomialFeatures(degree=10),
    # LinearRegression()
# )
# 
# # Train
# simple_model.fit(X_train, y_train)
# complex_model.fit(X_train, y_train)
# 
# # Predictions
# simple_train_pred = simple_model.predict(X_train)
# simple_test_pred = simple_model.predict(X_test)
# 
# complex_train_pred = complex_model.predict(X_train)
# complex_test_pred = complex_model.predict(X_test)
# 
# # Errors
# simple_train_error = mean_squared_error(
    # y_train,
    # simple_train_pred
# )
# 
# simple_test_error = mean_squared_error(
    # y_test,
    # simple_test_pred
# )
# 
# complex_train_error = mean_squared_error(
    # y_train,
    # complex_train_pred
# )
# 
# complex_test_error = mean_squared_error(
    # y_test,
    # complex_test_pred
# )
# 
# print("SIMPLE MODEL")
# print("Training MSE:", simple_train_error)
# print("Testing MSE:", simple_test_error)
# 
# print("\nCOMPLEX MODEL")
# print("Training MSE:", complex_train_error)
# print("Testing MSE:", complex_test_error)



# Program 5 ⭐ — Complete ML Workflow

# Create a small realistic dataset such as:

# Study Hours
# Attendance
# Previous Marks
# Assignments Completed
# Final Marks

# Perform:

# Load data
   # ↓
# Inspect
   # ↓
# X and y
   # ↓
# Train/Test Split
   # ↓
# Train model
   # ↓
# Predict
   # ↓
# Evaluate

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# ------------------------------------------------
# 1. Create dataset
# ------------------------------------------------

data = {
    "Study_Hours": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                    4, 6, 7, 8, 9],

    "Attendance": [55, 60, 65, 70, 75, 80, 85, 90, 95, 98,
                   68, 78, 82, 88, 92],

    "Previous_Marks": [35, 40, 45, 50, 55, 60, 65, 70, 75, 80,
                       48, 58, 63, 68, 73],

    "Assignments_Completed": [3, 4, 5, 6, 6, 7, 8, 9, 9, 10,
                              5, 7, 7, 8, 9],

    "Final_Marks": [38, 43, 50, 57, 63, 69, 76, 83, 89, 94,
                    52, 64, 70, 77, 84]
}

df = pd.DataFrame(data)

# ------------------------------------------------
# 2. Inspect dataset
# ------------------------------------------------

print("FIRST 5 ROWS")
print(df.head())

print("\nDATASET SHAPE")
print(df.shape)

print("\nDATASET INFORMATION")
print(df.info())

print("\nSTATISTICS")
print(df.describe())

print("\nMISSING VALUES")
print(df.isnull().sum())

# ------------------------------------------------
# 3. Select features and target
# ------------------------------------------------

X = df[
    [
        "Study_Hours",
        "Attendance",
        "Previous_Marks",
        "Assignments_Completed"
    ]
]

y = df["Final_Marks"]

print("\nFEATURES")
print(X)

print("\nTARGET")
print(y)

# ------------------------------------------------
# 4. Split data
# ------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTRAINING SAMPLES:", len(X_train))
print("TESTING SAMPLES:", len(X_test))

# ------------------------------------------------
# 5. Create model
# ------------------------------------------------

model = LinearRegression()

# ------------------------------------------------
# 6. Train model
# ------------------------------------------------

model.fit(X_train, y_train)

# ------------------------------------------------
# 7. Predict
# ------------------------------------------------

predictions = model.predict(X_test)

# ------------------------------------------------
# 8. Display predictions
# ------------------------------------------------

comparison = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": predictions
})

print("\nPREDICTIONS")
print(comparison)

# ------------------------------------------------
# 9. Evaluate
# ------------------------------------------------

mae = mean_absolute_error(
    y_test,
    predictions
)

r2 = r2_score(
    y_test,
    predictions
)

print("\nMODEL EVALUATION")

print("Mean Absolute Error:", mae)
print("R2 Score:", r2)