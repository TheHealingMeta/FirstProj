#Asks for input on the amount of the students
Amount = int(input("How many students? "))
#empty list
StudentList = []

for x in range(0,Amount):
    name = input("Enter the student's name: ")
    surname = input("Enter the student's surname: ")
    fullname = name + " " + surname
    StudentList.append(fullname)

for x in StudentList:
    print(x)
print(StudentList)