from sys import argv


mfa = argv[1]
# create list with sequenses
seqs = []
with open(mfa) as f:
    seq = ''
    for line in f:
        if line[0] != '>':
            seq += line.strip()
        else:
            seqs.append(seq)
            seq = ''
seqs.append(seq)
seqs = seqs[1:]

# create consensus sequence
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
    if most_freq[0] / len(seqs) > 0.5:
        cons += most_freq[1]
    else:
        cons += 'N'
print('>CONS-{}\n{}'.format('.'.join(mfa.split('.')[:-1]), cons))

