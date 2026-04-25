#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

df = pd.read_excel(r"C:\\Users\\pooja\\Desktop\\Client data.xlsx" ,sheet_name ="East_West")

print(df)


# In[4]:


df.info()
df.isnull().sum()


# In[42]:


df['Age'] =2024 - df['Year_Birth']
df[' Income ']= df[' Income '].replace('[\ $ ,]' ,'', regex=True).astype(float)


# In[5]:


df['Total_Spending'] = df[
    ['MntWines','MntFruits','MntMeatProducts','MntFishProducts','MntSweetProducts','MntGoldProds']
].sum(axis=1)


# In[6]:


df =df.dropna(subset =[' Income ' , 'Total_Spending'])


# In[9]:


from sklearn.cluster import KMeans

X = df[[' Income ','Total_Spending']]
kmeans = KMeans(n_clusters=3)

df['Cluster'] = kmeans.fit_predict(X)

df.head()


# In[37]:


df.columns


# In[2]:


result = df.groupby('Cluster')
[[' Income ','Total_Spending']].mean()


# In[ ]:


Print(result)


# In[27]:


import pandas as pd

df = pd.read_excel(r"C:\\Users\\pooja\\Desktop\\Client data.xlsx" ,sheet_name ="East_West")
df.columns =df.columns.str.strip()
df['Income'] = df['Income'].replace('[\ $ ,]' ,'', regex=True).astype(float)
df['Total_Spending'] = df[
    ['MntWines','MntFruits','MntMeatProducts','MntFishProducts','MntSweetProducts','MntGoldProds']
].sum(axis=1)

df =df.dropna(subset =['Income' , 'Total_Spending'])
from sklearn.cluster import KMeans

X = df[['Income','Total_Spending']]
kmeans = KMeans(n_clusters=3 ,random_state =42)

df['Cluster'] = kmeans.fit_predict(X)

result = df.groupby('Cluster')

[['Income','Total_Spending']].mean()

print(result)


# In[22]:


df.columns = df.columns.str.strip()
print(df.columns.tolist())


# In[24]:


print(type(df))


# In[29]:


print(type(['Income' ,'Total_spending']))
print(type(df))
print(type(df.groupby('Cluster')))


# In[32]:


import pandas as pd
data = pd.read_excel(r"C:\\Users\\pooja\\Desktop\\Client data.xlsx",sheet_name="East_West")
data.columns =data.columns.str.strip()
data['Income'] =data['Income'].replace('[\$,]','',regex=True).astype(float)
data['Total_Spending'] = data [
    ['MntWines','MntFruits','MntMeatProducts','MntFishProducts','MntSweetProducts','MntGoldProds']].sum(axis=1)
from sklearn.cluster import KMeans
X = data[['Income','Total_Spending']]
kmeans = KMeans(n_clusters=3,random_state=42)
data['Cluster'] =kmeans.fit_predict(X)
result = data.groupby('Cluster')
[['Income','Total_Spending']].mean()
print(result)


# In[33]:


print(data[['Income' ,'Total_Spending']].isnull().sum())


# In[35]:


data['Income'] =data['Income'].replace('[\$,]','',regex=True)
data['Income'] =pd.to_numeric(data['Income'],errors ='coerce')


# In[36]:


data =data.dropna(subset =['Income' , 'Total_Spending'])


# In[37]:


print(data[['Income' ,'Total_Spending']].isnull().sum())


# In[38]:





# In[39]:


from sklearn.cluster import KMeans
X = data[['Income','Total_Spending']]
kmeans = KMeans(n_clusters=3,random_state=42)
data['Cluster'] =kmeans.fit_predict(X)
print(data.head())


# In[40]:


print(data[['Income' ,'Total_Spending']].isnull().sum())


# In[41]:


data['Income'] =data['Income'].replace('[\$,]','',regex=True)
data['Income'] =pd.to_numeric(data['Income'],errors ='coerce')


# In[42]:


data =data.dropna(subset =['Income' , 'Total_Spending'])


# In[43]:


print(data[['Income' ,'Total_Spending']].isnull().sum())


# In[44]:


from sklearn.cluster import KMeans
X = data[['Income','Total_Spending']]
kmeans = KMeans(n_clusters=3,random_state=42)
data['Cluster'] =kmeans.fit_predict(X)
print(data.head())


# In[45]:





# In[46]:


data.isnull().sum()


# In[47]:


print(data.groupby('Cluster')
     [['Income','Total_Spending']].mean())
data.to_excel("final_project_data.xlsx", index=False)


# In[54]:


from sklearn.linear_model import LinearRegression
X = data[['Year_Birth']]
y = data['Total_Spending']
model = LinerRegression()
model.fit(X, y)
print("Forecast Model Ready")


# In[55]:


import sklearn
print(sklearn.__version__)


# In[57]:


from sklearn.linear_model import LinearRegression
X = data[['Year_Birth']]
y = data['Total_Spending']
model = LinearRegression()
model.fit(X, y)
print("Forecast Model Ready")


# In[ ]:




