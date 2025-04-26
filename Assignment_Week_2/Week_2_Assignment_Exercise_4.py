# Exercise 4
restriction_sites = ["GAATTC",   #EcoRI
                     "GGATCC",   #BamHI
                     "AAGCTT",   #HindIII
                    ]

seq = raw_input("Enter a sequence: ")
for i in restriction_sites:
    print(i,"is in the sequence:",i in seq)
