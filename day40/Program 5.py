# Program 5 — Gradient Boosting Hyperparameter Tuning 🔥
# 
# Tune:
# 
# n_estimators
# learning_rate
# max_depth
# 
# Example search space:
# 
# param_grid = {
    # "n_estimators": [50, 100, 150, 200],
    # "learning_rate": [0.01, 0.05, 0.1, 0.2],
    # "max_depth": [2, 3, 4]
# }
# 
# Use:
# 
# GridSearchCV
# 
# Then compare:
# 
# Before tuning
# vs
# After tuning
# 
# using:
# 
# Accuracy
# Precision
# Recall
# F1




import pandas as pd
from sklearn.model_selection import train_test_split,StratifiedKFold,GridSearchCV
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score

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


# BEFORE TUNING

before_model = GradientBoostingClassifier(
    random_state=42
)

before_model.fit(X_train, y_train)

before_pred = before_model.predict(X_test)

before_accuracy = accuracy_score(y_test, before_pred)
before_precision = precision_score(y_test, before_pred)
before_recall = recall_score(y_test, before_pred)
before_f1 = f1_score(y_test, before_pred)

print("\n========== BEFORE TUNING ==========")

print("\nAccuracy :")
print(before_accuracy)

print("\nPrecision :")
print(before_precision)

print("\nRecall :")
print(before_recall)

print("\nF1 Score :")
print(before_f1)


# AFTER TUNING 


cv=StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

model=GradientBoostingClassifier(
    random_state=42
)

param_grid={
    "n_estimators": [50, 100, 150, 200],
    "learning_rate": [0.01, 0.05, 0.1, 0.2],
    "max_depth": [2, 3, 4]
}

grid_search=GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=cv,
    scoring="f1",
    n_jobs=-1
)

grid_search.fit(X_train,y_train)

best_model=grid_search.best_estimator_

y_pred=best_model.predict(X_test)

accuracy=accuracy_score(y_test,y_pred)

precision=precision_score(y_test,y_pred)

recall=recall_score(y_test,y_pred)

f1=f1_score(y_test,y_pred)

print("\n==========AFTER TUNING========")
print("\nAccuracy :")
print(accuracy)

print("\nPrecision :")
print(precision)

print("\nRecall :")
print(recall)

print("\nF1_Score :")
print(f1)




comparison = pd.DataFrame({
    "Metric": [
        "Accuracy",
        "Precision",
        "Recall",
        "F1"
    ],

    "Before Tuning": [
        before_accuracy,
        before_precision,
        before_recall,
        before_f1
    ],

    "After Tuning": [
        accuracy,
        precision,
        recall,
        f1
    ]
})

print("\n========== BEFORE vs AFTER TUNING ==========")
print(comparison)