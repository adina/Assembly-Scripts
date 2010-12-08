import csv
import sys, os.path
import matplotlib
from pylab import *

def getPercentage(maps, total):
    percentages = []
    for x in range(0, len(maps)):
        if total[x] == 0:
            percentages.append(0)

        else:
            percentages.append(maps[x]/total[x])
    return percentages

#Read in distribution data from text file

if __name__=='__main__':

    filein = open(sys.argv[1], 'r')
    
    reader = csv.reader(filein, delimiter=' ')

    id = []
    map33 = []
    map45 = []
    mapk33 = []
    mapk45 = []
    total33 = []
    total45 = []
    totalk33 = []
    totalk45 = []
    
    for row in reader:
    
        id.append(str(row[0]))
        map33.append(int(row[1]))
        map45.append(int(row[3]))
        mapk33.append(int(row[4]))
        mapk45.append(int(row[2]))
        total33.append(float(row[5]))
        total45.append(float(row[7]))
        totalk33.append(float(row[8]))
        totalk45.append(float(row[6]))
    
    k33 = getPercentage(map33, total33)
    k45 = getPercentage(map45, total45)
    k33_filt = getPercentage(mapk33, totalk33)
    k45_filt = getPercentage(mapk45, totalk45)

    plot(id, k33, 'ro', label='k33')
    plot(id, k45, 'gs', label='k45')
    plot(id, k33_filt, 'bo', label='k33_filt')
    plot(id, k45_filt, 'cs', label='k45_filt')
    legend()
    xlabel('Partition Group #')
    ylabel('Total % mapped')
    axis([100, 277, 0, 1])


    title('Iowa Corn partitioned reads mapped to contigs >1000 bp')

    savefig(sys.argv[2]+'.png')
    #show()



