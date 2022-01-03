# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 13:33:17 2021

@author: samak
"""

# CIS 443-01 - Analytics Programming
## Program 4
# __Grading ID__: P8330 <br>
#__Due__: Saturday, 12/4 by 11:59 PM <br />
#__Worth__: 100 pts. <br />
#__Description__:  This assignment explores the use of TextBlob to perform sentiment analysis of reviews gathered from TextAdvisor

import pandas as pd

from textblob import TextBlob


# returns the classification of the sentiment of the star rating
def review_sent(star_rating):
    
    pos = 4
    neg = 2
    
    if star_rating >= pos:
        sentiment = 'postive'
    elif star_rating <= neg:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
        
    return sentiment

#  returns the classification of the sentiment polarity of the review's text
def rating_sent(polarity):
    
    pos = -0.05
    neg = 0.05
    
    if polarity >= pos:
        sentiment = 'postive'
    elif polarity <= neg:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
        
    return sentiment

#Loads the attached csv data into a Pandas dataframe
file = 'tripadvisor_hotel_reviews.csv'
df = pd.read_csv(file)  

# classification of the sentiment of the star rating
df['Total_Review'] = [review_sent(star_rating) for star_rating in df['Rating']]
                       
# add the review's sentiment polarity using each review's text   
blobs = [TextBlob(Review) for Review in df['Review']]
df['polar_rating'] = [blob.sentiment.polarity for blob in blobs]

df['S_text'] = [rating_sent (polarity) for polarity in df['polar_rating']]

df['Sent_agree'] = [df.Total_Review[i] == df.S_text[i] for i in range(len(df))]

# subset of columns
sub = df[['Rating', 'Total_Review', 'polar_rating', 'S_text', 'Sent_agree']]


# determines whether the star rating's sentiment agrees with the review text's sentiment 
agreement  = sub[sub.Sent_agree]
disagreement = sub[sub.Sent_agree == False]

Total = len(df)         
ag = len(agreement)       
dis_ag = len(disagreement) 

# prints the overall star-sentiment agreement
print('Overall Star-Sentiment Agreement')
print(f'Number of reviews: {Total}')
print(f'\nNumber agree:    {ag:4}, {ag/Total*100:.2f}%')
print(f'Number disagree: {dis_ag:4}, {dis_ag/Total*100:.2f}%')


# Print table header
print('\nRating |Total Reviews|Num Agree|% Agree|Num Disagree|% Disagree')
print('------------|-------------|---------|-------|------------|----------')

# ratings break down
for star_rating in range(5,0,-1):
    
    star_sub = sub[sub.Rating == star_rating]
    star_agree = agreement[agreement.Rating == star_rating]

    sub_num = len(star_sub)
    agree_num = len(star_agree)
    disagr_num = sub_num - agree_num

    a_pct = agree_num/sub_num
    d_pct = disagr_num/sub_num
    
    
print(f'{star_rating:^12}|     {sub_num:4}    |   {agree_num:4}  |{a_pct*100:6.2f}%|    {disagr_num:4}    |{d_pct*100:7.2f}%')

