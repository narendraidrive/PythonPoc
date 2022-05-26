import re  
  
#str = "How are you. How is everything"
  
# matches = re.findall("How", str)
  
# print(matches)

# matches = re.search("are", str) 
# print(matches)
# #print(matches.span())  
# #print(matches.group())
# match = re.search(r'[^a-d]', str)
# print(match)

# txt = "The rain in Spain"
# x = re.split("in", txt)
# print(x)


##Search for an upper case "S" character in the beginning of a word, and print its position:
# x = re.search(r"^H", str)
# print(x.string)

file = open('/home/narendra/project/python/PythonPoc/regex/regex.txt', 'r')
str = file.readlines()
print(str)
m=re.search(r"^.+?(?=Lorem)", str[0])
print(m.group())
for x in str:
    m = re.match(r"^.+?(?=Lorem)", x)
    if m:
        print(m.group())
