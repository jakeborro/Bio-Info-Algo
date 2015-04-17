# Returns count of target sequence in genome

def pattern_count(genome, sequence):
    count = 0
    for i in range(0, len(genome) - len(sequence) + 1):
        if genome[i : len(sequence) + i] == sequence:
            count += 1
    return count

print pattern_count("genome","sequence")
    
