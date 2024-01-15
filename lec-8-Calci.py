# Calculator

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
while(True):
    print("1-Addition\n2-Subtraction\n3-Multiplication\n4-Division\n5-Exit")
    val = int(input("Enter the value: "))
    
    if val == 1:
        print("Additon : ", a+b)
        continue
        

    if val == 2:
        print("Absolute Subtration : ", abs(a-b))
        continue
        
    
    if val == 3:
        print("Multiplication : ", a*b) 
        continue
           
    if val == 4:
        print("Division : ", a/b)
        continue

    if val == 5:
        break
    else:
        print("Enter Valid")
        continue
    
print("Thank you!")         