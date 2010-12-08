import bowtie_parser
import sys

files = sys.argv[2:]
dict1 = {}
fp = open(sys.argv[1], 'w')

for file in files:
    dict = {}

    for n, line in enumerate(bowtie_parser.read(open(file))):
        contig_id = line.seqid
        length = int(contig_id.split('_')[3])+33-1
        start = line.start
        read = line.read

        if dict.has_key(contig_id): 
            for index in range(start,int(start)+len(read)):
                dict[contig_id][1][index]=1
        
        else:
            count_mapped = [0]*length
            dict[contig_id]=[length]
            dict[contig_id].append(count_mapped)
    for key in dict.keys():
        mapped_bases = dict[key][1].count(1)
        dict[key][1] = mapped_bases
        mapped_percent = dict[key][1]/float(dict[key][0])
        dict[key].append(mapped_percent)

    group_index = file.find('group')
    group_id = int(file[(group_index+5):(group_index+8)])

    dict1[group_id]=dict.values()    
order = sorted(dict1.keys())

for group in order:
    
    fp.write(str(group) + ' ')
    contigs_list =  sorted(dict1[group], key=lambda x:x[0], reverse=True)
    
    for x in contigs_list:
        fp.write(str(x[2]) + ' ')
    fp.write('\n')
