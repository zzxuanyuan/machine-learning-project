# This file does regression test using Random Forest Regression.
# The input file should be insert_total_jobs.csv that contains total jobs info.

import matplotlib.pyplot as plt
import math
import sys
import pandas as pd
import numpy as np
from scipy.stats.stats import pearsonr
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn import preprocessing
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

class RegressionWindow:

	def __init__(self, model = "RandomForestRegressor"):
		self.model = model
		if model == "RandomForestRegressor":
			self.regressor = RandomForestRegressor()
		else:
			"TODO regressor"

	def process(self, xTrain, yTrain, xTest, yTest):
		self.regressor.fit(xTrain, yTrain)
		yPredict = self.regressor.predict(xTest)
		diff = yTest - yPredict
		return (yTest, yPredict, diff)
'''
	def show_test(self):
		print self.dfYTest

	def show_predict(self):
		print self.dfYPredict

	def get_diff(self):
		return self.diff
'''

def modulo_hour(x):
	return x%24

class SlidingWindow:

	def __init__(self, df, attribute = "DesktopTimeEndHour", target = "Duration", slide = 10 , split = 0.9):
		self.df = df
		self.curDF = df
		self.attribute = attribute
		self.target = target
		self.slide = slide
		self.split = split
		self.curStartAttr = int(df.loc[0, attribute])
		self.curEndAttr = int(self.curStartAttr + slide)
		self.curSplitAttr = int(self.curStartAttr + slide * split)
		self.curStartLine = 0
		self.curSplitLine = 0
		self.curEndLine = 0
		self.dfTrain = pd.DataFrame(index=df.index,columns=df.columns)
		self.dfTest = pd.DataFrame(index=df.index,columns=df.columns)
		self.curWindow = RegressionWindow()
		self.curTest = list()
		self.curPredict = list()
		self.curDiff = list()

	def slide_next(self):
		print self.curDF.head(1)
		lineInfo = self.grow(self.curStartAttr,self.curSplitAttr,self.curEndAttr)
		if lineInfo == (-1,-1,-1):
			return "EOF"
		print "lineInfo = ", lineInfo
		self.curStartLine = lineInfo[0]
		self.curSplitLine = lineInfo[1]
		self.curEndLine = lineInfo[2]
		xTrain = self.dfTrain.loc[:,self.dfTrain.columns != self.target].values
		yTrain = self.dfTrain.loc[:,self.dfTrain.columns == self.target].values[:,0]
                xTest = self.dfTest.loc[:,self.dfTest.columns != self.target].values
		yTest = self.dfTest.loc[:,self.dfTest.columns == self.target].values[:,0]
                tup = self.curWindow.process(xTrain, yTrain, xTest, yTest)
		self.curTest.extend(tup[0])
		self.curPredict.extend(tup[1])
		self.curDiff.extend(tup[2]*1.0/tup[0])
		self.reset_attr()
		return "CONTINUE"

	def grow(self, startAttr, splitAttr, endAttr):
		if self.attribute == "DesktopTimeEndHour":
			startAttrList = map(modulo_hour, range(startAttr, splitAttr))
			nextAttrList = map(modulo_hour, [startAttr])
			self.nextStartLine = self.curDF[~self.curDF[self.attribute].isin(nextAttrList)][self.attribute].index[0]
			self.curSplitLine = self.curDF[~self.curDF[self.attribute].isin(startAttrList)][self.attribute].index[0]
			endAttrList = map(modulo_hour, range(startAttr, endAttr))
			print "startAttrList = ", startAttrList
			print "nextAttrList = ", nextAttrList
			print "endAttrList = ", endAttrList
			if len(self.curDF[~self.curDF[self.attribute].isin(endAttrList)][self.attribute].index) == 0:
				return (-1,-1,-1)
			else:
				self.curEndLine = self.curDF[~self.curDF[self.attribute].isin(endAttrList)][self.attribute].index[0]
#			print "self.nextStartLine = ", self.curDF[~self.curDF[self.attribute].isin(nextAttrList)][self.attribute]
#			print "self.curSplitLine = ", self.curDF[~self.curDF[self.attribute].isin(startAttrList)][self.attribute]
#			print "self.curEndLine = ", self.curDF[~self.curDF[self.attribute].isin(endAttrList)][self.attribute]
		else:
			startAttrList = range(startAttr, splitAttr)
			nextAttrList = [startAttr]
			self.nextStartLine = self.curDF[~self.curDF[self.attribute].isin(nextAttrList)][self.attribute].index[0]
			self.curSplitLine = self.curDF[~self.curDF[self.attribute].isin(startAttrList)][self.attribute].index[0]
			endAttrList = range(splitAttr, endAttr)
			self.curEndLine = self.curDF[~self.curDF[self.attribute].isin(endAttrList)][self.attribute].index[0]

		self.dfTrain = self.df[self.curStartLine:self.curSplitLine]
		self.dfTest = self.df[self.curSplitLine:self.curEndLine]
		return (self.curStartLine, self.curSplitLine, self.curEndLine)

	def reset_attr(self):
		self.curStartLine = self.nextStartLine
		self.curSplitLine = self.curStartLine
		self.curEndLine = self.curStartLine
		self.curStartAttr += 1
		self.curSplitAttr += 1
		self.curEndAttr += 1
		self.curDF = self.df[self.nextStartLine:]

	def get_diff(self):
		return self.curDiff

	def get_test(self):
		return self.curTest

	def get_predict(self):
		return self.curPredict

df = pd.read_csv('weka.test')

df['TotalJobNum'] = map(int, df['TotalJobNum'])
df['MaxRetireTime'] = map(int, df['MaxRetireTime'])
df['MaxKillTime'] = map(int, df['MaxKillTime'])
df['DesktopTimeEndHour'] = map(int, df['DesktopTimeEndHour'])
df['PreemptionFrequency'] = map(int, df['PreemptionFrequency'])
df['Duration'] = map(int, df['Duration'])

le = preprocessing.LabelEncoder()
dfInput = df[['TotalJobNum', 'MaxRetireTime', 'MaxKillTime', 'DesktopTimeEndHour', 'PreemptionFrequency','Duration']]
le.fit(df['SiteName'])
dfInput.insert(3, 'SiteName', le.transform(df['SiteName']))
le.fit(df['ResourceName'])
dfInput.insert(4, 'ResourceName', le.transform(df['ResourceName']))
le.fit(df['EntryName'])
dfInput.insert(5, 'EntryName', le.transform(df['EntryName']))


#dfInput = df[df['Class']=='Preempted'][['TotalJobNum', 'MaxRetireTime', 'MaxKillTime', 'DesktopTimeEndHour', 'PreemptionFrequency', 'Duration']]
#dfInput = pd.DataFrame(df[['TotalJobNum', 'MaxRetireTime', 'MaxKillTime', 'DesktopTimeEndHour', 'PreemptionFrequency', 'Duration']].values, index=df.index, columns=['TotalJobNum', 'MaxRetireTime', 'MaxKillTime', 'DesktopTimeEndHour', 'PreemptionFrequency', 'Duration'])

slideWindow = SlidingWindow(dfInput, slide=20, split=0.8)

while(1):
	res = slideWindow.slide_next() 
	if res == "EOF":
		break
	diff = slideWindow.get_diff()
	test = slideWindow.get_test()
	predict = slideWindow.get_predict()
	print "length of diff: ", len(diff)
	print "length of test: ", len(test)
	print "length of predict: ", len(predict)

print pearsonr(test, predict)

result = [abs(a*1.0/b) for a,b in zip(diff,test)]
r_1p = [i for i in result if i < 0.01]
r_5p = [i for i in result if i < 0.05]
r_10p = [i for i in result if i < 0.1]
r_15p = [i for i in result if i < 0.15]
r_20p = [i for i in result if i < 0.2]
r_25p = [i for i in result if i < 0.25]
r_30p = [i for i in result if i < 0.3]
r_35p = [i for i in result if i < 0.35]
r_40p = [i for i in result if i < 0.4]
r_45p = [i for i in result if i < 0.45]
r_50p = [i for i in result if i < 0.5]
print "1% : ", len(r_1p)*1.0/len(result)
print "5% : ", len(r_5p)*1.0/len(result)
print "10% : ", len(r_10p)*1.0/len(result)
print "15% : ", len(r_15p)*1.0/len(result)
print "20% : ", len(r_20p)*1.0/len(result)
print "25% : ", len(r_25p)*1.0/len(result)
print "30% : ", len(r_30p)*1.0/len(result)
print "35% : ", len(r_35p)*1.0/len(result)
print "40% : ", len(r_40p)*1.0/len(result)
print "45% : ", len(r_45p)*1.0/len(result)
print "50% : ", len(r_50p)*1.0/len(result)

