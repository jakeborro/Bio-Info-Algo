# Builds lists of kmers and their frequencies
def freq_kmers(strand, k):
    kmers = {}
    freqs = {}
    positions = {}
    for i in range(len(strand) - k):
        kmers[strand[i:i+k]] = kmers.get(strand[i:i + k], 0) + 1
        positions[strand[i:i + k]] = positions.get(strand[i:i + k], []) + [i]
        f = kmers[strand[i:i + k]]
        if f>1:
            freqs[f-1].remove(strand[i:i + k])
        freqs[f] = freqs.get(f,[]) + [strand[i:i + k]]
    return kmers, freqs, positions

# Determines kmers that appear the most
def topkmers(strand, k):
    kmers, freqs, positions = freq_kmers(strand, k)
    output = freqs[max(freqs.keys())]
    print " ".join(output)
    return output
    
# Identifies loci of pattern start point
def patmatch(pattern, strand):
    kmers, freqs, positions = freq_kmers(strand, len(pattern))
    output = positions[pattern]
    print " ".join("{}".format(i) for i in output)
    return output
    
p = patmatch("pattern","""sequence""")


