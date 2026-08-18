# Program 3 — Compare Two Models
# 
# Use the same dataset.
# 
# Train:
# 
# Logistic Regression
# Decision Tree
# 
# Compare:
# 
# Accuracy
# Precision
# Recall
# F1
# 
# Create a small comparison table:
# 
# Model                 Accuracy    Precision    Recall    F1
# -------------------------------------------------------------
# Logistic Regression      ...
# Decision Tree            ...
# 
# The important lesson:
# 
# Don't automatically assume the more complicated model is better.


import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score

df=pd.read_csv("day35/Problem 3.csv")

X=df[["Age","Salary","Experience"]]

y=df["Passed"]

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model1=LogisticRegression()

model1.fit(X_train,y_train)

prediction1=model1.predict(X_test)

accuracy1=accuracy_score(y_test,prediction1)
precision1=precision_score(y_test,prediction1)
recall1=recall_score(y_test,prediction1)
f1_1=f1_score(y_test,prediction1)


model2=DecisionTreeClassifier()

model2.fit(X_train,y_train)

prediction2=model2.predict(X_test)

accuracy2=accuracy_score(y_test,prediction2)
precision2=precision_score(y_test,prediction2)
recall2=recall_score(y_test,prediction2)
f1_2=f1_score(y_test,prediction2)

comparison=pd.DataFrame({
    "Models":["Logistic Regression", "Decision Tree"],
    "Accuracy":[accuracy1,accuracy2],
    "Precision":[precision1,precision2],
    "Recall":[recall1,recall2],
    "F1_Score":[f1_1,f1_2]
})

print("\nComparsion :")
print(comparison)