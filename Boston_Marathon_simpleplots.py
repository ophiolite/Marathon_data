
# coding: utf-8

# In[93]:

import pandas as pd
import matplotlib.pyplot as plt
import marathonlib as m
import numpy as np
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
import scipy, scipy.stats

get_ipython().magic(u'matplotlib inline')


# In[94]:

df = pd.read_csv('data/boston2016_clean.csv')
df.columns


# In[95]:

model_df = pd.DataFrame()


# In[96]:

model_df['timehalf'] = df['timehalf']


# In[97]:

model_df['offltime'] = df['offltime']


# In[98]:

plt.plot(df['offltime'], df['timehalf'], 'ro')
plt.xlabel('Official Time')
plt.ylabel('Half Time')
plt.title('Boston 2016 Times: Half Marathon vs. Full Splits')
plt.show()



# In[110]:

par = np.polyfit(df['offltime'], df['timehalf'], 1, full=True)
slope=par[0][0]
intercept=par[0][1]
xl = [min(df['offltime']), max(df['timehalf'])]
yl = [slope*xx + intercept  for xx in xl]

plt.plot(df['offltime'], df['timehalf'], 'ro')
plt.xlabel('Official Time')
plt.ylabel('Half Time')
plt.title('Boston 2016 Times: Half Marathon vs. Full Splits')
plt.plot(xl, yl, linewidth=2.0)
plt.show()


# In[81]:

df['timehalf'] = np.ones(( len(df), ))
Y = df['timehalf']
X = df['offltime']
result = sm.OLS( Y, X ).fit()
result.summary()


# In[83]:

print('Parameters: ', result.params)
print('Standard errors: ', result.bse)
print('Predicted values: ', result.predict())


# In[126]:

df['delta'] = (df['offltime'] - df['timehalf']) - df['timehalf']
plt.plot(df['offltime'], df['delta'], 'ro')
plt.xlabel('Official Time')
plt.ylabel('Delta First and Second Half')
plt.title('Boston 2016 Times: Delta Split vs. Official Full Time')


# In[ ]:




# In[ ]:




# In[ ]:



