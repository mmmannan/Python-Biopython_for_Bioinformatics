# Exercise 1 Week 4

seq = raw_input("Enter a protein sequence: ")
hydrophobic_residues = "FILAPVM"
count = 0
for residue in seq:
    if residue in hydrophobic_residues:
        count = count + 1
        if count >= 5:
            print("Hydrophobic signal")
            break
    else:
        count = 0            
else:
    print("No hydrophobic signal")
