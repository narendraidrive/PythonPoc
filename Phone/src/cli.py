from phonebook import Phonebook
#import sys

def main():
    pbk = Phonebook()
    print("Press ")
    print("1 to Add contact")
    print("2 to Display contact entries ")
    print("3 clear entries")
    print("4 to Exit")
 
    ch = int(input("Enter your Choice \n"))
    if ch == 1:
        name = input("Enter name : ")
        number = int(input("Enter number : "))
        pbk.add(name, number)
    elif ch == 2:
        print(pbk.get_entries())
    elif ch == 3:
        pbk.clear()
    elif ch == 4:
        exit(0)
    else:
        print("Invalid Choice\n")
        menu()
main()
