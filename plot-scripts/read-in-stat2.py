import csv
import sys, os.path
import matplotlib
from pylab import *

#Read in distribution data from text file

filein = open(sys.argv[1])
filein2 = open(sys.argv[2])    
reader = csv.reader(filein, delimiter=' ')
reader2 = csv.reader(filein2, delimiter=' ')

id = []
k31 = []
k45 = []
k31_nonpe = []
k45_nonpe = []

for row in reader:
    group = str(row[1])
    id.append(group)
    k31.append(row[4])
    k45.append(row[5])
    #k31_filt.append(row[2])
    #k45_filt.append(row[3])
for row in reader2:
    k31_nonpe.append(row[2])
    k45_nonpe.append(row[3])

#figure(); hold(True)
#plot(id, k45)
plot(id, k31, 'rx', label='k31')
plot(id, k45, 'gx', label='k45')
plot(id, k31_nonpe, 'm-', label='k31_nonpe')
plot(id, k45_nonpe, 'c-', label='k45_nonpe')
legend()
xlabel('Partition Group #')
ylabel('Length, bp')
top_y = int(sys.argv[4])
axis([0,251,0,top_y])
title(sys.argv[1])

savefig(sys.argv[3]+'.png')
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
