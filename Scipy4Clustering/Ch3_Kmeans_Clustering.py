# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 14:15:06 2019 with Spyder

@author: Natarajan Ganapathi

About: K-Means Clustering with Scipy 

"""

#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

#%%

os.chdir('D:\\NG Data\\NG Learning Repository\\DataCamp\\DataScience in Python Series\\Clustering with SciPy')
wd = os.getcwd()
os.listdir(wd)

#%%

fifa = pd.read_csv('fifa_18_dataset.csv')
fifa.info()

#%%

comic_con = pd.read_csv('comic_con.csv')
comic_con.info()

#%%
from scipy.cluster.vq import whiten

x = [39, 42, 58, 43, 13, 32, 60, 13, 26, 27, 29, 51, 14, 50, 62, 59, 50, 62, 65, 17, 25, 45, 55, 48, 42, 58, 68, 58, 37, 55]
y = [3, 7, 3, 3, 6, 5, 3, 4, 0, 9, 6, 3, 0, 7, 4, 1, 3, 0, 2, 5, 9, 5, 8, 6, 3, 1, 4, 2, 8, 7]
x_scaled = whiten(x)
y_scaled = whiten(y)

my_dict = {'x': x, 'y':y, 'x_scaled': x_scaled, 'y_scaled': y_scaled}
uniform_data = pd.DataFrame(my_dict)

uniform_data.info()
#%%

uniform_data['x'].agg([np.mean, np.std, np.median])

#%%

uniform_data['x_scaled'].agg([np.mean, np.std, np.median])

#%%

np.std(y_scaled)

#%%

# Import the kmeans and vq functions
from scipy.cluster.vq import kmeans, vq

# Generate cluster centers
cluster_centers, distortion = kmeans(comic_con[['x_scaled', 'y_scaled']], 2)

#%%

print(cluster_centers)

#%% 

print(distortion)

#%%
# Assign cluster labels
comic_con['cluster_labels'], distortion_list = vq(comic_con[['x_scaled', 'y_scaled']], cluster_centers)

#%%

print(distortion_list)

#%%
print()
#%%

# Plot clusters
sns.scatterplot(x='x_scaled', y='y_scaled',hue='cluster_labels', data = comic_con)
plt.show()

#%%

 %timeit kmeans(comic_con[['x_scaled', 'y_scaled']], 2)
 
 #%%

# How many clusters?
# Determine by Elbow method

distortions = []
num_clusters = range(1, 7)

# Create a list of distortions from the kmeans function
for i in num_clusters:
    cluster_centers, distortion = kmeans(comic_con[['x_scaled','y_scaled']], i)
    distortions.append(distortion)

# Create a data frame with two lists - num_clusters, distortions
elbow_plot = pd.DataFrame({'num_clusters': num_clusters, 'distortions': distortions})

# Creat a line plot of num_clusters and distortions
sns.lineplot(x='num_clusters', y='distortions', data = elbow_plot)
plt.xticks(num_clusters)
plt.show()

#%%

# Elbow plot on a uniform data 

distortions = []
num_clusters = range(2, 7)

# Create a list of distortions from the kmeans function
for i in num_clusters:
    cluster_centers, distortion = kmeans(uniform_data[['x_scaled','y_scaled']], i)
    distortions.append(distortion)

# Create a data frame with two lists - number of clusters and distortions
elbow_plot = pd.DataFrame({'num_clusters': num_clusters, 'distortions': distortions})

# Creat a line plot of num_clusters and distortions
sns.lineplot(x='num_clusters', y='distortions', data = elbow_plot)
plt.xticks(num_clusters)
plt.show()

#%%

# Import random class
from numpy import random

# Initialize seed
random.seed(0)

# Run kmeans clustering
cluster_centers, distortion = kmeans(comic_con[['x_scaled', 'y_scaled']], 2)
comic_con['cluster_labels'], distortion_list = vq(comic_con[['x_scaled', 'y_scaled']], cluster_centers)

# Plot the scatterplot
sns.scatterplot(x='x_scaled', y='y_scaled', 
                hue='cluster_labels', data = comic_con)
plt.show()

#%%

# Import random class
from numpy import random


# Initialize seed
for lseed in [1,2,1000] :
    
    random.seed(lseed)

    # Run kmeans clustering
    cluster_centers, distortion = kmeans(comic_con[['x_scaled', 'y_scaled']], 2)
    comic_con['cluster_labels'], distortion_list = vq(comic_con[['x_scaled', 'y_scaled']], cluster_centers)
    
    print("Seed ", lseed)
    # Plot the scatterplot
    sns.scatterplot(x='x_scaled', y='y_scaled', 
                    hue='cluster_labels', data = comic_con)
    plt.show()

#%%

mouse = pd.read_csv('mouse.csv')
mouse.info()

#%%

mouse['x_scaled'] = whiten(mouse.x)
mouse['y_scaled'] = whiten(mouse.y)

#%%
# BIAS towards cluster size in K-Means
# Import the kmeans and vq functions

from scipy.cluster.vq import vq,kmeans

# Generate cluster centers
cluster_centers, distortion = kmeans(mouse[['x_scaled','y_scaled']], 3)

# Assign cluster labels
mouse['cluster_labels'], distortion_list = vq(mouse[['x_scaled','y_scaled']],cluster_centers)

# Plot clusters
sns.scatterplot(x='x_scaled', y='y_scaled', hue='cluster_labels', legend='false', data = mouse)
plt.show()


# Notice that kmeans is unable to capture the three visible clusters clearly, 
# and the two clusters towards the top have taken in some points along the boundary. 
# This happens due to the underlying assumption in kmeans algorithm to minimize 
# distortions which leads to clusters that are similar in terms of area.

#%%

# Set up a random seed in numpy
random.seed([1000,2000])

# Fit the data into a k-means algorithm
cluster_centers,_ = kmeans(fifa[['scaled_def', 'scaled_phy']], 3)

# Assign cluster labels
fifa['cluster_labels'], _ = vq(fifa[['scaled_def', 'scaled_phy']], cluster_centers)

# Display cluster centers 
print(fifa[['scaled_def', 'scaled_phy', 'cluster_labels']].groupby('cluster_labels').mean())

# Create a scatter plot through seaborn
sns.scatterplot(x='scaled_def', y='scaled_phy', hue='cluster_labels', data=fifa)
plt.show()


