#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue july  7 09:42:24 2018

@author: hassan
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder,LabelEncoder,Imputer,StandardScaler
import seaborn as sn
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression
from pandas import ExcelWriter
from pandas import ExcelFile


a = np.array([1,2,3])

data = pd.read_csv("houses_data.csv")
x_var = data.iloc[:,1:]
y_var = data.iloc[:,0]
columns = data.columns.values
print(x_var)


wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters = i,init = 'k-means++', max_iter = 1000, n_init = 11,random_state=0)
    kmeans.fit(data)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
plt.xlabel('Number of Clusters')
plt.ylabel('Score')
plt.title('Elbow Curve')
plt.show()

from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import pylab as pl
d = StandardScaler().fit_transform(data)
pca = PCA(n_components=2).fit(d)
pca_2d = pca.transform(d.data)
pl.figure('Reference Plot')
pl.scatter(pca_2d[:, 0], pca_2d[:, 1], c='y')
plt.savefig('before.png')
kmeans = KMeans(n_clusters=3, random_state=111)
kmeans.fit(d.data)
pl.figure('K-means with 3 clusters')
pl.scatter(pca_2d[:, 0], pca_2d[:, 1],s=50,marker='.',c=kmeans.labels_)
pl.show()


from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import pylab as pl
d = StandardScaler().fit_transform(data)
pca = PCA(n_components=2).fit(d)
pca_2d = pca.transform(d.data)
pl.figure('Reference Plot')
pl.scatter(pca_2d[:, 0], pca_2d[:, 1], c='y')
plt.savefig('before.png')
kmeans = KMeans(n_clusters=3, random_state=111)
kmeans.fit(d.data)
pl.figure('K-means with 3 clusters')
pl.scatter(pca_2d[:, 0], pca_2d[:, 1],s=50,marker='.',c=kmeans.labels_)
pl.show()

