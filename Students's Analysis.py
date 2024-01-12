#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing librariries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#read files
df = pd.read_csv('student_data.csv')
df.head()


# In[3]:


#numeric vaues in dat
df.describe()


# # Gender Distribution

# In[5]:


#Number of male and female students
ax = sns.countplot(data = df, x = 'sex')
ax.bar_label(ax.containers[0])
plt.show()


# # Age

# In[6]:


ag = sns.countplot(data = df, x = 'age')
ag.bar_label(ag.containers[0])
plt.show()


# In[7]:


#checking for missi ng values
df.isnull().sum()


# #Adress 

# # #Adress

# In[8]:


#Check students live in Urben areas or rural areas
# R is Rural & U is Urban
ad = sns.countplot(data = df, x = 'address')
ad.bar_label(ad.containers[0])
plt.show()


# # Guardian

# In[19]:


#Guardian impact on grades G1, G2, G3
gu = df.groupby("guardian").agg({"G1":'mean',"G2":'mean',"G3":'mean'})
print(gu)


# In[18]:


sns.heatmap(gu, annot=True)
plt.show()


# In[ ]:




