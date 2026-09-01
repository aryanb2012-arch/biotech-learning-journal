#This is a program to calculate the percentage of C and G in the DNA and to replace each dna strand with its complementary strand
dna = input("Please Enter A Specific DNA String: ")
dna1 = dna.upper()
cgene = dna1.count ("C")
ggene = dna1.count ("G")

#This calculates the percentage of C and G in the DNA
gccount = int(((cgene + ggene)/len(dna1)) * 100)

#This replaces each dna strand with its complimentary strand
result = dna1.replace("A","t").replace("T","a").replace("C","g").replace("G","c")

#This is to find the RNA transcription of this particular DNA
rna = dna1.replace("T","U")

#These are complementary DNA Strand in the reverse direction
complement_reverse = result.upper() [::-1]


print(f"Complement: {result.upper()}")
print(f"Percentage: {gccount}")
print(f"RNA Transcription: {rna}")
print(f"Reverse Complement: {complement_reverse}")

