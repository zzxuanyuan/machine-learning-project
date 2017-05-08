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
tup = JobLifeCycle.generateLifeCycleFromFile("/mnt/home.centos.data/04072017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]


print "2. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "2. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/mnt/home.centos.data/04082017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "3. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "3. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/mnt/home.centos.data/04092017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "4. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "4. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/mnt/home.centos.data/04102017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "5. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "5. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/mnt/home.centos.data/04112017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "6. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "6. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/mnt/home.centos.data/04122017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "7. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "7. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/mnt/home.centos.data/04132017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "8. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "8. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/mnt/home.centos.data/04142017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "9. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "9. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/mnt/home.centos.data/04152017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "10. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "10. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/mnt/home.centos.data/04162017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "11. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "11. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/mnt/home.centos.data/04172017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "12. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "12. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/mnt/home.centos.data/04182017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "13. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "13. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/mnt/home.centos.data/04192017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "14. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "14. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/mnt/home.centos.data/04202017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "15. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "15. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/mnt/home.centos.data/04212017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "16. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "16. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/mnt/home.centos.data/04222017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "17. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "17. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/mnt/home.centos.data/04232017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "18. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "18. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/mnt/home.centos.data/04242017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "19. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "19. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/mnt/home.centos.data/04252017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "20. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "20. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/mnt/home.centos.data/04262017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "21. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "21. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/mnt/home.centos.data/04272017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "22. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "22. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/mnt/home.centos.data/04282017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "23. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "23. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/mnt/home.centos.data/04292017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "24. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "24. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/mnt/home.centos.data/04302017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "25. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "25. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/mnt/home.centos.data/05012017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "26. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "26. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/mnt/home.centos.data/05022017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "27. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "27. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/mnt/home.centos.data/05032017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "28. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "28. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/mnt/home.centos.data/05042017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "29. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "29. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/mnt/home.centos.data/05052017.firsthalf.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "30.(first half) Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "30.(first half) Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/mnt/home.centos.data/05052017.secondhalf.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "30.(second half) Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "30.(second half) Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/mnt/home.centos.data/05062017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "31. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "31. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())

tup = JobLifeCycle.generateLifeCycleFromFile("/mnt/home.centos.data/05072017.data", totalLineCount, preJobSet, curJobSet, preJobLifeCycleDict, curJobLifeCycleDict, preSnapShot, curSnapShot)
totalLineCount += tup[0]
preJobSet = tup[1]
curJobSet = tup[2]
preJobLifeCycleDict = tup[3]
curJobLifeCycleDict = tup[4]
preSnapShot = tup[5]
curSnapShot = tup[6]

print "32. Job Freq Hisotry Dict:", len(JobLifeCycle.jobFreqHistoryDict.keys())
print "32. Job Time Hisotry Dict:", len(JobLifeCycle.jobTimeHistoryDict.keys())


