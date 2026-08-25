# Program 3 — Learning Rate Experiment 🔥
# 
# Keep:
# 
# n_estimators = 100
# 
# Try:
# 
# learning_rate = 0.01
# learning_rate = 0.05
# learning_rate = 0.1
# learning_rate = 0.2
# 
# Record:
# 
# Learning Rate
# Accuracy
# F1
# 
# Then explain:
# 
# How did changing the learning rate affect the model?

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score,f1_score

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

learning=[0.01,0.05,0.1,0.2]

for rate in learning :
    model=GradientBoostingClassifier(
        n_estimators=100,
        learning_rate=rate,
        random_state=42
    )

    model.fit(X_train,y_train)

    y_pred=model.predict(X_test)

    accuracy=accuracy_score(y_test,y_pred)

    f1=f1_score(y_test,y_pred)

    print("\nLearning Rate  :",rate)
    print("\nAccuracy_Score :",accuracy)
    print("\nF1_Score       :",f1)
    print("\n-----------------------------------")

print("\nObservation :\n")
print("Even when the learning rate is increasing , the accuracy & f1_score doesn't change .")