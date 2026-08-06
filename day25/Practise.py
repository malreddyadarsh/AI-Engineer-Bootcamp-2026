# # Program 1 – Student Marks Line Chart
# # 
# # Create a line graph showing marks of students.
# # 
# # Learn:
# # 
# # Labels
# # Grid
# # Legend
# 
# import matplotlib.pyplot as plt
# 
# students=["Adarsh","James","Venkat","Manish","Govardhan"]
# marks=[45,55,65,78,67]
# 
# plt.plot(students,marks,label="Marks",marker="o",color="red",linestyle="--",linewidth=2)
# plt.title("Student Marks Analysis")
# plt.xlabel("Students")
# plt.ylabel("Marks")
# plt.grid(True)
# plt.legend()
# plt.show()

# # Program 2 – Subject Comparison Bar Chart
# # 
# # Display marks for:
# # 
# # Maths
# # Physics
# # Chemistry
# # 
# # Compare using bars.

# import matplotlib.pyplot as plt

# subjects=["Maths","Physics","Chemistry"]
# marks=[75,80,65]

# plt.bar(subjects,marks,color=["red","Orange","Green"],label="Marks",width=.5)
# plt.title("Subject Comparsion Analysis")
# plt.xlabel("Subjects")
# plt.ylabel("Marks")
# plt.grid(axis="y", linestyle="--", alpha=0.5)
# plt.legend()
# plt.savefig("BarGraph.png")
# plt.show()



# # Program 3 – Marks Distribution Histogram

# # Show how marks are distributed across a class.

# # Interpret:

# # Are most students clustered together?
# # Are there outliers?

# import matplotlib.pyplot as plt

# marks=[
    # 45,50,54,59,60,
    # 62,65,68,70,73,
    # 75,77,79,80,81,
    # 85,90,95,96,99
# ]

# plt.hist(marks,color="red",bins=5,label="Marks")
# plt.title("Marks Distribution")
# plt.xlabel("Marks")
# plt.legend()
# plt.show()

# # Program 4 – Hours Studied vs Marks
# 
# # Create a scatter plot.
# 
# # Ask yourself:
# 
# # Do students who study longer generally score higher?
# 
# import matplotlib.pyplot as plt
# 
# hours=[1,2,3,4,5,6,7,8,9]
# marks=[45,50,55,60,65,70,75,80,90]
# 
# plt.scatter(hours,marks,color="red",s=100,label="Student Data")
# plt.title("Hours Studied vs Marks")
# plt.xlabel("Hours")
# plt.ylabel("Marks")
# plt.grid(linestyle="--",alpha=.5)
# plt.legend()
# plt.show()



# # Program 5 – Branch Distribution

# # Create a pie chart showing:

# # AIML
# # CSE
# # ECE
# # EEE

# import matplotlib.pyplot as plt

# branches=["AIML","CSE","ECE","EEE"]
# percent=[35.6,28.9,21.6,13.9]

# plt.pie(percent,labels=branches,autopct="%1.1f%%",explode=[.1,.1,.1,.1])

# plt.title("Branch Distribution")
# plt.show()


# Program 6 – Dashboard

# Create one script that generates:

# Line plot
# Bar chart
# Histogram
# Scatter plot

# Save all figures as image files.

