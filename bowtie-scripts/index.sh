#! /bin/bash
#scriptpath=$1
filename=$1
#K=$3

BASE=`basename $filename`
BASE2=${BASE%%.fa.ass*}

bowtie-build /mnt/prairie-assem/k33/contigs/$BASE2.fa.ass.33-contigs.fa-bowtie.fa /mnt/prairie-assem/bowtie/indexes-groups/$BASE2.fa-k33 
