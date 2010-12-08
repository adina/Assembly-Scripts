import csv
import sys, os.path
import matplotlib
from pylab import *

#Read in distribution data from text file

filein = open(sys.argv[1])
    
reader = csv.reader(filein, delimiter=' ')

id_33 = []
id_45 = []
id_33k = []
id_45k = []
reads_mapped_33 = []
reads_mapped_45 = []
reads_mapped_33k = []
reads_mapped_45k = []
total_reads_33 = [] 
total_reads_45 = [] 
total_reads_33k = [] 
total_reads_45k = [] 

for row in reader:
    if row[0].split('.')[1] == '033':
        id_33.append(row[0][:-3])
        reads_mapped_33.append(row[3])
        total_reads_33.append(row[1])
    elif row[0].split('.')[1] == '045':
        id_45.append(row[0][:-3])
        reads_mapped_45.append(row[3])
        total_reads_45.append(row[1])
    elif row[0].split('.')[1] == '133':
        id_33k.append(row[0][:-3])
        reads_mapped_33k.append(row[3])
        total_reads_33k.append(row[1])
    elif row[0].split('.')[1] == '145':
        id_45k.append(row[0][:-3])
        reads_mapped_45k.append(row[3])
        total_reads_45k.append(row[1])

plot(id_33, reads_mapped_33, 'ro', label='k33 % Reads mapped')
plot(id_33k, reads_mapped_33k, 'rx', label='k33filt % Reads mapped')
plot(id_45, reads_mapped_45, 'bo', label='k45 % Reads mapped')
plot(id_45k, reads_mapped_45k, 'bx', label='k45filt % Reads mapped')

#plot(id_33, total_reads_33, 'r--', label='k33 total reads')
#plot(id_45, total_reads_45, 'b--', label='k45 total reads')
#plot(id_33k, total_reads_33k, 'r--', label='k33filt total reads')
#plot(id_45k, total_reads_45k, 'b--', label='k45filt total reads')

#axis([0, 277, 0, 75000])


legend(loc='bottom right')

xlabel('Partition Group #')
ylabel('% Reads Mapped')
title('Iowa Corn')

savefig(sys.argv[2]+'.png')
#show()





#Plot graphs
'''
if __name__ == '__main__':
    file1 = open(sys.argv[1])
    file2 = open(sys.argv[2])
    file3 = open(sys.argv[3])
    file4 = open(sys.argv[4])
    
    x1, y1 = plot_dist(file1)
    x2, y2 = plot_dist(file2)
    x3, y3 = plot_dist(file3)
    x4, y4 = plot_dist(file4)
    
    
    line1 = plot(x1, y1, 'g+-', label=file1, linewidth=2)
    line2 = plot(x2, y2, 'r*-', label=file2, linewidth=1)
    line3 = plot(x3, y3, 'bd-', label=file3, linewidth=1)
    line4 = plot(x4, y4, 'kx-', label=file4, linewidth=1)
    
    axis([0,256, 0, 50000])
    xlabel('Abundance of k-mers, A')
    ylabel('Number of bins with A k-mers') 
    

    #Legend for simulated 10M dataset abundance distribution
    legend((line1, line2, line3, line4), ('4**7', '4**8', '4**9', '4**10'), loc=1)
    
    savefig('mem_hist.pdf')
'''
