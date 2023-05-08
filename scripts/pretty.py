from Bio.SeqIO import parse, write
from sys import argv


infa = parse(argv[1], 'fasta')
write(infa, argv[2], 'fasta')

