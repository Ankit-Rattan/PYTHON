# Raising custom errors 

# Custom errors are needed to stop the program at certain step to prevent any further unexpected event.

# Custom error can be done using 'raise' keyword
a = int(input("Enter the number the btw 5 and 8 :"))

if(a<5 or a>8):
    raise ValueError("Number should be between 5 and 8")