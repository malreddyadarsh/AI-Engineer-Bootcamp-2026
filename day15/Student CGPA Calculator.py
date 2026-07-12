# Student CGPA Calculator
# 
# Create a program that:
# 
# Takes marks for 6 subjects.
# Marks must be between 0 and 100.
# If the user enters invalid marks or non-numeric data, ask again.
# Calculate:
# Total
# Percentage
# Grade


marks=[]
print("Enter 6 Subject Marks:\n")

for i in range(1,7):
    while True:
        try:
            mark=int(input(f"Enter {i} Subject Marks :"))

            if mark<0 or mark>100:
                raise ValueError("Marks Must Be Between 0 and 100.")
            else:
                marks.append(mark)
                break
        except ValueError as e:
            print(e)

total=sum(marks)

percent=total/600*100
percentage=round(percent,2)
if percentage>=90:
    grade="A"
elif 80<=percentage<90:
    grade="B"
elif 70<=percentage<80:
    grade="C"
elif 55<=percentage<70:
    grade="D"
else:
    grade="Fail"

print("Total Subject Marks :",total)
print("Percentage is       :",percentage,"%")
print("Grade is            :",grade)