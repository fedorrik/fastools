import gzip
from Bio import Seq
from Bio.Data import IUPACData
from Bio.SeqIO import parse
from itertools import product
from re import findall, sub
from sys import argv


def extend_ambiguous_dna(seq): 
    # return list of all possible sequences given an ambiguous DNA input
    d = IUPACData.ambiguous_dna_values
    return list(map(''.join, product(*map(d.get, seq))))


infa = argv[1]
kmer_list = extend_ambiguous_dna(argv[2].upper())

# add reverse complement versions
kmer_list += [str(Seq.Seq(i).reverse_complement()) for i in kmer_list]

total_hits = 0

if infa[-3:] == '.gz':
    with gzip.open(infa, 'rt') as handle:
        for record in parse(handle, 'fasta'):
            seq = sub('-', '', str(record.seq))
            n_hits = 0
            for kmer in kmer_list:
                n_hits += len(findall(kmer, seq.upper()))
            print(record.id, n_hits, sep='\t')
            total_hits += n_hits          

else:
    for record in parse(infa, 'fasta'):
        seq = sub('-', '', str(record.seq))
        n_hits = 0
        for kmer in kmer_list:
            n_hits += len(findall(kmer, seq.upper()))
        print(record.id, n_hits, sep='\t')
        total_hits += n_hits

print()
print(infa, total_hits, sep='\t')

