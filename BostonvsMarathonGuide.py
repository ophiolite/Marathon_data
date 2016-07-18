
# coding: utf-8

# In[118]:

import pandas as pd
import matplotlib.pyplot as plt
import marathonlib as m
import numpy as np
from marathonlib import time_to_minutes

get_ipython().magic(u'matplotlib inline')


# In[108]:

df2 = pd.read_csv('data/boston2016_clean.csv')
df2.columns
df2.dtypes


# In[109]:

df = pd.read_csv('data/marathonguide/2015_2016master.csv')
df.columns
df.dtypes


# In[137]:

model_df = pd.DataFrame()


# In[138]:

model_df = pd.DataFrame()


# In[146]:

model_df['offltime'] = df['offltime']
df=df.convert_objects(convert_numeric=True)
model_df


# In[147]:

model_df['offltime2'] = df2['offltime']


# In[149]:

plt.plot(model_df['offltime'], y, 'ro')
plt.plot(model_df['offltime2'], y, 'ro')
plt.xlabel('Marathon Times')
plt.ylabel('Boston Times')
plt.title('Boston 2016 Times vs. All Marathon Times')
plt.show()


# In[ ]:



