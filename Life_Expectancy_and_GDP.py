#For this project, you will analyze data on GDP and life expectancy from the World Health Organization and the World Bank to try and identify the relationship between the GDP and life expectancy of six countries.
#During this project, you will analyze, prepare, and plot data in order to answer questions in a meaningful way.
#After you perform your analysis, you’ll be creating a blog post to share your findings on the World Health Organization website.
#Project Objectives:
#-Complete a project to add to your portfolio
#-Use seaborn and Matplotlib to create visualizations
#-Become familiar with presenting and sharing data visualizations
#-Preprocess, explore, and analyze data
#Prerequisites:
#-Data Acquisition
#-Data Visualization
#-Hypothesis Testing
#-Summarizing Quantitative Data
#-Data Wrangling and Tidying
#-Data Manipulation with Pandas

#import packages
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
%matplotlib inline

#loading the data
df = pd.read_csv("life_exp_gdp_data.csv")
df.head()

#exploring the data
print(df.Country.unique())
print(df.Year.unique())

#cleaning the data
df = df.rename({"Life expectancy at birth (years)":"LEABY"}, axis = "columns")
df.head()

#exploratory plots
plt.figure(figsize=(8,6))
sns.distplot(df.GDP, rug = True, kde=False)
plt.xlabel("GDP in Trillions of U.S. Dollars");

plt.figure(figsize=(8,6))
sns.distplot(df.LEABY, rug = True, kde=False)
plt.xlabel("Life expectancy at birth (years)");

dfMeans = df.drop("Year", axis = 1).groupby("Country").mean().reset_index()
dfMeans

plt.figure(figsize=(8,6))
sns.barplot(x="LEABY", y="Country", data=dfMeans)
plt.xlabel("Life expectancy at birth (years)");

plt.figure(figsize=(8,6))
sns.barplot(x="GDP", y="Country", data=dfMeans)
plt.xlabel("GDP in Trillions of U.S. Dollars");

#violin plots
fig, axes = plt.subplots(1, 2, sharey=True, figsize=(15, 5))
axes[0] = sns.violinplot(ax=axes[0], x=df.GDP, y=df.Country)
axes[0].set_xlabel("GDP in Trillions of U.S. Dollars")
axes[1] = sns.violinplot(ax=axes[1], x=df.LEABY, y=df.Country)
axes[1].set_xlabel("Life expectancy at birth (years)");

#swarm plots
fig, axes = plt.subplots(1, 2, sharey=True, figsize=(15, 5))
axes[0] = sns.swarmplot(ax=axes[0], x=df.GDP, y=df.Country)
axes[0].set_xlabel("GDP in Trillions of U.S. Dollars")
axes[1] = sns.swarmplot(ax=axes[1], x=df.LEABY, y=df.Country)
axes[1].set_xlabel("Life expectancy at birth (years)");

fig, axes = plt.subplots(1, 2, sharey=True, figsize=(15, 5))
axes[0] = sns.violinplot(ax=axes[0], x=df.GDP, y=df.Country,color = "black")
axes[0] = sns.swarmplot(ax=axes[0], x=df.GDP, y=df.Country)
axes[0].set_xlabel("GDP in Trillions of U.S. Dollars")
axes[1] = sns.violinplot(ax=axes[1], x=df.LEABY, y=df.Country, color = "black")
axes[1] = sns.swarmplot(ax=axes[1], x=df.LEABY, y=df.Country)
axes[1].set_xlabel("Life expectancy at birth (years)");

#line charts
plt.figure(figsize=(8,6))
sns.lineplot(x=df.Year, y=df.GDP, hue=df.Country)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol=1)
plt.ylabel("GDP in Trillions of U.S. Dollars");

graphGDP = sns.FacetGrid(df, col="Country", col_wrap=3,
                      hue = "Country", sharey = False)

graphGDP = (graphGDP.map(sns.lineplot,"Year","GDP")
         .add_legend()
         .set_axis_labels("Year","GDP in Trillions of U.S. Dollars"))

graphGDP;

plt.figure(figsize=(8,6))
sns.lineplot(x=df.Year, y=df.LEABY, hue=df.Country)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol=1)
plt.ylabel("Life expectancy at birth (years)");

graphLEABY = sns.FacetGrid(df, col="Country", col_wrap=3,
                      hue = "Country", sharey = False)

graphLEABY = (graphLEABY.map(sns.lineplot,"Year","LEABY")
         .add_legend()
         .set_axis_labels("Year","Life expectancy at birth (years)"))

graphLEABY;

#scatterplots
sns.scatterplot(x=df.LEABY, y=df.GDP, hue=df.Country).legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol=1);

graph = sns.FacetGrid(df, col="Country", col_wrap=3,
                      hue = "Country", sharey = False, sharex = False)
graph = (graph.map(sns.scatterplot,"LEABY", "GDP")
         .add_legend()
         .set_axis_labels("Life expectancy at birth (years)", "GDP in Trillions of U.S. Dollars"));


#Conclusions
#This project was able to make quite a few data visualizations with the data even though there were only 96 rows and 4 columns. 

#The project was also able to answer some of the questions posed in the beginning:

#- Has life expectancy increased over time in the six nations?
#    - Yes with Zimbabwe having the greatest increase.
#- Has GDP increased over time in the six nations?
#    - GDP has also increased for all countries in our list, especially for China.
#- Is there a correlation between GDP and life expectancy of a country?
#    - Yes there is a positive correlation between GDP and life expectancy for countries in our list.
#- What is the average life expectancy in these nations?
#    - Average life expectancy was between mid to high 70s for the countries except for Zimbabwe which was 50.
#- What is the distribution of that life expectancy?
#    - the life expectancy had a left skew, or most of the observations were on the right side.
