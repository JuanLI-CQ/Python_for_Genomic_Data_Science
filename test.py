import dnautil

dna='atgagggctaggt'
# specify the module to get the function
dnautil.gc(dna)

from dnautil import *
gc(dna)

from dnautil import gc, has_stop_codon
