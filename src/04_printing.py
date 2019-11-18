"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string
method, and by using f-strings.
"""

 #x = 10
 #y = 2.24552
 #z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
# print(b'x is %(value)i, y is %(number).2f , z is %(string)s !' %
#     {b"value": 10, b"number": 2.25, b'string': b" 'I like turtles'"})

# Use the 'format' string method to print the same thing

# '{}{}{}{.2f}{third}'.format('x is', 10, ',y is', 2.25, 'I like turtles')
#print("x is {}, y is {:.2f}, z is 'I like turtles!'".format(10, 2.25))


# Finally, print the same thing using an f-string
# indentation for all lines must be consistent!
val = 10
valu = 2.24552
value = 'I like turtles!'
print(f"x is {val}, y is {valu:.2f}, z is {value}")