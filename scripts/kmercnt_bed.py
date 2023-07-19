import gzip
from Bio import Seq
from Bio.Data import IUPACData
from Bio.SeqIO import parse
from itertools import product
from re import finditer
from sys import argv


def extend_ambiguous_dna(seq): 
    # return list of all possible sequences given an ambiguous DNA input
    d = IUPACData.ambiguous_dna_values
    return list(map(''.join, product(*map(d.get, seq))))


infa = argv[1]
kmer_list = extend_ambiguous_dna(argv[2].upper())

total_hits = 0
for record in parse(infa, 'fasta'):
    matches_coords = []
    for kmer in kmer_list:
        matches_coords += [(m.start(0), m.end(0), kmer) for m in finditer(kmer, str(record.seq).upper())]
    for i in matches_coords:
        print(record.id, i[0], i[1], i[2], sep='\t')

