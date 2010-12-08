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
    group_id.append(row[0])
    map_percent[row[0]]=row[1:-1]
    
print map_percent

list_lengths = []

for key in map_percent.keys():
    list_lengths.append(len(map_percent[key]))

print max(list_lengths)

'''
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
for z in group_id:
    xs = np.arange(20)
    ys = np.random.rand(20)

    # You can provide either a single color or an array. To demonstrate this,
    # the first bar of each set will be colored cyan.
    #cs = [c] * len(xs)
    #cs[0] = 'c'
    ax.bar(xs, ys, zs=z, zdir='y', color='r', alpha=0.8)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
'''
'''
fig = plt.figure()
ax =fig.add_subplot(111, projection='3d')
for z in range(100,315):
    xs=range(0,100)
    ys=range(0,100)

plt.show()
'''
