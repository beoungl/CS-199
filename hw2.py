#!/usr/bin/env python
# coding: utf-8

# In[9]:


import pandas as pd


# In[10]:


import matplotlib.pyplot as plt


# In[11]:


import seaborn as sns


# In[12]:


import numpy as np
df = open('SRR7877764_1.fastq')
count = 1
list_qual = []

for i in df.readlines():
    count +=1
    if (count%4) == 1:
        list_qual.append(i)


# In[ ]:





# In[13]:


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


# mean = 'average'
# x = np.linspace(0,1, len(myqual_mean_list))
# myqual_mean = pd.DataFrame(data = {'mean':myqual_mean_list, 'x': x} )
# print(myqual_mean[0:5])
# myqual_mean.head()

# In[14]:


myqual_mean = pd.DataFrame(data = {'mean':myqual_mean_list})
myqual_mean.head()


# In[21]:


scatterplot_mean = sns.boxplot(myqual_mean)
scatterplot_mean.set_title('FASTQ MEAN')
plt.show()


# In[22]:


myqual_median = pd.DataFrame(data = {'median':myqual_median_list})
myqual_median.head()


# In[17]:


fastq_median = sns.distplot(myqual_median)
fastq_median.set_title('FASTQ MEDIAN')
plt.show()


# In[ ]:





# In[18]:


myqual_min_max = pd.DataFrame({'min_score': myqual_min_list, 'max_score': myqual_max_list})
myqual_min_max.head()


# In[19]:


min_max_graph = sns.scatterplot(x = 'min_score', y= 'max_score', data= myqual_min_max)
min_max_graph.set_title('FASTQ SCATTERPLOT')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




