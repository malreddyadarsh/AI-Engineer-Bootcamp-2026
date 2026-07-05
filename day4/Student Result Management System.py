name=input("Enter name of the student :")
age=int(input("Enter Age :"))
print("Enter 5 subject marks :")
marks=[]
i=1
for i in range (1,6):
    mark=int(input())
    marks.append(mark)

sum=0
for mark in marks:
    sum=sum + mark

avg=sum/len(marks)

percent=(sum/500)*100.0

if percent>=90:
    grade='A'
elif percent>=80:
    grade='B'
elif percent>=65:
    grade='C'
elif percent>=45:
    grade='D'
else:
    grade='F'


print("===============\nSTUDENT REPORT\n===============\n")
print("Name :",name)
print("Age :",age)
print("Total marks of the student :",sum)
print("Average of the student :",avg)
print("Percentage of the student :",percent)
print("Grade of the student:",grade)

if percent>=45:
    print("The result of the student is PASS ")
else:
    print("The result of the student is FAIL ")
