# Compare subjects chosen by two students.
# Display:
# Common subjects.
# Different subjects.
# All available subjects.


student1={"Math","Physics","Social","Chemistry","Java"}
student2={"Biology","Python","English","Java","Math"}

print("\nCommon Subjects")
for subject in sorted(student1 & student2):
    print(subject)

print("\nUnique Subjects of Student1 :")
for student in sorted(student1-student2):
    print(student)

print("\nUnique Subjects of Student2 :")
for student in sorted(student2-student1):
    print(student)    

print("\n All Available Subjects are :")
for subject in sorted(student1|student2):
    print(subject)