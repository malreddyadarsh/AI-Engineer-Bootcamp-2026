# Program 2 — Cross-Validation Comparison
# 
# Compare:
# 
# Logistic Regression
# Decision Tree
# Random Forest
# Gradient Boosting
# 
# Use the same:
# 
# 5-fold CV
# 
# and calculate:
# 
# Mean F1
# Standard Deviation
# 
# Create:
# 
# Model	Mean CV F1	Std
# Logistic Regression	...	...
# Decision Tree	...	...
# Random Forest	...	...
# Gradient Boosting	...	...
# Goal
# 
# Determine:
# 
# Which model performs consistently across different folds?

import pandas as pd
from sklearn.model_selection import train_test_split,StratifiedKFold,cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier


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

# Logistic Regression
model1=LogisticRegression()

cv=StratifiedKFold(
    shuffle=True,
    n_splits=5,
    random_state=42
)

score1=cross_val_score(
    model1,
    X_train,
    y_train,
    cv=cv,
    scoring="f1"
)

mean1=score1.mean()
std1=score1.std()


# Decision_Tree
model2=DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)

score2=cross_val_score(
    model2,
    X_train,
    y_train,
    cv=cv,
    scoring="f1"
)

mean2=score2.mean()
std2=score2.std()


# Random_Forest
model3=RandomForestClassifier(
    n_estimators=50,
    max_depth=3,
    random_state=42
)

score3=cross_val_score(
    model3,
    X_train,
    y_train,
    cv=cv,
    scoring="f1"
)

mean3=score3.mean()
std3=score3.std()

# Gradient Boosting

model4=GradientBoostingClassifier(
    n_estimators=100,
    max_depth=5,
    learning_rate=0.05,
    subsample=0.85,
    random_state=42
)

score4=cross_val_score(
    model4,
    X_train,
    y_train,
    cv=cv,
    scoring="f1"
)

mean4=score4.mean()
std4=score4.std()

comparison=pd.DataFrame({
    "Models":["Logistic_Regression","Decision_Tree","Random_Forest","Gradient_Boosting"],
    "Mean_CV_F1":[mean1,mean2,mean3,mean4],
    "STD":[std1,std2,std3,std4]
})

print("\nComparison Table :")
print(comparison)


print("\nWhich model performs consistently across different folds?")
print("\nFor this dataset, Logistic Regression model performed consistently.")