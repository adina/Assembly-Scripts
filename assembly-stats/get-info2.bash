#!/bin/bash

for dir in /mnt/assembly/completed-assemblies/*ass.45;
do
    #echo $dir
    cp $dir/contigs.fa ~/${dir#*iowa-}-contigs.fa
    #echo $dir/contigs.fa
done