import gzip
from Bio.SeqIO import parse, write
from sys import argv


infa = argv[1]
out_dir = argv[2]


if infa[-3:] == '.gz':
    with gzip.open(infa, 'rt') as handle:
        for record in parse(handle, 'fasta'):
            write(record, '{}/{}.fa'.format(out_dir, record.id), 'fasta')

else:
    for record in parse(infa, 'fasta'):
        write(record, '{}/{}.fa'.format(out_dir, record.id), 'fasta')

