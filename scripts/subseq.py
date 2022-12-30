from sys import argv
from Bio.SeqIO import parse


seq_id = argv[2].split(':')[0]
start, end = [int(i) for i in argv[2].split(':')[1].split('-')]

for record in parse(argv[1], 'fasta'):
    if record.id == seq_id:
        seq = str(record.seq[start-1 : end])
        print('>{}:{}-{}\n{}'.format(record.id, start, end, seq))
