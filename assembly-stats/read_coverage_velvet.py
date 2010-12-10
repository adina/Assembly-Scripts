#! /usr/bin/env python

import screed
import sys

K=45
THRESHOLD=500

output = sys.argv[2]
fp = open(output, 'w')

for n, record in enumerate(screed.fasta.fasta_iter(open(sys.argv[1]), parse_description=False)):
    name = record['name']
    length = int(record['name'].split('_')[3])+45-1
    coverage = float(record['name'].split('_')[5])
    sequence = record['sequence']
    if length > THRESHOLD:
        print >>fp, round(coverage, 3)

