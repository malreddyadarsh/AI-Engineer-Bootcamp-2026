# # Program 1 — StandardScaler
# # 
# # Create:
# # 
# # Study Hours
# # Attendance
# # Previous Marks
# # 
# # Perform:
# # 
# # 1. Create DataFrame
# # 2. Select numerical features
# # 3. Apply StandardScaler
# # 4. Print original values
# # 5. Print scaled values
# # 
# # You should understand exactly what happened to the values.
# 
# import pandas as pd
# 
# from sklearn.preprocessing import StandardScaler
# 
# df=pd.read_csv("day34/sample1.1.csv")
# 
# X=df[["Study_Hours","Attendance","Previous_Marks"]]
# 
# scaler=StandardScaler()
# 
# X_scaled=scaler.fit_transform(X)
# 
# print("\nOriginal Values :")
# print(X)
# 
# print("\nScaled Values :")
# print(X_scaled)




# # Program 2 — OneHotEncoder

# # Create:

# # ```
# # Name
# # ```

# # City

# # Branch

# # Example:

# # ```
# # Adarsh    Hyderabad    CSE
# # ```

# # Rahul     Delhi        ECE

# # Priya     Mumbai       CSE

# # Use:

# # ```
# # OneHotEncoder
# # ```

# # and convert the categorical columns into numerical representations.

# # Your goal is to understand:

# # ```
# # categorical data
# # ```

       # # ↓

# # numerical representation

# import pandas as pd

# from sklearn.preprocessing import OneHotEncoder

# df=pd.read_csv("day34/sample.1.2.csv")

# X=df[["Name","City","Branch"]]

# encoder=OneHotEncoder()

# X_encoded=encoder.fit_transform(X)

# X_encoded=X_encoded.toarray()

# print("Actual Values :")
# print(X)

# print("\nEncoded Values :")
# print(X_encoded)




# # Program 3 — Complete Preprocessing

# # Create a dataset:

# # Age
# # Salary
# # City
# # Experience
# # Purchased

# # Example:

# # 22  30000   Hyderabad  1   0
# # 25  50000   Delhi      3   1
# # 30  70000   Mumbai     5   1
# # 35  90000   Hyderabad  8   1
# # 28  45000   Delhi      4   0

# # Separate:

# # Numerical columns
# # Categorical columns
# # Target

# # Then use:

# # ColumnTransformer
    # # ↓
# # StandardScaler
    # # +
# # OneHotEncoder

# # Do not train a model yet.

# # Today's goal is preprocessing.


# import pandas as pd

# from sklearn.compose import ColumnTransformer
# from sklearn.preprocessing import OneHotEncoder,StandardScaler

# df=pd.read_csv("day34/sample.1.3.csv")

# numerical_columns=["Age","Salary","Experience"]
# categorical_columns=["City"]

# X=df[numerical_columns + categorical_columns]

# y=df["Purchased"]

# preprocessor=ColumnTransformer(
    # transformers=[
        # ("num",StandardScaler(),numerical_columns),
        # ("cat",OneHotEncoder(),categorical_columns)
    # ]
# )

# X_processed=preprocessor.fit_transform(X)

# print("\nOriginal Features :")
# print(X)

# print("\nTarget :")
# print(y)

# print("\nProcessed Values :")
# print(X_processed)


import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.metrics import accuracy_score

df=pd.read_csv("day34/sample.1.3.csv")

X=df[["Age","Salary","City","Experience"]]

y=df["Purchased"]

numerical_columns=["Age","Salary","Experience"]

categorical_columns=["City"]

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


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

accuracy=accuracy_score(y_test,predictions)

print("\nActual Values :")
print(y_test.values)

print("\nPredicted Values :")
print(predictions)

print("\nAccuracy Score :")
print(accuracy)