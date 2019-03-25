# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 11:53:13 2019 with Spyder

@author: Natarajan Ganapathi

About: Hierarchical Clustering with Scipy 

"""

#%%
import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt
import os

#%%

os.chdir('D:\\NG Data\\NG Learning Repository\\DataCamp\\DataScience in Python Series\\Clustering with SciPy')
wd = os.getcwd()
os.listdir(wd)

#%%

fifa = pd.read_csv('fifa_18_sample_data.csv')

#%%
from scipy.cluster.vq import whiten

#%%

x = [17, 20, 35, 14, 37, 33, 14, 30, 35, 17, 11, 21, 13, 10, 81, 84, 87, 83, 90, 97, 94, 88, 89, 93, 92, 82, 81, 92, 91, 22, 23, 25, 25, 27, 17, 17]
y = [4, 6, 0, 0, 4, 3, 1, 6, 5, 4, 6, 10, 8, 10, 97, 94, 99, 95, 95, 97, 99, 99, 94, 99, 90, 98, 100, 93, 98, 15, 10, 0, 10, 7, 17, 15]
x_scaled = whiten(x)
y_scaled = whiten(y)
my_dict = {'x_coordinate': x, 'y_coordinate': y,  'x_scaled': x_scaled, 'y_scaled': y_scaled }
comic_con = pd.DataFrame(my_dict)
comic_con.to_csv('comic_con.csv')

#%%

# Import the fcluster and linkage functions
from scipy.cluster.hierarchy import fcluster, linkage

# Use the linkage() function
distance_matrix = linkage(comic_con[['x_scaled', 'y_scaled']], method = 'ward', metric = 'euclidean')

# Assign cluster labels
comic_con['cluster_labels'] = fcluster(distance_matrix, 2, criterion='maxclust')

#%%

import seaborn as sns
# Plot clusters
sns.scatterplot(x='x_scaled', y='y_scaled', 
                hue='cluster_labels', legend="full", data = comic_con)
plt.show()

#%%

# Import the fcluster and linkage functions
from scipy.cluster.hierarchy import linkage, fcluster

# Use the linkage() function
distance_matrix = linkage(comic_con[['x_scaled', 'y_scaled']], method = 'single', metric = 'euclidean')

# Assign cluster labels
comic_con['cluster_labels'] = fcluster(distance_matrix, 2, criterion="maxclust")

# Plot clusters
sns.scatterplot(x='x_scaled', y='y_scaled', 
                hue='cluster_labels', legend = "full", data = comic_con)
plt.show()

## No difference to the clusters formed using Ward method cpm

#%% 

# Import the fcluster and linkage functions
from scipy.cluster.hierarchy import linkage, fcluster

# Use the linkage() function
distance_matrix = linkage(comic_con[['x_scaled','y_scaled']], method = 'complete', metric = 'euclidean')

# Assign cluster labels
comic_con['cluster_labels'] = fcluster(distance_matrix, 2, criterion = 'maxclust')

# Plot clusters
sns.scatterplot(x='x_scaled', y='y_scaled', 
                hue='cluster_labels', data = comic_con)
plt.show()

# Again No difference with COmplete method as wwll

#%%

# Import the pyplot class
from matplotlib import pyplot as plt

# Define a colors dictionary for clusters
colors = {1:'red', 2:'blue'}

#%%
# Plot a scatter plot
comic_con.plot.scatter(x = 'x_scaled', y = 'y_scaled',
                	   c = comic_con['cluster_labels'].apply(lambda x: colors[x]))

plt.legend()
plt.show()

#%% 

# Import the seaborn module
import seaborn as sns

# Plot a scatter plot using seaborn
sns.scatterplot(x='x_scaled', 
                y='y_scaled', 
                hue='cluster_labels', 
                data = comic_con)
plt.show()


#%%

# Import the dendrogram function
from scipy.cluster.hierarchy import dendrogram

# Create a dendrogram
dn = dendrogram(distance_matrix)

# Display the dendogram
plt.show()

#%%

# Timeit - to measure the time that will be taken to execute

 %timeit linkage(comic_con[['x_scaled', 'y_scaled']], method = 'ward', metric='euclidean')
 
 #%%
 
fifa = pd.read_csv('fifa_18_dataset.csv')

#%%

fifa['scaled_sliding_tackle'] = whiten(fifa['sliding_tackle'])

fifa['scaled_aggression'] = whiten(fifa['aggression'])
 
 #%%
 
 # Fit the data into a hierarchical clustering algorithm
distance_matrix = linkage(fifa[['scaled_sliding_tackle', 'scaled_aggression']], 'ward')

# Assign cluster labels to each row of data
fifa['cluster_labels'] = fcluster(distance_matrix, 3, criterion='maxclust')

# Display cluster centers of each cluster
print(fifa[['scaled_sliding_tackle', 'scaled_aggression', 'cluster_labels']].groupby('cluster_labels').mean())

#%%
# Create a scatter plot through seaborn
sns.scatterplot(x='scaled_sliding_tackle', y='scaled_aggression', hue='cluster_labels', legend = "full",data=fifa)
plt.show()

#%%

