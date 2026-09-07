#Turning mRNA into series of 3-base codons
mRNA = input("Please type in a mRNA sequence: ")
mRNA1 = mRNA.upper()

for i in range (0,len(mRNA1),3):
    codon = mRNA1[i:i+3]
    if len(codon) == 3:
        print(f"Codon {i//3+1}: {codon}")
    else:
        print(f"Incomplete codon ignored : {codon}")