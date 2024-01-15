# TypeCasting -> To overwrite the  datatype of the variable
'''
 Typecasting has two types - Implicit : Typecasting doen by programe itself;
                           - Explicit : Typecasting done by user externally;
'''
a = '1'
b = '2'

print(a+b)    # as string concatenation
print(int(a)+int(b))
print(float(a)+int(b))

# Lec-10

# Taking Input -> using input() function
# By default input() will take string.

a = input()
print(a)
print(type(a))


# Lec- 11 and 12

# String
# String is Immutable

a = "Hello"
b = "World"

print(a+b)
print(a[1])

# For writing multiline string -> using '''/"""(triple single quotes or double quotes)
c = '''hello
I am Ankit
Rattan
'''
print(c)

# String Slicing
s = "Ankit Rattan"
print(s)
print(len(s)) #-> To find the length
print(s[0:5])
print(s[0:5:2])
