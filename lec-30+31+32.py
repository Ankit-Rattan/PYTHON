# Factorial

def fac(n):
    if n==1:
        return 1
    
    return n*fac(n-1)

print(fac(5)) 

# lec-32
# Sets -> sets is the unordered collection of data items.
#         it doesnot take the repeated vales in it.
#         Sets are unchangeable. i.e  Cannot change item once added  

s = {1, 3, 4, 3, 5}
# Here 3 is the repeated int, so it will not print it twice. It will show 3 at once only
print(s)
 
# lec-32
s1 = {1,2,3,4,5}
s2 = {4,2,5,7,8}
s3 = s1.union(s2)   # -> this will merge set-1 and set-2 i.e union of two sets
print(s3)
print(s1.intersection(s2)) # -> this will print the intersection of the two sets.

# To add the value of set2 in set1 : use update function
s1.update(s2)
print(s1)

# Symmetric difference -> when in two sets we remove the intersected values i.e common values between these two sets is called symmetric difference.

# Symmetric differece : (AUB)- (A^B) , where U-> union and ^ is intersection

# In python, symmetric difference can be done by difference function
print("\n")
setA = {1,4,2,5,7}
setB = {2,4,5,8,9}
print(setA.difference(setB)) # -> setA se vo hata od jo setB me hain
print(setB.difference(setA)) # -> setB me vo hata do jo steA me hain
print(setA,setB)

