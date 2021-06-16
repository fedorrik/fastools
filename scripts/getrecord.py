from Bio.SeqIO import parse, write
from sys import argv


wanted_id = argv[1]
infa = argv[2]

for record in parse(infa, 'fasta'):
    if record.id == wanted_id:
        print('>{}\n{}'.format(record.id, record.seq))
        break

