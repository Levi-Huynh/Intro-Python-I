"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though *you can also initialize and
populate dictionaries using comprehensions* just like you can with 
lists!). 

order not guaranteed when doing comprehensions with dictionaries

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictionaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Add a new waypoint to the list
# YOUR CODE HERE
# https://stackoverflow.com/questions/5244810/python-appending-a-dictionary-to-a-list-i-see-a-pointer-like-behavior
#b = {"lat": 51, "lon": -123, "name": "fourth"}

# waypoints.append(b)
# print(waypoints)

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# https://stackoverflow.com/questions/4291236/edit-the-values-in-a-list-of-dictionaries
# https://stackoverflow.com/questions/43060655/update-values-of-a-list-of-dictionaries-in-python
# https://www.pythonforbeginners.com/dictionary/dictionary-manipulation-in-python
# YOUR CODE HERE
#y = []
y = waypoints[0]['lon']
# y.append(-130)

waypoints[0]['lon'] = -131
waypoints[0]['name'] = "not a real place"

# print(waypoints)
# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE

for x in waypoints:
    print(x["lon"], x["lat"], x["name"])
