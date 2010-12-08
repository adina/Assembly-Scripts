#!/bin/bash

for dir in /mnt/assembly/completed-assemblies/*ass*;
do
    echo $dir
    #echo ${dir#*iowa-}
    python ~/khmer/scripts/assemstats2.py 0 $dir/contigs.fa > /mnt/stats/statistics-pe-asssemblies/${dir#*iowa-}.stat
done