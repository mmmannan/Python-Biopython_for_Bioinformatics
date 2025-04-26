# Exercise 1 Week 3

seq = input("Enter a sequence: ")
A_count = seq.count("A")
T_count = seq.count("T")
G_count = seq.count("G")
C_count = seq.count("C")

if A_count > 0:
    print("A count: ", A_count)

if T_count > 0:
    print("T count: ", T_count)

if C_count > 0:
    print("C count: ", C_count)
    
if G_count > 0:
    print("G count: ", G_count)
