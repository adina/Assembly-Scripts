import sys
import os
#kmer filt 31, kmer filt 45, 31, 45

fp = open(sys.argv[1], 'w')

if sys.argv[2] == 'total':
    PARSE_PHRASE = 'Total Trimmed Contigs'
elif sys.argv[2]== 'max':
    PARSE_PHRASE = 'Max contig size'
elif sys.argv[2] == 'N50':
    PARSE_PHRASE = 'N50 Length'
elif sys.argv[2] == 'length':
    PARSE_PHRASE = 'Total Length'

files = sys.argv[3:]

d = {}
for file in files:
    print file
    stats_info = open(file, 'r')
    group = file.split('.')[1]
    group = group[0:5] + ' ' + group[5:]
    print group
    stat_file = open(file, 'r')
    if os.stat(file)[6] == 0:
        print file, 'empty file'
        if d.has_key(group):
            d[group].append(0)
        else:
            d[group] = [0]
    else:
        for line in stats_info:
            if line.startswith(PARSE_PHRASE):
                if d.has_key(group):
                    d[group].append(int(line.rstrip().split()[-1]))
                else:
                    d[group]=[int(line.rstrip().split()[-1])]
print d

for x in range(0, len(d.keys())):

    fp.write('group '+str(x)+' ')
    for item in d['group ' + str(x)]:
        fp.write('%d ' % item)
    fp.write('\n')
