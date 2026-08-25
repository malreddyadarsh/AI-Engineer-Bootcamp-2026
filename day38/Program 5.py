# Program 5 — Random Forest Regression 🔥
# 
# Create:
# 
# Study Hours
# Attendance
# Previous Marks
# Assignments Completed
# Final Marks
# 
# Train:
# 
# RandomForestRegressor()
# 
# Evaluate using:
# 
# MAE
# MSE
# RMSE
# R²
# 
# Then compare:
# 
# Linear Regression
# Decision Tree Regressor
# Random Forest Regressor
# 
# This gives you your first proper three-model regression comparison.



import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

data = {

    "Study_Hours": [
        2.0, 3.0, 1.5, 5.0, 6.0,
        2.5, 4.0, 7.0, 3.5, 1.0,
        6.5, 5.5, 2.0, 4.5, 7.5,
        3.0, 6.0, 2.5, 5.0, 1.5,
        8.0, 4.0, 6.5, 2.0, 7.0,
        3.5, 5.5, 1.0, 4.5, 8.5,
        2.5, 6.0, 7.5, 3.0, 5.5,
        4.0, 8.0, 2.0, 6.5, 7.0
    ],

    "Attendance": [
        65, 70, 55, 80, 90,
        68, 75, 92, 72, 50,
        88, 85, 60, 78, 95,
        69, 91, 64, 82, 58,
        96, 76, 89, 62, 93,
        74, 87, 52, 81, 98,
        67, 86, 94, 71, 83,
        77, 97, 59, 90, 85
    ],

    "Previous_Marks": [
        55, 62, 48, 72, 85,
        58, 68, 90, 64, 42,
        82, 76, 50, 70, 88,
        60, 91, 56, 75, 45,
        94, 69, 84, 52, 92,
        65, 80, 40, 73, 97,
        57, 86, 89, 63, 78,
        72, 95, 54, 83, 88
    ],

    "Assignments_Completed": [
        6, 7, 4, 9, 10,
        6, 8, 10, 7, 3,
        9, 9, 5, 8, 10,
        6, 10, 5, 9, 4,
        10, 8, 10, 5, 10,
        7, 9, 3, 8, 10,
        6, 9, 10, 7, 8,
        9, 10, 5, 9, 10
    ],

    "Final_Marks": [
        52, 61, 45, 76, 86,
        56, 69, 91, 65, 39,
        84, 78, 48, 73, 90,
        58, 92, 54, 79, 43,
        96, 71, 86, 50, 94,
        67, 82, 38, 75, 98,
        60, 88, 93, 64, 81,
        74, 97, 51, 85, 89
    ]
}

df = pd.DataFrame(data)

X=df[["Study_Hours","Attendance","Previous_Marks","Assignments_Completed"]]

y=df["Final_Marks"]

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

model1=RandomForestRegressor(
    n_estimators=10,
    random_state=42
)

model1.fit(X_train,y_train)

y_pred1=model1.predict(X_test)

mae1=mean_absolute_error(y_test,y_pred1)
mse1=mean_squared_error(y_test,y_pred1)
rmse1=mse1**0.5
r2_1=r2_score(y_test,y_pred1)


model2=DecisionTreeRegressor(
    max_depth=5,
    random_state=42
)

model2.fit(X_train,y_train)

y_pred2=model2.predict(X_test)

mae2=mean_absolute_error(y_test,y_pred2)
mse2=mean_squared_error(y_test,y_pred2)
rmse2=mse2**0.5
r2_2=r2_score(y_test,y_pred2)

model3=LinearRegression()

model3.fit(X_train,y_train)

y_pred3=model3.predict(X_test)

mae3=mean_absolute_error(y_test,y_pred3)
mse3=mean_squared_error(y_test,y_pred3)
rmse3=mse3**0.5
r2_3=r2_score(y_test,y_pred3)

comparison=pd.DataFrame({
    "Models":["RandomForest","DecisionTree","LinearRegression"],
    "MAE_Score":[mae1,mae2,mae3],
    "MSE_Score":[mse1,mse2,mse3],
    "RMSE_Score":[rmse1,rmse2,rmse3],
    "R2_Score":[r2_1,r2_2,r2_3]
})

print("\nComparison Table :\n")
print(comparison)