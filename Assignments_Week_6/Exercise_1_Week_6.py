# Exercise 1 Week 6

seq = input("Enter DNA: ")
counts = {}
for base in seq:
    counts[base] = counts.get(base, 0) + 1

counts_keys = counts.keys()

for base in sorted(counts_keys):
    print(base,"=",counts[base])
