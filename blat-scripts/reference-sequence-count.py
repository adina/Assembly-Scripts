#! /usr/bin/env python
import screed
import sys

for record in screed.fasta.fasta_iter(open(sys.argv[1]), parse_description=False):
    name=record['name']
    sequence=record['sequence']

    print name, len(sequence)
