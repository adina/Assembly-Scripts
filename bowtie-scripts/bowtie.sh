#! /bin/bash
#scriptpath=$1
filename=$1
#K=$3

BASE=`basename $filename`
BASE2=${BASE%%.fa.ass*}

bowtie -v 2 -f /mnt/prairie-assem/bowtie/indexes-groups/$BASE2.fa-k33 /mnt/prairie-fastas/fastas/$BASE2.fa /mnt/prairie-assem/bowtie/maps-groups/$BASE2-k33.map

