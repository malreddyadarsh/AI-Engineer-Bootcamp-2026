# Program 4 — Three-Way Model Comparison
# 
# Use the same dataset and same train/test split.
# 
# Compare:
# 
# Logistic Regression
# Decision Tree
# Random Forest
# Gradient Boosting
# 
# Create:
# 
# Model	Accuracy	Precision	Recall	F1
# Logistic Regression	...	...	...	...
# Decision Tree	...	...	...	...
# Random Forest	...	...	...	...
# Gradient Boosting	...	...	...	...
# 
# This is a very important ML engineering exercise.
# 
# You're learning to evaluate algorithms rather than blindly selecting one.


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score

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

    "Passed": [
        0, 1, 0, 1, 1,
        1, 0, 1, 1, 1,
        0, 1, 1, 0, 1,
        1, 1, 1, 1, 1,
        0, 1, 1, 0, 1,
        1, 1, 1, 1, 1,
        0, 1, 1, 1, 0,
        1, 0, 1, 1, 1,
        1, 0, 1, 1, 1,
        0, 1, 1, 1, 0
    ]
}

df = pd.DataFrame(data)

X=df[["Study_Hours","Attendance","Previous_Marks","Assignments_Completed"]]

y=df["Passed"]

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model1=LogisticRegression()
model1.fit(X_train,y_train)
y_pred1=model1.predict(X_test)
accuracy_1=accuracy_score(y_test,y_pred1)
precision_1=precision_score(y_test,y_pred1)
recall_1=recall_score(y_test,y_pred1)
f1_1=f1_score(y_test,y_pred1)


model2=DecisionTreeClassifier(
    max_depth=5,
    random_state=42
)

model2.fit(X_train,y_train)
y_pred2=model2.predict(X_test)
accuracy_2=accuracy_score(y_test,y_pred2)
precision_2=precision_score(y_test,y_pred2)
recall_2=recall_score(y_test,y_pred2)
f1_2=f1_score(y_test,y_pred2)

model3=RandomForestClassifier(
    n_estimators=50,
    max_depth=3,
    random_state=42
)

model3.fit(X_train,y_train)
y_pred3=model3.predict(X_test)
accuracy_3=accuracy_score(y_test,y_pred3)
precision_3=precision_score(y_test,y_pred3)
recall_3=recall_score(y_test,y_pred3)
f1_3=f1_score(y_test,y_pred3)


model4=GradientBoostingClassifier(
    n_estimators=50,
    learning_rate=0.05,
    max_depth=2,
    subsample=0.7,
    random_state=42
)

model4.fit(X_train,y_train)
y_pred4=model4.predict(X_test)
accuracy_4=accuracy_score(y_test,y_pred4)
precision_4=precision_score(y_test,y_pred4)
recall_4=recall_score(y_test,y_pred4)
f1_4=f1_score(y_test,y_pred4)

comparison=pd.DataFrame({
    "Models":["LogisticRegression","DecisionTree","RandomForest","GraidentBoosting"],
    "Accuracy_Score":[accuracy_1,accuracy_2,accuracy_3,accuracy_4],
    "Pecision_Score":[precision_1,precision_2,precision_3,precision_4],
    "Recall_Score":[recall_1,recall_2,recall_3,recall_4],
    "F1_Score":[f1_1,f1_2,f1_3,f1_4]
})


print("\nComparison Table :\n")
print(comparison)

print("\nObservation :\n")
print("For this dataset , all the models performed exactly.")