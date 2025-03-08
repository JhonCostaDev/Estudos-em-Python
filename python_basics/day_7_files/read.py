file_path = 'zen_python.txt'

# Old way to open a file in python
#open_file = open(file)

#content = open_file.read()
#print(content)

#open_file.close()

# Common way to open a file in python

with open(file_path) as file:
    content = file.read()

print(content)
