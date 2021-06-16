from sys import argv
from Bio.SeqIO import parse, write

for record in parse(argv[1], 'fasta'):
    write(record, '{}.fa'.format(record.id), 'fasta')

