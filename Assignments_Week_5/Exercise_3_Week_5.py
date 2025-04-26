# Exercise 3 week 5

seq1 = raw_input("Enter Sequence 1: ")
seq2 = raw_input("Enter Seqeunce 2: ")

def gc_content(sequence):
    g_count = sequence.count("G")
    c_count = sequence.count("C")
    g_c_content = ((g_count + c_count) / len(sequence)) * 100
    return g_c_content

def compare_gc_content(sequence_1, sequence_2):
    gc_content_sequence_1 = gc_content(sequence_1)
    gc_content_sequence_2 = gc_content(sequence_2)
    if gc_content_sequence_1 >  gc_content_sequence_2:
        print("Sequence 1 has higher GC content")
    elif gc_content_sequence_2 > gc_content_sequence_1:
        print("Sequence 2 has higher GC content")
    else:
        print("Both sequences have the same GC content")


compare_gc_content(seq1, seq2)
