# Make a class LatLon that can be passed parameters `lat` and `lon` to the
"""
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.

----
class MyClass:
  x = 5
  p1 = MyClass()
print(p1.x)
---

-----
It does not have to be named self ,  (first param is the current instance of the class, used to access
variables that belongs to the class)
you can call it whatever you like, but it has to be the first parameter of any function in the class:

------
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
----

----ADDING FUNCTIONS
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
---------

----MODIFYING PROPERTIES ON OBJECTS
p1.age = 40
---------

----DELETE PROPERTIES FROM OBJECT
del p1.age
------

----CLASS DEF CAN'T BE EMPTY, BUT IF CLASS HAS NO CONTENT PUT IN PASS STATEMENT
class Person:
  pass
---

-----SUPER----
n order to use the function properly, the following conditions must be met:

The method being called upon by super() must exist
Both the caller and callee functions need to have a matching argument signature
Every occurrence of the method must include super() after you use it
You might start with a single inheritance class, but later, if you decide to add another base class – or more 
– the process goes a lot more smoothly. You only need to make a few changes as opposed to a lot.

class MyParentClass():
def __init__(self):
pass

class SubClass(MyParentClass):
def __init__(self, x, y):
super()._init_(x, y)
----

"""
# constructor

# YOUR CODE HERE

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE

# https://www.journaldev.com/22460/python-str-repr-functions


class LatLon():
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon


class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(name, lat, lon)

    def printWaypont(self):
        return 'Waypoint(name='+self.name+', lat='+str(self.lat)+', lon='+str(self.lon) + ')'

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
# https://www.geeksforgeeks.org/oop-in-python-set-3-inheritance-examples-of-object-issubclass-and-super/
# https://stackoverflow.com/questions/47007200/how-do-i-add-arguments-to-a-subclass-in-python-3
# def __init__ takes 4 positional arguments

# https://stackoverflow.com/questions/53043399/subclass-constructor-throws-typeerror-init-takes-2-positional-arguments-b
# JUST INCLUDE THE PARENT attributes IN `super().__int__()` keep all of the attributes you'll use in `def __init__(self, name, diff, size, lat, lon)
# `


class Geocache(LatLon):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.difficulty = difficulty
        self.size = size

    def printGeo(self):
        return 'Geo(name='+self.name+', diff='+str(self.difficulty)+', size='+str(self.size)+', lat='+str(self.lat)+', lon='+str(self.lon) + ')'

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521


# YOUR CODE HERE
d = Waypoint("catacombs", 41.70505, -125.51521)
waypoint1 = d.printWaypont()
print(waypoint1)


# Without changing the following line, how can you make it print into something
# https://www.journaldev.com/22460/python-str-repr-functions
# more human-readable? Hint: Look up the `object.__str__` method


# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556
g = Geocache("NewberryViews", 1.5, 2, 44.052137, -121.41556)
gprint = g.printGeo()
print(gprint)

# YOUR CODE HERE

# Print it--also make this print more nicely
# print(geocache)
