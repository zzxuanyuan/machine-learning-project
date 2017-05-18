# This file merges CleanUp to Succeeded; Stupid, NeedIdentify and Unkown together to a single class type called Other

import sys
import csv

lines = list()

with open(sys.argv[1], 'r') as fr:
	for row in csv.reader(fr):
		if(row[-1] == 'CleanUp'):
			row[-1] = 'Succeeded'
		elif(row[-1] == 'Stupid'):
			row[-1] = 'Other'
		elif(row[-1] == 'NeedIdentify'):
			row[-1] = 'Other'
		elif(row[-1] == 'Unknown'):
			row[-1] = 'Other'
		elif(row[-1] == 'NetworkIssue'):
			row[-1] = 'Other'
		elif(row[-1] == 'Benchmarking'):
			row[-1] = 'Other'
		lines.append(row)

with open(sys.argv[2], 'w') as fw:
	for row in lines:
		csv.writer(fw).writerow(row)

fr.close()
fw.close()
