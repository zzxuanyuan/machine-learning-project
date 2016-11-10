#!/usr/bin/python

import sys
import Parser

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
		self.startTime = job.timeAbs
		self.endTime = 0
		self.name = job.name
		self.site = job.site
		self.toRetire = job.toRetire
		self.toDie = job.toDie
		self.jobId = job.jobId
		self.pairActStateList = []
		tup = (job.timeAbs, job.activity, job.state)
		self.pairActStateList.append(tup)

	def stop(self, endTime):
		self.endTime = endTime

	def stay(self, curTime, activity, state):
		tup = (curTime, activity, state)
		self.pairActStateList.append(tup)

	def change(self, curTime, activity, state):
		tup = (curTime, activity, state)
		self.pairActStateList.append(tup)
	

print "this is joblifecycle"
preJobSet = []
curJobSet = []
preJobLifeCycleDict = {}
curJobLifeCycleDict = {}
parser = Parser.Parser(sys.argv[1])
with open(sys.argv[1], "r") as lines:
	cnt = 0
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
#			testKey = '"12468661"'
#			print "testKey length",testKey,len(preJobLifeCycleDict[testKey].pairActStateList)
		else:
			curJobSet = set(parser.extractJobList(line))
			finishJobSet = preJobSet - curJobSet
			beginJobSet = curJobSet - preJobSet
			intersectJobSet = preJobSet & curJobSet
#			print "preJobSet len is",len(preJobSet)
#			print "preJobLifeCycleDict len is",len(preJobLifeCycleDict)
#			testKey = '"12468661"'
#			print "testKey length",testKey,len(preJobLifeCycleDict[testKey].pairActStateList)
#			print "begin",len(beginJobSet),beginJobSet
#			print "finish",len(finishJobSet),finishJobSet
#			print "intersect",len(intersectJobSet),intersectJobSet
#			print "preJobSet",len(preJobSet),preJobSet
#			print "curJobSet",len(curJobSet),curJobSet
			for inter in intersectJobSet:
				interJobLifeCycle = preJobLifeCycleDict[inter]
				interJob = curSnapShot.jobDict[inter]
				interJobLifeCycle.stay(interJob.timeAbs,interJob.activity,interJob.state)
				curJobLifeCycleDict[inter] = interJobLifeCycle
			for fin in finishJobSet:
#				print snapShot.timeStamp
				finJob = preSnapShot.jobDict[fin]
				preJobLifeCycleDict[fin].stop(finJob.timeAbs)
				print finJob.jobId,preJobLifeCycleDict[fin].pairActStateList
				preJobLifeCycleDict.pop(fin)
			for beg in beginJobSet:
				job = curSnapShot.jobDict[beg]
				jobLifeCycle = JobLifeCycle(job)
				curJobLifeCycleDict[beg] = jobLifeCycle
			preJobSet = curJobSet
			preJobLifeCycleDict = curJobLifeCycleDict
			preSnapShot = curSnapShot
			cnt = cnt + 1

