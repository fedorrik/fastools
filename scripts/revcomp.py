from Bio.Seq import Seq
from Bio.SeqIO import parse
from os.path import exists
from sys import argv

if exists(argv[1]):
    data = [[record.id, record.seq] for record in parse(argv[1], 'fasta')]
    for i in sorted(data):
        print('>{}\n{}'.format(i[0], i[1].reverse_complement()))
else:
    seq = Seq(argv[1])
    print(str(seq.reverse_complement()))

