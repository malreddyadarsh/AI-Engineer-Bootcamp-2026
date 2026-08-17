# # Program 1 ⭐ — StandardScaler
# # 
# # Create a dataset:
# # 
# # Age
# # Salary
# # Experience
# # 
# # Perform:
# # 
# # Create X
# # ↓
# # Train/Test Split
# # ↓
# # StandardScaler
# # ↓
# # fit_transform(X_train)
# # ↓
# # transform(X_test)
# # ↓
# # Print results
# 
# import pandas as pd
# from sklearn.preprocessing import StandardScaler
# from sklearn.model_selection import train_test_split
# 
# df=pd.read_csv("day34/sample2.1.csv")
# 
# X=df[["Age","Salary","Experience"]]
# 
# X_train,X_test=train_test_split(
    # X,
    # test_size=0.2,
    # random_state=42
# )
# 
# scaler=StandardScaler()
# 
# X_train_scaled=scaler.fit_transform(X_train)
# 
# X_test_scaled=scaler.transform(X_test)
# 
# print("\nOriginal Training data :")
# print(X_train)
# 
# print("\nScaled Training Data :")
# print(X_train_scaled)
# 
# print("\nOriginal Testing Data :")
# print(X_test)
# 
# print("\nScaled Testing Data :")
# print(X_test_scaled)
# 
# 
# 
# Program 2 ⭐ — OneHotEncoder
# 
# 
# Create:
# 
# 
# City
# 
# 
# with:
# 
# 
# Hyderabad
# Delhi
# Mumbai
# Hyderabad
# Delhi
# 
# 
# Use:
# 
# 
# OneHotEncoder(handle_unknown="ignore")
# 
# 
# Print the encoded output.
# 
# 
# Also print the generated feature names.
# 


# import pandas as pd
# from sklearn.preprocessing import OneHotEncoder
# 
# df=pd.read_csv("day34/Sample2.2.csv")
# 
# X=df[["City"]]
# 
# encoder=OneHotEncoder(handle_unknown="ignore")
# encoded=encoder.fit_transform(X)
# encoded=encoded.toarray()
# print("\nOriginal Values :")
# print(X)
# print("Encoded Values :")
# print(encoded)
# 
# 
# 
# Program 3 ⭐⭐ — ColumnTransformer
# 
# 
# Create:
# 
# 
# Age
# Salary
# City
# 
# 
# Use:
# 
# 
# Age + Salary
       # ↓
# StandardScaler
# 
# 
# 
# 
# City
       # ↓
# OneHotEncoder
# 
# 
# Build a ColumnTransformer.
# 
# 
# Print the transformed dataset.
# 

# import pandas as pd

# from sklearn.compose import ColumnTransformer
# from sklearn.preprocessing import OneHotEncoder,StandardScaler

# df=pd.read_csv("day34/Sample2.3.csv")

# numerical_columns=["Age","Salary"]
# categorical_columns=["City"]

# X=df[numerical_columns + categorical_columns]

# preprocessor=ColumnTransformer(
    # transformers=[
        # ("num",StandardScaler(),numerical_columns),
        # ("cat",OneHotEncoder(),categorical_columns)
    # ]
# )

# processed=preprocessor.fit_transform(X)

# print("\nOriginal Features :")
# print(X)

# print("\nProcesses Features :")
# print(processed)





# Program 4 ⭐⭐⭐ — Pipeline


# Build:


# Dataset
   # ↓
# Train/Test Split
   # ↓
# StandardScaler
   # ↓
# Logistic Regression
   # ↓
# Predictions
   # ↓
# Accuracy


# Use:


# Pipeline


# Do not manually scale the test data.



# import pandas as pd
# from sklearn.pipeline import Pipeline
# from sklearn.preprocessing import StandardScaler
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score

# df=pd.read_csv("day34/Sample2.4.csv")

# X=df[["Age","Salary","Experience"]]

# y=df["Purchased"]

# X_train,X_test,y_train,y_test=train_test_split(
    # X,
    # y,
    # test_size=0.2,
    # random_state=42
# )

# pipeline=Pipeline([
    # ("scaler",StandardScaler()),
    # ("model",LogisticRegression())
# ])

# pipeline.fit(X_train,y_train)

# predictions=pipeline.predict(X_test)

# print("\nActual Values :")
# print(y_test.values)

# print("\nPredicted Values :")
# print(predictions)

# print("\nAccuracy :")
# print(accuracy_score(y_test,predictions))




# Program 5 ⭐⭐⭐⭐ — Complete ML Preprocessing Pipelin


# This is today's most important exercise.


# Create a dataset like:


# Age
# Salary
# Experience
# City
# Education
# Passed


# Example:


# Age	Salary	Experience	City	Education	Passed
# 22	30000	0	Hyderabad	B.Tech	0
# 25	50000	2	Delhi	B.Tech	1
# 28	65000	4	Mumbai	M.Tech	1
# 23	35000	1	Hyderabad	B.Tech	0
# 30	80000	6	Delhi	M.Tech	1
# 26	55000	3	Mumbai	B.Tech	1


# Build:


# Load/Create Dataset
        # ↓
# EDA
        # ↓
# X / y
        # ↓
# Train/Test Split
        # ↓
# Identify numerical columns
        # ↓
# Identify categorical columns
        # ↓
# ColumnTransformer
   # ↙             ↘
# Scaling       One-Hot
   # ↘             ↙
      # Pipeline
         # ↓
# Logistic Regression
         # ↓
# Predictions
         # ↓
# Accuracy
         # ↓
# Confusion Matrix





import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score,confusion_matrix

df=pd.read_csv("day34/Sample2.5.csv")

# EDA
print("\nFisrt Five rows of Dataset :\n")
print(df.head())

print("\nMissing Values :\n")
print(df.isnull().sum())

print("\nDuplicate Rows :\n")
print(df.duplicated().sum())

print("\nBasic Information :\n")
df.info()

print("\nStatistical Information :\n")
print(df.describe())

# X / y
X=df[["Age","Salary","Experience","City","Education"]]

y=df["Passed"]

# Train/Test Split
X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Identify numerical columns
numerical_columns=["Age","Salary","Experience"]

# Identify categorical columns
categorical_columns=["City","Education"]

preprocessor=ColumnTransformer(
    transformers=[
        ("num",StandardScaler(),numerical_columns),
        ("cat",OneHotEncoder(),categorical_columns)
    ]
)

pipeline=Pipeline([
    ("preprocessor",preprocessor),
    ("model",LogisticRegression())
])

pipeline.fit(X_train,y_train)
predictions=pipeline.predict(X_test)

print("\nActual Values :\n")
print(y_test.values)

print("\nPredicted Values :\n")
print(predictions)

print("\nAccuracy Score :")
print(accuracy_score(y_test,predictions))

print("\nConfusion Matrix :\n")
print(confusion_matrix(y_test,predictions))