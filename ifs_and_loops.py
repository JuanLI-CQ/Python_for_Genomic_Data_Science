# Decision making
# if statment
dna=input('Enter DNA sequence:')
# agcgcgggtatatatatgcnccann

if 'n' in dna :
    nbases=dna.count('n')
    print("dna sequence has %d undefined bases" % nbases)
else:
    print("dna sequencehas no undefined bases")

# boolean expression
0<1

len('atgcga') >=10

# comparison operators
'a' == "A"
"GT" != "AG"
'A' < 'C'
10+1 == 11

# memebership operators
motif='gtccc'
dna='atatattgtcccattt'
motif in dna

# identify operators
alphabet=['a','c','g','t']
newalphabet=alphabet[:]
alphabet == newalphabet

alphabet is newalphabet # it's gonna return False as the newalphabet variable is stored in different space, they are different objects

# multiple alternative executions with logical operators
dna=input('Enter DNA sequence:')
# agcgcgggtatatatatgcnccann

if 'n' in dna or 'N' in dna:
    nbases=dna.count('n') + dna.count('N')
    print("dna sequence has %d undefined bases" % nbases)
# elif 'N' in dna:
#     print("dna sequencehas undefined bases")
else:
    print("dna sequencehas no undefined bases")





