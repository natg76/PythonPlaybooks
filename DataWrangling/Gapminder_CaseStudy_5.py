# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 13:27:16 2019 with Spyder

@author: Natarajan Ganapathi

About: Gapmider data - Case study for EDA & DC

"""

#%% 
# Data type Inconsistencies

import pandas as pd
import os

os.chdir('D:\\NG Data\\NG Learning Repository\\DataCamp\\DataScience in Python Series\\Data Cleansing in Python')
wd = os.getcwd()
os.listdir(wd)

#%%

gap = pd.read_csv('gapminder.csv')

print(gap.shape)

print(gap.head())


#%%
gap.info()

gap.columns

#%%

# Construnct a list to hold required column names

list_cols = list(range(1800,1900))
list_cols = list(map(str,list_cols))
# append Life expectancy to the end 
list_cols.append('Life expectancy')

#%%
list_cols.remove('Life expectancy')

#%%
# append Life expectancy to the end 
list_cols.insert(0, 'Life expectancy')

#%%

#%%

# construct the g1800s dataframe with required columns

g1800s = gap[list_cols]

#%%
# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Create the scatter plot
g1800s.plot(kind='scatter', x='1800', y='1899')

# Specify axis labels
plt.xlabel('Life Expectancy by Country in 1800')
plt.ylabel('Life Expectancy by Country in 1899')

# Specify axis limits
plt.xlim(20, 55)
plt.ylim(20, 55)

# Display the plot
plt.show()

#%%
# Write a function that takes a row as input and validate if the rest of the fields are numeric and > 0

def check_null_or_valid(row_data):
    """Function that takes a row of data,
    drops all missing values,
    and checks if all remaining values are greater than or equal to 0
    """
    no_na = row_data.dropna()
    numeric = pd.to_numeric(no_na)
    ge0 = numeric >= 0
    return ge0

#%%
# Check whether the first column is 'Life expectancy'
assert g1800s.columns[0] == 'Life expectancy'

#%%
# Check whether the values in the row are valid
assert g1800s.iloc[:, 1:].apply(check_null_or_valid, axis=1).all().all()

#%%
# Check that there is only one instance of each country
assert g1800s['Life expectancy'].value_counts()[0] == 1

#%% 

g1800s['Life expectancy'].isunique()

#%%

# Concatenate the DataFrames row-wise
gapminder = pd.concat([g1800s,g1900s,g2000s]) #axis = 0, row wise

# Print the shape of gapminder
print(gapminder.shape)

# Print the head of gapminder
print(gapminder.head())



#%%
import pandas as pd

# Melt gapminder: gapminder_melt
gapminder_melt = pd.melt(frame=gapminder, id_vars='Life expectancy')

# Rename the columns
gapminder_melt.columns = ['country', 'year', 'life_expectancy']

# Print the head of gapminder_melt
print(gapminder_melt.head())



#%%
# Convert the year column to numeric
gapminder.year = pd.to_numeric(gapminder.year)

# Test if country is of type object
assert gapminder.country.dtypes == np.object

# Test if year is of type int64
assert gapminder.year.dtypes == np.int64

# Test if life_expectancy is of type float64
assert gapminder.life_expectancy.dtypes == np.float64


#%%

# Create the series of countries: countries
countries = gapminder.country

# Drop all the duplicates from countries
countries = countries.drop_duplicates()

# Write the regular expression: pattern
pattern = '^[A-Za-z\.\s]*$'

# Create the Boolean vector: mask
## mask contains the boolean value 
mask = countries.str.contains(pattern)

# Invert the mask: mask_inverse
# Find the entries, that do not contain the pattern. So inverse.
mask_inverse = ~mask

# Subset countries using mask_inverse: invalid_countries
invalid_countries = countries.loc[mask_inverse]

# Print invalid_countries
print(invalid_countries)


#%%

# Assert that country does not contain any missing values
assert pd.notnull(gapminder.country).all()

# Assert that year does not contain any missing values
assert gapminder.year.notnull().all()

# Drop the missing values
# WARNING: applying dropna on a column gives strange results.
## gapminder = gapminder.life_expectancy.dropna()
gapminder = gapminder.dropna(subset=['life_expectancy'])

# Print the shape of gapminder
print(gapminder.shape)



#%%

# Assert that country does not contain any missing values
assert pd.notnull(gapminder.country).all()

# Assert that year does not contain any missing values
assert  pd.notnull(gapminder.year).all()

# Drop the missing values
# WARNING: applying dropna on a column gives strange results.
## gapminder = gapminder.life_expectancy.dropna()

# So do it right way.. dropna method to be used on Dataframe always 
gapminder = gapminder.dropna(subset=['life_expectancy'])

# Print the shape of gapminder
print(gapminder.shape)

#%%

# Add first subplot
plt.subplot(2, 1, 1) 
plt.show()

# Create a histogram of life_expectancy
gapminder.life_expectancy.plot(kind='hist', x='life_expectancy')
plt.show()

#gapminder.plot(kind='hist', x='life_expectancy')
plt.show()

# Group gapminder: gapminder_agg
gapminder_agg = gapminder.groupby('year')['life_expectancy'].mean()

#gapminder_agg is a not a DataFrame! it is a Pandas series object.

# Print the head of gapminder_agg
print(gapminder_agg.head())

# Print the tail of gapminder_agg
print(gapminder_agg.tail())

# Add second subplot
plt.subplot(2, 1, 2)

# Create a line plot of life expectancy per year
gapminder_agg.plot(kind='line', x='year', y='life_expectancy')

#gapminder_agg.life_expectancy.plot(kind='line', x='year', y='life_expectancy')

# Add title and specify axis labels
plt.title('Life expectancy over the years')
plt.ylabel('Life expectancy')
plt.xlabel('Year')

# Display the plots
plt.tight_layout()
plt.show()

#%%
# Save both DataFrames to csv files
gapminder.to_csv('gapminder.csv')
gapminder_agg.to_csv('gapminder_agg.csv')


#%%
