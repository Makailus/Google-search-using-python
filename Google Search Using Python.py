#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install googlesearch-python


# In[3]:


import googlesearch

query = "python program for google search"
results = googlesearch.search(query, num_results=5)

for result in results:
    print(result)


# In[ ]:




