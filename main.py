import Parser
import JobLifeCycle


preJobSet = set()
curJobSet = set()
preJobLifeCycleDict = {}
curJobLifeCycleDict = {}
preSnapShot = Parser.SnapShot("", {})
curSnapShot = Parser.SnapShot("", {})

print "1. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "1. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

totalLineCount = 0
tup = JobLifeCycle.generateLifeCycleFromFile("/Users/zhezhang/mount/home.centos.data/04072017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]


print "2. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "2. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/Users/zhezhang/mount/home.centos.data/04082017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "3. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "3. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/Users/zhezhang/mount/home.centos.data/04092017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "4. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "4. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/Users/zhezhang/mount/home.centos.data/04102017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "5. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "5. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/Users/zhezhang/mount/home.centos.data/04112017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "6. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "6. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/Users/zhezhang/mount/home.centos.data/04122017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "7. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "7. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/Users/zhezhang/mount/home.centos.data/04132017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "8. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "8. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/Users/zhezhang/mount/home.centos.data/04142017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "9. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "9. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/Users/zhezhang/mount/home.centos.data/04152017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "10. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "10. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/Users/zhezhang/mount/home.centos.data/04162017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "11. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "11. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/Users/zhezhang/mount/home.centos.data/04172017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "12. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "12. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/Users/zhezhang/mount/home.centos.data/04182017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "13. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "13. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/Users/zhezhang/mount/home.centos.data/04192017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "14. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "14. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/Users/zhezhang/mount/home.centos.data/04202017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "15. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "15. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/Users/zhezhang/mount/home.centos.data/04212017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "16. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "16. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())
