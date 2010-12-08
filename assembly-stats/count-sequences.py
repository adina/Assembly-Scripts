#! /usr/bin/env python

import screed
import sys

files = open(sys.argv[2:])

for file in files:
    for n, record in screed.fasta.fasta_iter(open(file), parse_description=False):
        continue
    print n
