# Exercise 3 Week 3

file_path = "/Users/ACER/Documents/cBlast/Python/Week_3/10_sequences.txt"

count = 0
for line in open(file_path):
    line = line.rstrip()
    count = count + 1
    print(count, line)
