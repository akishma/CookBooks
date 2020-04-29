#!/usr/bin/env python
# coding: utf-8

#  ## Looping through rows
#  
#  
#  Thanks to [Wei Xia] (https://medium.com/@xiawei27149)
#  

# In[10]:


import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randint(0, 10, size=(10000, 4)), columns=list('ABCD'))
df.head()


# In[11]:


# The slowest way

temp = 0
for _, row in df.iterrows():
         temp += row.A + row.B

temp        


# In[12]:


# The common way

temp=df.apply(lambda x: x['A'] + x['B'], axis=1).sum()
temp


# In[13]:


# The shortest way

temp=(df['A'] + df['B']).sum()
temp


# In[14]:


# The fastest way

temp=(df['A'].values + df['B'].values).sum()
temp

