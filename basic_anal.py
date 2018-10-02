
# coding: utf-8

# In[1]:


import pandas as pd
a=pd.read_csv('odidata.csv')


# In[2]:


#a['Average']=a['Average'].str.replace('-','0')
#a['StrikeRate']=a['StrikeRate'].str.replace('-','0')
#a['Truns']=a['Truns'].str.replace('-','0')


# In[3]:


#a.to_csv('odidata.csv',index=True)


# In[ ]:


a['score']=6.5*pd.to_numeric(a['Average'])+3.5*pd.to_numeric(a['StrikeRate'])


# In[ ]:


b=[x for x in (input("enter two countries").split())]


# In[ ]:


play=(a['Nation']==b[1])
play2=(a['Nation']==b[0])
p=a[play]
player=p.append(a[play2])
c=pd.to_numeric(player['Truns'])
play=(c>500)
players=player[play]


players=players.sort_values(by=['score'])
players=players[::-1]
print(players)

