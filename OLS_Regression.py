from sklearn import linear_model
reg = linear_model.LinearRegression()
import numpy as np
import pandas as pd
import csv
import datetime
reader=csv.reader(open('byday.csv','rU'))
colx= [row[5] for row in reader]
reader2=csv.reader(open('byday.csv','rU'))
coly= [row[6] for row in reader2]
x=[]
y=[]
for i in range(1,len(colx)):
	x.append(float(colx[i]))
	y.append(float(coly[i]))
print len(x)
print len(y)
reg.fit (x, y)
#LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
print reg.coef_
