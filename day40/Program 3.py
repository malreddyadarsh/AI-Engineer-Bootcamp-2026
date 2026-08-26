# Program 3 — GridSearchCV for Decision Tree
# 
# Tune:
# 
# max_depth
# min_samples_split
# min_samples_leaf
# 
# Example search space:
# 
# param_grid = {
    # "max_depth": [2, 3, 4, 5, 6, 8, 10],
    # "min_samples_split": [2, 5, 10],
    # "min_samples_leaf": [1, 2, 4]
# }
# 
# Use:
# 
# GridSearchCV
# 
# Then print:
# 
# Best Parameters
# Best CV Score
# Final Test Score


import pandas as pd
from sklearn.model_selection import StratifiedKFold,GridSearchCV,train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score

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

param_grid={
    "max_depth": [2, 3, 4, 5, 6, 8, 10],
    "min_samples_split": [2, 5, 10],
    "min_samples_leaf": [1, 2, 4]
}

cv=StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

model=DecisionTreeClassifier(
    random_state=42
)

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

final_score=f1_score(y_test,y_pred)

print("\nBest Parameters :")
print(grid_search.best_params_)

print("\nBest CV Score :")
print(grid_search.best_score_)

print("\nFinal Test Score :")
print(final_score)