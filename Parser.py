# Author: Zhe Zhang <zhan0915@huskers.unl.edu>

# This file is to parse job snapshots from OSG to Job object that contains meta info for a job at this particular snapshot.
# This file is imported to JobLifeCycle.py to generate life cycles for jobs.

#!/usr/bin/python

import sys

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
		self.activity = activity
		self.timeAbs = timeAbs
		self.name = name
		self.host = "\"" + extractHost(name)
		self.state = state
		self.site = site
		self.resource = resource
		self.entry = entry
		self.daemonStart = daemonStart
		self.toRetire = toRetire
		self.toDie = toDie
		self.jobId = jobId
		self.cycle = 1

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
		timeAbs = itemDict["MyCurrentTime"]
	else:
		timeAbs = 0

	if "Name" in itemDict:
		name = itemDict["Name"]
	else:
		name = ""

	if "State" in itemDict:
		state = itemDict["State"].strip("\"")
	else:
		state = ""

	if "GLIDEIN_Site" in itemDict:
		site = itemDict["GLIDEIN_Site"]
	else:
		site = ""

	if "GLIDEIN_ResourceName" in itemDict:
		resource = itemDict["GLIDEIN_ResourceName"]
	else:
		resource = ""

	if "GLIDEIN_Entry_Name" in itemDict:
		entry = itemDict["GLIDEIN_Entry_Name"]
	else:
		entry = ""

	if "DaemonStartTime" in itemDict:
		daemonStart = itemDict["DaemonStartTime"]
	else:
		daemonStart = ""

	if "JobStart" in itemDict:
		jobStart = itemDict["JobStart"]
	else:
		jobStart = ""

	if "GLIDEIN_ToRetire" in itemDict:
		toRetire = itemDict["GLIDEIN_ToRetire"]
	else:
		toRetire = 0

	if "GLIDEIN_ToDie" in itemDict:
		toDie = itemDict["GLIDEIN_ToDie"]
	else:
		toDie = 0

	if "GLIDEIN_SITEWMS_JobId" in itemDict:
		jobId = itemDict["GLIDEIN_SITEWMS_JobId"]
	else:
		jobId = ""
	item = Act(activity,timeAbs,name,state,site,resource,entry,daemonStart,jobStart,toRetire,toDie,jobId)
	return item

def actParser(desktopTime, acts):
	itemDict = {}
	actList = acts.split(', ')
	for i in range(len(actList)):
		item = itemParser(actList[i])
		job = Job(desktopTime,item.activity,item.timeAbs,item.name,item.state,item.site,item.resource,item.entry,item.daemonStart,item.toRetire,item.toDie,item.jobId)
		itemDict[item.jobId] = job
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
	actDict = actParser(timeStrip, substr)
	snapShot = SnapShot(timeStrip, actDict)
	return snapShot

class Parser:
	fileName = ""
	lineNumber = 0
	snapShotList = []

	def __init__(self,fileName):
		self.fileName = fileName
		with open(self.fileName, "r") as lines:
			for line in lines:
				self.lineNumber = self.lineNumber + 1

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
