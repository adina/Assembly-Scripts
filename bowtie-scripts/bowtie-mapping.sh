#! /bin/bash
scriptpath=$1
filename=$2
K=$3

BASE=`basename $filename`
python $scriptpath/strip-and-split-for-assembly.py $filename `basename $filename`

velveth $BASE.ass.$K $K -fasta -short ${BASE}.se -shortPaired ${BASE}.pe && \
velvetg $BASE.ass.$K -read_trkg yes -exp_cov 3 -cov_cutoff 0
