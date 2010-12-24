import bowtie_parser2
import sys

map_file = sys.argv[1]
fp = open(sys.argv[2], 'w')

for n, line in enumerate(bowtie_parser2.read(open(map_file))):
    readname = line.readname
    contig_id = line.seqid
    fp.write(readname.split(' ')[0].rstrip()+'\n')
    #fp.write()
    #fp.write('\n')
