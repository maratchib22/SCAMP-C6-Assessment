# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 04:22:12 2022

@author: USER
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset=pd.read_csv("F:/Mes activités/Analyse de données/SCAMP/fake_job_postings.csv",sep=",")


print(dataset.head())
print(dataset.info())

mydataset=dataset[["job_id","title","industry","fraudulent"]]
print(mydataset.info())
mydataset=mydataset.dropna()
print(mydataset.info())
print(mydataset.shape)

Industries=mydataset.industry.unique()

Ind=mydataset.industry.value_counts()

data_not_fraud=mydataset[mydataset["fraudulent"]==1]
data_fraud=mydataset[mydataset["fraudulent"]==0]
pourcentage_fraud=data_fraud.shape[0]*100/mydataset.shape[0]
pourcentage_not_fraud=data_not_fraud.shape[0]*100/mydataset.shape[0]

mydata=[]
nb_by_ind=[]
ratio=[]
for element in Industries:
    data_filter=mydataset.loc[(mydataset["fraudulent"]==1) & (mydataset["industry"]== element)]
    val=data_filter.shape[0]
    mydata.append(val)
    data_filter2=mydataset.loc[(mydataset["industry"]== element)]
    val2=data_filter2.shape[0]
    nb_by_ind.append(val2)
    ratio.append(val*100/val2)
    



d = {"Industry": Industries, "Nombre fraudulent": mydata}
d2= {"Industry": Industries, "Pourcentage fraudulent": ratio}
dataframe1 = pd.DataFrame(d)
dataframe2 = pd.DataFrame(d2)

dataframe1.sort_values(by="Nombre fraudulent", axis=0, ascending=False, inplace= True)
dataframe2.sort_values(by="Pourcentage fraudulent", axis=0, ascending=False,inplace= True)

ax1 = dataframe1.iloc[0:19].plot.bar(x='Industry', y='Nombre fraudulent', rot=80, title="20 first industries which contain more fraudulent jobs according to number of fraudulent")

ax2 = dataframe2.iloc[0:19].plot.bar(x='Industry', y='Pourcentage fraudulent', rot=80, title="20 first industries which contain more fraudulent jobs according to pourcentage of fraudulent")




