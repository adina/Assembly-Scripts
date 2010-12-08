import csv
import sys, os.path
import matplotlib
#matplotlib.use('Cairo')
from pylab import plot, savefig, hist, axis, legend, xlabel, ylabel, title

def plot_dist(filein):
    
    reader = csv.reader(filein, delimiter=' ')
    xdata = []
    ydata = []
    list = []

    for row in reader:
        xdata.append(int(row[0]))
        ydata.append(int(row[1]))

    return(xdata, ydata)

if __name__ == '__main__':
    file1 = open(sys.argv[1])
   

    x1, y1 = plot_dist(file1)
   
    
    line1 = plot(x1, y1, 'go-', label=file1, linewidth=2)
   
    axis([0,256, 0, 1000])
    xlabel('Abundance of 25-mers')
    ylabel('Count') 
    title('Distribution of 25-mer abundance')
    
    savefig('hist1.png')
#for bar histogram
'''
for row in reader:
    value = int(row[0])
    count = int(row[1])
    value_list = [value] * count
    for item in value_list:
        list.append(item)
#print list
hist(list, n_bins, cumulative=False, normed=False, alpha=0.8)
filename = os.path.basename(sys.argv[1])
savefig(filename + '.png')
'''
