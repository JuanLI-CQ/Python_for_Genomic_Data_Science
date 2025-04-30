#!/usr/bin/python3
"""
processfasta.py builds a dictionary with all sequences from a FASTA file.
"""

import sys
filename=sys.argv[1]

try:
    f = open(filename)
except IOError:
    print("File %s does not exist!!" % filename)

# To give python program more flexibility, some to be executed always, some need to be revoked for the functions
# It's parsing command line arguments, and we can achieve it with getopt.
# Python's getopt module can help with processing the arguments sys.argv.

import getopt

# suppose the processfasta.py script reads a FASTA file 
# but only stores in the dictionary the sequences bigger than a given length provided in the command line
# processfasta.py -l 250 file.fasta

def usage():
    """
    processfasta.py: reads a FASTA file and builds a dictionary with all sequences bigger than a given length

    processfasta.py [-h] [-l <length>] <filename>
        -h print this message
        -l <length> filter all sequences with a length smaller than <length>
                    (default <length>=0)
        filename the file has to be in FASTA format
    """

# o = list of optional arguments; a = list of required arguments
o, a = getopt.getopt(sys.argv[1:], 'l:h')  
# 'l:h': a list of all the arguments that the user can be provided with a - command. e.g. -l, -h
# when ':' is added just after, this means that the option expects a value. here means, the -l needs a value if the user is gonna use this parameter.

# create a dictionary
opts={}
# initialize the length of our sequence to be zero
seqlen=0

for k,v in o:
    # store all arguments that get passed to in the dictionary, in this case, {"-l":"250", "-h":"..."}
    opts[k] = v
# if -h argument is in the keys of dict opts, we are gonna print out usage message
if '-h' in opts.keys():
    usage(); sys.exit()

# user not need help, we need to look at the argument, to see if user give us required arguments, in this case user has to give us a filename.
# to check if the filename is there, to check the length of the list a. 
# In this case, the list of argument a needs to have the filename with length greater than 1.
if len(a) < 1:
    usage(); sys.exit("input fasta file is missing")

# Next, we are gonna to check if user pass optional arguments, in this case -l.
if '-l' in opts.keys():
    if int(opts['-l']) < 0:
        print("Length of sequence should be positive!"); sys.exit(0)
    seqlen=opts['-l']

# Reminder (using the system environment): when we run a script/program in the UNIX envrionment there are standard streams recognized by a computer program
# Standard input or stdin is stream data (often text) going into a program. Unless redirected, standard imput is expexted from the keyboard which started the program.
# Standard output or stdout is the stram where a program writes its output. Unless redirected, standard output is the text terminal which initiated the program.
# Standard error or stderr is another output stream typically used by programs to output error messages or diagnostics. It is a stream independent of standard output 
# and can provide error messages even when stdout has been redirected. stderr can also be redirected separately

# my_program | my_script.sh 1>program_output.txt 2>error_messages.txt

# sys.stdin.read()
# sys.stdout.write()
# sys.stderr.write()