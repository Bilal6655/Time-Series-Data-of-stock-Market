import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
dataset = pd.read_csv("index.csv.csv")



dataset.head(10)

dataset.describe()

plt.hist(x = dataset.spx)
dataset.spx.plot(figsize=(20,5), title = 'spx VS ftse')
dataset.ftse.plot(figsize=(20,5), title = 'spx VS ftse')

# plotting QQ plot to check the distribution of the data

import scipy.stats
import pylab


scipy.stats.probplot(dataset.spx, plot = pylab)

# converting date column into date time


dataset.head()

dataset.date = pd.to_datetime(dataset.date , dayfirst= True)

dataset.date.describe()

# convert date column to index of dataset


dataset.set_index('date', inplace = True)

dataset.head()

# setting frequincy of data



dataset = dataset.asfreq('b')

dataset.head()




# filling missing values

dataset.isnull().sum()

dataset.spx=dataset.spx.fillna(method = 'ffill')
dataset.dax=dataset.dax.fillna(method = 'bfill')

dataset.ftse = dataset.ftse.fillna(dataset.ftse.mean())

dataset.nikkei = dataset.nikkei.fillna(dataset.nikkei.mean())


# simplifing data for univariate analysis

dataset['Market_Values'] = dataset.spx

dataset.head()
del dataset['nikkei'] ,dataset['ftse'] ,dataset['dax'] 

dataset

# splitting data into train and test

size = int(len(dataset))

train = dataset.iloc[:int(len(dataset)*0.8)]
test = dataset.iloc[int(len(dataset)*0.8):]

train.tail()
test.head()


