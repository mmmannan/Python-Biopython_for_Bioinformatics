# Excercise 4 Week 3

file_path = "/Users/ACER/Documents/cBlast/Python/Week_3/10_sequences.txt"

with open(file_path) as f:
    data = f.readlines()

for line in data:
    line = line.rstrip()
    if "CTATA" in line:
        print(line)


# print the index of the first time that pattern is found
for line in open(file_path):
    if "CTATA" in line:
        index = line.find("CTATA")
        print(f"The first time pattern CTATA is found at index {index} in line {data.index(line) + 1}")
        break
