#! /bin/bash

filename=$1

BASE=`basename $filename`

python ~/khmer/scripts/calc-kmer-to-partition-ratio.py $filename > /mnt/corn-assem/ratio-files/$BASE.ratio


