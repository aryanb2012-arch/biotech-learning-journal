# Broken DNA Analyzer Script
sequence = input("Enter a DNA sequence: ")

# Clean up input string
clean_seq = sequence.upper()

# Count specific bases
a_count = clean_seq.count("A")
t_count = clean_seq.count("T")

# Calculate total length
total_length = len(sequence)

# Print metrics
print(f"Total bases: {total_length}")
print(f"Adenine count: {a_count}")

# Generate simple RNA sequence
rna_seq = clean_seq.replace("T", "U")
print(f"RNA Transcript: {rna_seq}")

# Check if sequence contains only A and T
if a_count + t_count == total_length:
    print("This sequence is strictly AT-rich!")
else:
    print("This sequence is not strictly AT-rich!")