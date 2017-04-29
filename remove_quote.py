# This file cleans quote symbols and extra whitespaces

import sys
import csv

with open(sys.argv[1], 'rt') as fr:
	with open(sys.argv[2], 'w') as fw:
		title = ['JobId' , 'Duration' , 'MaxRetireTime' , 'MaxKillTime' , 'DesktopTimeMeanHour' , 'DesktopTimeMeanMinute' , 'DesktopTimeEndHour' , 'DesktopTimeEndMinute' , 'HostName' , 'SiteName' , 'ResourceName' , 'EntryName' , 'JobEndTime' , 'JobRetireTime' , 'JobDieTime' , 'PreemptionFrequency' , 'Class']
		csv.writer(fw).writerow(title)
		for row in csv.reader(fr):
			row = [col.strip() for col in row]
			row = [col.strip('"') for col in row]
			csv.writer(fw).writerow(row)
fr.close()
fw.close()
