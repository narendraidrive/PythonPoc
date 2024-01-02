#inpute return sring not integer
a = input('inter value of a:')
b = input('inter value of b:')

#result = a / b  # this wil give an error 

# need to convert into integer
result = int(a) / int(b)
print('value of a/b', result)
