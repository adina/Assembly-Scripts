import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import csv
import sys
from pylab import *

group_id = []
map_percent = {}

filein = open(sys.argv[1], 'r')
reader = csv.reader(filein, delimiter=' ')
for row in reader:
    group_id.append(int(row[0]))
    map_percent[int(row[0])]=row[1:-1]
for item in map_percent.keys():
    for index in range(0,len(map_percent[item])):
        map_percent[item][index]=float(map_percent[item][index])
for item in map_percent.keys():
    length_index = len(map_percent[item])
    if length_index < 100:
        print 'fill with zeroes up to 100'
        to_fill = 100-length_index
        print length_index, to_fill
        for counting_to_add in range(length_index, 101):
            map_percent[item].append(0)
print map_percent
        
sorted_keys =  sorted(map_percent.keys())
list_lengths = []

print 'check', sorted_keys
for key in map_percent.keys():
    list_lengths.append(len(map_percent[key]))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for z in sorted_keys:
    xs = range(0, 100)
    ys = map_percent[z][0:100]
    print z
    print xs, 'check', len(xs)
    print ys, 'check', len(ys)
    ax.bar(xs, ys, zs=z, zdir = 'y', color='r', alpha=0.8)


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()


