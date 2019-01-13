# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 11:58:45 2019 with Spyder

@author: Natarajan Ganapathi

About: Data Cleaning in Python 1

Details: Pandas data transformation functions

"""

#%%
import pandas as pd
import os

os.chdir('D:\\NG Data\\NG Learning Repository\\DataCamp\\DataScience in Python Series\\Data Cleansing in Python')
wd = os.getcwd()
os.listdir(wd)

airquality = pd.read_csv('airquality.csv')

#%%

# Print the head of airquality
print(airquality.head())

# Melt airquality: airquality_melt
airquality_melt = pd.melt(airquality, id_vars=['Month', 'Day'], value_vars=['Ozone','Solar.R','Wind', 'Temp'])

# Print the head of airquality_melt
print(airquality_melt.head())

#%%

# Print the head of airquality
print(airquality.head())

# Melt airquality: airquality_melt
airquality_melt = pd.melt(airquality, id_vars=['Month', 'Day'], var_name='measurement', value_name='reading')

# Print the head of airquality_melt
print(airquality_melt.head())

#%%

# Print the head of airquality_melt
print(airquality_melt.head())

# Pivot airquality_melt: airquality_pivot
airquality_pivot = airquality_melt.pivot_table(index=['Month', 'Day'], columns='measurement', values='reading')

# Call the function
airquality_pivot = pd.pivot_table(data=airquality_melt, index=['Month', 'Day'], columns='measurement', values='reading')

# Print the head of airquality_pivot
print(airquality_pivot.head())

#%%

# Print the index of airquality_pivot
print(airquality_pivot.index)

# Reset the index of airquality_pivot: airquality_pivot_reset
airquality_pivot_reset = airquality_pivot.reset_index()

# Print the new index of airquality_pivot_reset
print(airquality_pivot_reset.index)

airquality_pivot_reset.head()

print(airquality_pivot.head())
#%%

## handling duplicate values

# Pivot table the airquality_dup: airquality_pivot
airquality_pivot = airquality_dup.pivot_table(index=['Month', 'Day'], columns='measurement', values='reading', aggfunc=np.mean)

# Print the head of airquality_pivot before reset_index
print(airquality_pivot.head())

# Reset the index of airquality_pivot
airquality_pivot = airquality_pivot.reset_index()

# Print the head of airquality_pivot
print(airquality_pivot.head())

# Print the head of airquality
print(airquality.head())

#%%

## TB dataset

tb = pd.read_csv('tb.csv')

# Call melt function as method on tb dataframe

tb_melt = tb.melt(id_vars = ['country', 'year'])

#%%

tb_melt.info()
tb_melt.head()

# Split the variable into Gender & Age Group

tb_melt['gender'] = tb_melt.variable.str[0]

# tb_melt.age_group = tb_melt.variable.str[1:]

tb_melt['age_group'] = tb_melt.variable.str[1:]

# Check the new variables created.
tb_melt.head()

#%%

ebola = pd.read_csv('ebola.csv')

ebola_melt = pd.melt(frame=ebola, id_vars=['Date', 'Day'], 
                     var_name='type_country', value_name='counts')



#%%

# Create astring split column which contains a list of two strings.

ebola_melt['str_split'] = ebola_melt.type_country.str.split('_')

#%%

# Create the 'type' column
ebola_melt['type'] = ebola_melt.str_split.str.get(0)

# Create the 'country' column
ebola_melt['country'] = ebola_melt.str_split.str.get(1)

# Print the head of ebola_melt
print(ebola_melt.head())

#%%

