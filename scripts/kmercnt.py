from Bio.SeqIO import parse
from re import findall
from sys import argv


kmer = argv[2].upper()

total_hits = 0
for record in parse(argv[1], 'fasta'):
    n_hits = len(findall(kmer, str(record.seq).upper()))
    print(record.id, n_hits, sep='\t')
    total_hits += n_hits

print()
print(argv[1], total_hits, sep='\t')

