# # Program 3 — Decision Tree vs Logistic Regression
# 
# Use the same classification dataset.
# 
# Train:
# 
# ```
# Logistic Regression
# ```
# 
# Decision Tree
# 
# Compare:
# 
# ```
# Accuracy
# ```
# 
# Precision
# 
# Recall
# 
# F1
# 
# Example structure:
# 
# ```
# Model                 Accuracy    Precision    Recall    F1
# ```
# 
# \-------------------------------------------------------------
# 
# Logistic Regression      ...          ...         ...      ...
# 
# Decision Tree            ...          ...         ...      ...
# 
# Then write:
# 
# > Which model performed better on the test data and why might that be?
# 
# Don't simply choose the larger accuracy.
# 
# Look at all the metrics. 


import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score


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

    "Passed": [
        0, 0, 0, 0, 0,
        0, 0, 1, 1, 1,
        1, 1, 1, 1, 1,
        1, 1, 1, 1, 1,
        1, 0, 0, 1, 1
    ]
})

X=data[["Study_Hours","Attendance","Previous_Marks"]]

y=data["Passed"]

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model1=LogisticRegression()

model1.fit(X_train,y_train)

pred_1=model1.predict(X_test)

accuracy_1=accuracy_score(y_test,pred_1)
precision_1=precision_score(y_test,pred_1)
recall_1=recall_score(y_test,pred_1)
f1_1=f1_score(y_test,pred_1)

model2=DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)

model2.fit(X_train,y_train)

pred_2=model2.predict(X_test)

accuracy_2=accuracy_score(y_test,pred_2)
precision_2=precision_score(y_test,pred_2)
recall_2=recall_score(y_test,pred_2)
f1_2=f1_score(y_test,pred_2)

comparsion=pd.DataFrame({
    "Models":["LogisticRegression","DecisionTree"],
    "Accuracy_Score":[accuracy_1,accuracy_2],
    "Precision_Score":[precision_1,precision_2],
    "Recall_Score":[recall_1,recall_2],
    "F1_Score":[f1_1,f1_2]
})

print("Comparsion Complex :")
print(comparsion)