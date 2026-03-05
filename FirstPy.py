#This is a program that asks a user
#for their name, surname, age and current_year then prints
#a message that says Hello name surname, you were
#born in year_of_birth

#message to the user
message= "hello nerd, Welcome to Python"
print(message)

#getting input from user
name = input("Enter your first name: ")
Surname = input("Enter your surname: ")
age = int(input("Enter your age: "))
Current_Year = int(input("Enter the current year: "))

#Processing - calculating the year_of_birth
year_of_birth = Current_Year - age

#Output-Dispaly a message
print("Hello", name, Surname, "you are born in", year_of_birth)