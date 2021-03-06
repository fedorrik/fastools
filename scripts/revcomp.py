from Bio.SeqIO import parse
from sys import argv


data = [[record.id, record.seq] for record in parse(argv[1], 'fasta')]
for i in sorted(data):
    print('>{}\n{}'.format(i[0], i[1].reverse_complement()))

