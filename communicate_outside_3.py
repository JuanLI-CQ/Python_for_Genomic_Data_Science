#!/usr/bin/python3
"""
processfasta.py builds a dictionary with all sequences from a FASTA file.
"""

import sys
import getopt
# filename=sys.argv[1]

# try:
#     f = open(filename)
# except IOError:
#     print("file %s does not exist!!" % filename)

# parsing command line arguments with getopt
# python's getopt module can help with processing the arguments of sys.argv.

# suppose the processfasta.py script reads a FASTA file 
# but only stores in the dictionary the sequences bigger than a given length provided in the command line
# processfasta.py -l 250 file.fasta

# import sys
# print(sys.argv)
# command will give output as ['processfasta.py', 'myfile.fa'], sys.argv[0] is the script's name.
# if "python3 processfasta.py myfile.fa" get executed, then the "processfasta.py" and "myfile.fa" will be stored as variables. 
# we can access them by import sys program 



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
o, a = getopt.getopt(sys.argv[1:], '1:h')  
