# # 25. Mini Project
# 
# ## Student Performance — Model Selection & Tuning
# 
# This is an important project because it combines the last several days.
# 
# Build:
# 
# ```
# ```
# 
# ```
# Student Dataset
      # ↓
# EDA
      # ↓
# Feature Engineering
      # ↓
# Train/Test Split
      # ↓
# Baseline Models
      # ↓
# Cross-Validation
      # ↓
# Hyperparameter Tuning
      # ↓
# Best Models
      # ↓
# Final Test Evaluation
      # ↓
# Model Selection
# ```
# 
# Models:
# 
# ```
# ```
# 
# ```
# Logistic Regression
# Decision Tree
# Random Forest
# Gradient Boosting
# ```
# 
# ---
# 
# # 📊 26. Your Final Comparison
# 
# Create something like:
# 
# | ModelCV F1Test F1AccuracyPrecisionRecall |   |   |   |   |   |
# | ---------------------------------------- | - | - | - | - | - |
# | Logistic Regression                      |   |   |   |   |   |
# | Decision Tree                            |   |   |   |   |   |
# | Random Forest                            |   |   |   |   |   |
# | Gradient Boosting                        |   |   |   |   |   |
# 
# Then:
# 
# ### Tune the best 2 models.
# 
# For example:
# 
# ```
# ```
# 
# ```
# Random Forest
# Gradient Boosting
# ```
# 
# Then create:
# 
# | ModelBefore TuningAfter Tuning |   |   |
# | ------------------------------ | - | - |
# | Random Forest                  |   |   |
# | Gradient Boosting              |   |   |
# 
# Finally answer:
# 
# > **Which model would you select for deployment? GIVE ME DATSET FOR IT** 



import pandas as pd
from sklearn.model_selection import train_test_split,StratifiedKFold,RandomizedSearchCV,cross_val_score,GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
from sklearn.metrics import accuracy_score,f1_score,precision_score,recall_score

# Student Dataset
data = {
    "Student_ID": [
        "S001","S002","S003","S004","S005",
        "S006","S007","S008","S009","S010",
        "S011","S012","S013","S014","S015",
        "S016","S017","S018","S019","S020",
        "S021","S022","S023","S024","S025",
        "S026","S027","S028","S029","S030"
    ],

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


# EDA
print("\n=================EDA==================")
print("\nFirst Five Rows of Dataset :")
print(df.head())

print("\nMissing Values in the Dataset :")
print(df.isnull().sum().sum())

print("\nDuplicate Rows in the Dataset :")
print(df.duplicated().sum())

print("\nBasic Information of the Dataset :")
df.info()

print("\nStatistical Information of the Dataset :")
print(df.describe())



X=df[["Age","Study_Hours","Attendance","Assignments_Completed","Previous_Marks","Total_Marks"]]

y=df["Passed"]


# Train/Test Split

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model1=LogisticRegression()

model2=DecisionTreeClassifier(random_state=42)

model3=RandomForestClassifier(random_state=42)

model4=GradientBoostingClassifier(random_state=42)

cv=StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

score1=cross_val_score(
    model1,
    X_train,
    y_train,
    cv=cv,
    scoring="f1"
)
cv_f1_1=score1.mean()

score2=cross_val_score(
    model2,
    X_train,
    y_train,
    cv=cv,
    scoring="f1"
)
cv_f1_2=score2.mean()

score3=cross_val_score(
    model3,
    X_train,
    y_train,
    cv=cv,
    scoring="f1"
)
cv_f1_3=score3.mean()

score4=cross_val_score(
    model4,
    X_train,
    y_train,
    cv=cv,
    scoring="f1"
)
cv_f1_4=score4.mean()


param_grid_lr = {
    "C": [0.01, 0.1, 1, 10, 100],
    "solver": ["liblinear", "lbfgs"],
    "max_iter": [100, 200, 500]
}

random_search_1=RandomizedSearchCV(
    estimator=model1,
    param_distributions=param_grid_lr,
    n_iter=10,
    cv=cv,
    scoring="f1",
    random_state=42,
    n_jobs=-1
)

random_search_1.fit(X_train,y_train)
best_model_1=random_search_1.best_estimator_
y_pred1=best_model_1.predict(X_test)

final_f1_1=f1_score(y_test,y_pred1)
accuracy_1=accuracy_score(y_test,y_pred1)
precision_1=precision_score(y_test,y_pred1)
recall_1=recall_score(y_test,y_pred1)


param_grid_dt = {
    "max_depth": [2, 3, 4, 5, 6, 8, 10],
    "min_samples_split": [2, 5, 10],
    "min_samples_leaf": [1, 2, 4]
}

random_search_2=RandomizedSearchCV(
    estimator=model2,
    param_distributions=param_grid_dt,
    n_iter=10,
    cv=cv,
    scoring="f1",
    random_state=42,
    n_jobs=-1
)

random_search_2.fit(X_train,y_train)
best_model_2=random_search_2.best_estimator_
y_pred2=best_model_2.predict(X_test)

final_f1_2=f1_score(y_test,y_pred2)
accuracy_2=accuracy_score(y_test,y_pred2)
precision_2=precision_score(y_test,y_pred2)
recall_2=recall_score(y_test,y_pred2)

param_distributions_rf = {
    "n_estimators": [50, 100, 150, 200, 300],
    "max_depth": [None, 3, 5, 7, 10, 15],
    "min_samples_split": [2, 5, 10],
    "min_samples_leaf": [1, 2, 4],
    "max_features": ["sqrt", "log2", None]
}

random_search_3=RandomizedSearchCV(
    estimator=model3,
    param_distributions=param_distributions_rf,
    n_iter=10,
    cv=cv,
    scoring="f1",
    random_state=42,
    n_jobs=-1
)

random_search_3.fit(X_train,y_train)
best_model_3=random_search_3.best_estimator_
y_pred3=best_model_3.predict(X_test)

final_f1_3=f1_score(y_test,y_pred3)
accuracy_3=accuracy_score(y_test,y_pred3)
precision_3=precision_score(y_test,y_pred3)
recall_3=recall_score(y_test,y_pred3)


param_grid_gb = {
    "n_estimators": [50, 100, 150, 200],
    "learning_rate": [0.01, 0.05, 0.1, 0.2],
    "max_depth": [2, 3, 4]
}

random_search_4=RandomizedSearchCV(
    estimator=model4,
    param_distributions=param_grid_gb,
    n_iter=10,
    cv=cv,
    scoring="f1",
    random_state=42,
    n_jobs=-1
)

random_search_4.fit(X_train,y_train)
best_model_4=random_search_4.best_estimator_
y_pred4=best_model_4.predict(X_test)

final_f1_4=f1_score(y_test,y_pred4)
accuracy_4=accuracy_score(y_test,y_pred4)
precision_4=precision_score(y_test,y_pred4)
recall_4=recall_score(y_test,y_pred4)

comparison=pd.DataFrame({
    "Models":["LogisticRegression","DecisionTree","RandomForest","GradientBoosting"],
    "CV_F1":[cv_f1_1,cv_f1_2,cv_f1_3,cv_f1_4],
    "Test_F1":[final_f1_1,final_f1_2,final_f1_3,final_f1_4],
    "Accuracy":[accuracy_1,accuracy_2,accuracy_3,accuracy_4],
    "Precision":[precision_1,precision_2,precision_3,precision_4],
    "Recall":[recall_1,recall_2,recall_3,recall_4]
})

print("\nComparsion Table :\n")
print(comparison)


print("\nThe Best two Models are LogisticRegression & DecisionTree based on the values of CV_F1.\n")



# 1. LOGISTIC REGRESSION — BEFORE TUNING
# ============================================================

model_lr_before = LogisticRegression()

model_lr_before.fit(X_train, y_train)

y_pred_lr_before = model_lr_before.predict(X_test)

lr_before_accuracy = accuracy_score(
    y_test,
    y_pred_lr_before
)

lr_before_precision = precision_score(
    y_test,
    y_pred_lr_before
)

lr_before_recall = recall_score(
    y_test,
    y_pred_lr_before
)

lr_before_f1 = f1_score(
    y_test,
    y_pred_lr_before
)


# ============================================================
# 2. LOGISTIC REGRESSION — AFTER TUNING
# ============================================================

param_distributions_lr = {

    "C": [
        0.01,
        0.1,
        1,
        10,
        100
    ],

    "solver": [
        "liblinear",
        "lbfgs"
    ],

    "max_iter": [
        100,
        200,
        500
    ]
}


random_search_lr = RandomizedSearchCV(

    estimator=LogisticRegression(),

    param_distributions=param_distributions_lr,

    n_iter=10,

    cv=cv,

    scoring="f1",

    random_state=42,

    n_jobs=-1
)


random_search_lr.fit(
    X_train,
    y_train
)


best_model_lr = random_search_lr.best_estimator_


y_pred_lr_after = best_model_lr.predict(
    X_test
)


lr_after_accuracy = accuracy_score(
    y_test,
    y_pred_lr_after
)

lr_after_precision = precision_score(
    y_test,
    y_pred_lr_after
)

lr_after_recall = recall_score(
    y_test,
    y_pred_lr_after
)

lr_after_f1 = f1_score(
    y_test,
    y_pred_lr_after
)


# ============================================================
# 3. DECISION TREE — BEFORE TUNING
# ============================================================

model_dt_before = DecisionTreeClassifier(
    random_state=42
)


model_dt_before.fit(
    X_train,
    y_train
)


y_pred_dt_before = model_dt_before.predict(
    X_test
)


dt_before_accuracy = accuracy_score(
    y_test,
    y_pred_dt_before
)

dt_before_precision = precision_score(
    y_test,
    y_pred_dt_before
)

dt_before_recall = recall_score(
    y_test,
    y_pred_dt_before
)

dt_before_f1 = f1_score(
    y_test,
    y_pred_dt_before
)


# ============================================================
# 4. DECISION TREE — AFTER TUNING
# ============================================================

param_grid_dt = {

    "max_depth": [
        2,
        3,
        4,
        5,
        6,
        8,
        10
    ],

    "min_samples_split": [
        2,
        5,
        10
    ],

    "min_samples_leaf": [
        1,
        2,
        4
    ]
}


grid_search_dt = GridSearchCV(

    estimator=DecisionTreeClassifier(
        random_state=42
    ),

    param_grid=param_grid_dt,

    cv=cv,

    scoring="f1",

    n_jobs=-1
)


grid_search_dt.fit(
    X_train,
    y_train
)


best_model_dt = grid_search_dt.best_estimator_


y_pred_dt_after = best_model_dt.predict(
    X_test
)


dt_after_accuracy = accuracy_score(
    y_test,
    y_pred_dt_after
)

dt_after_precision = precision_score(
    y_test,
    y_pred_dt_after
)

dt_after_recall = recall_score(
    y_test,
    y_pred_dt_after
)

dt_after_f1 = f1_score(
    y_test,
    y_pred_dt_after
)


# ============================================================
# 5. PRINT BEST PARAMETERS
# ============================================================

print("\n================================================")
print("LOGISTIC REGRESSION — AFTER TUNING")
print("================================================")

print("\nBest Parameters:")
print(random_search_lr.best_params_)

print("\nBest CV F1:")
print(random_search_lr.best_score_)


print("\n================================================")
print("DECISION TREE — AFTER TUNING")
print("================================================")

print("\nBest Parameters:")
print(grid_search_dt.best_params_)

print("\nBest CV F1:")
print(grid_search_dt.best_score_)


# ============================================================
# 6. BEFORE vs AFTER TUNING TABLE
# ============================================================

comparison_tuning = pd.DataFrame({

    "Model": [

        "Logistic Regression",
        "Logistic Regression",

        "Decision Tree",
        "Decision Tree"
    ],

    "Stage": [

        "Before Tuning",
        "After Tuning",

        "Before Tuning",
        "After Tuning"
    ],

    "Accuracy": [

        lr_before_accuracy,
        lr_after_accuracy,

        dt_before_accuracy,
        dt_after_accuracy
    ],

    "Precision": [

        lr_before_precision,
        lr_after_precision,

        dt_before_precision,
        dt_after_precision
    ],

    "Recall": [

        lr_before_recall,
        lr_after_recall,

        dt_before_recall,
        dt_after_recall
    ],

    "F1": [

        lr_before_f1,
        lr_after_f1,

        dt_before_f1,
        dt_after_f1
    ]
})


print("\n================================================")
print("BEFORE vs AFTER TUNING")
print("================================================")

print(comparison_tuning)