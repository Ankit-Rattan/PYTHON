# "finally" keyword -> it is the block which will always execute irrespective of the error occured. 
'''
 NOTE: Differnce between 'finally' and normal print statement:
                    - In general both are same, i.e both will always execute.
                    - The difference comes when we are using it in the function which returns some values. Then  only 'finally' block execute and not the normal print statement

'''

def normal():
    try:
        l =[4,2,1,5]
        a =int(input("Enter the number: "))
        print(l[a])
        return 1
    except: 
        print("Exceeded index")
        return 0
    finally:
        print("finally statementn execute")
    print("Normal print statement")
    
    
normal()                    