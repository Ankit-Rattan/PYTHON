# String Format
l = "I am {} and I am fron {}"
name = "Ankit"
college = "NIT"
print(l.format(name, college))

# If the order is reverse then it will add the strign there in reverse order.
print(l.format(college, name))

# To overcome this, we can number the format bracker ({}), in the string.

l = "I am {1} and I am fron {0}"
print(l.format(college, name))


#  To do the above thing, python provides another feature called -> f-strings;

txt  = f"I am {name} and I am fron {college}"
print(txt)