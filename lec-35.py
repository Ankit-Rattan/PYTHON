# for-loop with else

'''
Jab for loop ki given condition satisfy nahi hoti, tab vo else part execute karega.
OR
Jab for loop ki saari execution kho jaygi, tab else section execute hoga
'''

for i in range(5):
    print(i, end=" ")
    
else:
    print("\nEnded.")   
    
# else ke ecexute hone ka meaning hain ki loop properly khatam hua hai, vo break nahi hua hain. 
     
for i in range(5):
    print(i, end=" ")
    if(i==3): break    # here it is breaked using break, so else will not exectute.
    
else:
    print("\nEnded.")    
    
    
    
# Same else can be used to with while loop also. 
