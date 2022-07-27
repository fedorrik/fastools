from Bio.SeqIO import parse
from re import findall
from sys import argv


kmer = argv[2].upper()

for record in parse(argv[1], 'fasta'):
    n_hits = len(findall(kmer, str(record.seq).upper()))
    print(record.id, n_hits)

