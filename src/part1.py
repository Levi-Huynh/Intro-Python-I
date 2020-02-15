
# declaring variable
name = 'austen'


CONST_NAME = ' '  # variables don't need to be defined with any special type to them

# place you declare variable or scope, variable will only live in that scope

# string concatenation
print("Hello" + name)

# f-stirngs
# `Hello {name}`
print(f'Hello, {name}')  # make sure python 3.6 version
# create a list with some numbers
p = [10, 60, 20, 5]  # can combine other data types here
print(p)
p.append(77)
print(p)
#
# """
# print all values in each list
squares = []
for number in p:
    squares.append(number*number)
    print(number)

for (i, e) in enumerate(p):
    print(f'Element at {i} is {e}')

# [10, 60, 30] => [(0,10), (1, 60), (2, 30)]
"""
The two most widely known and easy to understand approaches to parameter passing amongst programming languages are pass-by-reference and pass-by-value. Unfortunately, Python is “pass-by-object-reference”, of which it is often said: “Object references are passed by value.


"""
# empty dictionary
new_dict = {}

food = {'apple': 'fruit', 'cucumber': 'vegg'}


for key, value in food_dict.items():
    print(f'{key} {value}')

    if 'carrot' in fruits:
        print('blah blah')
