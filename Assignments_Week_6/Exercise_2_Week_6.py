# Exercise 2 Week 6

seq = input("Enter DNA: ")
ambiguous_dna_complement = {
"A": "T",
"C": "G",
"G": "C",
"T": "A",
"M": "K",
"R": "Y",
"W": "W",
"S": "S",
"Y": "R",
"K": "M",
"V": "B",
"H": "D",
"D": "H",
"B": "V",
"N": "N",
}

new_seq = []
for base in seq:
    complement_base = ambiguous_dna_complement[base]
    new_seq.append(complement_base)
    
new_seq.reverse()
print("".join(new_seq))

