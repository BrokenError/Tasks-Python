import collections

def arrays_similar(seq1, seq2): 
    if collections.Counter(seq1) != collections.Counter(seq2):
        return False
    else:
        return True