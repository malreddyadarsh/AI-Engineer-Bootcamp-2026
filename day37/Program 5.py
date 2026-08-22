# Program 5 — Decision Tree Regression 🔥
# 
# Create:
# 
# Study Hours
# Attendance
# Previous Marks
# Final Marks
# 
# Train:
# 
# DecisionTreeRegressor()
# 
# Predict Final Marks.
# 
# Evaluate using:
# 
# MAE
# MSE
# RMSE
# R²
# 
# Then compare it with your Day 31:
# 
# LinearRegression
# 
# This is a very important experiment.
# 
# You're learning that different algorithms can solve the same problem in different ways.


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score


data = pd.DataFrame({
    "Study_Hours": [
        1, 2, 2, 3, 3,
        4, 4, 5, 5, 6,
        6, 7, 7, 8, 8,
        9, 9, 10, 10, 11,
        3, 4, 5, 6, 7
    ],

    "Attendance": [
        55, 60, 62, 65, 68,
        70, 72, 74, 76, 78,
        80, 82, 84, 85, 87,
        88, 90, 92, 94, 96,
        82, 58, 65, 88, 76
    ],

    "Previous_Marks": [
        40, 42, 45, 48, 50,
        52, 55, 58, 60, 63,
        65, 68, 70, 73, 75,
        78, 80, 84, 87, 90,
        72, 45, 55, 62, 78
    ],

    "Final_Marks": [
        45, 48, 50, 53, 55,
        58, 60, 64, 66, 69,
        71, 74, 76, 79, 81,
        84, 86, 89, 92, 94,
        57, 51, 61, 73, 77
    ]
})

X=data[["Study_Hours","Attendance","Previous_Marks"]]

y=data["Final_Marks"]

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model1=DecisionTreeRegressor(
    max_depth=3,
    random_state=42
)

model1.fit(X_train,y_train)

pred1=model1.predict(X_test)

mse1=mean_squared_error(y_test,pred1)
rmse1=mse1 ** 0.5
mae1=mean_absolute_error(y_test,pred1)
r2_1=r2_score(y_test,pred1)

model2=LinearRegression()

model2.fit(X_train,y_train)

pred2=model2.predict(X_test)

mse2=mean_squared_error(y_test,pred2)
rmse2=mse2 ** 0.5
mae2=mean_absolute_error(y_test,pred2)
r2_2=r2_score(y_test,pred2)

comparsion=pd.DataFrame({
    "Models":["DecisionTree","LinearRegression"],
    "MSE":[mse1,mse2],
    "RMSE":[rmse1,rmse2],
    "MAE":[mae1,mae2],
    "R2_score":[r2_1,r2_2]
})

print("\nComparsion Table :")
print(comparsion)