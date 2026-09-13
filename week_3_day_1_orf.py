gen_code = {
    'AUG': 'M', 'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'UAA': 'STOP',
    'UAG': 'STOP', 'UGA': 'STOP'
}

mrna = input("Please input a mRNA sequence: ").upper()
protein = " "
translating = False

for i in range(0, len(mrna), 3):
    codon = mrna[i:i+3]
    if len(codon) < 3:
        break
    
    
    if codon == "AUG":
        translating = True
        
    if translating:
        amino_acid = gen_code.get(codon, "?")
        if amino_acid == "STOP":
            print(f"STOP codon {codon} encountered. Translation finished")
            break
        protein += amino_acid
    
    
print(f"Translated ORF Protein: {protein}")
