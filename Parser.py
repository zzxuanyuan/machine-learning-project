#!/usr/bin/python

import sys

class Job:
	activity = ""
	timeAbs = 0
	name = ""
	state = ""
	site = ""
	toRetire = 0
	toDie = 0
	jobId = ""

	def __init__(self,activity,timeAbs,name,state,site,toRetire,toDie,jobId):
		self.activity = activity
		self.timeAbs = timeAbs
		self.name = name
		self.state = state
		self.site = site
		self.toRetire = toRetire
		self.toDie = toDie
		self.jobId = jobId

	
class SnapShot:
	timeStamp = ""
	jobList = []

	def __init__(self,timeStamp,jobList):
		self.timeStamp = timeStamp
		self.jobList = jobList

	
def itemParser(its):
	itemDict = {}
	startItem = its.index("[")
	endItem = its.rfind("]")
	substr = its[startItem+2:endItem]
	itemList = substr.split('; ')
	for i in range(len(itemList)):
		[key, value] = itemList[i].split(' = ')
		keyStrip = key.strip()
		itemDict[keyStrip] = value
	if "Activity" in itemDict:
		activity = itemDict["Activity"]
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
		state = itemDict["State"]
	else:
		state = ""

	if "GLIDEIN_Site" in itemDict:
		site = itemDict["GLIDEIN_Site"]
	else:
		site = ""

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
	item = Job(activity,timeAbs,name,state,site,toRetire,toDie,jobId)
	return item

def actParser(acts):
	itemList = []
	actList = acts.split(', ')
	for i in range(len(actList)):
		item = itemParser(actList[i])
		itemList.append(item)
	return itemList

def lineParser(line):
	startTime = line.index("#")
	endTime = line.rfind("#")
	time = line[startTime+2:endTime]
	body = line[endTime+1:]
	startList = body.index("[")
	endList = body.rfind("]")
	substr = body[startList+1:endList]
	actList = actParser(substr)
	timeStrip = time.strip()
	snapShot = SnapShot(timeStrip, actList)
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

	def readFile(self):
		with open(self.fileName, "r") as lines:
			for line in lines:
				snapShot = lineParser(line)
				self.snapShotList.append(snapShot)
		return self.snapShotList


parser = Parser(sys.argv[1])
with open(sys.argv[1], "r") as lines:
	for line in lines:
		snapShot = parser.readLine(line)
		for job in snapShot.jobList:
			print job.state,job.activity

#print parser.readFile()

'''
with open(sys.argv[1], "r") as lines:
	cnt = 0
	for line in lines:
		if cnt == 0:
			print parser.readLine(line)
		cnt = cnt + 1
'''
