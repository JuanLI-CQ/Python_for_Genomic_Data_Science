#!/usr/bin/python3

# Loops operation, while and for loops
# while loop test a condition, if true, loop
# given a DNA sequence find the positons of all canonical donor splice site candidates in the sequence
dna=input('Enter DNA sequence:')
pos=dna.find('gt',0) # postion of donor splice site

while pos>-1 :
    print("Donor splice site candidate at positon %d"%pos)
    pos=dna.find('gt',pos+1)


# for loop
motifs=["attccgt","agggggtttttcg","gtagc"]
for m in motifs:
    print(m, len(m))

# iterate over a range of numbers
for i in range(4):
    print(i)

for i in range(1,10,2):
    print(i)

# find if all characters in a given protein sequence are valid amino acids
# pseudocode
# for each character in protein sequence:
# .   if character is not amino acid:
# .        print invalid character and its positon in protein

protein='SDVIHRYKUUPAKSHGWYVCJRSRFTWMVWWRFRSCRA'
for i in range(len(protein)):
    if protein[i] not in 'ABCDEFGHIKLMNPQRSTVWXYZ':
        print("protein contains invalid amino acid %s at postion %d" % (protein[i],i))

# breaking out of loops
protein='SDVIHRYKUUPAKSHGWYVCJRSRFTWMVWWRFRSCRA'
for i in range(len(protein)):
    if protein[i] not in 'ABCDEFGHIKLMNPQRSTVWXYZ':
        print("This is not a valid protein sequence!")
        break # terminate the loop

