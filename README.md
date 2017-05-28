# jiaqi-tang.github.com
my online resume 
Welcome to my project which is on robbery crime prediction using twitter sentiment and demographics:

1. First, I analyzed the tweets and I used sentiment analysis for processing each tweet and then got sentiment score of each 
tweet. Finally I export the result to a csv file. The file which is " Sentiment analysis.py " is my python file for sentiment
analysis.

2. After getting sentiment scores and polarities of tweets,I used basic machine learing method for predictive modeling:sentiment
Scores is predictor. Robbery crime counts is outcome. I used OLS regression ,for Y and X are continous variables.



Y= a+ β X+ u
For each day:
Y                               occurrences of robbery crime
X                               average sentiment scores 
Use gradient Function to complete the Gradient Descent for robbery crime prediction in my project:


