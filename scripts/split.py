from sys import argv
from Bio.SeqIO import parse, write


out_dir = argv[2]
for record in parse(argv[1], 'fasta'):
    write(record, '{}/{}.fa'.format(out_dir, record.id), 'fasta')

