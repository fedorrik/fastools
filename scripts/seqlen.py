import gzip
from sys import argv
from Bio.SeqIO import parse


infa = argv[1]

if infa[-3:] == '.gz':
    with gzip.open(infa, 'rt') as handle:
        for record in parse(handle, 'fasta'):
            print(record.id, len(record.seq), sep='\t')
            
else:
    for record in parse(infa, 'fasta'):
        print(record.id, len(record.seq), sep='\t')

