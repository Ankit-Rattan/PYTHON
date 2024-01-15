# lec-40
# Secret code Exercise


# lec-41
# Short Hand if else

'''
Syntax: 
    _statement_ if condition else _statement_
    
    -> suitable for small programs only.
'''

a = 10
b = 20
print("b") if a<b else print("a")


# lec-42
# Enumeration function
'''
It is a built nin function in python that allows you to loop over a sequence [ list, tuples, strings ] and get the value and index of each value of that sequence at same time
'''

a = [3, 2, 5, 6, 7, 8]


# first one (ind in this case) will give index and second one (i.e val) will give value
for ind, val in enumerate(a):
    print(ind, " = ", val)  

print('\n')    
# Changing starting index
for ind, val in enumerate(a, start = 1):
    print(ind, " = ", val)  

 