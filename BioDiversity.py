#This goal of this project is to analyze biodiversity data from the National Parks Service, particularly around various species observed in different national park locations.
#This project will scope, analyze, prepare, plot data, and seek to explain the findings from the analysis.
#Here are a few questions that this project has sought to answer:

#- What is the distribution of conservation status for species?
#- Are certain types of species more likely to be endangered?
#- Are the differences between species and their conservation status significant?
#- Which animal is most prevalent and what is their distribution amongst parks?

#**Data sources:**

#Both `Observations.csv` and `Species_info.csv`

# Project Goals

#In this project the perspective will be through a biodiversity analyst for the National Parks Service. The National Park Service wants to ensure the survival of at-risk species, to maintain the level of biodiversity within their parks. Therefore, the main objectives as an analyst will be understanding characteristics about the species and their conservations status, and those species and their relationship to the national parks. Some questions that are posed:

#- What is the distribution of conservation status for species?
#- Are certain types of species more likely to be endangered?
#- Are the differences between species and their conservation status significant?
#- Which animal is most prevalent and what is their distribution amongst parks?

# Data

#This project has two data sets that came with the package. The first `csv` file has information about each species and another has observations of species with park locations. This data will be used to analyze the goals of the project. 

# Analysis

#In this section, descriptive statistics and data visualization techniques will be employed to understand the data better. Statistical inference will also be used to test if the observed values are statistically significant. Some of the key metrics that will be computed include: 

#1. Distributions
#2. counts
#3. relationship between species
#4. conservation status of species
#5. observations of species in parks. 

#import modules
import pandas as pd
import numpy as np

from matplotlib import pyplot as plt
import seaborn as sns

%matplotlib inline

#loading up data
species = pd.read_csv('species_info.csv',encoding='utf-8')
species.head()
observations = pd.read_csv('observations.csv', encoding='utf-8')
observations.head()

#exploring datasets
print(f"species shape: {species.shape}")
print(f"observations shape: {observations.shape}")
print(f"number of species:{species.scientific_name.nunique()}")
print(f"nnumber of categories:{species.category.nunique()}")
print(f"categories:{species.category.unique()}")
species.groupby("category").size()
print(f"number of conservation statuses:{species.conservation_status.nunique()}")
print(f"unique conservation statuses:{species.conservation_status.unique()}")
print(f"na values:{species.conservation_status.isna().sum()}")
print(species.groupby("conservation_status").size())
print(f"number of parks:{observations.park_name.nunique()}")
print(f"unique parks:{observations.park_name.unique()}")
print(f"number of observations:{observations.observations.sum()}")

#analysis
species.fillna('No Intervention', inplace=True)
species.groupby("conservation_status").size()
conservationCategory = species[species.conservation_status != "No Intervention"]\
    .groupby(["conservation_status", "category"])['scientific_name']\
    .count()\
    .unstack()
conservationCategory

ax = conservationCategory.plot(kind = 'bar', figsize=(8,6), 
                               stacked=True)
ax.set_xlabel("Conservation Status")

species['is_protected'] = species.conservation_status != 'No Intervention'
category_counts = species.groupby(['category', 'is_protected'])\
                        .scientific_name.nunique()\
                        .reset_index()\
                        .pivot(columns='is_protected',
                                      index='category',
                                      values='scientific_name')\
                        .reset_index()
category_counts.columns = ['category', 'not_protected', 'protected']

category_counts

category_counts['percent_protected'] = category_counts.protected / \
                                      (category_counts.protected + category_counts.not_protected) * 100

category_counts

#determine statistical signifcance
ax.set_ylabel("Number of Species");

from scipy.stats import chi2_contingency

contingency1 = [[30, 146],
              [75, 413]]
chi2_contingency(contingency1)

contingency2 = [[30, 146],
               [5, 73]]
chi2_contingency(contingency2)

#species in parks
from itertools import chain
import string

def remove_punctuations(text):
    for punctuation in string.punctuation:
        text = text.replace(punctuation, '')
    return text

common_Names = species[species.category == "Mammal"]\
    .common_names\
    .apply(remove_punctuations)\
    .str.split().tolist()

common_Names[:6]

cleanRows = []

for item in common_Names:
    item = list(dict.fromkeys(item))
    cleanRows.append(item)
    
cleanRows[:6]

res = list(chain.from_iterable(i if isinstance(i, list) else [i] for i in cleanRows))
res[:6]

words_counted = []

for i in res:
    x = res.count(i)
    words_counted.append((i,x))

pd.DataFrame(set(words_counted), columns =['Word', 'Count']).sort_values("Count", ascending = False).head(10)

species['is_bat'] = species.common_names.str.contains(r"\bBat\b", regex = True)

species.head(10)
species[species.is_bat]
bat_observations = observations.merge(species[species.is_bat])
bat_observations
bat_observations.groupby('park_name').observations.sum().reset_index()
obs_by_park = bat_observations.groupby(['park_name', 'is_protected']).observations.sum().reset_index()
obs_by_park
plt.figure(figsize=(16, 4))
sns.barplot(x=obs_by_park.park_name, y= obs_by_park.observations, hue=obs_by_park.is_protected)
plt.xlabel('National Parks')
plt.ylabel('Number of Observations')
plt.title('Observations of Bats per Week')
plt.show()

#Conclusions
#The project was able to make several data visualizations and inferences about the various species in four of the National Parks that comprised this data set.
#This project was also able to answer some of the questions first posed in the beginning:

#- What is the distribution of conservation status for species?
#    - The vast majority of species were not part of conservation.(5,633 vs 191)
#- Are certain types of species more likely to be endangered?
#    - Mammals and Birds had the highest percentage of being in protection.
#- Are the differences between species and their conservation status significant?
#    - While mammals and Birds did not have significant difference in conservation percentage, mammals and reptiles exhibited a statistically significant difference.
#- Which animal is most prevalent and what is their distribution amongst parks?
#    - the study found that bats occurred the most number of times and they were most likely to be found in Yellowstone National Park.
