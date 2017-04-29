# Author: Zhe Zhang <zhan0915@huskers.unl.edu>

# This file is to use linear regression model to predict pilot job run time(a job stops due to many reasons such as preemption, succeeded and etc.).

import sys
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

#df = pd.read_csv(sys.argv[1], names=['JobId' , 'Duration' , 'MaxRetireTime' , 'MaxKillTime' , 'DesktopTimeMeanHour' , 'DesktopTimeMeanMinute' , 'DesktopTimeEndHour' , 'DesktopTimeEndMinute' , 'HostName' , 'SiteName' , 'ResourceName' , 'EntryName' , 'JobEndTime' , 'JobRetireTime' , 'JobDieTime' , 'PreemptionFrequency' , 'Class'])
df = pd.read_csv(sys.argv[1])
#X = df[['MaxRunTime', 'DesktopMeanTime', 'HostName', 'SiteName', 'ResourceName', 'EntryName', 'Class']]
#X = df[['MaxRunTime', 'DesktopMeanTime', 'SiteName', 'ResourceName', 'EntryName', 'Class']]
#y = df['Duration']

#X = df[['SiteName', 'ResourceName', 'EntryName']]
#y = df['Class']
#est = smf.ols(formula='Duration ~ MaxRunTime + C(DesktopMeanTime) + HostName + SiteName + ResourceName + EntryName + Class', data=df).fit()
#est = smf.ols(formula='Duration ~ Class', data=df).fit()
#est = smf.ols(formula='Duration ~ MaxRetireTime + MaxKillTime + C(DesktopTimeMeanHour) + C(DesktopTimeEndHour) + SiteName + ResourceName + EntryName + PreemptionFrequency', data=df).fit()
est = smf.ols(formula='Duration ~ PreemptionFrequency', data=df).fit()
#est = smf.ols(formula='Duration ~ MaxRetireTime + C(DesktopTimeEndHour) + SiteName + PreemptionFrequency', data=df).fit()

print est.summary()
