# This file merges LightPreempted, HeavyPreempted and Weird(A job id only occurs once but the last job activity was Busy)
# into Preempted. The output file will be used for classification

import sys
import csv

preemptDict = dict()

lines = list()

with open(sys.argv[1], 'r') as fr:
	for row in csv.reader(fr):
		if(row[-1] == 'LightPreempted'):
			row[-1] = 'Preempted'
			if row[0] not in preemptDict:
				preemptDict[row[0]] = 0
				row[-2] = preemptDict[row[0]]
			else:
				preemptDict[row[0]] += 1
				row[-2] = preemptDict[row[0]]
		elif(row[-1] == 'HeavyPreempted'):
			row[-1] = 'Preempted'
			if row[0] not in preemptDict:
				preemptDict[row[0]] = 0
				row[-2] = preemptDict[row[0]]
			else:
				preemptDict[row[0]] += 1
				row[-2] = preemptDict[row[0]]
		elif(row[-1] == 'Weird'):
			row[-1] = 'Preempted'
		lines.append(row)

with open(sys.argv[2], 'w') as fw:
	for row in lines:
		csv.writer(fw).writerow(row)

fr.close()
fw.close()
