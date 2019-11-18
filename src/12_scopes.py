# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
#x = 12

"""
def changeX():
    x = 99
    print(x)
"""

# This prints 12. What do we have to modify in changeX() to get it to print 99?

# changeX() #99
# print(x) #12


# This nested function has a similar problem.
# In the above code there is a nested function inner(). We use nonlocal keyword to create nonlocal variable. The inner() function is defined in the scope of another function outer().
# Note : If we change value of nonlocal variable, the changes appears in the local variable.
"""
def outer():
    y = 120

    def inner():
        y = 999
        print(y)
    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999? Google "python nested function scope".
    print(y)
    
outer()
"""
# notes------------
# UnboundLocalError: local variable 'x' referenced before assignment

# A variable declared inside the function's body or in the local scope is known as local variable.
# The output shows an error, because we are trying to access a local variable y
# def foo():
# y = "local"

# foo()
# print(y)
# in a global scope whereas the local variable only works inside foo() or local scope.
# -------------local & global in same code
"""
x = "global"

def foo():
   
    y = "local"
    
    print(x)
    print(y)
    
foo()
"""
# -----------------nonLocal Variables-----------
"""
def outer():
    x = "local"
    
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    
    inner() #must be invoked for inner print to work 
    print("outer:", x)

print("outer1", outer()) #must be invoked for outer print to work
"""
"""
x = "global"


def foo():
    global x
    #y = "local"
    #x = x * 2
    print(x)  # global x not defined
    # print(y)


print("foo", foo())
"""