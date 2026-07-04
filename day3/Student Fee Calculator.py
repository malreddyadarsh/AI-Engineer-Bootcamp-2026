name=input("Enter Student Name:")
course_fee=int(input("Enter Course Fee:"))
scholarship=int(input("Enter Scholarship amount:"))

remaining_fee=course_fee - scholarship

print("\n-----Student Fee Calculator-----")
print("Student Name :",name)
print("Course Fee :",course_fee)
print("Scholarship Amount :",scholarship)
print("Remaining Amount :",remaining_fee)