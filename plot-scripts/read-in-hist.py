import csv
import sys, os.path
import matplotlib
from pylab import *

#Read in distribution data from text file

def plot_dist(filein):
    
    reader = csv.reader(filein, delimiter=' ')
    kmer_abundance = []
    count = []

    for row in reader:
        kmer_abundance.append(int(row[0]))
        count.append(int(row[1]))

    return(kmer_abundance, count)

#Plot graphs

if __name__ == '__main__':
    file1 = open(sys.argv[1])
    file2= open(sys.argv[2])
    x1, y1 = plot_dist(file1)
    x2, y2 = plot_dist(file2)
    
    line1 = plot(x1, y1, 'g+-', label=file1, linewidth=2)
    line2 = plot(x2, y2, 'r*-', label=file2, linewidth=1)
    
    axis([0,30, 0, .2e9])
    xlabel('Abundance of k-mers, A')
    ylabel('Number of bins with A k-mers') 
    

    #Legend for simulated 10M dataset abundance distribution
    legend((line1, line2), ('Everything in big lump', 'Just kmers used for k45 assembly'), loc=1)
    
    show()
