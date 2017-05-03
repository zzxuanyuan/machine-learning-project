# This file reads csv files reversely and change the first occurance of a preempted job to Preempted
# In addition, this file also records the preempted counts for each job.

import sys
import csv

preemptDict = dict()
preemptOrder = dict()

lines = list()

def preemptAdd(dic, key):
	if key not in dic:
		dic[key] = 1
	else:
		dic[key] += 1
	return dic

with open(sys.argv[1], 'r') as fr:
	for row in reversed(list(csv.reader(fr))):
		row = [col.strip() for col in row]
		row = [col.strip('"') for col in row]
		if(row[-1] == 'LightPreempted'):
			for i in range(0, int(row[-2])):
				preemptDict = preemptAdd(preemptDict, row[0])
				lines.append(row)
		elif(row[-1] == 'HeavyPreempted'):
			preemptDict = preemptAdd(preemptDict, row[0])
			lines.append(row)
		else:
			if row[0] in preemptDict:
				row[-1] = 'HeavyPreempted'
				preemptDict = preemptAdd(preemptDict, row[0])
				lines.append(row)
			else:
				lines.append(row)

with open(sys.argv[2], 'w') as fw:
	title = ['JobId' , 'Duration' , 'MaxRetireTime' , 'MaxKillTime' , 'DesktopTimeMeanHour' , 'DesktopTimeMeanMinute' , 'DesktopTimeEndHour' , 'DesktopTimeEndMinute' , 'HostName' , 'SiteName' , 'ResourceName' , 'EntryName' , 'JobEndTime' , 'JobRetireTime' , 'JobDieTime' , 'PreemptionFrequency' , 'Class']
	csv.writer(fw).writerow(title)
	for row in reversed(lines):
		if (row[0] in preemptDict):
			if (row[-1] == 'LightPreempted') or (row[-1] == 'HeavyPreempted'):
				preemptOrder = preemptAdd(preemptOrder, row[0])
				preemptDict[row[0]] = preemptDict[row[0]] - 1
				row[-2] = str(preemptOrder[row[0]]-1)
		csv.writer(fw).writerow(row)

for key in preemptDict:
	print preemptOrder[key],preemptDict[key]
fr.close()
fw.close()
