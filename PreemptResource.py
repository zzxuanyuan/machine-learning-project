# Author: Zhe Zhang <zhan0915@huskers.unl.edu>

# This file generates figures of Total Jobs vs. Preempted Jobs on different grid resources.
# Input: @ARGV[1]: The csv file that contains preempted information such as days.csv(It uses day01, days02,... to separate different days' data.
#        @ARGV[2]: The csv file that contains total jobs info on different resources such as resource.csv(Add day01, day02,... to separate different days' data.

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure, show
import statsmodels.api as sm
import statsmodels.formula.api as smf

resourceList = ['MWT2','IIT_CE1','Hyak','AGLT2','UCR-HEP','CancerComputer_Miron_CE','SWT2_CPB','GLOW','UColorado_HEP','SU-OG-CE','SU-OG-CE1','CIT_CMS_T2','NWICG_NDCMS','cinvestav','HOSTED_STANFORD','UTA_SWT2','Purdue-Hadoop','UCSDT2','SPRACE','Crane','IIT_CE2','BNL-ATLAS','USCMS-FNAL-WC1','Sandhills','Clemson-Palmetto','FIU_HPCOSG_CE','UConn-OSG','SMU_ManeFrame_CE','IIT_CE','FLTECH','Comet','GridUNESP_CENTRAL','Tusker','Nebraska','OSG_US_OSU_COWBOY','GPGrid','MIT_CMS']

lineSkipList = list()
lineLengthList = list()

totalLine = 0
with open(sys.argv[1], 'r') as fr:
	skip = 0
	length = 0
	cnt = 0
	for line in fr:
		cnt += 1
		totalLine += 1
		if line[0:3] == 'day':
			if line[0:5] == 'day01':
				skip = cnt
				lineSkipList.append(skip)
			else:
				lineLengthList.append(cnt-skip-1)
				skip = cnt
				lineSkipList.append(skip)

lineLengthList.append(totalLine-lineSkipList[-1])

print lineSkipList
print lineLengthList
print totalLine

resourceDict = dict()
for resource in resourceList:
	resourceDict[resource] = list()

for i in range(0,len(lineSkipList)):
	df = pd.read_csv('days.csv', names=['JobId' , 'Duration' , 'MaxRetireTime' , 'MaxKillTime' , 'DesktopTimeMeanHour' , 'DesktopTimeMeanMinute' , 'DesktopTimeEndHour' , 'DesktopTimeEndMinute' , 'HostName' , 'SiteName' , 'ResourceName' , 'EntryName' , 'JobEndTime' , 'JobRetireTime' , 'JobDieTime' , 'PreemptionFrequency' , 'Class'], skiprows=lineSkipList[i], nrows=lineLengthList[i])
	jobs = df[df['Class'].isin(['LightPreempted','HeavyPreempted','Weired'])]
	for resource in resourceList:
		listCur = [0] * 1440
		r = jobs[jobs['ResourceName']==resource]
		d = r['DesktopTimeEndMinute'].value_counts()
		print d
		for index in d.index:
			listCur[index] = d[index]
		resourceDict[resource].extend(listCur)
'''
fig = plt.figure(1)

for resource in resourceList:
	plt.scatter(range(0,len(resourceDict[resource])),resourceDict[resource],label=resource)

plt.title('Distribution of Preemption Probability')
ax = plt.gca()
ax.set_xlabel("Time")
ax.set_ylabel("Number of Jobs")
ax.set_xlim(xmin=0)
ax.set_ylim(ymin=0)
#bx.set_xticks([1,2,3,4,5,6,7,8,9,10])
#bx.set_xticklabels(['1', '8', '16', '32', '64', '128', '256', '512', '1024'])
plt.grid()
#plt.legend(loc='upper right')
#plt.show()
'''
resourceSkipList = list()
resourceLengthList = list()

resourceLine = 0
with open(sys.argv[2], 'r') as fr:
	skip = 0
	length = 0
	cnt = 0
	for line in fr:
		cnt += 1
		resourceLine += 1
		if line[0:3] == 'day':
			if line[0:5] == 'day01':
				skip = cnt
				resourceSkipList.append(skip)
			else:
				resourceLengthList.append(cnt-skip-1)
				skip = cnt
				resourceSkipList.append(skip)

resourceLengthList.append(resourceLine-resourceSkipList[-1])

print resourceSkipList
print resourceLengthList
print resourceLine

resnewDict = dict()
for resource in resourceList:
	resnewDict[resource] = list()

for i in range(0,len(resourceSkipList)):
	df = pd.read_csv('resource.csv', names=['DesktopTime','Hour','Minute','TotalJob','MWT2','IIT_CE1','Hyak','AGLT2','UCR-HEP','CancerComputer_Miron_CE','SWT2_CPB','GLOW','UColorado_HEP','SU-OG-CE','SU-OG-CE1','CIT_CMS_T2','NWICG_NDCMS','cinvestav','HOSTED_STANFORD','UTA_SWT2','Purdue-Hadoop','UCSDT2','SPRACE','Crane','IIT_CE2','BNL-ATLAS','USCMS-FNAL-WC1','Sandhills','Clemson-Palmetto','FIU_HPCOSG_CE','UConn-OSG','SMU_ManeFrame_CE','IIT_CE','FLTECH','Comet','GridUNESP_CENTRAL','Tusker','Nebraska','OSG_US_OSU_COWBOY','GPGrid','MIT_CMS'], skiprows=resourceSkipList[i], nrows=resourceLengthList[i])
	print df['Minute'].values
	print "value = ", df[df['Minute']==1312][resource].values
	
	for resource in resourceList:
		listCur = [0] * 1440
#		print resource
		for index in df['Minute'].values:
#			print index
			listCur[index] = df[df['Minute']==index][resource].values[0]
		
#		print type(listCur)
		for index in range(1,1440):
#			print index,listCur[index]
			if listCur[index] == 0:
				listCur[index] = listCur[index-1]
		resnewDict[resource].extend(listCur)
		
#fig = plt.figure(2)
'''
for resource in resourceList:
	plt.scatter(range(0,len(resnewDict[resource])),resnewDict[resource],label=resource)

plt.title('Number of Jobs on Different Resource')
ax = plt.gca()
ax.set_xlabel("Time")
ax.set_ylabel("Number of Jobs")
ax.set_xlim(xmin=0)
ax.set_ylim(ymin=0)
#bx.set_xticks([1,2,3,4,5,6,7,8,9,10])
#bx.set_xticklabels(['1', '8', '16', '32', '64', '128', '256', '512', '1024'])
plt.grid()
plt.legend(loc='upper right')
plt.show()
'''

for resource in resourceList:
	fig = figure()
	fname = resource + ".png"
	plt.plot(range(0,len(resnewDict[resource])),resnewDict[resource],label='Total Jobs')
	plt.plot(range(0,len(resourceDict[resource])),resourceDict[resource],label='Preemptions')
	ftitle = "Preemptions on " + resource
	plt.title(ftitle)
	ax = plt.gca()
	ax.set_xlabel("Time")
	ax.set_ylabel("Number of Instances")
	ax.set_xlim(xmin=0)
	ax.set_ylim(ymin=0)
	plt.grid()
	plt.legend(loc='upper right')
	fig.savefig(fname)
	fig.clear()
