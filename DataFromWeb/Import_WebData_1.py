# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 01:10:20 2019
@author: Natarajan Ganapathi

Data from Web - WebScrapping

urllib, beautifulsoup

"""


#%%

import os
wd = os.getcwd()
os.listdir(wd)

os.chdir('D:\\NG Data\\NG Learning Repository\\DataCamp\\DataScience in Python Series\\Importing Data into Python II')

#%%


# Import package
from urllib.request import urlretrieve

# Import pandas
import pandas as pd

# Assign url of file: url
url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

# Save file locally
urlretrieve(url, 'winequality-red.csv')

# Read file into a DataFrame and print its head
df = pd.read_csv('winequality-red.csv', sep=';')
print(df.head())
