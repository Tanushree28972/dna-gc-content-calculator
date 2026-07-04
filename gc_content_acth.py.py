# Function to read FASTA file
def read_fasta(filename):
    with open(filename,"r") as file:
        lines = file.readlines()
        sequence = ""
        for line in lines:
            if not line.startswith(">"):
                sequence += line.strip()
    return sequence

# Function to calculate GC content
def calculate_gc(sequence):
    g = sequence.count("G")
    c = sequence.count("C")
    total = len(sequence)
    gc_content = ((g + c) / total) * 100
    return gc_content

def count_codons(sequence):
    codon_count = {}
    for i in range(0, len(sequence) - 2, 3):
        codon = sequence[i:i+3]
        if len(codon) == 3:
            codon_count[codon] = codon_count.get(codon, 0) + 1
    return codon_count

# Main execution
seq = read_fasta(r"C:\Users\Asus\Downloads\actb.fasta")

print("Sequence Length:", len(seq))
print("A count:", seq.count("A"))
print("T count:", seq.count("T"))
print("G count:", seq.count("G"))
print("C count:", seq.count("C"))
print("GC Content: {:.2f}%".format(calculate_gc(seq)))

codons = count_codons(seq)
print("Total Codons:", sum(codons.values()))
print("Most Frequent Codons:", sorted(codons.items(), key=lambda x: x[1], reverse=True)[:5])

# Print top 5 codons
sorted_codons = sorted(codons.items(), key=lambda x: x[1], reverse=True)
print("Top 5 Codons:", sorted_codons[:5])

