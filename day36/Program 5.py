# Program 5 — Feature Engineering + ML Pipeline 🔥
# 
# This is today's most important exercise.
# 
# Create:
# 
# Age
# Salary
# Experience
# City
# Education
# Purchased
# 
# Create at least one meaningful numerical engineered feature.
# 
# Then build:
# 
# Dataset
 # ↓
# Feature Engineering
 # ↓
# X/y
 # ↓
# Train/Test Split
 # ↓
# Preprocessing
 # ↓
# ColumnTransformer
 # ↓
# Pipeline
 # ↓
# Logistic Regression
 # ↓
# Evaluation
# 
# Evaluate:
# 
# Accuracy
# Precision
# Recall
# F1
# Important
# 
# Feature engineering must happen in a way that does not leak information from the test set.
# 
# For simple deterministic transformations based only on each row's existing input values, creating the feature before the split can be fine.
# 
# But transformations that learn statistics from the dataset—such as means, target encoding, scaling parameters, imputation values, etc.—must be fitted using training data only, preferably inside the pipeline.
# 
# This distinction matters.

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
from sklearn.linear_model import LogisticRegression

df=pd.read_csv("day36/Program 5.csv")

# Feature Engineering
df["Salary_Per_Experience"]=df["Salary"]/(df["Experience"]+1)

numerical_columns=["Age","Salary","Experience","Salary_Per_Experience"]

categorical_columns=["City","Education"]

# X/y
X=df[["Age","Salary","Experience","City","Education","Salary_Per_Experience"]]

y=df["Purchased"]

df.to_csv("day36/Program 5.1.csv",index=False)
df=pd.read_csv("day36/Program 5.1.csv")
# Train/Test Split

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# ColumnTransformer

preprocessor=ColumnTransformer(
    transformers=[
        ("num",StandardScaler(),numerical_columns),
        ("cat",OneHotEncoder(),categorical_columns)
    ]
)

# Pipeline

model=Pipeline([
    ("preprocessor",preprocessor),
    ("Classifier",LogisticRegression())
])

model.fit(X_train,y_train)

model_predictions=model.predict(X_test)

# Evaluation

print("\nAccuracy :",accuracy_score(y_test,model_predictions))
print("\nPrecicion Score :",precision_score(y_test,model_predictions))
print("\nRecall Score    :",recall_score(y_test,model_predictions))
print("\nF1 Score        :",f1_score(y_test,model_predictions))