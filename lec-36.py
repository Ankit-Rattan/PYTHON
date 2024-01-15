'''
Exceptional Handling -> It is the process of responding to the unwanted and unexpected errors or events when a computer program runs.
'''
'''
a = int(input("Enter the number: "))
print(f"Multiplication Table of {a} is ->")

for i in range(1,11):
    print(f"{a} X {i} = {a*i}")
    
'''    
    
    
'''
Try-Except -> This is used to handle errors and blocks.The code written in the "try block" will run only when that code leads to NO error. If it leads to error, then it will execute the "except block"
'''    
# For ex -> in the above code if we give input as string then the for loop will geenerte error.

a =input("Enter the number: ")
print(f"Multiplication Table of {a} is ->")

try:  
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
        
except Exception as e:
        print(e)   # e -> represent the type of error generated
        print("Sorry some error occured")
    
print(" Line after error are executing...")    



# There are different types of "excpet blocks" user can use to handle specific errors- Like, ValueError, IndexError




try: 
    v = input("Enter the value :")
    b = [4,3] 
    print(b[int(v)])
except IndexError:
    print("No Index exist")    