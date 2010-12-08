#! /bin/bash
#scriptpath=$1
filename=$1
#K=$3

BASE=`basename $filename`
python ~/khmer/scripts/add-groupid-for-bowtie.py $filename/contigs.fa /mnt/bowtie/bowtie-indexes/$BASE-groupid.fa

