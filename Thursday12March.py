username = "admin"
password = "admin@2026"

user = input("Enter username: ")
Pass = input("Enter password: ")
pwrong = "Password is wrong"
uwrong = "Username is wrong"

if username != user and password != Pass:
    print(pwrong)
    print(uwrong)
elif username != user and password == Pass:
    print(uwrong)
elif user == username and password != Pass:
    print(pwrong)
else:
    print("You have successfully Logged in")
