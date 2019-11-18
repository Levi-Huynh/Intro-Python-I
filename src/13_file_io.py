"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

A whence value of 0 measures from the beginning of the file, 1 uses the current file position, and 2 uses the end of the file as the reference point. whence can be omitted and defaults to 0, using the beginning of the file as the reference point.
f.tell() returns an integer giving the file object’s current position in the file represented as number of bytes from the beginning of the file when in binary mode and an opaque number when in text mode.
f.write(string) writes the contents of string to the file, returning the number of characters written.
For reading lines from a file, you can loop over the file object. This is memory efficient, fast, and leads to simple code:

To change the file object’s position, use f.seek(offset, whence). 
The position is computed from adding offset to a reference point; 
the reference point is selected by the whence argument.
whence:
 A whence value of 0= beginning of the file, 
 1 = current file position, 
  2 = the end of the file as the reference point. 
  
  whence can be omitted and defaults to 0, using the beginning of the file as the reference point.
>>>
>>> for line in f:
...     print(line, end='')
...
This is the first line of the file.
Second line of the file
If you want to read all the lines of a file in a list you can also use list(f) or f.readlines().
f.readline() reads a single line from the file; a newline character (\n) is left at the end of the string, and is only omitted on the last line of the file if the file doesn’t end in a newline. This makes the return value unambiguous; if f.readline() returns an empty string, the end of the file has been reached, while a blank line is represented by '\n', a string containing only a single newline.

o read a file’s contents, call f.read(size), which reads some quantity of data and returns it as a string (in text mode) or bytes object (in binary mode).

b in mode string? (in text files)
mode
r- read
a-append
w-write


text mode: read and write strings from and to file  (encoded in specific encoding)
-if encoding not spec, default is platform dependent 
-'b' appended to mode == binary 
now data is read & written in form of bytes objects
    'b' this mode should be used for all files that DONT contain text 

- text mode: default when READING is to convert platform specific line endings
    (\n on Unix, \r\n on Windows) to just \n 
-TM: WRITING: 
    -Default: convert occurences of \n back to platform specific line endings 
    -use 'b' mode can corrupt binary data like JPEG & EXE files (care when reading & writing such files)

- with Keyword: File Objects
    -advantage: file properly closed after suite finishes 
    -with shorter w/ try-finally blocks:

>>> with open('workfile') as f:
...     read_data = f.read()

>>> # We can check that the file has been automatically closed.
>>> f.closed
True

-If you’re not using the with keyword, then you should call f.close() to close the file 
- if not, file will stay open,  or diff python implementation will clean up at diff times

-after file is closed, (using with or f.close()) attempts to use file objects will fail

LIST- READ
-Read all lines in file list : 
    - list(f) or f.readlines()

  f.write(string)
  f.write(string) writes the contents of string to the file, returning the number of characters written. 
  >>> f.write('This is a test\n')
15

BEFORE WRITING: OBJECTS NEED TO BE CONVERTED: TO STRING (TEXT MODE) OR BYTES OBJECT(BINARY MODE)
"""

"""
https://www.guru99.com/reading-and-writing-files-in-python.html#3
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
"""
f = open("foo.txt", "r")
if f.mode == "r":
    contents=f.read()
    print(contents)
    f.close()
    close=f.closed
    print(close)
"""


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain
#https://cmdlinetips.com/2012/09/three-ways-to-write-text-to-a-file-in-python/

# YOUR CODE HERE
textList = ["One", "Two", "Three", "Four", "Five"]
"""
issues reading unles comment out the write new text  ==> can't read since not hoisted?   or stops after the write code
not sure
newF = open("bar.txt", "w")
for line in textList: 
    newF.write(line)
    newF.write("\n")
    #newF.close()
    """
f= open("bar.txt", "r")
if f.mode == "r":
    contents=f.read()
    print(contents)

