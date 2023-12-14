#what is DocString? and pep-8 in the python

def add(a,b):
    '''This function takes two numbers as arguments and return their sum'''
    return a+b
print(add(4,5))
# this is called docstring it is specipal type of comment in python which we can use to describe the function or class or module
print(add.__doc__)#This is also we print using this way