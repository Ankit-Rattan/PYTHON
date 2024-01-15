# DataType and Variables

# Variable : variable is like container which holds the data.
# DataType : It specifies the type of value that variable hold.

a = 1
b = "Hello"
c = 4.3
d = None
print(a,b,c, d)

e = 5 + 6j   # -> Complex Number
e1 = complex(2,3)  # -> another way of complex number
print(e)
print(e1)

# String Concatenate (Two variable should be of same datatype)

v1 = "Ankit"
v2 = "Rattan"
res = v1+v2
print(res)

# Multplication of string

res1 = v2*4
print(res1)

# for knowing datatype of a variable use --> type(variable_name)

print("Datatype of a is: ", type(a))
print("Datatype of b is: ", type(b))
print("Datatype of c is: ", type(c))
print("Datatype of e is: ", type(e))


# List -> it is the ordered collection of datatype.
#      -> It is mutable (i.e it can be modified after the creation)

l = [2,3,"Hello", ['r', 3,2.3], "World"]

print(l)
print(l[2])
print(l[3][1])

l[2] = 4
print(l)
print(l[2])

print("\n")
# Tuple -> It is also the ordered colleciton  of data.
#       -> But it is immutable

t = (3,1,"Hello", [4,2,3], "World")

print(t)
print(t[2])
t[3][2] = 4    # -> Tuple ke andar jo list tha usme change kr sakte hain.
print(t)
print("\n")

# Dictionary-> This is used to store key-value pairs.
#            -> It is mutable.

dic={1:"Ramesh", 2: "Suresh", 3: "Mahesh"}
print(dic)
print(dic[1])
dic[1] = "Saresh"
print(dic)



