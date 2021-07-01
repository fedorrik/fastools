# Usage: python3 mfa2cons.py input.mfa output_cons.fa
from sys import argv


mfa = argv[1]
# Create list with sequenses
seqs = []
with open(mfa) as f:
    seq = ''
    for line in f:
        if line[0] != '>':
            seq += line.strip()
        else:
            seqs.append(seq)
            seq = ''
seqs = seqs[1:]

# Create consensus sequence
cons = ''
for i in range(len(seqs[0])):
    pos = []
    for seq in seqs:
        base = seq[i]
        pos.append(base)
    a = (pos.count('A'), 'A')
    t = (pos.count('T'), 'T')
    g = (pos.count('G'), 'G')
    c = (pos.count('C'), 'C')
    gap = (pos.count('-'), '-')
    most_freq = max((a, t, g, c, gap))
    if most_freq[1] == '-':
        continue
    cons += most_freq[1]

name = '.'.join(mfa.split('.')[:-1]).split('/')[-1]
print('>CONS-{}\n{}'.format(name, cons))

