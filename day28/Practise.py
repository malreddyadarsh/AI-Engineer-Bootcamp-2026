# # Program 1 — Statistical Summary
# # 
# # Create a NumPy array containing around 15–20 numbers.
# # 
# # Calculate:
# 
# # Mean
# # Median
# # Minimum
# # Maximum
# # Range
# # Variance
# # Standard deviation
# # Q1
# # Q2
# # Q3
# # IQR
# 
# # Use NumPy where appropriate.
# 
# import numpy as np
# 
# num=np.array([45,50,52,55,58,60,85,62,65,68,70,75,77,80,85,90,95,99])
# 
# print(np.sort(num))
# print("The Average is :",np.mean(num))
# print("Middle Value is :",np.median(num))
# print("Minimum Value is :",np.min(num))
# print("Maximum Value is :",np.max(num))
# print("Range is :",np.max(num)-np.min(num))
# print("Variance is :",np.var(num))
# print("Standard Deviation is :",np.std(num))
# print("Q1 Percentile is :",np.percentile(num,q=25))
# print("Q2 Percentile is :",np.percentile(num,q=50))
# print("Q3 Percentile is :",np.percentile(num,q=75))
# print("IQR is :",np.percentile(num,75)-np.percentile(num,25))

# # Program 2 — Quartiles & IQR
# # 
# # Create a dataset containing some unusual values.
# # 
# # Calculate:
# # 
# # Q1
# # Q2
# # Q3
# # IQR
# # Lower bound
# # Upper bound
# # 
# # Then identify the outliers.
# # 
# # Goal
# # 
# # Understand the complete IQR method rather than simply calling a function.
# 
# import numpy as np
# 
# data=np.array([
    # 12, 15, 18, 20, 21,
    # 22, 24, 25, 26, 27,
    # 28, 30, 31, 32, 35,
    # 36, 38, 40, 42, 45,
    # 85, 100
# ])
# 
# q1=np.percentile(data,25)
# q2=np.percentile(data,50)
# q3=np.percentile(data,75)
# 
# iqr=q3-q1
# 
# lower_bound=q1-(1.5*iqr)
# upper_bound=q3+(1.5*iqr)
# print("Q1 :",q1)
# print("Q2 :",q2)
# print("Q3 :",q3)
# print("Lower Bound :",lower_bound)
# print("Upper Bound :",upper_bound)
# print("\nOutliers :\n")
# for num in data:
    # if num<lower_bound or num>upper_bound:
        # print(num)


# # Program 3 — Z-Score Calculator
# 
# # Create a small dataset.
# 
# # Calculate the Z-score for every observation.
# 
# # Then identify:
# 
# # Values above the mean.
# # Values below the mean.
# # Values more than 2 standard deviations away.
# 
# import numpy as np
# 
# data=np.array([
     # 40, 45, 50, 55, 60,
    # 65, 70, 75, 80, 100
# ])
# 
# mean=np.mean(data)
# std=np.std(data)
# print("Score--------Z-Score")
# for observation in data:
    # print(observation,"        ",(observation - mean)/std)
# 
# print("\nValues above the mean :")
# for num in data:
    # if num>mean:
        # print(num)
# 
# print("\nValues below the mean :")
# for num in data:
    # if num<mean:
        # print(num)
# 
# print("\nValues more than 2 standard deviations away:")
# for num in data:
    # z = (num - mean) / std
    # if abs(z) > 2:
        # print(num)

# # Program 4 — Probability Simulator
# #
# # Simulate 10,000 dice rolls using NumPy.
# #
# # Calculate experimental probability of getting:
# # 1, 2, 3, 4, 5, 6
# #
# # Compare with theoretical probability = 1/6

# import numpy as np

# # Generate 10,000 dice rolls
# rolls = np.random.randint(1, 7, size=10000)

# # Total number of rolls
# total = len(rolls)

# # Theoretical probability
# theoretical = 1 / 6

# print("Outcome    Count    Experimental    Theoretical")
# print("-----------------------------------------------")

# # Calculate probability for each dice outcome
# for number in range(1, 7):

    # # Count how many times the number appeared
    # count = np.sum(rolls == number)

    # # Experimental probability
    # experimental = count / total

    # print(
        # number,
        # "       ",
        # count,
        # "      ",
        # round(experimental, 4),
        # "        ",
        # round(theoretical, 4)
    # )

# Program 5 — Correlation Analyzer
# 
# Create two arrays:
# 
# study_hours
# marks
# 
# Calculate:
# 
# Correlation coefficient.
# Mean study hours.
# Mean marks.
# 
# Then write a conclusion.
# 
# For example:
# 
# "There is a strong positive linear relationship between study hours and marks."
# 
# But don't automatically claim that studying causes the marks to increase.

import pandas as pd

df = pd.DataFrame({
    "Name": ["A", "B", "C", "D", "E"],
    "Age": [21, 22, 21, 23, 22],
    "Marks": [65, 72, 58, 90, 75],
    "StudyHours": [3, 4, 2, 6, 5]
})

print("Correlation Matrix")
corr=df[["Marks","StudyHours"]].corr()
print(corr)

#  Mean study hours
print("\nMean study hours is :",df["StudyHours"].mean())

# Mean marks.
print("\nMean marks is :",df["Marks"].mean())

print("\nObservations :")
print("There is a strong positive linear relationship between study hours and marks. In this dataset, students who studied more hours tended to have higher marks. However, this correlation does not prove that increased study hours directly caused the higher marks.")