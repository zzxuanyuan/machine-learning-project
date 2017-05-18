# This file does regression test using Random Forest Regression.
# The input file should be insert_total_jobs.csv that contains total jobs info.

import math
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, show
import pickle

df = pd.read_csv('test.out')
print df.shape
df = df[df['Class']=='Preempted']
print df.shape
jobHistDict = dict()

distanceList = list()

for index, row in df.iterrows():

	if row['JobId'] not in jobHistDict.keys():
		jobHistDict[row['JobId']] = (row['Day']-1)*1440 + row['DesktopTimeEndMinute']
	else:
		distanceList.append((row['Day']-1)*1440 + row['DesktopTimeEndMinute'] - jobHistDict[row['JobId']])
		jobHistDict[row['JobId']] = (row['Day']-1)*1440 + row['DesktopTimeEndMinute']

print jobHistDict
print distanceList

with open('outfile', 'wb') as fp:
	pickle.dump(distanceList, fp)

fig = figure()

heights,bins = np.histogram(distanceList,bins=range(0,14*1800+1,1800))
heights = heights**1.0/sum(heights)
plt.bar(bins[:-1],heights,width=(max(bins) - min(bins))/len(bins), color="blue", alpha=0.5)

ax = plt.gca()
#ax.set_xlim(xmin=0)
#ax.set_ylim(0,1.0)
#ax.set_xticklabels([])
#ax.set_ylabel('')
#ax.set_yscale('log')
ax.set_xticks(range(0,7*3600+1,3600))
ax.set_xticklabels(['0','1','2','3','4','5','6','7'])
ax.set_xlabel('Time Distance between Job Preemptions (Hours)')
ax.set_ylabel('Probability')
plt.legend(loc='upper right')
plt.title('Probability Mass Function (0~7 Hours)')
fig.savefig("preemptiontimedistance.png")
plt.show()
