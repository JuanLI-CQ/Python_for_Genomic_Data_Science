# reading a fasta file
# exercise: build a dictionary containing all sequences from a fasta file

# pseudo code

try:
    f = open('file.fasta')
except IOError:
    print("File file.fasta does not exist!!")

seqs={}
for line in f:
    # let's discard the newline at the end (if any)
    line=line.rstrip() # the method rstrip([chars]) returns a copy of the string with trailing characters chars removed
    # distinguish header from sequence
    if line[0]=='>': # or line.statswith('>')
        words=line.split()
        name=words[0][1:]
        seqs[name]=''
    else: # sequence, not header
        seqs[name] = seqs[name] + line
f.close()

# retrieving data from dictionaries
# we can retrieve the key and corresponding value from our dictionary using the items() method
for name,seq in seqs.items():
    print(name,seq)

# command line arguments
# scripts often need to process command line arguments.
# suppose a script that parses a FASTA file is called processfasta.py and you want to run it on a file whose
# name we give as an argument in the command line

# python processfasta.py file.fasta

# The arguments of the above command are stored in the sys module's argv attribute as a list
import sys
print(sys.argv)
