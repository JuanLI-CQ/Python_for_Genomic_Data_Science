# reading and writing files
# to read or write files use the built-in function open(filename, mode)
f=open('myfile.txt','r') # 'r' is the default value for the mode parameter, so we can just omit it
f=open('myfile.txt')

# write into a file
f=open('myfile','w')

# if the file 'myfile' already exists using mode 'w' truncates its content first. 
# To append to the end of the file, if it exits, use mode 'a'.
f = open('myfile', 'a')

# if you attempt to open a file that does not exist, Python will produce an error message.
# A common way to let your program handle this type of error properly is to specify what to do in case of errors
try:
    f=open('myfile.txt')
except IOError:
    print("the file myfile does not exist!!")

# reading from a file
# an efficient and fast way to read the content of a file is by looping over the file object
for line in f:
    print(line)

# the content of a file can be also read using the read() method of the file object f
f.read() # nothing print out 'cuz it just finished reading, nothing left to be read
# changing positions within a file object
# to change the file object's position, use f.seek(offset, from_what). 
# The position is computed from by adding offset to a refenrence point. 
# the reference point is selected by the from_what argument, 
# which in text files is only allowed to be 0 signifying the beginning of the file
f.seek(0)
f.read()
# you can also read a single line from the file
f.seek(0)
f.readline()


# write into a file
# f.write(string) writes the contents of string to the file, returning the number of characters 
# written in python 3.x or None in Python 2.x
f=open('myfile.txt', 'a')
f.write('This is the third line.')

# closing a file object
# when you're done with a file, call f.close() to close it and free up any system resources taken up by the open file
f.close()
