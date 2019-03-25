# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 18:58:53 2019 with Spyder

@author: Natarajan Ganapathi

About: Clustering Case Studies

1. Identifying dominant colours in images
2. 

"""

#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


#%%
import os
os.chdir('D:\\NG Data\\NG Learning Repository\\DataCamp\\DataScience in Python Series\\Clustering with SciPy')
wd = os.getcwd()
os.listdir(wd)

#%%

# Read about matplotlib.image.imread & matplotlib.pyplot.imshow

import matplotlib.image as img

batman_image = img.imread('batman_1.jpg')

batman_image.shape

#%%

# Store RGB values of all pixels in lists r, g and b
r = []
g = []
b = []

for row in batman_image:
    for temp_r, temp_g, temp_b in row:
        r.append(temp_r)
        g.append(temp_g)
        b.append(temp_b)


#%%

# Convert extracted data into a data frame

batman_df = pd.DataFrame({'red':r, 'green': g,  'blue': b})
#%%

#%%
from scipy.cluster.vq import kmeans
from scipy.cluster.vq import whiten


#%% Scale the variables

batman_df['scaled_red'] = whiten(batman_df.red)
batman_df['scaled_green'] = whiten(batman_df.green)
batman_df['scaled_blue'] = whiten(batman_df.blue)


#%%
distortions = []
num_clusters = range(1, 7)

# Create a list of distortions from the kmeans function
for i in num_clusters:
    cluster_centers, distortion = kmeans(batman_df[['scaled_red','scaled_green','scaled_blue']], i)
    distortions.append(distortion)

#%%
# Create a data frame with two lists, num_clusters and distortions
elbow_plot = pd.DataFrame({'num_clusters': num_clusters, 'distortions': distortions})

# Create a line plot of num_clusters and distortions
sns.lineplot(x='num_clusters', y='distortions', data = elbow_plot)
plt.xticks(num_clusters)
plt.show()

# You can see that there are only two distinct colours in the image. 
# The elbow chart also indicates that 2 is the optiaml no.

#%%

colors = []
# Get standard deviations of each color
r_std, g_std, b_std = batman_df[['red', 'green', 'blue']].std()

for cluster_center in cluster_centers:
    scaled_r, scaled_g, scaled_b = cluster_center
    # Convert each standardized value to scaled value
    colors.append((
        scaled_r * r_std / 255,
        scaled_g * g_std / 255,
        scaled_b * b_std / 255
    ))

#%%
# Display colors of cluster centers
plt.imshow([colors])
plt.show()

#%%


## Case Study 2: Document Clustering

# Import TfidfVectorizer class from sklearn
from sklearn.feature_extraction.text import TfidfVectorizer

#%%

from nltk.tokenize import word_tokenize
import re

#%%

stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
#%%

def remove_noise(text, stop_words = list(stop_words) ):
    tokens = word_tokenize(text)
    cleaned_tokens = []
    for token in tokens:
        token = re.sub('[^A-Za-z0-9]+', '', token)
        if len(token) > 1 and token.lower() not in stop_words:
# Get lowercase
            cleaned_tokens.append(token.lower())
    return cleaned_tokens

#%%


remove_noise("It is lovely weather we are having. I hope the weather continues.")

#%%

plots_df = pd.read_csv('movies_plot.csv')
plots_df.shape

#%% 

plots_df.info()
#%%

plots = list(plots_df.Plot)

#%%

# Initialize TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer(max_df = 0.75, min_df = 0.1, max_features=50, tokenizer = remove_noise )

#%%

# Use the .fit_transform() method on the list plots
tfidf_matrix = tfidf_vectorizer.fit_transform(plots)

#%%

num_clusters = 2

# Generate cluster centers through the kmeans function
cluster_centers, distortion = kmeans(tfidf_matrix.todense(), num_clusters)

#%%
# Generate terms from the tfidf_vectorizer object
terms = tfidf_vectorizer.get_feature_names()
terms

#%%
for i in range(num_clusters):
    # Sort the terms and print top 3 terms
    center_terms = dict(zip(terms, list(cluster_centers[i])))
    sorted_terms = sorted(center_terms, key=center_terms.get, reverse=True)
    print(sorted_terms[:3])
    
#%%

#%%


# FIFA Clustering based on Pace, Dribbles & Shoot





#%%

# Post Cluster Analysis
# Print the size of the clusters

print(fifa.groupby('cluster_labels')['ID'].count())

# print(fifa[['ID','cluster_labels']].groupby('cluster_labels').count())

# Print the mean value of wages in each cluster

print(fifa.groupby('cluster_labels')['eur_wage'].mean())

# print(fifa[['eur_wage','cluster_labels']].groupby('cluster_labels').mean())


#%%

features = ['pac', 'sho', 'pas', 'dri', 'def', 'phy']
scaled_features = ['scaled_pac', 'scaled_sho','scaled_pas', 'scaled_dri', 'scaled_def', 'scaled_phy']

#%%
# Cluster based on 6 Features: pac, sho, pas, dri, def, phy.

# Create centroids with kmeans for 2 clusters
cluster_centers,_ = kmeans(fifa[scaled_features], 2)

# cluster_centers,_ = kmeans(fifa[features], 2)
# Only float and double data types supported. Integers to be converted into double.
    
#%%

# Create centroids with kmeans for 2 clusters
cluster_centers,_ = kmeans(fifa[scaled_features], 2)

# Assign cluster labels and print cluster centers
fifa['cluster_labels'], _ = vq(fifa[scaled_features], cluster_centers)

print(fifa.groupby('cluster_labels')[scaled_features].mean())


#%%

# Plot cluster centers to visualize clusters
fifa.groupby('cluster_labels')[scaled_features].mean().plot(legend=True, kind='bar')
plt.show()

#%%

# Get the name column of top 5 players in each cluster
for cluster in fifa['cluster_labels'].unique():
    print(cluster, fifa[fifa['cluster_labels'] == cluster]['name'].values[:5])

#%%


