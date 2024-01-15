# String Methods

# NOTE-> As string are immutable, so all thses method will not change the real string but will create new string and then print it.

a = "!!- Ankit - !!"
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))   # -> only removes from backside.
print(a.replace("Ankit","Rattan"))

print(a.split("-"))
 
b = "rattAn"
print(b)
print(b.capitalize())

c = "Hello I am Ankit, How are You all, Happy?"
print(c.count("H"))
print(c.find("I"))  # return the index of the first occurnece of the finding value 

 #NOTE :  index() -> is same as find(), but in find if the given string is not found then it will return -1 but in index(), it will return error.
