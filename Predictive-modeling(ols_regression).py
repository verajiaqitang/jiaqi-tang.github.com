import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import csv
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import time
reader=csv.reader(open('filename.csv','rU'))
reader2=csv.reader(open('filename.csv','rU'))
d = [row[n] for row in reader]
c=[row[m] for row in reader2]
train_score=[]
train_crimes=[]
test_score=[]
test_crimes=[]
testset_y=[]
for i in range(1,101):
	train_score.append(float(d[i]))
for i in range(1,101):
	train_crimes.append(int(c[i]))

lmr3 = linear_model.LinearRegression()
lmr3.fit(np.transpose(np.matrix(train_score)), np.transpose(np.matrix(train_crimes)))

trainset_y=[]
for i in range(len(train_crimes)):
	if train_crimes[i]>=22:
		trainset_y.append(1)
	else:
		trainset_y.append(0)

for i in range(101,len(d)):
	test_score.append(float(d[i]))

for i in range(101,len(c)):
	testset_y.append(float(c[i]))  

	
vy=np.matrix(trainset_y)
vx=np.matrix(train_score)
Y =np.transpose(np.matrix(trainset_y))
X = sm.add_constant(np.transpose(np.matrix(train_score)))
ans=np.corrcoef(vy,vx)
#print ans
results = sm.Logit(Y,X).fit()
betas=lmr3.coef_
test_score=np.matrix(test_score)
test_score=test_score.transpose()
testset_y=np.matrix(testset_y)
testset_y=testset_y.transpose()
alph = 0.00001
niter=1.
betas=np.vstack((betas,betas))
def gradient(X, y, betas):
	err = y - np.dot(X, betas)
	return -2*np.dot(X.transpose(),err)/len(y)

grad = gradient(X,Y,betas)
err = Y - np.dot(X, betas)
tol = 1e-8
while (alph*np.linalg.norm(gradient(X,Y,betas)) > tol) and (niter < 20000):
    #****************************
    # Your code here!
    betas = betas - alph*gradient(X,Y,betas)
    niter += 1
   


print betas

s=lmr3.intercept_
betas=np.matrix(betas[1,0])
y_true=testset_y
intercept=[]
for i in range(len(y_true)):
	intercept.append(s)
intercept=np.matrix(intercept)
intercept=intercept.transpose()
	
y_pred=np.dot(test_score, betas)+intercept
def new_error(y_true, y_pred):
    diff = (y_true-y_pred)
    return np.sqrt(np.dot(diff.T, diff))
errors=new_error(y_true, y_pred)
print errors


