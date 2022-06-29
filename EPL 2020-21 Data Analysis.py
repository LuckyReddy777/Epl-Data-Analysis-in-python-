#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


epl_df = pd.read_csv('C:\\Users\\medgini\\Downloads\\Ebook\\EPL_20_21.csv')


# In[3]:


epl_df.head()


# In[4]:


epl_df.info()


# In[5]:


epl_df.describe()


# In[6]:


epl_df.isna().sum()


# In[7]:


epl_df['Minspermatch'] = (epl_df['Mins'] / epl_df['Matches']).astype(int)
epl_df['Goalspermatch'] = (epl_df['Goals'] / epl_df['Matches']).astype(float)
epl_df.head()


# In[8]:


total_goals = epl_df['Goals'].sum()
total_goals


# In[9]:


total_penalitygoals = epl_df['Penalty_Goals'].sum()
total_penalitygoals


# In[10]:


total_penalityattempts = epl_df['Penalty_Attempted'].sum()
total_penalityattempts


# In[14]:


plt.figure(figsize=(13,6))
pl_not_scored = total_penalityattempts - total_penalitygoals
data = [pl_not_scored, total_penalitygoals]
labels = ['penalities missed', 'penality scored']
color = sns.color_palette("husl", 8)
plt.pie(data, labels=labels, colors = color, autopct = '%.0f%%')
plt.show()


# In[16]:


epl_df['Position'].unique()


# In[19]:


epl_df[epl_df['Position'] == 'FW']


# In[21]:


np.size((epl_df['Nationality'].unique()))


# In[29]:


nationality = epl_df.groupby('Nationality').size().sort_values(ascending=False)
nationality.head(15).plot(kind = 'bar', figsize = (12,6), color = sns.color_palette('magma'))


# In[32]:


epl_df['Club'].value_counts().nlargest(5).plot(kind='bar',color=sns.color_palette('viridis'))


# In[33]:


epl_df['Club'].value_counts().nsmallest(5).plot(kind='bar',color=sns.color_palette('crest'))


# In[36]:


under20 = epl_df[epl_df['Age'] <= 20]
age20_25 = epl_df[(epl_df['Age'] <= 25) & (epl_df['Age'] > 20)]
age25_30 = epl_df[(epl_df['Age'] > 25) & (epl_df['Age'] <= 30)]
above_30 = epl_df[epl_df['Age'] > 30]


# In[41]:


x = np.array([under20['Name'].count(),age20_25['Name'].count(),age25_30['Name'].count(),above_30['Name'].count()])
mylabels = ["<20","20-25","25-30",">30"]
plt.title('total players with age group', fontsize=20)
plt.pie(x, labels = mylabels, autopct = '%.1f%%')
plt.show()


# In[48]:


players_under_20 = epl_df[epl_df['Age'] < 20]
players_under_20['Club'].value_counts().plot(kind='bar', color=sns.color_palette("cubehelix"))


# In[51]:


players_under_20[players_under_20["Club"]=="Manchester United"]


# In[53]:


plt.figure(figsize=(12,6))
sns.boxplot(x='Club', y='Age', data=epl_df)
plt.xticks(rotation=90)


# In[54]:


num_player = epl_df.groupby('Club').size()
data = (epl_df.groupby('Club')['Age'].sum())/ num_player
data.sort_values(ascending=False)


# In[61]:


Assists_by_clubs = pd.DataFrame(epl_df.groupby('Club', as_index=False)['Assists'].sum())
sns.set_theme(style='whitegrid',color_codes=True)
ax=sns.boxplot(x='Club',y='Assists',data=Assists_by_clubs.sort_values(by='Assists'),palette='Set2')
ax.set_xlabel('Club',fontsize='30')
ax.set_ylabel('Assists',fontsize='20')
plt.xticks(rotation=75)
plt.rcParams["figure.figsize"]=(20,8)
plt.title("Plot of Title vs Total assists", fontsize=20)


# In[64]:


top_10_assists = epl_df[['Name','Club','Assists','Matches']].nlargest(n=10, columns='Assists')
top_10_assists


# In[67]:


Goals_by_club = pd.DataFrame(epl_df.groupby('Club', as_index=False)['Goals'].sum())
sns.set_theme(style='whitegrid',color_codes=True)
ax = sns.barplot(x='Club',y='Goals',data=Goals_by_club.sort_values(by='Goals'),palette='rocket')
ax.set_xlabel('Club',fontsize='30')
ax.set_ylabel('Goals',fontsize='20')
plt.xticks(rotation=75)
plt.rcParams["figure.figsize"]=(20,8)
plt.title("Plot of Clubs vs Total Goals", fontsize=20)


# In[68]:


top_10_goals = epl_df[['Name','Club','Goals','Matches']].nlargest(n=10, columns='Goals')
top_10_goals


# In[71]:


top_10_goals_per_match = epl_df[['Name','Goalspermatch','Matches','Goals']].nlargest(n=10, columns='Goalspermatch')
top_10_goals_per_match


# In[75]:


plt.figure(figsize=(14,7))
assists = epl_df['Assists'].sum()
data = [total_goals-assists, assists]
labels=['Goals with out assist','Goals with assist']
color = sns.color_palette('Set1')
plt.pie(data, labels = labels, colors=color, autopct='%.0f%%')
plt.show()


# In[81]:


epl_yellow = epl_df.sort_values(by='Yellow_Cards', ascending=False)[:10]
plt.figure(figsize=(20,6))
plt.title=('players with the most yellow cards')
c=sns.barplot(x=epl_yellow['Name'], y=epl_yellow['Yellow_Cards'],label='Players',color='yellow')
plt.ylabel('Name of yellow cards')
c.set_xticklabels(c.get_xticklabels(),rotation=45)
c


# In[ ]:




