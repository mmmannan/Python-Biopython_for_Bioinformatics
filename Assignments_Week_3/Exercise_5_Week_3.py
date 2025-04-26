# Week_3
# Exercise 5 - Filtering

file_path = "/Users/ACER/Documents/cBlast/Python/Week_3/Sequences.seq"

with open(file_path) as f:
    data = f.readlines()


# A. How many sequences are in that file?
# Answer to the Question No. (A)
# Code:
num_of_seqs = len(data)
print(f"There are {num_of_seqs} sequences in the file")
# Result: There are 999 sequences in the file



# B. How many have the pattern CTATA?
# Answer to the Question No. (B)
# Code:
n = 0
for seq in data:
    if "CTATA" in seq:
        n = n + 1

print(f"{n} sequences have the pattern CTATA")
# Result: 391 sequences have the pattern CTATA



# C. How many have more than 1000 bases?
# Answer to the Question No. (C)
# Code:
count = 0
for seq in data:
    if len(seq) > 1000:
        count = count + 1
        
print(f"{count} sequences have more than 1000 bases")
# Result: 483 sequences have more than 1000 bases



# D. How many have over 50% GC composition?
# Answer to the Question No. (D)
gc_seq_count = 0
for seq in data:
    g_count = seq.count("G")
    c_count = seq.count("C")
    gc_content = ((g_count + c_count)/len(seq))*100
    if gc_content > 50:
        gc_seq_count = gc_seq_count + 1
        
print(f"{gc_seq_count} sequences have over 50% GC composition")
# Result: 320 sequences have over 50% GC composition



# E. How many have more than 2000 bases and more than 50% GC composition?
# Answer to the Question No. (E)
seq_count = 0
for seq in data:
    seq_length = len(seq)
    g_count = seq.count("G")
    c_count = seq.count("C")
    gc_content = ((g_count + c_count)/len(seq))*100
    if (seq_length > 2000) and (gc_content > 50):
        seq_count = seq_count + 1
    
print(f"{seq_count} sequences have more than 2000 bases and more than 50% GC composition")
# Result: 16 sequences have more than 2000 bases and more than 50% GC composition

