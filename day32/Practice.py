# # Program 1 ⭐ — Your First Classification Model
# # 
# # Create a student dataset:
# # 
# # Study Hours
# # Attendance
# # Passed
# # 
# # Example:
# # 
# # Study Hours   Attendance   Passed
# # 2             60           0
# # 3             65           0
# # 4             70           1
# # 5             75           1
# # 6             80           1
# # 8             90           1
# # 
# # Use:
# # 
# # LogisticRegression
# # 
# # Perform:
# # 
# # X/y
 # # ↓
# # Train/Test Split
 # # ↓
# # Train
 # # ↓
# # Predict
# # 
# # Display:
# # 
# # Actual values
# # Predicted values
# 
# import pandas as pd
# 
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# 
# data = {
    # "Study_Hours": [
        # 1, 2, 2, 3, 3,
        # 4, 4, 5, 5, 6,
        # 6, 7, 7, 8, 8,
        # 9, 9, 10, 10, 11
    # ],
# 
    # "Attendance": [
        # 50, 55, 60, 62, 65,
        # 68, 70, 72, 75, 78,
        # 80, 82, 85, 87, 90,
        # 91, 93, 94, 96, 98
    # ],
# 
    # "Passed": [
        # 0, 0, 0, 0, 0,
        # 0, 1, 1, 1, 1,
        # 1, 1, 1, 1, 1,
        # 1, 1, 1, 1, 1
    # ]
# }
# 
# df=pd.DataFrame(data)
# 
# X=df[["Study_Hours","Attendance"]]
# 
# y=df["Passed"]
# 
# X_train,X_test,y_train,y_test=train_test_split(
    # X,
    # y,
    # test_size=0.2,
    # random_state=42
# )
# 
# model=LogisticRegression()
# 
# model.fit(X_train,y_train)
# 
# y_pred=model.predict(X_test)
# 
# 
# print("\nActual Values :")
# print(y_test)
# print("\nPredicted Values :")
# print(y_pred)
# 
# 



# # GIVE ME INLY DATA SET Program 2 — Probability Predictions ⭐
# # Use:
# # model.predict_proba(X_test)
# # Understand the difference between:
# # model.predict()
# # and:
# # model.predict_proba()
# # Example:
# # Probability:
# # 
# # Class 0 → 0.18
# # Class 1 → 0.82
# # Then the model predicts:
# # Class 1

# import pandas as pd

# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression

# data = {
    # "Study_Hours": [
        # 1, 2, 2, 3, 3,
        # 4, 4, 5, 5, 6,
        # 6, 7, 7, 8, 8,
        # 9, 9, 10, 10, 11
    # ],

    # "Attendance": [
        # 50, 55, 60, 62, 65,
        # 68, 70, 72, 75, 78,
        # 80, 82, 85, 87, 90,
        # 91, 93, 94, 96, 98
    # ],

    # "Passed": [
        # 0, 0, 0, 0, 0,
        # 0, 1, 1, 1, 1,
        # 1, 1, 1, 1, 1,
        # 1, 1, 1, 1, 1
    # ]
# }

# df=pd.DataFrame(data)

# X=df[["Study_Hours","Attendance"]]

# y=df["Passed"]

# X_train,X_test,y_train,y_test=train_test_split(
    # X,
    # y,
    # test_size=0.2,
    # random_state=42
# )

# model=LogisticRegression()

# model.fit(X_train,y_train)

# predictions=model.predict(X_test)

# probability=model.predict_proba(X_test)

# print("\nProbability :")
# print(probability)

# print("\nModel Predictions :")
# print(predictions)




# # GIVE ME ONLY DATASET Program 3 — Confusion Matrix

# # Calculate:

# # -  TP 
# # -  TN 
# # -  FP 
# # -  FN 

# # Use:

# # ```
# # from sklearn.metrics import confusion_matrix
# # ```

# # Then visualize it using a heatmap.

# # You should be able to look at the matrix and explain what every cell means.

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import confusion_matrix
# data = {
    # "Study_Hours": [
        # 1, 2, 2, 3, 3,
        # 4, 4, 5, 5, 6,
        # 6, 7, 7, 8, 8,
        # 9, 9, 10, 10, 11
    # ],

    # "Attendance": [
        # 50, 55, 60, 62, 65,
        # 68, 70, 72, 75, 78,
        # 80, 82, 85, 87, 90,
        # 91, 93, 94, 96, 98
    # ],

    # "Passed": [
        # 0, 0, 0, 0, 0,
        # 0, 1, 1, 1, 1,
        # 1, 1, 1, 1, 1,
        # 1, 1, 1, 1, 1
    # ]
# }

# df = pd.DataFrame(data)

# X=df[["Study_Hours","Attendance"]]

# y=df["Passed"]

# X_train,X_test,y_train,y_test=train_test_split(
    # X,
    # y,
    # test_size=0.2,
    # random_state=42
# )

# model=LogisticRegression()

# model.fit(X_train,y_train)

# predictions=model.predict(X_test)

# matrix=confusion_matrix(y_test,predictions)

# print("\nConfusion Matrix :")
# print(matrix)



# # Program 4 — Precision, Recall & F1

# # Calculate:

# # precision_score()
# # recall_score()
# # f1_score()

# # Then answer:

# # Which metric would you prioritize for this problem, and why?

# # Test yourself with three scenarios:

# # Spam filter

# # Precision may matter significantly.

# # Disease screening

# # Recall may matter significantly.

# # Fraud detection

# # The trade-off depends on the cost of missed fraud versus false alarms.

# # There isn't one universally best metric.

# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import (precision_score,recall_score,f1_score)

# data = {
    # "Study_Hours": [
        # 1, 2, 2, 3, 3,
        # 4, 4, 5, 5, 6,
        # 6, 7, 7, 8, 8,
        # 9, 9, 10, 10, 11
    # ],

    # "Attendance": [
        # 50, 55, 60, 62, 65,
        # 68, 70, 72, 75, 78,
        # 80, 82, 85, 87, 90,
        # 91, 93, 94, 96, 98
    # ],

    # "Passed": [
        # 0, 0, 0, 0, 0,
        # 0, 1, 1, 1, 1,
        # 1, 1, 1, 1, 1,
        # 1, 1, 1, 1, 1
    # ]
# }

# df = pd.DataFrame(data)

# X=df[["Study_Hours","Attendance"]]

# y=df["Passed"]

# X_train,X_test,y_train,y_test=train_test_split(
    # X,
    # y,
    # test_size=0.2,
    # random_state=42
# )

# model=LogisticRegression()

# model.fit(X_train,y_train)

# prediction=model.predict(X_test)

# precision=precision_score(y_test,prediction)

# recall=recall_score(y_test,prediction)

# f1=f1_score(y_test,prediction)

# print("\nPrecision Score is :",precision)

# print("\nRecall Score is :",recall)

# print("\nF1 Score is :",f1)



# Program 5 ⭐ — Complete Classification Pipeline

# Create a realistic dataset such as:

# Study Hours
# Attendance
# Previous Marks
# Assignments Completed
# Passed

# Build:

# Load data
   # ↓
# EDA
   # ↓
# X/y
   # ↓
# Train/Test Split
   # ↓
# Logistic Regression
   # ↓
# Predictions
   # ↓
# Confusion Matrix
   # ↓
# Accuracy
# Precision
# Recall
# F1

# Then write 3 conclusions.


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (confusion_matrix,accuracy_score,precision_score,recall_score,f1_score)


data = {
    "Study_Hours": [
        1, 2, 2, 3, 3,
        4, 4, 5, 5, 6,
        6, 7, 7, 8, 8,
        9, 9, 10, 10, 11
    ],

    "Attendance": [
        45, 50, 55, 58, 60,
        62, 65, 68, 70, 72,
        75, 78, 80, 82, 85,
        88, 90, 92, 95, 98
    ],

    "Previous_Marks": [
        35, 40, 42, 45, 48,
        50, 52, 55, 58, 60,
        62, 65, 68, 70, 72,
        75, 78, 82, 85, 88
    ],

    "Assignments_Completed": [
        2, 3, 3, 4, 4,
        5, 5, 6, 6, 7,
        7, 8, 8, 9, 9,
        10, 10, 11, 11, 12
    ],

    "Passed": [
        0, 0, 0, 0, 0,
        0, 0, 0, 0, 1,
        1, 1, 1, 1, 1,
        1, 1, 1, 1, 1
    ]
}

df = pd.DataFrame(data)

df.to_csv("day32/Practice5.csv",index=False)

df=pd.read_csv("day32/Practice5.csv")

print("\nFirst Five Rows of Dataset :")
print(df.head())

print("\nMissing Values of Each Column :")
print(df.isnull().sum())

print("\nColumns Names of Dataset :")
print(df.columns)

print("\nShape of Dataset :")
print(df.shape)

print("\n Basic Information Of the Datset :")
df.info()

print("Statistical Information of the Dataset :")
print(df.describe())

X=df[["Study_Hours","Attendance","Previous_Marks","Assignments_Completed"]]

y=df["Passed"]

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model=LogisticRegression()

model.fit(X_train,y_train)

prediction=model.predict(X_test)

matrix=confusion_matrix(y_test,prediction)
print("\nConfusion Matrix :\n",matrix)

accuracy=accuracy_score(y_test,prediction)
print("Accuracy Score Is :",accuracy)

precision=precision_score(y_test,prediction)
print("\nPrecision Matrix :",precision)

recall=recall_score(y_test,prediction)
print("\nRecall Score :",recall)

f1=f1_score(y_test,prediction)
print("\nF1 Score :",f1)