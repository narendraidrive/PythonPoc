class Getemp():
    def get_emp(self):
        try:
            file = open('/home/narendra/project/python/PythonPoc/FileHandling/employee.txt', 'r')
            print(file.read())
        except IOError:
            print("File not found")