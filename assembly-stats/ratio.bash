#!/bin/bash

for file in *.fa;
do
    echo $file >> calc-kmer-part.out
    python ~/khmer/scripts/calc-kmer-to-partition-ratio.py $file >> calc-kmer-part.out
done 