#!/bin/bash

for file in /mnt/assemblies/*.fa;
do
    echo $file
    python ~/khmer/scripts/filter-inexact-all.py $file $file-kmer-filt.fa
done