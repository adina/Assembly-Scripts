#! /usr/bin/env python

import sys
import screed
import bowtie_parser

#order = 1) 33 2)45filt 3) 45 4) 33filt
filenames = sys.argv[2:]
list_kmer = []
list = []
dict = {}
dict2 = {}
MAXLENGTH = 315+1
dict['33']=[0] * MAXLENGTH
dict['33k']=[0] * MAXLENGTH
dict['45']=[0] * MAXLENGTH
dict['45k']=[0] * MAXLENGTH
dict2['33']=[0] * MAXLENGTH
dict2['33k']=[0] * MAXLENGTH
dict2['45']=[0] * MAXLENGTH
dict2['45k']=[0] * MAXLENGTH
dict3={}

for file in filenames:

    print file

    index = file.find('group')
    group_id = int(file[(index+5):(index+8)])
    print group_id
    if file.find('kmer-filt') != -1:
        assem_id = file[index+5:].split('-kmer-filt-')[1][1:3] + 'k'
        fasta_file = '/mnt/prairie-fastas/fastas-filtered/iowa-prairie.group' + str(group_id) + '.fa-kmer-filt.fa'
        if fasta_file in list_kmer:
            dict2[assem_id][group_id]=dict3[str(group_id)+'k']
        
        else: 
            
            list_kmer.append(fasta_file)
            count_file = open(fasta_file, 'r')
            record_count = 0
            for record in screed.fasta.fasta_iter(count_file, parse_description=False):
                record_count += 1
            dict3[str(group_id)+'k']=record_count
        dict2[assem_id][group_id]=dict3[str(group_id)+'k']
    else:
        assem_id = file[index+5:].split('-')[1][1:3]
        print assem_id
        fasta_file = '/mnt/prairie-fastas/fastas/iowa-prairie.group' + str(group_id) + '.fa'
        if fasta_file in list:
            dict2[assem_id][group_id]=dict3[str(group_id)]
        
        else:
            list.append(fasta_file)
            count_file = open(fasta_file, 'r')
            record_count = 0
            for record in screed.fasta.fasta_iter(count_file, parse_description=False):
                record_count += 1
            dict3[str(group_id)]=record_count
        dict2[assem_id][group_id]=dict3[str(group_id)]
    
    #fp = open(file + '.mappedreads', 'w')
    for n, line in enumerate(bowtie_parser.read(open(file))):
    
        #read = line.readname
        #print >> fp, '%s' % read
        dict[assem_id][group_id]=n+1
    #fp.close()
print dict
#print dict2    

fp2 = open(sys.argv[1], 'w')

for i in range(0, int(MAXLENGTH)):
    fp2.write(str(i) + ' ')
    for keys in dict.keys():
        fp2.write(str(dict[keys][i])+ ' ')
    for keys in dict2.keys():
        fp2.write(str(dict2[keys][i])+ ' ')
    fp2.write('\n')
    
    

