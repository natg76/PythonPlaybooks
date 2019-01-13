"""
Created on Wed Jan  9 01:10:20 2019
@author: Natarajan Ganapathi

Data Cleaning in Python 1

#pandas

"""

#%%

# Import pandas
import pandas as pd

# Read the file into a DataFrame: df
df = pd.read_csv('dob_job_application_filings_subset.csv')

# Print the head of df
print(df.head())

# Print the tail of df
print(df.tail())

# Print the shape of df
print(df.shape)

# Print the columns of df
print(df.columns)


"""
df_subset is a subset of main data frame with following columns

## Index(['Job #', 'Doc #', 'Borough', 'Initial Cost', 'Total Est. Fee',
       'Existing Zoning Sqft', 'Proposed Zoning Sqft',
       'Enlargement SQ Footage', 'Street Frontage', 'ExistingNo. of Stories',
       'Proposed No. of Stories', 'Existing Height', 'Proposed Height'],
      dtype='object')
"""

# Print the head and tail of df_subset
print(df_subset.head())
print(df_subset.tail())


#%%

# Print the info of df
print(df.info())

# Print the info of df_subset
print(df_subset.info())

df.describe()

df["Street Frontage"].describe()

dfcolname.describe()

#%%

# Print the value counts for 'Borough'
print(df['Borough'].value_counts(dropna=False))

# Print the value_counts for 'State'
print(df.State.value_counts(dropna=False))

# Print the value counts for 'Site Fill'
print(df["Site Fill"].value_counts(dropna = False))

#%%

# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Describe the column
df['Existing Zoning Sqft'].describe()

# Plot the histogram
df['Existing Zoning Sqft'].plot(kind='hist', rot=70, logx=True, logy=True)

# Display the histogram
plt.show()


#%%
# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt

# Create the boxplot
_ = df.boxplot(column='initial_cost', by='Borough', rot=90)

# Display the plot
plt.show()


#%%
# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt

# Create and display the first scatter plot
df.plot(kind='scatter', x='initial_cost', y='total_est_fee', rot=70)
plt.show()

# Create and display the second scatter plot
df_subset.plot(kind='scatter', x='initial_cost', y='total_est_fee', rot=70)

plt.show()
plt.show()

#%%

# Print the head of airquality
print(airquality.head())

# Melt airquality: airquality_melt
airquality_melt = pd.melt(airquality, id_vars=['Month', 'Day'], value_vars=['Ozone','Solar.R','Wind', 'Temp'])

# Print the head of airquality_melt
print(airquality_melt.head())




