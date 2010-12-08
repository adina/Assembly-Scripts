import csv
import sys, os.path
import matplotlib
from pylab import *

#Read in distribution data from text file

filein = open(sys.argv[1])
    
reader = csv.reader(filein, delimiter=' ')

id = []
id_k = []
partitions = []
unique = []
total_k = []
depth = []
breadth = []
partitions_k = []
unique_k = []
total_k_k = []
depth_k = []
breadth_k = []

for row in reader:
    if len(row[0].split('.')) == 2:
        id_k.append(row[0][:-2])
        partitions_k.append(row[1])
        unique_k.append(row[2])
        total_k_k.append(row[3])
        depth_k.append(row[4])
        breadth_k.append(row[5])
    if len(row[0].split('.')) == 1:
        id.append(row[0])    
        partitions.append(row[1])
        unique.append(row[2])
        total_k.append(row[3])
        depth.append(row[4])
        breadth.append(row[5])
print id_k
print id
print partitions

#plot(id, partitions, 'ro', label='Total Partitions')
#plot(id_k, partitions_k, 'rx', label='Total Partitions - kmer filt')
#plot(id, unique, 'bo', label='Unique Kmers')
#plot(id_k, unique_k, 'bx', label='Unique Kmers - kmer filt')
#plot(id, total_k, 'go', label='Total Kmers')
#plot(id_k, total_k_k, 'gx', label='Total Kmers - kmer filt')

#plot(id, breadth, 'ro', label='K-mer Breadth')
#plot(id_k, breadth_k, 'rx', label='Kmer Breadth - kmer filt')
plot(id, depth, 'bo', label='K-mer Depth')
plot(id_k, depth_k, 'bx', label='K-mer Depth - kmer filt')
#axis([0,277,0,1])
legend()

xlabel('Partition Group #')
ylabel('Count')
title('Iowa Corn')

savefig(sys.argv[2]+'.png')
show()





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
