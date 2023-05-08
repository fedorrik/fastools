import gzip
from Bio.SeqIO import parse
from re import findall
from sys import argv


infa = argv[1]
kmer = argv[2].upper()

total_hits = 0

if infa[-3:] == '.gz':
    with gzip.open(infa, 'rt') as handle:
        for record in parse(handle, 'fasta'):
            n_hits = len(findall(kmer, str(record.seq).upper()))
            print(record.id, n_hits, sep='\t')
            total_hits += n_hits          

else:
    for record in parse(infa, 'fasta'):
        n_hits = len(findall(kmer, str(record.seq).upper()))
        print(record.id, n_hits, sep='\t')
        total_hits += n_hits

print()
print(infa, total_hits, sep='\t')

