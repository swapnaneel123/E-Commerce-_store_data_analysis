#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[3]:


dataset=pd.read_excel("C:/Users/HP/Desktop/Superstore_USA.xlsx")


# In[4]:


dataset.head(2)


# In[5]:


dataset.shape


# In[9]:


#dataset.isnull().sum()#missing value


# In[7]:


dataset["Product Base Margin"].fillna(dataset['Product Base Margin'].mean(),inplace=True)


# In[22]:


dataset['Order Priority'].value_counts()


# In[17]:


#dataset['Order Priority'].unique()


# In[21]:


#dataset['Order Priority']=dataset['Order Priority'].replace('Critical ','Critical')


# # ORDER PRIORITY

# In[29]:


plt.figure(figsize=(5,4))
sns.countplot(x="Order Priority",data=dataset)
plt.savefig("Count of Order Priority.jpg")
plt.title("Count of Order Priority")


# # ship Mode

# In[31]:


dataset['Ship Mode'].value_counts()


# In[34]:


x=dataset['Ship Mode'].value_counts().index
y=dataset['Ship Mode'].value_counts().values


# In[43]:


plt.figure(figsize=(5,4))
plt.pie(y,labels=x,startangle=60,autopct="%0.2f%%")#autopct is for percentage
plt.legend(loc=3)


# In[56]:


sns.countplot(x="Ship Mode",data=dataset,hue="Product Category")#hue for bivarent data analysis
plt.figure(figsize=(4,3))


# # Customer Segment

# In[60]:


plt.figure(figsize=(6,4))
sns.countplot(x="Customer Segment",data=dataset)


# # Product Category

# In[67]:


plt.figure(figsize=(10,6))
sns.countplot(x="Product Category",data=dataset[dataset["Product Category"]=="Office Supplies"],hue="Product Sub-Category")


# In[68]:


plt.figure(figsize=(10,6))
sns.countplot(x="Product Category",data=dataset[dataset["Product Category"]=="Technology"],hue="Product Sub-Category")


# # Order Year

# In[71]:


dataset['Order Year']=dataset['Order Date'].dt.year#sare year alag ho gye


# In[73]:


dataset["Order Year"].value_counts()


# In[75]:


sns.countplot(x="Order Year",data=dataset)


# # PROFIT

# In[76]:


sns.barplot(x="Product Category",y="Profit",data=dataset,estimator='sum' )


# # State wise Sales

# In[81]:


dataset['State or Province'].value_counts()[:5]#top 5 sales


# In[82]:


sns.barplot(x="Product Category",y="Product Base Margin",data=dataset,estimator='sum' )

