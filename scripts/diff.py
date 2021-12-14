# Usage: python3 
from Bio.SeqIO import parse
from sys import argv


seqs = [record.seq for record in parse(argv[1], 'fasta')]
ids = [record.id for record in parse(argv[1], 'fasta')]

print('pos', *ids, sep='\t')

for position in range(len(seqs[0])):
    bases = [seq[position] for seq in seqs]
    if len(set(bases)) > 1:
        print(position+1, *bases, sep='\t')
