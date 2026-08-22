# Program 4 — Feature Importance + Tree Visualization

# Train a Decision Tree.
# 
# Print:
# 
# ```
# model.feature_importances_
# ```
# 
# Then visualize the tree using:
# 
# ```
# plot_tree()
# ```
# 
# Your output should answer:
# 
# ```
# Which feature was used most heavily?
# ```
# 
# What were the major decision rules?
# 
# What does the first split mean?

import pandas as pd
from sklearn.tree import DecisionTreeClassifier,plot_tree
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
data = pd.DataFrame({
    "Study_Hours": [
        1, 2, 2, 3, 3,
        4, 4, 5, 5, 6,
        6, 7, 7, 8, 8,
        9, 9, 10, 10, 11,
        3, 4, 5, 6, 7
    ],

    "Attendance": [
        55, 60, 62, 65, 68,
        70, 72, 74, 76, 78,
        80, 82, 84, 85, 87,
        88, 90, 92, 94, 96,
        82, 58, 65, 88, 76
    ],

    "Previous_Marks": [
        40, 42, 45, 48, 50,
        52, 55, 58, 60, 63,
        65, 68, 70, 73, 75,
        78, 80, 84, 87, 90,
        72, 45, 55, 62, 78
    ],

    "Passed": [
        0, 0, 0, 0, 0,
        0, 0, 1, 1, 1,
        1, 1, 1, 1, 1,
        1, 1, 1, 1, 1,
        1, 0, 0, 1, 1
    ]
})


X=data[["Study_Hours","Attendance","Previous_Marks"]]

y=data["Passed"]

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model1=DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)

model1.fit(X_train,y_train)

predictions=model1.predict(X_test)

print("\nImportant Features :")
print(model1.feature_importances_)

plot_tree(model1,
          feature_names=X.columns,
          class_names=["Fail","Pass"],
          filled=True)

plt.show()