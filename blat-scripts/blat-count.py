import sys
import blat_parser

CUTOFF = 500
K=45
#JGI -- add 60 for full length
file = sys.argv[1]
dict={}
frat_count = 0
sap_count = 0
threshold_count =0
for n, line in enumerate(blat_parser.read(open(file))):
    contig = line.query
    contig_length=int(contig.split('_')[3])+45-1
    #print contig, contig_length
    hit = line.subject
    hit_length = int(hit.split('_')[4])+60
    start = line.sub_start
    end = line.sub_end
    if contig_length > CUTOFF:
        threshold_count += 1
        if hit.startswith('Frat'):
            frat_count += 1
        if hit.startswith('Sapro'):
            sap_count += 1
        length = line.length
        if dict.has_key(hit):
            dict[hit].append([start, end])
        else:
            dict[hit]=[[start, end]]
#print frat_count
#print sap_count
#print dict

dict2={}
for key in dict.keys():
    set1=set()
    for item in range(0, len(dict[key])):
        
        to_add = range(int(dict[key][item][0]), int(dict[key][item][1]))
        for item2 in to_add:
            set1.add(item2)
    dict2[key]= len(set1)

dict3={}
sorted_list = sorted(dict2.items(), key=lambda x:x[1], reverse=True)
for item3 in sorted_list:
    #print item3[0], item3[1]
    dict3[item3[0]] = int(item3[1])/float((int(item3[0].split('_')[4])+60))

sorted_list2=sorted(dict3.items(), key=lambda x:x[1], reverse=True)
for item4 in sorted_list2:
    print item4[0], item4[1]

print frat_count
print sap_count
print threshold_count
print n


