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

import json

# Load JSON: json_data
with open("a_movie.json") as json_file:
    json_data = json.load(json_file)

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])
    
#%%

import json
with open("a_movie.json") as json_file:
    json_data = json.load(json_file)
    
for k in json_data.keys():
    print(k + ': ', json_data[k])
    

print(json_data.keys())
print(json_data["Year"])
print(json_data["Title"])

#%%

## APIs

# Import requests package
import requests

# Assign URL to variable: url
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=the+social+network'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Print the text of the response
print(r.text)

#%%
# Import package
import requests

# Assign URL to variable: url
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=social+network'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])

#%%
# Import package
import requests

# Assign URL to variable: url
url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print the Wikipedia page extract
pizza_extract = json_data['query']['pages']['24768']['extract']
print(pizza_extract)

#%%
