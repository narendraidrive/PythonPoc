from oprations.employee.addemp import Addemp
from oprations.employee.getemp import Getemp


def menu():
    print("Welcome to Employee Management Record")
    print("Press ")
    print("1 to Add Employee")
    print("2 to Display Employees")
    print("3 to Exit")
 
    ch = int(input("Enter your Choice \n"))
    if ch == 1:
        Addemp().add_emp()
    elif ch == 2:
        Getemp().get_emp()
    elif ch == 3:
        exit(0)
    else:
        print("Invalid Choice\n")
        menu()

menu()