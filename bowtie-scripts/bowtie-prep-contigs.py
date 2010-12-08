#! /usr/bin/env python

import screed
import sys

'''
Usage:  python bowtie-prep-contigs.py [/mnt/assem1/contigs.fa] [1000]
Note that the input file must contain directory.
'''

THRESHOLD = int(sys.argv[2])

for record in screed.fasta.fasta_iter(open(sys.argv[1]), parse_description=False):
    name = record['name']
    sequence = record['sequence']
    index = sys.argv[1].find('group')
    group_id = str(sys.argv[1][index+5:].split('.')[0])
    name = name.split()[0]
    new_name = 'group'+ group_id + '|' + name
    if len(sequence) >= THRESHOLD:
        print '>%s\n%s' % (new_name, sequence,)

    
