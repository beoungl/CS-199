#!/usr/bin/env python
# coding: utf-8

import pandas as pd


import matplotlib.pyplot as plt


import seaborn as sns


import numpy as np
df = open('SRR7877764.fastq')
count = 1
list_qual = []

for i in df.readlines():
    count +=1
    if (count%4) == 1:
        list_qual.append(i)


myqual_mean_list = []
myqual_median_list = []
myqual_min_list = []

myqual_max_list = []
for i in list_qual:
    qual = []
    for x in i:
        if x != '\n':
            qual.append(1-(10.0**(-(ord(x)-33)/10.0)))
    mean_score = float(np.average(qual))
    median_score = float(np.median(qual))
    min_score = float(np.min(qual))
    max_score = float(np.max(qual))
    myqual_mean_list.append(mean_score)
    myqual_median_list.append(median_score)
    myqual_min_list.append(min_score)
    myqual_max_list.append(max_score)



myqual_mean = pd.DataFrame(data = {'mean':myqual_mean_list})
myqual_mean.head()

scatterplot_mean = sns.boxplot(myqual_mean)
scatterplot_mean.set_title('FASTQ MEAN')
plt.show()



myqual_median = pd.DataFrame(data = {'median':myqual_median_list})
myqual_median.head()


fastq_median = sns.distplot(myqual_median)
fastq_median.set_title('FASTQ MEDIAN')
plt.show()




myqual_min_max = pd.DataFrame({'min_score': myqual_min_list, 'max_score': myqual_max_list})
myqual_min_max.head()

min_max_graph = sns.scatterplot(x = 'min_score', y= 'max_score', data= myqual_min_max)
min_max_graph.set_title('FASTQ SCATTERPLOT')
plt.show()




