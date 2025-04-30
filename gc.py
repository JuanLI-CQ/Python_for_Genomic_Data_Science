#!/usr/bin/python3

"""
This is my first Python program.
It computes the GC content of a DNA sequence.
"""

dna = 'acgctcgc'
no_c = dna.count("c")
no_g = dna.count('g')
dna_length = len(dna)
gc_percent = (no_c + no_g) * 100.0 / dna_length
print("The DNA sequence's GC content is %5.3f %%" % gc_percent)

print("%d" % 10.6) # 10.6 is first tarnsformed into an integer
print("%%3d" % 10.6) # notice the space in front of 10
print("%o" % 10) # use %o for an octal/%x for a hexadecimal integer
print("%e" % 10.6) # 'E' notation uses powers of 10
print("%s" % dna) # print string