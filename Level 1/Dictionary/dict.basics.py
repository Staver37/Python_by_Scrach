# python type / dict /associative array / literal object
# * dict = ordered 3.5+ keyed ( collection of key=value pairs)
# formula
# indexed (lists) ->   homogenous [10, 20, 30], [0.25, 0.50, .... ]
# keyed   (dict)  ->   mixt       {"name": "John", "age": 30  }
from os import system
system ("clear")
todo = {
    # key        :   value
    "2021-01-01" : "Start a NEW HAPPY YEAR! :)",
    "2021-01-02" : "LEARN PYTHON BASICS",
    "2021-01-03" : "Ghet a job"

}
todo["2021-01-03"] = "Get an intership" # <------- change value for a key
print("------------------------------------------------------------------------------------------------------------------------------------")
print(todo["2021-01-03"])
print("------------------------------------------------------------------------------------------------------------------------------------")
print (todo)
print("------------------------------------------------------------------------------------------------------------------------------------")
print("\n"*7)