# Author: Zhe Zhang <zhan0915@huskers.unl.edu>

# This file is to collect job info from each snapshot and interpret the life cycles for each job.
# This file loads Parser.py to generate life cycles for jobs.
# This file also classify jobs into five categories: Succeeded, CleanUp, Retired, Killed, LightPreempted, HeavyPreempted.(Further analysis needs to be done including combining CleanUp and Succeeded and Combining LightPreempted and HeavyPreempted. More importantly, we need to characterize network problem that is determined as a pilot job reappears after some cycles of absence but the job start time does not change over this period).

#!/usr/bin/python

import sys
from datetime import datetime
import operator
import Parser

print "this is joblifecycle"
global jobFreqHistoryDict
global jobTimeHistoryDict
jobFreqHistoryDict = {}
jobTimeHistoryDict = {}

#preJobSet = []
#curJobSet = []
#preJobLifeCycleDict = {}
#curJobLifeCycleDict = {}
#preSnapShot = Parser.SnapShot("", {})
#curSnapShot = Parser.SnapShot("", {})

class JobFormat:

	def __init__(self, job):
		self.duration = int(job.endTime) - int(job.startTime)
		self.retireRuntime = int(job.toRetire) - int(job.startTime)
		self.killRuntime = int(job.toDie) - int(job.startTime)
		self.desktopTimeInfo = getDesktopTimeInfo(job.desktopStart, job.desktopEnd)
		self.host = job.host
		self.site = job.site
		self.resource = job.resource
		self.entry = job.entry
		self.endTime = job.endTime
		self.toRetire = job.toRetire
		self.toDie = job.toDie
		self.jobId = job.jobId
		self.daemonStartSet = job.daemonStartSet
		self.activityDict = job.activityDict
		self.stateDict = job.stateDict
		self.preemptedFreq = job.preemptedFreq
		self.lastActivity = job.pairActStateList[-1][1]
		self.label = ""

class JobLifeCycle:
#	startTime = 0
#	endTime = 0
#	name = ""
#	site = ""
#       toRetire = 0
#	toDie = 0
#	jobId = ""
#	pairActStateList = []

	def __init__(self, job):
		self.startTime = job.daemonStart
		self.endTime = 0
		self.desktopStart = job.desktopTime
		self.desktopEnd = ""
		self.name = job.name
		self.host = job.host
		self.site = job.site
		self.resource = job.resource
		self.entry = job.entry
		self.toRetire = job.toRetire
		self.toDie = job.toDie
		self.jobId = job.jobId
		self.daemonStartSet = set()
		self.daemonStartSet.add(job.daemonStart)
		self.activityDict = {"Idle":0,"Benchmarking":0,"Busy":0,"Suspended":0,"Retiring":0,"Vacating":0,"Killing":0}
		self.stateDict = {"Owner":0,"Unclaimed":0,"Matched":0,"Claimed":0,"Preempting":0,"Backfill":0,"Drained":0}
		self.activityDict[job.activity] = 1
		self.stateDict[job.state] = 1
		self.preemptedFreq = 0
		self.pairActStateList = []
		self.cycle = job.cycle
		tup = (job.timeAbs, job.activity, job.state)
		self.pairActStateList.append(tup)

	def stop(self, endTime, desktopEnd):
		self.endTime = endTime
		self.desktopEnd = desktopEnd

	def stay(self, curTime, daemonStart, activity, state):
		self.cycle = self.cycle + 1
		self.activityDict[activity] += 1
		self.stateDict[state] += 1
		self.daemonStartSet.add(daemonStart)
		tup = (curTime, activity, state)
		self.pairActStateList.append(tup)

	def change(self, curTime, daemonStart, activity, state):
		tup = (curTime, activity, state)
		self.pairActStateList.append(tup)
	
def getDesktopTimeInfo(deskStart, deskEnd):
	startTimeList = deskStart.split(".")
	endTimeList = deskEnd.split(".")
	timeStart = startTimeList[0]
	timeEnd = endTimeList[0]
	timeStartList = timeStart.split(" ")
	timeEndList = timeEnd.split(" ")
	dateStart = timeStartList[0]
	dateEnd = timeEndList[0]
	clockStart = timeStartList[1]
	clockEnd = timeEndList[1]
	dateStartList = dateStart.split("-")
	dateEndList = dateEnd.split("-")
	dateRepStart = dateStartList[1] + "/" + dateStartList[2] + "/" + dateStartList[0][2:]
	dateRepEnd = dateEndList[1] + "/" + dateEndList[2] + "/" + dateEndList[0][2:]
	startTime = datetime.strptime(dateRepStart + " " + clockStart, "%m/%d/%y %H:%M:%S")
	endTime = datetime.strptime(dateRepEnd + " " + clockEnd, "%m/%d/%y %H:%M:%S")
	meanTime = startTime+(endTime-startTime)/2
	timeInfoDict = {}
	timeInfoDict['meanHour'] = meanTime.hour
	timeInfoDict['meanMinute'] = meanTime.hour * 60 + meanTime.minute
	timeInfoDict['endHour'] = endTime.hour
	timeInfoDict['endMinute'] = endTime.hour * 60 + endTime.minute
	return timeInfoDict

def label(jobFreqHistoryDict, jobTimeHistoryDict, jobFormat):
	if int(jobFormat.endTime) < int(jobFormat.toDie) and int(jobFormat.endTime) > int(jobFormat.toRetire):
		if jobFormat.lastActivity == "Killing" or jobFormat.lastActivity == "Vacating":
			jobFormat.label = "Killed"
		else:
			jobFormat.label = "Retired"
	elif int(jobFormat.endTime) > int(jobFormat.toDie):
		jobFormat.label = "Killed"
	elif len(jobFormat.daemonStartSet) > 1:
		jobFormat.preemptedFreq = len(jobFormat.daemonStartSet)
		jobFormat.label = "LightPreempted"
	elif jobFormat.jobId in jobFreqHistoryDict:
		if jobTimeHistoryDict[jobFormat.jobId] not in jobFormat.daemonStartSet:
			jobFreqHistoryDict[jobFormat.jobId] += 1
			jobFormat.preemptedFreq = jobFreqHistoryDict[jobFormat.jobId]
			jobFormat.label = "HeavyPreempted"
		else:
			jobFormat.label = "NetworkIssue"
	elif max(jobFormat.activityDict.iteritems(), key=operator.itemgetter(1))[0] is "Idle":
		if jobFormat.lastActivity == "Idle":
			jobFormat.label = "CleanUp"
		else:
			jobFormat.label = "Stupid"
	elif max(jobFormat.activityDict.iteritems(), key=operator.itemgetter(1))[0] is "Busy":
		if jobFormat.lastActivity == "Idle":
			jobFormat.label = "Succeeded"
		elif jobFormat.lastActivity == "Busy":
			jobFormat.label = "Weird"
		else:
			jobFormat.label = "NeedIdentify"
	elif max(jobFormat.activityDict.iteritems(), key=operator.itemgetter(1))[0] is "Benchmarking":
		jobFormat.label = "Benchmarking"
	else:
		jobFormat.label = "Unknown"
	if jobFormat.jobId not in jobFreqHistoryDict:
		jobFreqHistoryDict[jobFormat.jobId] = 1
		

def generateLifeCycleFromFile(fileName, lineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot):
	cnt = lineCount
	parser = Parser.Parser(fileName)
	with open(fileName, "r") as lines:
		for line in lines:
			curSnapShot = parser.readLine(line)
			if cnt == 0:
				preJobSet = set(parser.extractJobList(line))
				for beg in preJobSet:
					job0 = curSnapShot.jobDict[beg]
					job0LifeCycle = JobLifeCycle(job0)
					preJobLifeCycleDict[beg] = job0LifeCycle
				preSnapShot = curSnapShot
				cnt = cnt + 1
			else:
				curJobSet = set(parser.extractJobList(line))
				finishJobSet = preJobSet - curJobSet
				beginJobSet = curJobSet - preJobSet
				intersectJobSet = preJobSet & curJobSet
				for inter in intersectJobSet:
					interJobLifeCycle = preJobLifeCycleDict[inter]
					interJob = curSnapShot.jobDict[inter]
					interJobLifeCycle.stay(interJob.timeAbs,interJob.daemonStart,interJob.activity,interJob.state)
					curJobLifeCycleDict[inter] = interJobLifeCycle
				for fin in finishJobSet:
					finJob = preSnapShot.jobDict[fin]
					preJobLifeCycleDict[fin].stop(finJob.timeAbs, finJob.desktopTime)
					jobFormat = JobFormat(preJobLifeCycleDict[fin])
	#				print finJob.jobId,preJobLifeCycleDict[fin].pairActStateList
	#				print finJob.jobId,preJobLifeCycleDict[fin].cycle,preJobLifeCycleDict[fin].desktopStart,preJobLifeCycleDict[fin].desktopEnd,preJobLifeCycleDict[fin].startTime,preJobLifeCycleDict[fin].endTime
	#				print jobFormat.jobId,jobFormat.endTime,jobFormat.toRetire,jobFormat.toDie,jobFormat.label
	#				print jobFormat.activityDict,jobFormat.stateDict,jobFormat.daemonStartSet
	#				print jobFormat.label
					label(jobFreqHistoryDict, jobTimeHistoryDict, jobFormat)
					jobTimeHistoryDict[finJob.jobId] = finJob.daemonStart
					print jobFormat.jobId,",",jobFormat.duration,",",jobFormat.retireRuntime,",",jobFormat.killRuntime,",",jobFormat.desktopTimeInfo['meanHour'],",",jobFormat.desktopTimeInfo['meanMinute'],",",jobFormat.desktopTimeInfo['endHour'],",",jobFormat.desktopTimeInfo['endMinute'],",",jobFormat.host,",",jobFormat.site,",",jobFormat.resource,",",jobFormat.entry,",",jobFormat.endTime,",",jobFormat.toRetire,",",jobFormat.toDie,",",jobFormat.preemptedFreq,",",jobFormat.label
					preJobLifeCycleDict.pop(fin)
				for beg in beginJobSet:
					job = curSnapShot.jobDict[beg]
					jobLifeCycle = JobLifeCycle(job)
					curJobLifeCycleDict[beg] = jobLifeCycle
				preJobSet = curJobSet
				preJobLifeCycleDict = curJobLifeCycleDict
				preSnapShot = curSnapShot
				cnt = cnt + 1
	tup = (cnt, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
	return tup

