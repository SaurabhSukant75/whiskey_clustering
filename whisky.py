# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 17:06:50 2018

@author: saurabhsukant75
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster.bicluster import SpectralCoclustering
#reading of file using pandas data frame
df=pd.read_csv("file:///C:/Users/dell/Desktop/whiskey_clustering/whisky.txt",engine='python')
df["Region"] = pd.read_csv("file:///C:/Users/dell/Desktop/whiskey_clustering/regions.txt")
flavour=df.iloc[:,2:14]  #extraction of all 12 different flavour matrix
corr_whisky=pd.DataFrame.corr(flavour.transpose()) #computing of co-relation coefficient

#co-relation coefficient graph
plt.figure(figsize=(8,8))
plt.pcolor(corr_whisky)
plt.colorbar()
#ALGORITHM
model=SpectralCoclustering(n_clusters=5,random_state=45) #instantiation of Algorithm
model.fit(corr_whisky) #training 
y=model.column_labels_
x=model.row_labels_
#uncomment to see what co-clustering do
#print("co-clustering meaning (row ,clomn): ",list(zip(x,y)))

#sorting according to cluster
df["disteliries_group"]=pd.Series(model.row_labels_,index=df.index)
cluster=list(zip(df.iloc[:,1],df.iloc[:,18]))
cluster=sorted(cluster, key=lambda x: x[1])

print("the resultant grouped classified whiskey based on their flavour")
print("\n")

print(pd.DataFrame(cluster))




