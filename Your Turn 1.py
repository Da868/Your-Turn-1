#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
Location ="datasets/floridadata.csv"
df=pd.read_csv(Location)


# In[2]:


df.head(*)


# In[7]:


print(df.head())


# In[8]:


df.to_csv('floridadata.csv',index=False,header=False)


# In[ ]:




