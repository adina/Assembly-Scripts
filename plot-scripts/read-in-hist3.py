import csv
import sys, os.path
import matplotlib
from pylab import *

#Read in distribution data from text file
 
filein = open(sys.argv[1], 'rU')
reader = csv.reader(filein, delimiter=',', dialect='excel')


iteration = []
sequences_1 = []
sequences_75 = []
sequences_50 = []
sequences_25 = []
hashtable_1 = []
hashtable_75 = []
hashtable_50 = []
hashtable_25 = []

sequences_m1 = []
sequences_m75 = []
sequences_m50 = []
sequences_m25 = []
hashtable_m1 = []
hashtable_m75 = []
hashtable_m50 = []
hashtable_m25 = []


for row in reader:
    iteration.append(row[0])
    sequences_25.append(row[1])
    hashtable_25.append(row[2])
    sequences_50.append(row[3])
    hashtable_50.append(row[4])
    sequences_75.append(row[5])
    hashtable_75.append(row[6])
    sequences_1.append(row[7])
    hashtable_1.append(row[8])
    
    sequences_m25.append(row[9])
    hashtable_m25.append(row[10])
    sequences_m50.append(row[11])
    hashtable_m50.append(row[12])
    sequences_m75.append(row[13])
    hashtable_m75.append(row[14])
    sequences_m1.append(row[15])
    hashtable_m1.append(row[16])

figure(); hold(True)
subplot(2,1,1)
line1=plot(iteration, sequences_25, 'g+-', label='0.25 Gb')
line2=plot(iteration, sequences_50, 'r*-', label='0.50 Gb')
line3=plot(iteration, sequences_75, 'bd-', label='0.75 Gb')
line4=plot(iteration, sequences_1, 'kx-', label='1.0 Gb')

line11=plot(iteration, sequences_m25, 'g--')
line22=plot(iteration, sequences_m50, 'r--')
line33=plot(iteration, sequences_m75, 'b--')
line44=plot(iteration, sequences_m1, 'k--')
ylabel('Number of Reads Remaining')

legend()

subplot(2,1,2)
line5=plot(iteration, hashtable_25, 'g+-')
line6=plot(iteration, hashtable_50, 'r*-')
line7=plot(iteration, hashtable_75, 'bd-')
line8=plot(iteration, hashtable_1, 'kx-')

line55=plot(iteration, hashtable_m25, 'g--')
line66=plot(iteration, hashtable_m50, 'r--')
line77=plot(iteration, hashtable_m75, 'b--')
line88=plot(iteration, hashtable_m1, 'k--')

xlabel('K-mer Abudundance Filtering Iteration')
ylabel('Hashtable Occupancy')


#show()
savefig('kmer-abund-filter.pdf')

