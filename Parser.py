# Author: Zhe Zhang <zhan0915@huskers.unl.edu>

# This file is to parse job snapshots from OSG to Job object that contains meta info for a job at this particular snapshot.
# This file is imported to JobLifeCycle.py to generate life cycles for jobs.

#!/usr/bin/python

import sys
import operator

class Job:
#	activity = ""
#	timeAbs = 0
#	name = ""
#	state = ""
#	site = ""
#	toRetire = 0
#	toDie = 0
#	jobId = ""

	def __init__(self,desktopTime,activity,timeAbs,name,state,site,resource,entry,daemonStart,toRetire,toDie,jobId):
		self.desktopTime = desktopTime
		self.activityDict = {"Idle":0,"Benchmarking":0,"Busy":0,"Suspended":0,"Retiring":0,"Vacating":0,"Killing":0}
		self.stateDict = {"Owner":0,"Unclaimed":0,"Matched":0,"Claimed":0,"Preempting":0,"Backfill":0,"Drained":0}
		self.activity = "NONE"
		self.state = "NONE"
		self.activityDict[activity] = 1
		self.stateDict[state] = 1
		self.timeAbs = timeAbs
		self.name = set([name])
		self.host = set([extractHost(name)])
		self.site = site
		self.resource = resource
		self.entry = entry
		self.daemonStart = int(daemonStart)
		self.toRetire = toRetire
		self.toDie = toDie
		self.jobId = jobId
		self.cycle = 1

	def merge(self,timeAbs,activity,state,name):
		self.timeAbs = min(self.timeAbs,timeAbs)
		self.activityDict[activity] += 1
		self.stateDict[state] += 1
		self.name.add(name)
		self.host.add(extractHost(name))
		

class Act:
#	activity = ""
#	timeAbs = 0
#	name = ""
#	state = ""
#	site = ""
#	toRetire = 0
#	toDie = 0
#	jobId = ""

	def __init__(self,activity,timeAbs,name,state,site,resource,entry,daemonStart,jobStart,toRetire,toDie,jobId):
		self.activity = activity
		self.timeAbs = timeAbs
		self.name = name
		self.state = state
		self.site = site
		self.resource = resource
		self.entry = entry
		self.daemonStart = daemonStart
		self.jobStart = jobStart
		self.toRetire = toRetire
		self.toDie = toDie
		self.jobId = jobId

class SnapShot:
#	timeStamp = ""
#	jobDict = {}

	def __init__(self,timeStamp,jobDict):
		self.timeStamp = timeStamp
		self.jobDict = {}
		self.jobDict = jobDict
		self.jobNum = len(jobDict)

def extractHost(name):
	atSplitList = name.split('@')
	hostName = atSplitList[-1].strip()
	return hostName

def itemParser(its):
	itemDict = {}
	startItem = its.index("[")
	endItem = its.rfind("]")
	substr = its[startItem+2:endItem]
	itemList = substr.split('; ')
	for i in range(len(itemList)):
		[key, value] = itemList[i].split(' = ')
		keyStrip = key.strip()
		itemDict[keyStrip] = value.strip()
	if "Activity" in itemDict:
		activity = itemDict["Activity"].strip("\"")
	else:
		activity = ""

	if "MyCurrentTime" in itemDict:
		timeAbs = int(itemDict["MyCurrentTime"].strip())
	else:
		timeAbs = 0

	if "Name" in itemDict:
		name = itemDict["Name"].strip("\"")
	else:
		name = ""

	if "State" in itemDict:
		state = itemDict["State"].strip("\"")
	else:
		state = ""

	if "GLIDEIN_Site" in itemDict:
		site = itemDict["GLIDEIN_Site"].strip("\"")
	else:
		site = ""

	if "GLIDEIN_ResourceName" in itemDict:
		resource = itemDict["GLIDEIN_ResourceName"].strip("\"")
	else:
		resource = ""

	if "GLIDEIN_Entry_Name" in itemDict:
		entry = itemDict["GLIDEIN_Entry_Name"].strip("\"")
	else:
		entry = ""

	if "DaemonStartTime" in itemDict:
		daemonStart = int(itemDict["DaemonStartTime"].strip())
	else:
		daemonStart = 0

	if "JobStart" in itemDict:
		jobStart = itemDict["JobStart"]
	else:
		jobStart = ""

	if "GLIDEIN_ToRetire" in itemDict:
		toRetire = int(itemDict["GLIDEIN_ToRetire"].strip())
	else:
		toRetire = 0

	if "GLIDEIN_ToDie" in itemDict:
		toDie = int(itemDict["GLIDEIN_ToDie"].strip())
	else:
		toDie = 0

	if "GLIDEIN_SITEWMS_JobId" in itemDict:
		jobId = itemDict["GLIDEIN_SITEWMS_JobId"].strip("\"")
	else:
		jobId = ""
	item = Act(activity,timeAbs,name,state,site,resource,entry,daemonStart,jobStart,toRetire,toDie,jobId)
	return item

def actParser(desktopTime, acts):
	itemDict = {}
	actList = acts.split(', ')
	for i in range(len(actList)):
		item = itemParser(actList[i])
		if item.jobId in itemDict:
			itemDict[item.jobId].merge(item.timeAbs,item.activity,item.state,item.name)
		else:
			job = Job(desktopTime,item.activity,item.timeAbs,item.name,item.state,item.site,item.resource,item.entry,item.daemonStart,item.toRetire,item.toDie,item.jobId)
			itemDict[item.jobId] = job
	for item in itemDict:
		itemDict[item].activity = max(itemDict[item].activityDict.iteritems(), key=operator.itemgetter(1))[0]
		itemDict[item].state =  max(itemDict[item].stateDict.iteritems(), key=operator.itemgetter(1))[0]
#		print item,itemDict[item].activity,itemDict[item].state
#		print item,itemDict[item].activityDict,itemDict[item].stateDict
	return itemDict

def lineParser(line):
	startTime = line.index("#")
	endTime = line.rfind("#")
	time = line[startTime+2:endTime]
	body = line[endTime+1:]
	startList = body.index("[")
	endList = body.rfind("]")
	substr = body[startList+1:endList]
	timeStrip = time.strip()
#	print "timeStrip: ",timeStrip
	actDict = actParser(timeStrip, substr)
	snapShot = SnapShot(timeStrip, actDict)
	return snapShot

class Parser:
	fileName = ""
	lineNumber = 0
	snapShotList = []

	def __init__(self,fileName):
		self.fileName = fileName

	def readLine(self,line):
		snapShot = lineParser(line)
		return snapShot

	def extractJobList(self,line):
		snapShot = lineParser(line)
		jobDict = snapShot.jobDict
		return jobDict.keys()

	def readFile(self):
		with open(self.fileName, "r") as lines:
			for line in lines:
				snapShot = lineParser(line)
				self.snapShotList.append(snapShot)
		return self.snapShotList

'''
parser = Parser(sys.argv[1])
with open(sys.argv[1], "r") as lines:
	for line in lines:
		snapShot = parser.readLine(line)
		for job in snapShot.jobDict:
			print "jobId: %s , value: " % (job)

#print parser.readFile()

with open(sys.argv[1], "r") as lines:
	cnt = 0
	for line in lines:
		if cnt == 0:
			print parser.readLine(line)
		cnt = cnt + 1
'''
