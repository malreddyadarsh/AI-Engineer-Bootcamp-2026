# Program 5 — Gradient Boosting Regression
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
# GradientBoostingRegressor(
    # random_state=42
# )
# 
# Evaluate:
# 
# MAE
# MSE
# RMSE
# R²
# 
# Compare:
# 
# Linear Regression
# Decision Tree Regressor
# Random Forest Regressor
# Gradient Boosting Regressor
# 
# This is your first proper four-model regression comparison.



import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

data = {
    "Study_Hours": [
        2, 3, 1, 5, 4,
        6, 2, 7, 3, 8,
        1, 4, 6, 2, 5,
        7, 3, 9, 4, 6,
        2, 8, 5, 1, 7,
        4, 6, 3, 9, 5,
        2, 7, 4, 8, 3,
        6, 1, 5, 7, 4,
        9, 2, 6, 5, 8,
        3, 7, 4, 10, 2
    ],

    "Attendance": [
        65, 70, 55, 85, 78,
        92, 68, 95, 72, 98,
        50, 80, 90, 62, 88,
        94, 73, 99, 82, 91,
        60, 96, 86, 48, 93,
        79, 89, 75, 97, 84,
        64, 92, 81, 95, 70,
        87, 52, 83, 91, 77,
        99, 67, 88, 85, 96,
        74, 93, 80, 100, 58
    ],

    "Previous_Marks": [
        45, 52, 38, 72, 65,
        80, 48, 88, 55, 92,
        35, 68, 84, 42, 75,
        90, 58, 95, 70, 82,
        40, 91, 73, 30, 87,
        62, 78, 57, 96, 69,
        44, 85, 66, 89, 51,
        76, 36, 71, 93, 60,
        98, 49, 81, 74, 94,
        56, 86, 67, 99, 41
    ],

    "Assignments_Completed": [
        5, 6, 4, 8, 7,
        9, 5, 10, 6, 10,
        3, 8, 9, 5, 8,
        10, 6, 10, 8, 9,
        4, 10, 8, 3, 9,
        7, 9, 6, 10, 8,
        5, 9, 7, 10, 6,
        8, 4, 8, 10, 7,
        10, 5, 9, 8, 10,
        6, 9, 7, 10, 4
    ],

    "Final_Marks": [
        42, 50, 35, 72, 64,
        82, 45, 89, 54, 94,
        32, 67, 85, 40, 76,
        91, 57, 96, 71, 83,
        38, 93, 74, 28, 88,
        63, 79, 55, 97, 68,
        43, 86, 65, 90, 49,
        77, 34, 70, 92, 59,
        99, 47, 80, 75, 95,
        53, 87, 66, 100, 39
    ]
}

df = pd.DataFrame(data)

X=df[["Study_Hours","Attendance","Previous_Marks","Assignments_Completed"]]

y=df["Final_Marks"]

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model1=LinearRegression()

model1.fit(X_train,y_train)

y_pred1=model1.predict(X_test)

mae_1=mean_absolute_error(y_test,y_pred1)
mse_1=mean_squared_error(y_test,y_pred1)
rmse_1=mse_1**0.5
r2_1=r2_score(y_test,y_pred1)


model2=DecisionTreeRegressor(
    max_depth=5,
    random_state=42
)

model2.fit(X_train,y_train)

y_pred2=model2.predict(X_test)

mae_2=mean_absolute_error(y_test,y_pred2)
mse_2=mean_squared_error(y_test,y_pred2)
rmse_2=mse_2**0.5
r2_2=r2_score(y_test,y_pred2)

model3=RandomForestRegressor(
    n_estimators=100,
    max_depth=3,
    random_state=42
)

model3.fit(X_train,y_train)

y_pred3=model3.predict(X_test)

mae_3=mean_absolute_error(y_test,y_pred3)
mse_3=mean_squared_error(y_test,y_pred3)
rmse_3=mse_3**0.5
r2_3=r2_score(y_test,y_pred3)

model4=GradientBoostingRegressor(
    n_estimators=50,
    max_depth=3,
    learning_rate=0.05,
    subsample=0.7,
    random_state=42
)

model4.fit(X_train,y_train)

y_pred4=model4.predict(X_test)

mae_4=mean_absolute_error(y_test,y_pred4)
mse_4=mean_squared_error(y_test,y_pred4)
rmse_4=mse_4**0.5
r2_4=r2_score(y_test,y_pred4)

comparison=pd.DataFrame({
    "Models":["LinearRegression","DecisionTree","RandomForest","GradientBoosting"],
    "MAE_Score":[mae_1,mae_2,mae_3,mae_4],
    "MSE_Score":[mse_1,mse_2,mse_3,mse_4],
    "RMSE_Score":[rmse_1,rmse_2,rmse_3,rmse_4],
    "R2_Score":[r2_1,r2_2,r2_3,r2_4]
})

print("\nComparison Table :")
print(comparison)


print("\nObservation :")
print("\nObservation :")
print(
    "Based on the MAE, MSE, RMSE, and R² values, "
    "Linear Regression performed best on this dataset "
    "and this train/test split. It achieved the lowest "
    "MAE, MSE, and RMSE and the highest R²."
)