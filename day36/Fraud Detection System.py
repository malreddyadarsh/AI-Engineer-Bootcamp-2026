# 3. Real AI Use Case
# 
# Let's take a fraud detection system.
# 
# Raw data:
# 
# Transaction Amount
# Timestamp
# Customer ID
# Location
# 
# Feature engineering might produce:
# 
# Transaction Amount
# Hour
# Day of Week
# Transactions in Last 1 Hour
# Average Transaction Amount
# Distance From Previous Transaction
# Number of Locations Used Today
# Is Weekend
# 
# Now the model has much more meaningful information.
# 
# Architecture:
# 
# Raw Transactions
       # ↓
# Feature Engineering
       # ↓
# Useful Features
       # ↓
# Preprocessing
       # ↓
# ML Model
       # ↓
# Fraud Probability
# 
# In modern AI systems, feature engineering still exists, although deep learning can learn many representations automatically.
# 
# For example:
# 
# Traditional ML
# Raw Data → Hand-designed Features → Model
# 
# 
# Deep Learning
# Raw/less-processed Data → Neural Network → Learned Representations
# 
# This is one reason deep learning changed the field.
# 
# But data representation remains critical.

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

df=pd.read_csv("day36/FraudDataset.csv")

df["Timestamp"] = pd.to_datetime(df["Timestamp"])

# Feature engineering

df["Hour"]=df["Timestamp"].dt.hour

df["Day_of_Week"]=df["Timestamp"].dt.day_of_week

df["Is_Weekend"]=(df["Day_of_Week"]>=5).astype(int)

df["Is_High_Amount"] = (
    df["Transaction_Amount"] >= 10000
).astype(int)

df["Customer_Transaction_Count"] = (
    df.groupby("Customer_ID").cumcount() + 1
)

numerical_columns=["Transaction_Amount","Hour","Day_of_Week","Is_Weekend","Is_High_Amount","Customer_Transaction_Count"]

categorical_columns=["Customer_ID","Location"]

X=df[["Transaction_Amount","Hour","Day_of_Week","Is_Weekend","Is_High_Amount","Customer_Transaction_Count","Customer_ID","Location"]]

y=df["Fraud"]

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

preprocessor=ColumnTransformer(
    transformers=[
        ("num",StandardScaler(),numerical_columns),
        ("cat",OneHotEncoder(),categorical_columns)
    ]
)

model=Pipeline([
    ("preprocessor",preprocessor),
    ("Classifier",LogisticRegression())
])

model.fit(X_train,y_train)

prediction_probability=model.predict_proba(X_test)

predictions=model.predict(X_test)

print("\nPredictions :")
print(predictions)

print("\nPredictions Probability :")
print(prediction_probability)