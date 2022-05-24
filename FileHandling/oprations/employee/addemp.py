class Addemp:
    def add_emp(self):
        Name = input("Enter Employee Name : ")
        Post = input("Enter Employee Post : ")
        Salary = input("Enter Employee Salary : ")
        try:
            file = open('/home/narendra/project/python/PythonPoc/FileHandling/employee.txt', 'a+')
        except IOError:
            print("File not found")
        
        file.write('Name: '+Name+'\n')
        file.write('Post: '+Post+'\n')
        file.write('Salary: '+Salary+'\n\n')