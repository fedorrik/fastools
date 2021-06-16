from Bio.SeqIO import parse, write
from sys import argv


infa = parse(argv[0], 'fasta')
write(infa, argv[1], 'fasta')

