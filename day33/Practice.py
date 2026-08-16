# # Program 1 ⭐ — Calculate Classification Metrics Manually
# # Goal
# # 
# # Understand the mathematics before relying on libraries.
# # 
# # Create:
# # 
# # TP = 80
# # TN = 90
# # FP = 10
# # FN = 20
# # 
# # Calculate:
# # 
# # Accuracy
# # Precision
# # Recall
# # F1
# # Your task
# # 
# # Do this without sklearn metrics first.
# 
# TP = 80
# TN = 90
# FP = 10
# FN = 20
# 
# Accuracy=(TP+TN)/(TP+TN+FP+FN)
# Precision=TP/(TP+FP)
# Recall=TP/(TP+FN)
# F1=2*((Precision*Recall)/(Precision+Recall))
# 
# print("\nAccuracy :",Accuracy)
# print("\nPrecision :",Precision)
# print("\nRecall :",Recall)
# print("\nF1 :",F1)



# # Program 2 ⭐ — Classification Model Evaluation

# # Use the student dataset/model you worked with on Day 32.

# # Pipeline:

# # Student Dataset
      # # ↓
# # X / y
      # # ↓
# # Train/Test Split
      # # ↓
# # Logistic Regression
      # # ↓
# # Prediction
      # # ↓
# # Evaluation

# # Use:

# # from sklearn.metrics import (
    # # accuracy_score,
    # # precision_score,
    # # recall_score,
    # # f1_score,
    # # confusion_matrix
# # )

# # Then calculate:

# # accuracy_score(y_test, y_pred)
# # precision_score(y_test, y_pred)
# # recall_score(y_test, y_pred)
# # f1_score(y_test, y_pred)
# # confusion_matrix(y_test, y_pred)

# # Print all five.

# # Your output should look conceptually like:
# # Accuracy: 0.90
# # Precision: 0.88
# # Recall: 0.92
# # F1 Score: 0.90


# # Confusion Matrix:
# # [[... ...]
 # # [... ...]]

# # Your actual numbers will depend on your dataset.

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import (accuracy_score,confusion_matrix,precision_score,recall_score,f1_score)


# data = {
    # "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                    # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                    # 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],

    # "Attendance": [55, 60, 65, 70, 75, 80, 85, 90, 92, 95,
                    # 50, 58, 68, 72, 78, 82, 88, 91, 94, 96,
                    # 62, 67, 73, 77, 81, 86, 89, 93, 97, 98],

    # "Previous_Marks": [35, 40, 45, 50, 55, 60, 65, 70, 75, 80,
                       # 30, 38, 43, 48, 53, 58, 63, 68, 73, 78,
                       # 42, 47, 52, 57, 62, 67, 72, 77, 82, 88],

    # "Assignments_Completed": [2, 3, 4, 5, 6, 7, 8, 9, 9, 10,
                              # 1, 2, 3, 5, 6, 7, 8, 9, 10, 10,
                              # 3, 4, 5, 6, 7, 8, 9, 9, 10, 10],

    # "Passed": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1,
               # 0, 0, 0, 0, 1, 1, 1, 1, 1, 1,
               # 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
# }

# df=pd.DataFrame(data)

# X=df[["Study_Hours","Attendance","Previous_Marks","Assignments_Completed"]]

# y=df["Passed"]

# X_train,X_test,y_train,y_test=train_test_split(
    # X,
    # y,
    # test_size=0.2,
    # random_state=42,
    # stratify=y
# )

# model=LogisticRegression()

# model.fit(X_train,y_train)

# prediction=model.predict(X_test)

# accuracy=accuracy_score(y_test,prediction)
# print("\nAccuracy :",accuracy)
# precision=precision_score(y_test,prediction)
# print("\nPrecision :",precision)
# recall=recall_score(y_test,prediction)
# print("\nRecall Score :",recall)
# f1=f1_score(y_test,prediction)
# print("\nF1 Score :",f1)
# matrix=confusion_matrix(y_test,prediction)
# print("\nConfusion Matrix :\n",matrix)


# # Program 3 ⭐ — Regression Evaluation

# # Use the student-performance regression problem from Day 31.

# # Features:

# # Study Hours
# # Attendance
# # Previous Marks

# # Target:

# # Marks

# # Train:

# # LinearRegression()

# # Then calculate:

# # MAE
# # MSE
# # RMSE
# # R²

# # Use:

# # from sklearn.metrics import (
    # # mean_absolute_error,
    # # mean_squared_error,
    # # r2_score
# # )

# # For RMSE:

# # import numpy as np


# # rmse = np.sqrt(mean_squared_error(y_test, y_pred))

# # Print:

# # MAE:
# # MSE:
# # RMSE:
# # R²:
# # Think about this

# # If:

# # MAE = 4

# # you should be able to explain:

# # The model's predictions are off by about 4 marks on average.

# # That's more valuable in an interview than simply saying:

# # "MAE is a regression metric."


# import pandas as pd
# import numpy as np
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import (mean_absolute_error,mean_squared_error,r2_score)


# data = {
    # "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                    # 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                    # 1, 3, 5, 7, 9, 2, 4, 6, 8, 10],

    # "Attendance": [55, 60, 65, 70, 75, 80, 85, 90, 92, 95,
                    # 58, 63, 68, 73, 78, 83, 88, 91, 94, 97,
                    # 52, 64, 76, 86, 93, 57, 69, 81, 89, 96],

    # "Previous_Marks": [35, 40, 45, 50, 55, 60, 65, 70, 75, 80,
                       # 38, 43, 48, 53, 58, 63, 68, 73, 78, 83,
                       # 32, 46, 58, 67, 76, 36, 51, 64, 72, 85],

    # "Marks": [38, 43, 48, 54, 61, 66, 72, 78, 84, 89,
              # 41, 47, 52, 58, 64, 70, 75, 81, 86, 92,
              # 35, 49, 60, 69, 80, 40, 55, 67, 76, 90]
# }

# df=pd.DataFrame(data)

# X=df[["Study_Hours","Attendance","Previous_Marks"]]

# y=df["Marks"]

# X_train,X_test,y_train,y_test=train_test_split(
    # X,
    # y,
    # test_size=0.2,
    # random_state=42
    # )

# model=LinearRegression()

# model.fit(X_train,y_train)

# y_pred=model.predict(X_test)

# mse=mean_squared_error(y_test,y_pred)
# mae=mean_absolute_error(y_test,y_pred)
# r2=r2_score(y_test,y_pred)

# rmse=np.sqrt(mean_squared_error(y_test,y_pred))

# print("\nMean Absolute Error is :",mae)
# print("\nMean Squared Error is :",mse)
# print("\nRoot Mean Squared Error is :",rmse)
# print("\nR2 Score is :",r2)




# Program 4 ⭐ — Compare Two Classification Models

# Now we move from:

# "Is my model good?"

# to:

# "Which model is better?"

# Use the same dataset.

# Train:

# Model 1 → Logistic Regression
# Model 2 → another classifier you've learned

# If you haven't learned another classifier yet, use two Logistic Regression configurations with different decision thresholds.

# For each model calculate:

# Accuracy
# Precision
# Recall
# F1

# Create a comparison table:

# Model              Accuracy   Precision   Recall   F1
# -------------------------------------------------------
# Model 1              ...        ...        ...     ...
# Model 2              ...        ...        ...     ...
# Important lesson

# Don't automatically choose:

# highest accuracy

# Instead ask:

# What does the application care about?

# For example:

# Fraud detection

# might prioritize recall.

# A spam filter might care strongly about precision.


# import pandas as pd

# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.tree import DecisionTreeClassifier

# from sklearn.metrics import (
    # accuracy_score,
    # precision_score,
    # recall_score,
    # f1_score
# )

# data = {
    # "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                    # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                    # 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],

    # "Attendance": [55, 60, 65, 70, 75, 80, 85, 90, 92, 95,
                   # 50, 58, 68, 72, 78, 82, 88, 91, 94, 96,
                   # 62, 67, 73, 77, 81, 86, 89, 93, 97, 98],

    # "Previous_Marks": [35, 40, 45, 50, 55, 60, 65, 70, 75, 80,
                       # 30, 38, 43, 48, 53, 58, 63, 68, 73, 78,
                       # 42, 47, 52, 57, 62, 67, 72, 77, 82, 88],

    # "Assignments_Completed": [2, 3, 4, 5, 6, 7, 8, 9, 9, 10,
                              # 1, 2, 3, 5, 6, 7, 8, 9, 10, 10,
                              # 3, 4, 5, 6, 7, 8, 9, 9, 10, 10],

    # "Passed": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1,
               # 0, 0, 0, 0, 1, 1, 1, 1, 1, 1,
               # 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
# }

# df=pd.DataFrame(data)

# X=df[["Study_Hours","Attendance","Previous_Marks","Assignments_Completed"]]

# y=df["Passed"]

# X_train,X_test,y_train,y_test=train_test_split(
    # X,
    # y,
    # test_size=0.2,
    # random_state=42,
    # stratify=y
# )

# model1=LogisticRegression()

# model1.fit(X_train,y_train)

# y_pred1=model1.predict(X_test)

# accuracy1=accuracy_score(y_test,y_pred1)
# precision1=precision_score(y_test,y_pred1)
# recall1=recall_score(y_test,y_pred1)
# f1_1=f1_score(y_test,y_pred1)

# model2=DecisionTreeClassifier()

# model2.fit(X_train,y_train)

# y_pred2=model2.predict(X_test)

# accuracy2=accuracy_score(y_test,y_pred2)
# precision2=precision_score(y_test,y_pred2)
# recall2=recall_score(y_test,y_pred2)
# f1_2=f1_score(y_test,y_pred2)

# comparsion=pd.DataFrame({
    # "Models":["Logistic Regression","Decision Tree"],
    # "Accuracy":[accuracy1,accuracy2],
    # "Precision":[precision1,precision2],
    # "Recall":[recall1,recall2],
    # "F1_score":[f1_1,f1_2]
# })
# print("\nComparsion :")
# print(comparsion)






# Program 5 ⭐ — Complete Model Evaluation Pipeline

# This is today's most important coding exercise.

# Build:

# Load Dataset
     # ↓
# EDA
     # ↓
# X / y
     # ↓
# Train/Test Split
     # ↓
# Train Model
     # ↓
# Predictions
     # ↓
# Confusion Matrix
     # ↓
# Accuracy
     # ↓
# Precision
     # ↓
# Recall
     # ↓
# F1
     # ↓
# Interpret Results

# Use the student classification dataset from Day 32.

# Your program should produce something like:

# ========== MODEL EVALUATION ==========


# Accuracy  : 0.xx
# Precision : 0.xx
# Recall    : 0.xx
# F1 Score  : 0.xx


# Confusion Matrix:
# [[... ...]
 # [... ...]]


# ========== INTERPRETATION ==========


# The model correctly classified ...
# Precision indicates ...
# Recall indicates ...
# F1 score indicates ...
# This is the first exercise where I want you to think like an engineer.

# Don't just print numbers.

# Interpret them.


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (accuracy_score,precision_score,recall_score,f1_score,confusion_matrix)


data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                    2, 3, 4, 5, 6, 7, 8, 9, 10, 11],

    "Attendance": [55, 60, 65, 70, 75, 80, 85, 90, 92, 95,
                   50, 58, 68, 72, 78, 82, 88, 91, 94, 96,
                   62, 67, 73, 77, 81, 86, 89, 93, 97, 98],

    "Previous_Marks": [35, 40, 45, 50, 55, 60, 65, 70, 75, 80,
                       30, 38, 43, 48, 53, 58, 63, 68, 73, 78,
                       42, 47, 52, 57, 62, 67, 72, 77, 82, 88],

    "Assignments_Completed": [2, 3, 4, 5, 6, 7, 8, 9, 9, 10,
                              1, 2, 3, 5, 6, 7, 8, 9, 10, 10,
                              3, 4, 5, 6, 7, 8, 9, 9, 10, 10],

    "Passed": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1,
               0, 0, 0, 0, 1, 1, 1, 1, 1, 1,
               0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
}

df=pd.DataFrame(data)

print("\nFirst Five Lines of Dataset :")
print(df.head())

print("\nMissing Values :")
print(df.isnull().sum())

print("\nDuplicate Rows :")
print(df.duplicated().sum())

print("\nBasic Information of Datset :")
df.info()

print("\nStatistical Information of the Datset :")
print(df.describe())

X=df[["Study_Hours","Attendance","Previous_Marks","Assignments_Completed"]]

y=df["Passed"]

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model=LogisticRegression()

model.fit(X_train,y_train)

y_pred=model.predict(X_test)

matrix=confusion_matrix(y_test,y_pred)
print("\nConfusion Matrix :\n",matrix)

accuracy=accuracy_score(y_test,y_pred)
print("\nAccuracy :",accuracy)

precision=precision_score(y_test,y_pred)
print("\nPrecision :",precision)

recall=recall_score(y_test,y_pred)
print("\nRecall :",recall)

f1=f1_score(y_test,y_pred)
print("\nF1 Score :",f1)