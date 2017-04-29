# Import the necessary modules and libraries
import matplotlib.pyplot as plt
import math
import sys
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn import preprocessing
from sklearn.tree import DecisionTreeRegressor

df = pd.read_csv(sys.argv[1], names=['JobId' , 'Duration' , 'MaxRetireTime' , 'MaxKillTime' , 'DesktopTimeMeanHour' , 'DesktopTimeMeanMinute' , 'DesktopTimeEndHour' , 'DesktopTimeEndMinute' , 'HostName' , 'SiteName' , 'ResourceName' , 'EntryName' , 'JobEndTime' , 'JobRetireTime' , 'JobDieTime' , 'PreemptionFrequency' , 'Class'])

le = preprocessing.LabelEncoder()
print le.fit(df['DesktopTimeMeanHour'])
print list(le.classes_)
print le.transform([0,1,23]) 

print le.fit(df['SiteName'])
print list(le.classes_)
print le.transform(df['SiteName']) 


X = df[['MaxRetireTime' , 'MaxKillTime' , 'DesktopTimeMeanHour' , 'DesktopTimeMeanMinute' , 'DesktopTimeEndHour' , 'DesktopTimeEndMinute' , 'PreemptionFrequency']]
le.fit(df['SiteName'])
X.insert(6, 'SiteName', le.transform(df['SiteName']))
le.fit(df['ResourceName'])
X.insert(6, 'ResourceName', le.transform(df['ResourceName']))
le.fit(df['EntryName'])
X.insert(6, 'EntryName', le.transform(df['EntryName']))

print X.loc[[0,1,2,3],['SiteName']]
print X.head()
X_train = X.loc[np.arange(0,int(math.floor(0.8*len(X.index))))]
X_test = X.loc[np.arange(int(math.floor(0.8*len(X.index))), len(X.index))]
y = df['Duration']
y_train = y[np.arange(0,int(math.floor(0.8*len(y.index))))]
y_test = y[np.arange(int(math.floor(0.8*len(y.index))),len(y.index))]

# Fit regression model
regr_1 = DecisionTreeRegressor(max_depth=9)
regr_2 = DecisionTreeRegressor(max_depth=10)
regr_1.fit(X_train, y_train)
regr_2.fit(X_train, y_train)
print regr_1.score(X_train, y_train)
print regr_2.score(X_train, y_train)

'''
# Predict
y_1 = regr_1.predict(X_test)
y_2 = regr_2.predict(X_test)

# Plot the results
plt.figure()
plt.scatter(X_test, y_test, c="darkorange", label="data")
plt.plot(X_test, y_1, color="cornflowerblue", label="max_depth=2", linewidth=2)
plt.plot(X_test, y_2, color="yellowgreen", label="max_depth=5", linewidth=2)
plt.xlabel("data")
plt.ylabel("target")
plt.title("Decision Tree Regression")
plt.legend()
plt.show()
'''
