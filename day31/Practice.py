# # Program 1 — Simple Linear Regression ⭐
# # 
# # Create:
# # 
# # Study Hours → Marks
# # 
# # Use:
# # 
# # from sklearn.linear_model import LinearRegression
# # 
# # Your program should:
# # 
# # Create X.
# # Create y.
# # Split data.
# # Create the model.
# # Train it.
# # Predict.
# # Print predictions.
# # 
# # Then predict marks for a new number of study hours.
# 
# # Program 2 — Understand Coefficient & Intercept
# 
# # After training:
# 
# # model.coef_
# # model.intercept_
# 
# # Print both.
# 
# # Then explain in your own words:
# 
# # What does the coefficient mean?
# # What does the intercept mean?
# 
# # Program 3 — Evaluate the Model
# 
# # Calculate:
# 
# # MSE
# # RMSE
# # R²
# 
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
# 
# data={
    # "Study_Hours":[1,2,3,4,5,6,7,8],
    # "Marks":[50,55,60,65,70,75,80,90]
# }
# 
# df=pd.DataFrame(data)
# 
# X=df[["Study_Hours"]]
# 
# y=df["Marks"]
# 
# X_train ,X_test,y_train,y_test=train_test_split(
    # X,
    # y,
    # test_size=.2,
    # random_state=42
# )
# 
# model=LinearRegression()
# 
# model.fit(X_train,y_train)
# 
# print("\nCoefficients :")
# print(model.coef_)
# 
# print("\nIntercepts :")
# print(model.intercept_)
# 
# predictions=model.predict(X_test)
# 
# print("\nPredictions :")
# print(predictions)
# 
# student=pd.DataFrame({
    # "Study_Hours":[9]
# })
# 
# new_predictions=model.predict(student)
# print("Prediction for 9 Hours :")
# print(new_predictions)
# 
# mae=mean_absolute_error(y_test,predictions)
# print("\nMean Absolute Error is :",mae)
# 
# mse=mean_squared_error(y_test,predictions)
# rmse=mse ** 0.5
# print("\n Root Mean Squared Error is :",rmse)
# 
# r2=r2_score(y_test,predictions)
# print("\nR2_Score is :",r2)




# # Program 4 — Multiple Linear Regression ⭐

# # Use:

# # Study Hours
# # Attendance
# # Previous Marks

# # to predict:

# # Final Marks

# # Perform:

# # X/y selection
     # # ↓
# # Train/Test Split
     # # ↓
# # Model Training
     # # ↓
# # Prediction
     # # ↓
# # Evaluation

# # Then inspect the coefficients.

# import pandas as pd

# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score

# data={
    # "Study_Hours":[1,2,3,4,5,6,7,8,9],
    # "Attendance":[34,45,49,53,56,60,65,70,80],
    # "Previous_Marks":[40,42,50,54,58,62,67,72,75],
    # "Final_Marks":[44,45,54,57,61,68,71,76,80]
# }

# df=pd.DataFrame(data)

# X=df[["Study_Hours","Attendance","Previous_Marks"]]

# y=df["Final_Marks"]

# X_train,X_test,y_train,y_test=train_test_split(
    # X,
    # y,
    # test_size=0.2,
    # random_state=42
# )

# model=LinearRegression()

# model.fit(X_train,y_train)

# print("\nCoefficients :")
# print(model.coef_)

# print("\nIntercepts :")
# print(model.intercept_)

# prediction=model.predict(X_test)

# print("\nPrediction :")
# print(prediction)

# print("\nEvaluation :")

# mae=mean_absolute_error(y_test,prediction)
# mse=mean_squared_error(y_test,prediction)
# rmse=mse ** 0.5
# r2=r2_score(y_test,prediction)
# print("\nMean Absolute Error :",mae)
# print("Mean Squared Error :",mse)
# print("Root Mean Squared Error :",rmse)
# print("R2 Score :",r2)




# Program 5 — Actual vs Predicted Visualization

# Create a scatter plot:

# Actual Marks
      # vs
# Predicted Marks

# Add a reference line:

# y=x

# Interpret:

# The closer the predictions are to the reference line, the closer they are to the actual values.

# This combines:

# Pandas + NumPy + Matplotlib + Scikit-learn + Statistics

# That's exactly the integration we're looking for.

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt
import seaborn as sns 

data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                    2, 4, 6, 8, 10],

    "Attendance": [55, 60, 65, 70, 72, 75, 80, 85, 88, 92,
                    58, 68, 78, 86, 95],

    "Previous_Marks": [42, 48, 52, 58, 61, 66, 70, 75, 79, 84,
                       45, 57, 68, 76, 88],

    "Final_Marks": [45, 50, 55, 60, 64, 68, 73, 78, 82, 87,
                    48, 59, 70, 79, 91]
}

df=pd.DataFrame(data)

X=df[["Study_Hours","Attendance","Previous_Marks"]]
y=df["Final_Marks"]

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model=LinearRegression()

model.fit(X_train,y_train)

prediction=model.predict(X_test)

sns.scatterplot(x=y_test,y=prediction)
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    linestyle="--"
)
plt.xlabel("Actual Marks")
plt.ylabel("Predicted Marks")
plt.title("Actual Marks vs Predicted Marks")
plt.show()