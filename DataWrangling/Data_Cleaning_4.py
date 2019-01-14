# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 08:32:50 2019 with Spyder

@author: Natarajan Ganapathi

About: Data Cleaning for Analysis - Field Level Cleaning

"""

#%% 
# Data type Inconsistencies

import pandas as pd
import os

os.chdir('D:\\NG Data\\NG Learning Repository\\DataCamp\\DataScience in Python Series\\Data Cleansing in Python')
wd = os.getcwd()
os.listdir(wd)

#%%

tips = pd.read_csv('tips.csv')

print(tips.shape)

print(tips.head())


#%%
tips.info()

"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 244 entries, 0 to 243
Data columns (total 7 columns):
total_bill    244 non-null float64
tip           244 non-null float64
sex           244 non-null object
smoker        244 non-null object
day           244 non-null object
time          244 non-null object
size          244 non-null int64
dtypes: float64(2), int64(1), object(4)
memory usage: 13.4+ KB

"""

#%%

# Convert the sex column to type 'category'
tips.sex = tips.sex.astype('category')

# Convert the smoker column to type 'category'
tips.smoker = tips.smoker.astype('category')

# Print the info of tips
print(tips.info())

"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 244 entries, 0 to 243
Data columns (total 7 columns):
total_bill    244 non-null float64
tip           244 non-null float64
sex           244 non-null category
smoker        244 non-null category
day           244 non-null object
time          244 non-null object
size          244 non-null int64
dtypes: category(2), float64(2), int64(1), object(2)
memory usage: 10.3+ KB
None
"""

#%%

# Convert 'total_bill' to a numeric dtype
tips['total_bill'] = pd.to_numeric(tips['total_bill'], errors='coerce')

# Convert 'tip' to a numeric dtype
tips['tip'] = pd.to_numeric(tips.tip,errors='coerce' )

# Print the info of tips
print(tips.info())

#%%

# Import the regular expression module
import re

# Compile the pattern: prog
prog = re.compile('^\d{3}-\d{3}-\d{4}$')

# See if the pattern matches
result = prog.match('123-456-7890')
print(bool(result))

# See if the pattern matches
result2 = prog.match('1123-456-7890')
print(bool(result2))


#%%

# Import the regular expression module
import re

# Find the numeric values: matches
matches = re.findall('\d+', 'the recipe calls for 10 strawberries and 1 banana')

# Print the matches
print(matches)

#%%

# Write the first pattern
pattern1 = bool(re.match(pattern='\d{3}-\d{3}-\d{3}', string='123-456-7890'))
print(pattern1)

# Write the second pattern
pattern2 = bool(re.match(pattern='\$\d*\.\d{2}', string='$123.45'))
print(pattern2)

# Write the third pattern
pattern3 = bool(re.match(pattern='[A-Z]\w*', string='Australia01'))
print(pattern3)

#%%

import numpy as np

# Define recode_gender()
def recode_gender(gender):

    # Return 0 if gender is 'Female'
    if gender == 'Female':
        return 0
    
    # Return 1 if gender is 'Male'    
    elif gender == 'Male':
        return 1
    
    # Return np.nan    
    else:
        return np.NaN

#%%
# Apply the function to the sex column
tips['recode'] = tips.sex.apply(recode_gender)


# Print the first five rows of tips
print(tips.head())


#%%

## Lambda Functions

# Write the lambda function using replace
tips['total_dollar_replace'] = tips.total_dollar.apply(lambda x: x.replace('$', ''))

# Write the lambda function using regular expressions
tips['total_dollar_re'] = tips.total_dollar.apply(lambda x: re.findall('\d+\.\d+', x)[0])

# Print the head of tips
print(tips.head())

#%%

# Create the new DataFrame: tracks
tracks = billboard[['year','artist', 'track','time']]

# Print info of tracks
print(tracks.info())

# Drop the duplicates: tracks_no_duplicates
tracks_no_duplicates = tracks.drop_duplicates()

# Print info of tracks
print(tracks_no_duplicates.info())


#%%

airquality = pd.read_csv('airquality.csv')

#%%

print(airquality.info())

# Calculate the mean of the Ozone column: oz_mean
oz_mean = airquality.Ozone.mean()

# Replace all the missing values in the Ozone column with the mean
airquality['Ozone'] = airquality['Ozone'].fillna(oz_mean)

# Print the info of airquality
print(airquality.info())

#%%

# Assert that there are no missing values
assert ebola.notnull().all().all()

# Assert that all values are >= 0
assert (ebola >= 0).all().all()


#%%
