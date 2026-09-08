gen_code = {
    'AUG': 'M', 'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'UAA': 'STOP',
    'UAG': 'STOP', 'UGA': 'STOP'
}



#Turning mRNA into series of 3-base codons
mRNA = input("Please type in a mRNA sequence: ").upper()
protein = " "

for i in range (0,len(mRNA),3):
    codon = mRNA[i:i+3]
    if len(codon) < 3:
        break
    
    
    amino_acid = gen_code.get(codon,"?")
    
    if amino_acid == "STOP":
        print(f"STOP codon {codon} encountered at position {i}. Translation Terminated")
        break
    
    protein += amino_acid
    
print(f"Translated Protein Sequence: {protein}")