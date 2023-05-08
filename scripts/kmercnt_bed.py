from Bio.SeqIO import parse
from re import finditer
from sys import argv


kmer = argv[2].upper()

total_hits = 0
for record in parse(argv[1], 'fasta'):
    matches_coords = [(m.start(0), m.end(0)) for m in finditer(kmer, str(record.seq).upper())]
    for i in matches_coords:
        print(record.id, i[0], i[1], sep='\t')

