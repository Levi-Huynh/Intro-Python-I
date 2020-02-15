"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import os
import sys
# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
#https://www.pythonforbeginners.com/system/python-sys-argv
#https://www.pythonforbeginners.com/argv/more-fun-with-sys-argv
#The list of command line arguments passed to a Python script. argv[0] is the script 
# name (it is operating system dependent whether this is a full pathname or not). If the command was executed using the -c command line option to the interpreter, argv[0] is set to the string '-c'. If no script name was passed to the Python interpreter, argv[0] is the empty string.
#gets info about the users's sytem (get login, os, platform version)

#To loop over the standard input, or the list of files given on the command line, see the fileinput module.
print((sys.argv))
#sys.argv[0] items typed in

# Print out the OS platform you're using:
# YOUR CODE HERE
# print(sys.platform)

# Print out the version of Python you're using:
# YOUR CODE HERE
# print(sys.version)

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
# print(os.getpid())

# Print the current working directory (cwd):
# YOUR CODE HERE
# print(os.getcwd)

# Print out your machine's login name
# YOUR CODE HERE
#print(os.getlogin())
