# create a helper function param (text) > split()

def split(text):
    
    words =[]
    word = ""
    for c in text:
        if c != " ":
            word += c
        else:
            words.append(word)
            word = ""
    
    words.append(word)
    return words
# CALLING OUR FUNCTION
print(split("hello people") )
print(split("i love python3") )
