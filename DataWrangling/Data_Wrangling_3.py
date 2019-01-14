# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 19:00:39 2019 with Spyder

@author: Natarajan Ganapathi

About: Data Wrangling - Dataframe Concat/Merge

"""

#%%
import pandas as pd
import os

os.chdir('D:\\NG Data\\NG Learning Repository\\DataCamp\\DataScience in Python Series\\Data Cleansing in Python')
wd = os.getcwd()
os.listdir(wd)

#%%

uber = pd.read_csv('nyc_uber_2014.csv')

uber.shape
uber.info()
uber.describe()

#%%

airquality(axis=0)

#%%


#%%
import pandas as pd

df1 = pd.DataFrame({"x":[1, 2, 3, 4, 5], 
                    "y":[3, 4, 5, 6, 7]}, 
                   index=['a', 'b', 'c', 'd', 'e'])


df2 = pd.DataFrame({"y":[1, 3, 5, 7, 9], 
                    "z":[9, 8, 7, 6, 5]}, 
                   index=['b', 'c', 'd', 'e', 'f'])

#%%

# AXIS = 0 or 1? 

# axis = 0 is an operation along the rows. When used with concat, it performs a UNION ALL
# axis = 1 is an operation along the columns, when used with concat, it performs a JOIN 

df3 = pd.concat([df1, df2], join='inner') # by default axis=0

df4 = pd.concat([df1, df2], join='outer') # by default axis=0

df5 = pd.concat([df1, df2], join='inner', axis=1)  #Axix = 1 performs a JOIN, by default on INDEX field

#%%

df3.head()

#%%

# Concatenate ebola_melt and status_country column-wise: ebola_tidy
ebola_tidy = pd.concat([ebola_melt, status_country], axis=1)

# Print the shape of ebola_tidy
print(ebola_tidy.shape)

# Print the head of ebola_tidy
print(ebola_tidy.head())

#%%

# Globbing - File name pattern matching

# Import necessary modules
import glob
import pandas as pd

# Write the pattern: pattern
pattern = '*.csv'
# pattern1 = 'uber_raw_data_????_??.csv'
# pattern2 = 'uber_raw_data_2018_??.csv'

# Save all file matches: csv_files
csv_files = glob.glob(pattern)

# Print the file names
print(csv_files)

# Load the second file into a DataFrame: csv2
csv2 = pd.read_csv(csv_files[1])

# Print the head of csv2
print(csv2.head())

#%%

# Create an empty list: frames
frames = []

#  Iterate over csv_files
for csv in csv_files:

    #  Read csv into a DataFrame: df
    df = pd.read_csv(csv)
    
    # Append df to frames
    frames.append(df)

# Concatenate frames into a single DataFrame: uber
# What is axis=? here
uber = pd.concat(frames)

# Print the shape of uber
print(uber.shape)

# Print the head of uber
print(uber.head())

#%%

## How to do more versatile joins?LOJ, ROJ, FOJ etc
## What if the join need to use custom join condition aka non-index field
## What if the column names are different?

## Introducing pandas Merge 

# Merge the DataFrames: o2o
o2o = pd.merge(left=site, right=visited, left_on='name', right_on='site')

# Print o2o
print(o2o)


#%%

# Merge the DataFrames: m2o
m2o = pd.merge(left=site, right=visited, left_on='name', right_on='site')

# Print m2o
print(m2o)


#%%

# Merge site and visited: m2m
m2m = pd.merge(left=site, right=visited, left_on='name', right_on='site')

# Merge m2m and survey: m2m
m2m = pd.merge(left=m2m, right=survey, left_on='ident', right_on='taken')

# Print the first 20 lines of m2m
print(m2m.head(20))

#%%

