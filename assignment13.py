import urllib2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

page = urllib2.urlopen('https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data')
df1 = pd.read_csv(page, index_col=False, header=None, names=['Poisonous?', 'Cap Color', 'Odor'], usecols=[0,3,5])


# poisonous = 1, edible = 0
df1.replace(to_replace={'Poisonous?':{'p':1, 'e': 0}}, inplace=True)

countsp = df1['Poisonous?'].value_counts()
print countsp

#Poisonous/Edible Distribution
objects1 = ['Edible', 'Poisonous']
y_pos = np.arange(len(objects1))
data = countsp
plt.bar(y_pos, data, align='center', alpha=0.5)
plt.xticks(y_pos, objects1)
plt.ylabel('Count')
plt.title('Poisonous/Edible Distribution')
plt.show()


#3. cap-color:                brown=n=0,buff=b=1,cinnamon=c=2,gray=g=3,green=r=4,
#                             pink=p=5,purple=u=6,red=e=7,white=w=8,yellow=y=9
df1.replace(to_replace={'Cap Color':{'n':0, 'b':1, 'c':2, 'g':3, 'r':4, 'p':5, 'u':6, 'e':7, 'w':8, 'y':9}}, inplace=True)

countsc = df1['Cap Color'].value_counts()
print countsc

#Cap Color Distribution
objects2 = ['Brown', 'Yellow', 'White', 'Gray', 'Red', 'Pink', 'Buff', 'Purple', 'Cinnamon', 'Green']
y_pos = np.arange(len(objects2))
data = countsc
plt.bar(y_pos, data, align='center', alpha=0.5)
plt.xticks(y_pos, objects2)
plt.ylabel('Count')
plt.title('Cap Color Distribution')
plt.show()


# 5. odor:                     almond=a=0,anise=l=1,creosote=c=2,fishy=y=3,foul=f=4,
#                              musty=m=5,none=n=6,pungent=p=7,spicy=s=8
df1.replace(to_replace={'Odor':{'a':0, 'l':1, 'c':2, 'y':3, 'f':4, 'm':5, 'n':6, 'p':7, 's':8}}, inplace=True)

countso = df1['Odor'].value_counts()
print countso

#Odor Distribution
objects3 = ['None', 'Foul', 'Fishy', 'Spicy', 'Anise', 'Almond', 'Pungent', 'Creosote', 'Musty']
y_pos = np.arange(len(objects3))
data = countso
plt.bar(y_pos, data, align='center', alpha=0.5)
plt.xticks(y_pos, objects3)
plt.ylabel('Count')
plt.title('Odor Distribution')
plt.show()

# Scatter Plot
sns.set(style="ticks", context="talk")
pal = sns.cubehelix_palette(4, 1.5, .75, light=.6, dark=.2)
g = sns.lmplot(x='Odor', y='Cap Color', hue='Poisonous?', data=df1, palette=pal, size=7)
g.set_axis_labels("Odor", "Cap Color")
sns.plt.show()