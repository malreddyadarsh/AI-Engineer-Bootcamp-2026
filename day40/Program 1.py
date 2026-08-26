# Program 1 — Cross-Validation

# Use your student classification dataset.

# Train:

# Logistic Regression

# Perform:

# 5-Fold Cross-Validation

# Calculate:

# CV Scores
# Mean CV Score
# Standard Deviation

# Use:

# cross_val_score()
# Your output should look conceptually like:
# Fold Scores:
# [... ... ... ... ...]

# Mean F1:
# ...

# Standard Deviation:
# ...



import pandas as pd
from sklearn.model_selection import cross_val_score,train_test_split,StratifiedKFold
from sklearn.linear_model import LogisticRegression

data = {
    "Age": [
        18,19,18,20,21,19,20,22,18,21,
        19,20,18,22,21,19,20,18,22,21,
        20,19,18,22,21,19,20,18,22,21
    ],

    "Study_Hours": [
        2.0,3.0,4.0,5.0,6.0,2.5,4.5,7.0,1.5,5.5,
        3.5,6.0,2.0,8.0,4.0,2.5,5.0,3.0,7.5,3.5,
        6.5,2.0,4.5,8.0,5.0,3.0,6.0,1.0,7.0,4.0
    ],

    "Attendance": [
        65,70,75,80,85,68,78,90,60,82,
        72,88,64,92,76,66,81,71,91,73,
        86,63,77,94,80,69,84,58,89,74
    ],

    "Assignments_Completed": [
        6,7,8,9,9,6,8,10,5,9,
        7,10,6,10,8,6,9,7,10,7,
        9,5,8,10,9,7,9,4,10,8
    ],

    "Previous_Marks": [
        55,62,68,72,78,58,70,85,50,75,
        64,80,53,88,69,57,74,61,87,65,
        82,52,71,90,76,60,79,48,84,67
    ],

    "Passed": [
        0,0,1,1,1,0,1,1,0,1,
        0,1,0,1,1,0,1,0,1,0,
        1,0,1,1,1,0,1,0,1,0
    ]
}

df = pd.DataFrame(data)

X=df[["Age","Study_Hours","Attendance","Assignments_Completed","Previous_Marks"]]

y=df["Passed"]

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model=LogisticRegression()

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)
scores=cross_val_score(
    model,
    X_train,
    y_train,
    cv=5,
    scoring="f1"
)

print("Fold Scores :")
print(scores)

print("\nMean F1 :")
print(scores.mean())

print("\nStandard Deviation :")
print(scores.std())