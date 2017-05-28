# jiaqi-tang.github.com
my online resume 
Welcome to my project which is on robbery crime prediction using twitter sentiment and demographics(In my github, there is a small start part of my project, I'll post my code and modeling more later):

1. First, I analyzed the tweets and I used sentiment analysis for processing each tweet and then got sentiment score of each 
tweet. Finally I export the result to a csv file. The file which is " Sentiment analysis.py " is my python file for sentiment
analysis.

2. After getting sentiment scores and polarities of tweets,I used basic machine learing method for predictive modeling:sentiment
Scores is predictor. Robbery crime counts is outcome. I used OLS regression ,for Y and X are continous variables.

Y= a+ β X+ u
For each day:
Y                               occurrences of robbery crime
X                               average sentiment scores 
Use gradient Function to complete the Gradient Descent for robbery crime prediction in my project for getting optimal beta
Then find the errors between observed y and predicted y by using rest of my dataset for finishing testing process.
the file Predictive-modeling(ols_regression).py is my python file for predictive modeling for this case.

3. Demographics part:
first , get the first names of people who post the tweet in my dataset, and get the median age by their first name:

Methodology:

Baby name dataset: I created a dataset that show how many people were born in each first name in this year, the year range is from 1990 to 2015, I created this dataset by getting the data of baby name dataset from Social Security Administrition. 
Use the method from life table to remove the people who are supposed to be dead, and the get the median age and gender in 2015 of each first name.
Finally, match each first name of my twitter dataset with their median age and gender , in this way, I got the age distribution and gender distribution of the people who post these tweets in my dataset.

5. Furture work:
I intend to create 3D modeling for spatial temporal for crime distribtuion ,for I have data of locations and time of tiwtter data and crime data. Additionally, use machine learning for create predictive modeling using twitter sentiment and demographics for this spatial temporal model.
