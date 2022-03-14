#!/usr/bin/env python
# coding: utf-8

# ## LEGO Data Analysis

# #### Objective
# 
# **1. What percentage of all licenced sets ever released were Star Wars themed?**
# <br>
# **2. In which year was Star Wars not the most popular licenced theme (in terms of number of sets released that year)?** 

# In[112]:


import pandas as pd


# In[113]:


#Pull datasets from github

df = pd.read_csv('https://raw.githubusercontent.com/avishakdebroy/lego-data-analysis/main/datasets/lego_sets.csv')
theme = pd.read_csv('https://raw.githubusercontent.com/avishakdebroy/lego-data-analysis/main/datasets/parent_themes.csv')


# In[114]:


df.head()


# In[115]:


theme.head()


# In[116]:


merged_df = df.merge(theme, left_on='parent_theme', right_on='name')
merged_df.drop(columns='name_y', inplace=True)
merged_df.head(10)


# In[117]:


licensed = merged_df[merged_df['is_licensed'] == True]
licensed = licensed.dropna(subset = ['set_num'])

star_wars = licensed[licensed['parent_theme'] == 'Star Wars']
star_wars.shape

the_force = int(star_wars.shape[0]/licensed.shape[0] * 100)
print(f'{the_force} percentage of all licenced sets ever released were Star Wars themed.')


# **1. Ans: 51% of all licenced sets ever released were Star Wars themed.**

# In[118]:


licensed_sorted = licensed.sort_values('year')
licensed_sorted['count'] = 1

sum_df = licensed_sorted.groupby(['year', 'parent_theme']).sum().reset_index()
max_df = sum_df.sort_values('count', ascending=False).drop_duplicates(['year'])

max_df.sort_values('year', inplace= True)
max_df


# In[119]:


new_era = 2017
print(new_era)


# **2. Ans: In 2017 Star Wars was not the most popular licenced theme.** 
