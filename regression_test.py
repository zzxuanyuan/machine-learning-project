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

df = pd.read_csv(sys.argv[1])

le = preprocessing.LabelEncoder()
print le.fit(df['DesktopTimeMeanHour'])
print list(le.classes_)
print le.transform([0,1,23]) 

print le.fit(df['SiteName'])
print list(le.classes_)
print le.transform(df['SiteName']) 


X = df[['TotalJobs', 'MaxRetireTime', 'MaxKillTime', 'PreemptionFrequency']]
le.fit(df['SiteName'])
X.insert(3, 'SiteName', le.transform(df['SiteName']))
le.fit(df['ResourceName'])
X.insert(4, 'ResourceName', le.transform(df['ResourceName']))
le.fit(df['EntryName'])
X.insert(5, 'EntryName', le.transform(df['EntryName']))

print X.loc[[0,1,2,3],['SiteName']]
print X.head()
X_train = X.loc[np.arange(0,int(math.floor(0.8*len(X.index))))]
X_test = X.loc[np.arange(int(math.floor(0.8*len(X.index))), len(X.index))]
y = df['Duration']
y_train = y[np.arange(0,int(math.floor(0.8*len(y.index))))]
y_test = y[np.arange(int(math.floor(0.8*len(y.index))),len(y.index))]

# Fit regression model
#regr_1 = DecisionTreeRegressor(max_depth=2)
#regr_2 = DecisionTreeRegressor(max_depth=5)
regr_1 = RandomForestRegressor()
#regr_2 = RandomForestRegressor()
regr_1.fit(X_train, y_train)
#regr_2.fit(X_train, y_train)
print regr_1.score(X_train, y_train)
#print regr_2.score(X_test, y_test)

# Predict
y_1 = regr_1.predict(X_test)
#y_2 = regr_2.predict(X_test)

print "correlation = "
#print np.corrcoef(y_1, y_test)[0,1]
print pearsonr(y_1, y_test)
est = sm.OLS(y_1, y_test)
est = est.fit()
print est.summary()

# Plot the results
plt.figure()
plt.plot(range(0,len(y_test)), y_test, c="blue", label="target values")
plt.plot(range(0,len(y_1)), y_1, color="red", label="predicted values")
#plt.plot(range(0,len(y_2)), y_2, color="yellowgreen", label="max_depth=5", linewidth=2)
plt.xlabel("Time Series")
plt.ylabel("Job Run Time (s)")
plt.title("Random Forest Regression")
plt.legend(loc='upper left')
plt.show()
