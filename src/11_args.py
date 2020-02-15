# Experiment with positional arguments, arbitrary arguments, and keyword
# arguments.
# https://www.programiz.com/python-programming/function-argument ,<--GOOD ARTICLE

# Write a function f1 that takes two integer positional arguments and returns
# the sum. This is what you'd consider to be a regular, normal function.
# https://realpython.com/python-conditional-statements/
# YOUR CODE HERE


# def f1(x, y):
# return x + y


# print(f1(1, 2))

# Write a function f2 that takes any number of integer arguments and prints the
# sum. Google for "python arbitrary arguments" and look for "*args"
# https://www.geeksforgeeks.org/args-kwargs-python/
# https://www.geeksforgeeks.org/sum-function-python/

# https://wsvincent.com/python-args-kwargs/


# YOUR CODE HERE
# def f2(*argv):
# for arg in argv:
# return sum(argv)


# print(f2(1))                    # Should print 1
# print(f2(1, 3))                 # Should print 4
# print(f2(1, 4, -12))            # Should print -7
# print(f2(7, 9, 1, 3, 4, 9, 0))  # Should print 33
# https://www.geeksforgeeks.org/python-program-to-find-sum-of-elements-in-list/
# https://stackoverflow.com/questions/4362586/sum-a-list-of-numbers-in-python
# def f2(a):
#  b = sum(a)
# return b


#a = [7, 6, 5, 4]


# What thing do you have to add to make this work?
# print(f2(a))    # Should print 22


# Write a function f3 that accepts either one or two arguments. If one argument,
# it returns that value plus 1. If two arguments, it returns the sum of the
# arguments. Google "python default arguments" for a hint.
# https://www.geeksforgeeks.org/default-arguments-in-python/
# https://www.w3schools.com/python/python_conditions.asp

# YOUR CODE HERE
"""
def f3(x=0, y=0):
    if x and y:
        return x + y
    elif x:
        return x + 1
    else:
        print('add arguments')


#print(f3(1, 2))  # Should print 3
print(f3(8))     # Should print 9
"""


"""
Often *args and **kwargs are used together in a 
function where we have at least one required argument. 
In these instances, order matters. Positional-only parameters (required arguments)
must come first, so ``argsand**kwargs` are placed *after any required arguments.
"""
# https://wsvincent.com/python-args-kwargs/
# By using *args we can attach a variable-length number of arguments into our function.
# ---
# **kwargs lets you pass a keyworded variable-length of arguments to your function.
# items() method for **kwargs : just returns key/value with no {} outside

# Write a function f4 that accepts an arbitrary number of keyword arguments and
# prints out the keys and values like so:
# As we can see, we can mix positional arguments with keyword arguments during a function call.
#  But we must keep in mind that keyword arguments must follow positional arguments.
# SyntaxError: non-keyword arg after keyword arg
# the * or ** is what matters, name after is foobar for arbitrary arguments &
# arbitrary key word arguments

# key: foo, value: bar
# key: baz, value: 12
#
# Google "python keyword arguments".

# YOUR CODE HERE
# vscode tabs for me?


def f4(reqArg, **things):
    print(reqArg)
    if things:
        for key, value in things.items():
            print("key:", key, ":", "value:", value)

def f5(*arg):
    return arg[0] * arg[1] * arg[2]

function f5(...z){
 return z
}

f5(1,2,3) 



# Should print
# key: a, value: 12
# key: b, value: 30
#f4(a=12, b=30)

# Should print
# key: city, value: Berkeley
# key: population, value: 121240
# key: founded, value: "March 23, 1868"
#f4(city="Berkeley", population=121240, founded="March 23, 1868")

# https://wsvincent.com/python-args-kwargs/
# using required args,*args & **kwargs)
d = {
    "monster": "goblin",
    "hp": 3
}


# What thing do you have to add to make this work?
f4(d)
