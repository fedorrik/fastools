import gzip
from Bio.SeqIO import parse, write
from sys import argv


wanted_id = argv[1]
infa = argv[2]


if infa[-3:] == '.gz':
    with gzip.open(infa, 'rt') as handle:
        for record in parse(handle, 'fasta'):
            if record.id == wanted_id:
                print('>{}\n{}'.format(record.id, record.seq))
                break

else:
    for record in parse(infa, 'fasta'):
        if record.id == wanted_id:
            print('>{}\n{}'.format(record.id, record.seq))
            break


