#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 22:40:02 2018

@author: hassan
"""

from modules import *
from connection import Connection
import time as Time
con = Connection(); 
data = con.get_data();
data = data.iloc[:,1:]
import os
print("---------------------------KMeans clustering algorithm-----------------\n")
print("\t\t\t 1. To find optimal number of clusters.\n")
print("\t\t\t 2. Kmeans clustering without PCA and feature scaling.\n")
print("\t\t\t 3. Kmeans clustering with PCA and feature scaling.\n")
print("\t\t\t 4. press any other to exit.\n")

os.system('clear')
choice = int(input("Enter your choice\t: "));

if choice == 1:
    x = data
    wcss = []
    for i in range(1,11):
        kmeans = KMeans(n_clusters = i,init = 'k-means++', max_iter = 2000, n_init = 11,random_state=0)
        kmeans.fit(x)
        wcss.append(kmeans.inertia_)
    plt.plot(range(1,11),wcss)
    plt.xlabel('Number of Clusters')
    plt.ylabel('Score')
    plt.title('Elbow Curve')
    plt.show()

        
        
    
elif choice == 2:
    kmeans = KMeans(n_clusters = 3,init = 'k-means++', max_iter = 400, n_init = 10,random_state=0)
    y_kmeans = kmeans.fit_predict(data)
    x = np.array(data)
    kmeans.fit_predict(x)
    plt.plot(x[y_kmeans == 0,0],x[y_kmeans == 0,1], marker="x", c='r',label="cluster1")
    plt.plot(x[y_kmeans == 1,0],x[y_kmeans == 1,1],  marker="*",c='b',label="cluster2")
    plt.plot(x[y_kmeans == 2,0],x[y_kmeans == 2,1], marker="*",c='black',label="cluster3")
    
    plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,2],c='y',label="centroids")
    plt.xlabel("square feet")
    plt.ylabel("price")
    plt.legend()
    plt.show()
    print("2001 data are clustered into 3 clusters using unsupervised K-means algorithm ")
    
elif choice == 3:
    print("\n")
    print("\t\t Before clustering")
    print("--------------------------------------------------")
    start_time = Time.time()
    #time = time.time()
    d = StandardScaler().fit_transform(data)
    pca = PCA(n_components=2).fit(d)
    pca_2d = pca.transform(d.data)
    
    
    pl.figure("Before clustering")
    pl.scatter(pca_2d[:, 0], pca_2d[:, 1],s=50,marker='*',c='b')
    pl.figure('Reference Plot')
    plt.savefig('before.png')
    pl.show()
    
    print("\n\t Kmeans is clustering the data......")
    kmeans = KMeans(n_clusters=3, random_state=111)
    kmeans.fit(d.data)
  
    
    for i in range(0, pca_2d.shape[0]):
        if kmeans.labels_[i] == 1:
            c1 = pl.scatter(pca_2d[i,0],pca_2d[i,1],c='r',
            marker='+')
        elif kmeans.labels_[i] == 0:
            c2 = pl.scatter(pca_2d[i,0],pca_2d[i,1],c='g',
            marker='*')
        elif kmeans.labels_[i] == 2:
            c3 = pl.scatter(pca_2d[i,0],pca_2d[i,1],c='b',
            marker='.')   
    pl.legend([c1, c2, c3],['Cluster 0', 'Cluster 2','Cluster 1'])
    pl.title('K-means clustered the 20001 observations  into 3 clusters')
    plt.savefig('clusering.png')
    pl.show()

    clustered_data = data
    clustered_data.drop(['cluster'],axis=1)
    clustered_data['cluster'] = kmeans.labels_;
    
    
    print("Kmeans clustered 2001 Real estate data  \n ")
    m = Time.time()-start_time
    print("in {0} ms".format(m))
    #print(m)
    import sqlite3 
    from sqlalchemy import create_engine
    engine = create_engine('sqlite:///:memory')
    con = sqlite3.connect('house.db')
    cur = con.cursor();
    clustered_data.to_sql("clustered_data", con, if_exists="replace")
    print("\n")
    print("The clustered data has been persisted to the database in a table clustered_data")
    
else:
    print("\n\t     Invalid choice!")


