# Builds lists of kmers and their frequencies
def freq_kmers(genome, k):
    kmers = {}
    freqs = {}
    positions = {}
    for i in range(len(genome) - k):
        kmers[genome[i:i+k]] = kmers.get(genome[i:i + k], 0) + 1
        positions[genome[i:i + k]] = positions.get(genome[i:i + k], []) + [i]
        f = kmers[genome[i:i + k]]
        if f>1:
            freqs[f-1].remove(genome[i:i + k])
        freqs[f] = freqs.get(f,[]) + [genome[i:i + k]]
    return kmers, freqs, positions

# Determines kmers that appear the most
def topkmers(genome, k):
    kmers, freqs, positions = freq_kmers(genome, k)
    output = freqs[max(freqs.keys())]
    print " ".join(output)
    return output

print freq_kmers("genome", k)
print topkmers("genome", k)
