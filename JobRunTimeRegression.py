# Author: Zhe Zhang <zhan0915@huskers.unl.edu>

# This file is to use linear regression model to predict pilot job run time(a job stops due to many reasons such as preemption, succeeded and etc.).

import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

df_adv = pd.read_csv('/Users/zhezhang/Desktop/04082017.csv', index_col=0)
#X = df_adv[['MaxRunTime', 'DesktopMeanTime', 'HostName', 'SiteName', 'ResourceName', 'EntryName', 'Class']]
X = df_adv[['MaxRunTime', 'DesktopMeanTime', 'SiteName', 'ResourceName', 'EntryName', 'Class']]
y = df_adv['Duration']

#est = smf.ols(formula='Duration ~ MaxRunTime + C(DesktopMeanTime) + HostName + SiteName + ResourceName + EntryName + Class', data=df_adv).fit()
est = smf.ols(formula='Duration ~ MaxRunTime + C(DesktopMeanTime) + SiteName + ResourceName + EntryName + Class', data=df_adv).fit()

print est.summary()
