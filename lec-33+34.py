# Dictionary
# Dictionary is ordered.    

dic = {
    1:"harry",
    2:"ankit",
    3:"rattan"
}
print(dic)

print(dic[1])
print(dic.get(1))
# NOTE: Both the above is same, the difference is in dic.get if the key-value is not there in the dictionary, then it will print NONE, and dic[] will throw an error.

print(dic.keys())
print(dic.values())
print(dic.items())  # -> key-value pairs    
    
    
# Lec: 34

# Dictionar Methods

d1 ={ 2:"A", 3:"d", 1:"S"}
d2 ={ 5:"a", 8:"b"}

d1.update(d2)
print(d1)

d2.clear() # -> to clear
print(d2)   # -> d2 now is empty dictionary

     