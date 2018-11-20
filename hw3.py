


import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
matplotlib.use('TkAgg')

#open quickmerge file and read it.
file1 = open('quickmergelength.txt')
qmlength = file1.readlines()
qmlength_list = []
for length in qmlength:
    number = length.split()
    qmlength_list.append(int(number[1]))


#Sort the list into the
qmlength_list.sort(reverse = True)

#open flybase file and read it.
file2 = open('flybase1.txt')
referencelength = file2.readlines()
reflength_list = []

#Only add contigs that are greater than 3kb. First, I only added contigs grater than 1kb, but it resulted in not-so-great-looking graph.
#Higher the cut off, more resemblance did the graph had with the quickmerge 2x bionanao file. This is why I thought we needed some polishing here.
for length in referencelength:
    number = length.split()
    if int(number[1]) > 3000:
        reflength_list.append(int(number[1]))


#Sort the list
reflength_list.sort( reverse = True)



contig_n90 = pd.DataFrame({"Contig": qmlength_list})

#n90 = 601105
#I chose to separate the values at 601105 because that was the n90 value of the quickmerge 2x bionano sequence.

contig_ref = pd.DataFrame({"Contig": reflength_list})


#Histogram for the value below n90
histogram_plot = sns.distplot(contig_n90.iloc[17:], bins = 20, kde = False, axlabel = 'Base Pair Lengths', norm_hist = False, )
histogram_plot.set_title('Distribution of Quickmerge 2x Bionano Assembly, bp =< 601105 histogram')
histogram_plot.set_ylabel('Counts')
plt.xlim(xmin= 0)
plt.show()

#Histogram for the value above n90
histogram_plot1 = sns.distplot(contig_n90.iloc[:17], bins = 20, kde = False, axlabel = 'Base Pair Lengths', norm_hist = False, )
histogram_plot1.set_title('Distribution of Quickmerrge 2x Bionano Assembly, bp > 6001105')
histogram_plot1.set_ylabel('Counts')
plt.xlim(xmin = 0)
plt.show()

#CDF Plot
cdf_plot = sns.distplot(contig_n90,  kde_kws = dict(cumulative=True), bins = 1000, label = 'QM 2X BN')
sns.distplot(contig_ref, kde_kws = dict(cumulative=True),  bins = 1000, label = 'Reference')
cdf_plot.set_title('CDF Plot of Reference Genome vs QuickMerge 2x Bionano Assembly')
cdf_plot.set_ylabel('Proportion')
cdf_plot.set_xlabel('Contig Size(in 10Mbs)')
plt.legend()
plt.show()


