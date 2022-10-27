# SAVE structure to ----> JSON file
from json  import dumps
# data structure (Python)
person = {
    "name" : "John",
    "age"  : 30,
    "alive": True,
    "interests":[
        "programing",
        "hacking",
    ]
}

# save the data
file = open("person.json","w")
file.write(  dumps(person)  ) # dict -> str (JSON)
file.close()
