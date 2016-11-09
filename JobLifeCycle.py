#!/usr/bin/python

import Parser

class JobLifeCycle:
	startTime = 0
	endTime = 0
	actStateList = []
	name = ""
	site = ""
        toRetire = 0
	toDie = 0
	jobId = ""

	def __init__(self, startTime,activity,state):
		self.startTime = startTime
		tup = (startTime, activity, state)
		self.pairActStateList.append(tup)

	def stop(self, endTime):
		self.endTime = endTime

	def change(self, curTime, activity, state):
		tup = (curTime, activity, state)
		self.pairActStateList.append(tup)
	

preJobSet = {}
curJobSet = {}
parser = Parser(sys.argv[1])
with open(sys.argv[1], "r") as lines:
	cnt = 0
	for line in lines:
		snapShot = parser.readLine(line)
		if cnt == 0:
			preJobSet = parser.extractJobSet(line)
		else:
			curJobSet = parser.extractJobSet(line)
			finishJobSet = preJobSet.difference(curJobSet)
			beginJobSet = curJobSet.difference(preJobSet)
			for fin in finishJobSet:
				snapShot[fin]
		snapShot = parser.readLine(line)
		for job in snapShot.jobList:
			print job.state,job.activity

