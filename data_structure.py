gene_expression=["gene", 5.15e-08, 0.000138511, 7.33e-08]

gene_expression[2]

gene_expression[0]='Lif'
print(gene_expression)

# change elements in string with motif[0] is not possible
motif='nacggggtc'

gene_expression[-3:]
gene_expression[:]

# replace the second and third elements to 6.06e-07, two elements are going to be replace with one element
gene_expression[1:3]=[6.09e-07]
# gene_expression[:]=[] # this clears the list, it's changed to an empty list.

# concatenate string
gene_expression+[5.16e-08, 0.000138511]

len(gene_expression)

# The del statement can be used to remove elements and slices from a list destructively
del gene_expression[1]

# extend a list
gene_expression.extend([5.16e-08, 0.000138511])

# count the number of times an element appears in a list
print(gene_expression.count('Lif'), gene_expression.count('gene'))

# reverse all elements in a list
gene_expression.reverse()

# Treat list as stacks, by using list methods append and pop, where the last element added is the first element retrieved ("last-in,first-out")
stack=['a','b','c','d']

# To add an item to the top of the stack, use append()
stack.append('e')

# To retrieve an iterm from the top of the stack
elem=stack.pop()

# sorting lists, sorted() does not change the order of elements, .sort() do not
mylist=[3,31,123,1,5]
sorted(mylist)
mylist

mylist.sort()
mylist

# .sort() can sort strings 
mylist=['c','g','a','f']

# Tuple consists of a number of values separated by commas
t=1,2,3
t

t=(1,2,3)
t

# set is an unordered collection with no duplicate elements
brca1={'DNA repair', 'zinc ion binding', 'DNA binding', 'ubiquitin-protein transferase activity', 'DNA repair', 'protein ubiquitination'} # duplicates are gonna be removed
brca1

brca2={'protein binding','H4 histone acetyltransferase activity', 'nucleoplasm', 'DNA repair','double-strand break repair',
       'double-strand repair vioa homologous recombination'}

# operation with sets
brca1 | brca2 # union

brca1 & brca2 # intersection

brca1 - brca2 # difference

# An dictionary is an unordered set of key and value pairs, with the requirement that the keys are unique (withing one dictionary)
TF_motif ={'SP1':'gggcgg', 'C/EBP':'attgcgcaat', 'ATF':'tgacgtca','c-Myc':'cacgtg','Oct-1':'atgcaaat'}

# Access dictionary values
print("The recognition sequence for the ATF transcription is %s." % TF_motif['ATF'])

# Access a key is not part of the dictionary produces an error
print("The recognition sequence for the ATF transcription is %s." % TF_motif['BF-1'])

# So check first if a key is present
'NF-1' in TF_motif 

# Add a new key:value pair to the dictionary
TF_motif['AP-1'] ='tgagtca'
TF_motif

# Modify an existing entry
TF_motif['AP-1'] ='tga(g/c)tca'
TF_motif

# delect a key from the dictionary
del TF_motif['SP1']
TF_motif

# Add another dictionary (multiple key:value pairs) to the current one
TF_motif.update({'SP1':'gggcgg', 'C/EBP':'attgcgcaat','Oct-1':'atgcaaa'})
TF_motif

# The size of a dict
len(TF_motif)

# Get a list of all the keys in the dict
list(TF_motif.keys())

# get a list of all the values
list(TF_motif.values()) # return in arbitrary order
# Get sorted
sorted(TF_motif.keys())
sorted(TF_motif.values()) # uppercase always comes first than the lowercase