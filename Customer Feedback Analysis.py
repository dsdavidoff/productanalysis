# -*- coding: utf-8 -*-
"""
Danielle Davidoff
4/11/19
"""
import numpy as np
import pandas as pd
import os
import re
from nltk.corpus import stopwords

df = pd.read_excel('Filename.xlsx')
#read original dataset into pandas dataframe

df = df.dropna()
#drop null values

import matplotlib.pyplot as plt
plt.hist(df['NPS Score'],bins=11)
plt.title('User Feedback')
plt.xlabel('Rating')
plt.ylabel('Number of Users')
plt.show()
#histogram of all scores

plt.hist(dfComments['NPS Score'],bins=11) 
plt.title('User Feedback with Comments')
plt.xlabel('Rating')
plt.ylabel('Number of Users')
plt.show()
#histogram of all scores from the group of users who left comments

comments = list(dfComments['Feedback'])
comments = [x.lower() for x in comments]
#create list of comments from Feedback column

strlist = ','.join(comments)
#create one long string of all comments

spaced = re.split('[,./\;:!? ]',strlist)
#split list into individual words to analyze

from collections import Counter
counts=Counter(spaced)
#create Counter object with words from comments and number of times left

dfcounts = pd.DataFrame.from_dict(counts,orient='index').reset_index()
#turn Counter object into pandas dataframe

stop_words = set(stopwords.words('english'))
#import list of stopwords (and,or,but,etc) to filter out from list

stop_words = list(stop_words) + ['I','The','It','get','would',' ','one']
#added a few more stopwords not in nltk package
 
positivewords = ['good','like','love','great','well']
constructivewords = ['could','need','better','still','able',"wish","but"]
negativewords = ["doesn\'t",'hard']
unknownwords = [')','not','one','-','also','way','really','using','used','long','see','time','times','go',"i'm","it's","10",'different','give','sure','take','not','getting','keep','make']
unknownwords2 = ['use','sometimes','much','like','feel','quality','','little','much','work','use','sometimes']
productRelatedWords = []
#filter out more words unrelated to product, and sort them into categories
#create empty list of productRelatedWords

for x in dfcounts['index']:
    if not x in stop_words and not x in positivewords and not x in constructivewords and not x in negativewords and not x in unknownwords:
        productRelatedWords.append(x)
#fill empty productRelatedWords set with all words that are not stopwords or meaningless words listed above
        
productRelatedFeedback = dfcounts[dfcounts['index'].isin(productRelatedWords)]      
#create DataFrame which contains only feedback related to product related words

productRelatedFeedback.columns = ['Word','Count']
#rename columns

productRelatedFeedback.dropna(subset=['Word']) 
#drop null values

productRelatedFeedback['Word'].replace('', np.nan, inplace=True)
#replace blank values with null values\

productRelatedFeedback2 = productRelatedFeedback.dropna(subset=['Word'])
#drop newly null values

productRelatedFeedback2 = productRelatedFeedback2.sort_values('Count', ascending=False)
#sort in descending order according to count

productMask = productRelatedFeedback2['Count'] >= 10
#select only for words that occur at least ten times

productFeedback =  productRelatedFeedback2[productMask]
#create new dataframe with only words selected for in previous line

productFeedback.plot.bar(x='Word', y='Count', rot=0)
plt.title('Occurrences of Product Related Words in Feedback')
plt.xticks(rotation=90)
plt.show()
#create bar graph with product feedback

#Now to repeat this process for positive and negative feedback

positiveMask = dfComments['NPS Score'] >= 6
positiveComments = dfComments[positiveMask]
#create dataframe with only ratings of at least six

positiveWordList = list(positiveComments['Feedback'])
positiveWordList = [x.lower() for x in positiveWordList]
#create list of comments from Feedback column

positiveList = ','.join(positiveWordList)
#create one long string of all comments

positiveSpaced = re.split('[,./\;:!? ]',positiveList)
#split list into individual words to analyze

from collections import Counter
positiveCounts=Counter(positiveSpaced)
#create Counter object with words from comments and number of times left

dfPositiveCounts = pd.DataFrame.from_dict(positiveCounts,orient='index').reset_index()
#turn Counter object into pandas dataframe

positiveRelatedWords = []

for x in dfPositiveCounts['index']:
    if not x in stop_words and not x in positivewords and not x in constructivewords and not x in negativewords and not x in unknownwords and not x in unknownwords2:
        positiveRelatedWords.append(x)
        
positiveRelatedFeedback = dfPositiveCounts[dfPositiveCounts['index'].isin(positiveRelatedWords)]      
#create DataFrame which contains only feedback related to product related words

positiveRelatedFeedback.columns = ['Word','Count']
#rename columns

positiveRelatedFeedback['Word'].replace('', np.nan, inplace=True)
#replace blank values with null values\

positiveRelatedFeedback2 = positiveRelatedFeedback.dropna(subset=['Word'])
#drop newly null values

positiveRelatedFeedback2 = positiveRelatedFeedback2.sort_values('Count', ascending=False)
#sort in descending order according to count

positiveFreqMask = positiveRelatedFeedback2['Count'] >= 10
#select only for words that occur at least ten times

positiveFeedback =  positiveRelatedFeedback2[positiveFreqMask]
#create new dataframe with only words selected for in previous line

positiveFeedback.plot.bar(x='Word', y='Count', rot=0)
plt.title('Occurrences of Product Related Words in Feedback When Rating >= 6')
plt.xticks(rotation=90)
plt.show()
#create bar graph with product feedback
#####################################################

negativeMask = dfComments['NPS Score'] <= 5
negativeComments = dfComments[negativeMask]
#create dataframe with only ratings of at least six

negativeWordList = list(negativeComments['Feedback'])
negativeWordList = [x.lower() for x in negativeWordList]
#create list of comments from Feedback column

negativeList = ','.join(negativeWordList)
#create one long string of all comments

negativeSpaced = re.split('[,./\;:!? ]',negativeList)
#split list into individual words to analyze

from collections import Counter
negativeCounts=Counter(negativeSpaced)
#create Counter object with words from comments and number of times left

dfNegativeCounts = pd.DataFrame.from_dict(negativeCounts,orient='index').reset_index()
#turn Counter object into pandas dataframe

negativeRelatedWords = []

for x in dfNegativeCounts['index']:
    if not x in stop_words and not x in positivewords and not x in constructivewords and not x in negativewords and not x in unknownwords and not x in unknownwords2:
        negativeRelatedWords.append(x)
        
negativeRelatedFeedback = dfNegativeCounts[dfNegativeCounts['index'].isin(negativeRelatedWords)]      
#create DataFrame which contains only feedback related to product related words

negativeRelatedFeedback.columns = ['Word','Count']
#rename columns

negativeRelatedFeedback['Word'].replace('', np.nan, inplace=True)
#replace blank values with null values\

negativeRelatedFeedback2 = negativeRelatedFeedback.dropna(subset=['Word'])
#drop newly null values

negativeRelatedFeedback2 = negativeRelatedFeedback2.sort_values('Count', ascending=False)
#sort in descending order according to count

negativeFreqMask = negativeRelatedFeedback2['Count'] >= 6
#select only for words that occur at least ten times

negativeFeedback =  negativeRelatedFeedback2[negativeFreqMask]
#create new dataframe with only words selected for in previous line

negativeFeedback.plot.bar(x='Word', y='Count', rot=0)
plt.title('Occurrences of Product Related Words in Feedback When Rating <= 5')
plt.xticks(rotation=90)
plt.show()
#create bar graph with product feedback

newPositiveWords = []
newNegativeWords = []

for x in list(productFeedback['Word']):
    if x in list(positiveFeedback['Word']):
        newPositiveWords.append(x)
    if x in list(negativeFeedback['Word']):
        newNegativeWords.append(x)

finalList = []
finalList.remove(10)

for x in newPositiveWords:
    if x in newNegativeWords:
        finalList.append(x)

positiveFeedback = positiveFeedback[positiveFeedback['Word'].isin(finalList)]
negativeFeedback = negativeFeedback[negativeFeedback['Word'].isin(finalList)]

finalPositiveList = list(positiveFeedback['Count'])
finalNegativeList = list(negativeFeedback['Count'])

width = 0.4
 
p1 = plt.bar(11, finalPositiveList, width)
p2 = plt.bar(11, finalNegativeList, width,
             bottom=finalPositiveList)

# Now to create a stacked bar graph
bars = np.add(finalPositiveList, finalNegativeList).tolist()
 
# The position of the bars on the x-axis
r = [0,1,2,3,4,5,6,7,8,9,10]
 
# Names of group and bar width
names = finalList
barWidth = 0.6
 

plt.bar(r, finalNegativeList, color='red', edgecolor='white', width=barWidth)
plt.bar(r, finalPositiveList, bottom=finalNegativeList, color='green', edgecolor='white', width=barWidth)
 
# Custom X axis
plt.xticks(r, names, fontweight='bold')
plt.xlabel("Word")
plt.ylabel("Frequency")
plt.xticks(rotation=90)
plt.title('Feedback')
plt.legend(["Score greater than or equal to six","Score less than or equal to five"])
 
# Show graphic
plt.show()







