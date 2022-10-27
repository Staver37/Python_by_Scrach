# SAVE structure to ----> JSON file
from json  import loads

# data structure (Python)


# save the data
file = open("person.json","r")
person =file.read()
file.close()

print(person)
