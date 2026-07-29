"""
=========================================
        AI DATASET EXPLORER
=========================================

Features
--------
1. Load Sample Dataset
2. Display Dataset
3. Show Dataset Shape
4. Display Statistics
5. Filter Records
6. Generate Random Dataset
7. Compare Two Datasets
8. Exit

Concepts Used
-------------
✔ NumPy Arrays
✔ Statistics
✔ Boolean Indexing
✔ Random Module
✔ Array Operations
✔ Shape
✔ Mean
✔ Median
✔ Standard Deviation
✔ Variance
✔ Maximum
✔ Minimum
"""

import numpy as np

np.random.seed(42)

# -------------------------------------------------
# Sample Dataset
# Columns:
# Age, Height(cm), Weight(kg), Score
# -------------------------------------------------

dataset = np.array([
    [20,170,65,85],
    [21,168,72,90],
    [22,175,68,78],
    [19,165,60,88],
    [23,180,80,95],
    [20,172,70,82],
    [21,169,75,91],
    [22,178,77,87],
    [24,182,85,98],
    [20,171,66,80]
])

while True:

    print("\n========== AI DATASET EXPLORER ==========")
    print("1. Display Dataset")
    print("2. Dataset Shape")
    print("3. Dataset Statistics")
    print("4. Filter Records")
    print("5. Generate Random Dataset")
    print("6. Compare Two Datasets")
    print("7. Exit")

    choice = int(input("\nEnter Choice : "))

    # -------------------------------------------------
    # Display Dataset
    # -------------------------------------------------

    if choice == 1:

        print("\nDataset\n")

        print("Age Height Weight Score")

        for i, row in enumerate(dataset, start=1):
            print(f"Student {i:2d} :", row)

    # -------------------------------------------------
    # Dataset Shape
    # -------------------------------------------------

    elif choice == 2:

        rows, cols = dataset.shape

        print("\nDataset Shape")
        print("-----------------------")
        print("Rows    :", rows)
        print("Columns :", cols)

    # -------------------------------------------------
    # Statistics
    # -------------------------------------------------

    elif choice == 3:

        print("\n===== DATASET STATISTICS =====")

        print("\nColumn Means")
        print(np.mean(dataset, axis=0))

        print("\nColumn Medians")
        print(np.median(dataset, axis=0))

        print("\nStandard Deviation")
        print(np.std(dataset, axis=0))

        print("\nVariance")
        print(np.var(dataset, axis=0))

        print("\nMaximum Values")
        print(np.max(dataset, axis=0))

        print("\nMinimum Values")
        print(np.min(dataset, axis=0))

    # -------------------------------------------------
    # Filter Records
    # -------------------------------------------------

    elif choice == 4:

        while True:

            print("\n------ FILTER MENU ------")
            print("1. Score >= 90")
            print("2. Age > 21")
            print("3. Weight > 70")
            print("4. Height >= 175")
            print("5. Back")

            ch = int(input("Enter Choice : "))

            if ch == 1:

                result = dataset[dataset[:,3] >= 90]

                print("\nStudents Scoring >=90\n")
                print(result)

            elif ch == 2:

                result = dataset[dataset[:,0] > 21]

                print("\nAge >21\n")
                print(result)

            elif ch == 3:

                result = dataset[dataset[:,2] > 70]

                print("\nWeight >70\n")
                print(result)

            elif ch == 4:

                result = dataset[dataset[:,1] >= 175]

                print("\nHeight >=175\n")
                print(result)

            elif ch == 5:
                break

            else:
                print("Invalid Choice.")

    # -------------------------------------------------
    # Generate Random Dataset
    # -------------------------------------------------

    elif choice == 5:

        n = int(input("\nEnter Number of Students : "))

        random_dataset = np.column_stack((
            np.random.randint(18,26,n),
            np.random.randint(160,191,n),
            np.random.randint(50,91,n),
            np.random.randint(35,101,n)
        ))

        print("\nGenerated Dataset\n")
        print("Age Height Weight Score")

        for i,row in enumerate(random_dataset,start=1):
            print(f"Student {i:2d} :",row)

    # -------------------------------------------------
    # Compare Two Datasets
    # -------------------------------------------------

    elif choice == 6:

        print("\nCreating another random dataset...")

        dataset2 = np.column_stack((
            np.random.randint(18,26,10),
            np.random.randint(160,191,10),
            np.random.randint(50,91,10),
            np.random.randint(35,101,10)
        ))

        print("\nDataset 1 Mean")
        print(np.mean(dataset,axis=0))

        print("\nDataset 2 Mean")
        print(np.mean(dataset2,axis=0))

        print("\nDifference Between Means")
        print(np.mean(dataset,axis=0)-np.mean(dataset2,axis=0))

        print("\nElement-wise Difference")
        print(dataset-dataset2)

        print("\nAre Both Datasets Equal?")
        print(np.array_equal(dataset,dataset2))

    # -------------------------------------------------
    # Exit
    # -------------------------------------------------

    elif choice == 7:

        print("\nThank You For Using AI DATASET EXPLORER")
        break

    else:
        print("\nInvalid Choice.")