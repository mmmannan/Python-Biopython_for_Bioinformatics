# Exercise 2 Week 3

seq = input("Enter a sequence: ")
A_count = seq.count("A")
T_count = seq.count("T")
G_count = seq.count("G")
C_count = seq.count("C")

if A_count > 0:
    print("A count: ", A_count)
else:
    print("A not found")

if T_count > 0:
    print("T count: ", T_count)
else:
    print("T not found")

if C_count > 0:
    print("C count: ", C_count)
else:
    print("C not found")
    
if G_count > 0:
    print("G count: ", G_count)
else:
    print("G not found")
