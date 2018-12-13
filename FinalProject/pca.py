import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import numpy as np

species_name = 'Alligator mississipiensis	Maiasaura peeblesorum #2	South American Saltasaurid	French Titanosaur	Heyuannia huangi	Mongolian Microtroodontid #1	Mongolian Microtroodontid #2	Mongolian Troodontid #1	Mongolian Troodontid #2	Chinese Troodontid	North American Troodontid	Deinonychus antirrhopus	Enanthiornithine	Psammornis rothschildi	Rhea americana	Dromaius novaehollandiae	Gallus domesticus	Sediment Chinese Troodontid	Sediment French Titanosaur	Sediment Heyuannia huangi	Sediment Maiasaura peeblesorum #1	Sediment Maiasaura peeblesorum #2	Sediment Mongolian Microtroodontid	Sediment Enanthiornithine	Sediment Mongolian Troodontid	Sediment North American Ratite	Sediment South American Saltasaur	Sediment North American Troodontid'
pigment_list = ['Unpigmented fossil and extand eggshells', 'Pigmented Fossil and Extand Eggshells', 'Fossil egg shell sediments']

df = pd.read_csv('dinosaur2.csv', header = None)
fake_columns = list(range(2897))
df.columns = [fake_columns]
df = df.rename(columns = {0: 'Species'})
df = df.rename(columns = {1: ' Eggshell'})


y = df.iloc[:,1].values
x = df.iloc[:,2:].values

#Change this to see the change when result is standardized
#x = StandardScaler().fit_transform(x)

pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
X_pca = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2'])
species = pd.DataFrame(data = y, columns = ['Eggshell'])
finalDf = pd.concat([X_pca, species], axis = 1)
print(pca.explained_variance_ratio_)
target_ids = range(28)
fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1)
colors = ['r','g','b']
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('PCA Plot of Sediment and the Extant Eggshells', fontsize = 20)
for i, target, color in zip(target_ids,pigment_list, colors):
    indicesToKeep =  finalDf['Eggshell'] == target
    ax.scatter(finalDf.loc[indicesToKeep,'principal component 1'],
               finalDf.loc[indicesToKeep,'principal component 2'],
               c = color,
               s = 100)
ax.grid()
ax.legend(pigment_list, loc = 'upper center', bbox_to_anchor=(0.5, 1.17))
plt.show()


kf = pd.read_csv('dinosaur3.csv', header = None)
placeholder = list(range(365))
kf.columns = [placeholder]
kf = kf.rename(columns = {0:'Eggshell'})
fossil_list = ['Unpigmented fossil eggshells', 'Pigmented fossil eggshells']
a = kf.iloc[:,1].values
b = kf.iloc[:,2:].values

#Remove the hashtag to see the see the effect of standardization.
#b = StandardScaler().fit_transform(b)

pca = PCA(n_components=2)
principalCom = pca.fit_transform(b)
X2_pca = pd.DataFrame(data = principalCom, columns = ['principal component 1', 'principal component 2'])
eggshell = pd.DataFrame(data=a, columns = ['Eggshell'])
dataDf = pd.concat([X2_pca, eggshell], axis = 1)
print(pca.explained_variance_ratio_)
target_id = range(12)
fig = plt.figure(figsize = (8,8))
ax = fig.add_subplot(1,1,1)
colors = ['r','g']
ax.set_xlabel('Principal Component 1', fontsize = 15)
ax.set_ylabel('Principal Component 2', fontsize = 15)
ax.set_title('PCA Plot of Unpigmented and Pigmented Eggshells', fontsize = 20)
for i, target, color in zip(target_id,fossil_list, colors):
    indicesToKeep = dataDf['Eggshell'] == target
    ax.scatter(dataDf.loc[indicesToKeep,'principal component 1'],
               dataDf.loc[indicesToKeep,'principal component 2'],
               c = color,
               s = 100)
ax.grid()
ax.legend(fossil_list, loc = 'upper center', bbox_to_anchor=(0.5, 1.15))
plt.show()
