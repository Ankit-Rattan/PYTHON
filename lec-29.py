# Doctring : are the string that appears right after definition of the function.

def add(a,b):
    # below is not comment, it is the docstring
    ''' This is a function of addition'''
    print("a+b")
    
    # docstring is just after the function def. Below is just a normal comment not a string.
    '''Hello, This is comment not docstring'''
    return a+b


a= 10
b = 20
print(add(a,b))
print(add.__doc__)


# PEP 8 - (Python Enhancement Proposal) : It provides the guidline and best practise on how to write Python code. It was made to improve the readability and consisetensy of python code.


# NOTE : Zen of python : it is the poem by Tim Peters
#  To access this poem : wrtie import this on terminal after opening python in terminal.