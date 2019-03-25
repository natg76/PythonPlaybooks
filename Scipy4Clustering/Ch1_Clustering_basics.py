# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 17:10:26 2019 with Spyder

@author: Natarajan Ganapathi

About: Basics of Clustering with Scipy 

"""

#%%
import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns
import os

os.chdir('D:\\NG Data\\NG Learning Repository\\DataCamp\\DataScience in Python Series\\Clustering with SciPy')
wd = os.getcwd()
os.listdir(wd)

#%%

fifa = pd.read_csv('fifa_18_sample_data.csv')

#%%


# Import plotting class from matplotlib library
from matplotlib import pyplot as plt

# Create a scatter plot
plt.scatter(x, y)

# Display the scatter plot
plt.show()



#%%
# Hierarchical clustering
# Import linkage and fcluster functions
from scipy.cluster.hierarchy import linkage, fcluster
import seaborn as sns
sns.set()
#%%
# Use the linkage() function to compute distance
Z = linkage(df, 'ward')

# Generate cluster labels
df['cluster_labels'] = fcluster(Z, 2, criterion='maxclust')
#%%

# Plot the points with seaborn
sns.scatterplot(x='x', y='y', hue='cluster_labels', data=df)
plt.show()


#%%
# K Means clustering

x = [9.0, 6.0, 2.0, 3.0, 1.0, 7.0, 1.0, 6.0, 1.0, 7.0, 23.0, 26.0, 25.0, 23.0, 21.0, 23.0, 23.0, 20.0, 30.0, 23.0]

y = [8.0, 4.0, 10.0, 6.0, 0.0, 4.0, 10.0, 10.0, 6.0, 1.0, 29.0, 25.0, 30.0, 29.0, 29.0, 30.0, 25.0, 27.0, 26.0, 30.0]

my_dict = {'x': x, 'y':y}

df = pd.DataFrame(my_dict)


#%%

# Import kmeans and vq functions
from scipy.cluster.vq import kmeans, vq

# Compute cluster centers
centroids,_ = kmeans(df, 2)

# Assign cluster labels
df['cluster_labels'], _ = vq(df, centroids)

# Plot the points with seaborn
sns.scatterplot(x='x', y='y', hue='cluster_labels', data=df)

plt.show()

#%%

# Normalization of data : Scale = x/sd 

# Import the whiten function
from scipy.cluster.vq import whiten

goals_for = [4,3,2,3,1,1,2,0,1,4]

# Use the whiten() function to standardize the data
scaled_data = whiten(goals_for)
print(scaled_data)

#%%

# Plot original data
plt.plot(goals_for, label='original')

# Plot scaled data
plt.plot(scaled_data, label='scaled')

# Show the legend in the plot
plt.legend()

# Display the plot
plt.show()

# The scaled values will still retain the trend. Variations are reduced through.

#%%

# What about for smaller values?

# Prepare data
rate_cuts = [0.0025, 0.001, -0.0005, -0.001, -0.0005, 0.0025, -0.001, -0.0015, -0.001, 0.0005]

# Use the whiten() function to standardize the data
scaled_data = whiten(rate_cuts)

# Plot original data
plt.plot(rate_cuts, label='original')

# Plot scaled data
plt.plot(scaled_data, label='scaled')

plt.legend()
plt.show()

#%%

#%%

fifa.head(10)
#%%

fifa1 = fifa[['ID', 'name','eur_wage','eur_value']]

#%%

fifa1.plot(x='eur_wage', y='eur_value', kind = 'scatter')
plt.show()

#%%
# Scale wage and value
fifa1['scaled_wage'] = whiten(fifa1['eur_wage'])
fifa1['scaled_value'] = whiten(fifa1['eur_value'])

#%%

#%%
# Plot the two columns in a scatter plot
fifa1.plot(x='scaled_wage', y='scaled_value', kind = 'scatter')
plt.show()

#%%

# Check mean and standard deviation of scaled values
print(fifa1[['eur_wage','scaled_wage', 'eur_value','scaled_value']].describe())

#%%
# Chapter 1 END
