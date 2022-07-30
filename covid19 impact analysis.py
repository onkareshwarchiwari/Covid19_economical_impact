#!/usr/bin/env python
# coding: utf-8

# # Import statements

# In[54]:


import pandas as pd

import matplotlib.pyplot as plt

import plotly.express as px

import plotly.offline as pyo

get_ipython().run_line_magic('matplotlib', 'inline')
pyo.init_notebook_mode(connected = True)


# # Section  1:

# # Data import on COVID19 

# In[3]:


df_covid19=pd.read_csv('WHO-COVID-19-global-data.csv')
df_covid19.head()


# In[4]:


df_covid19=df_covid19[['Date_reported','Country','New_cases',]]


# ## Filter world data for getting only India specific values

# In[5]:


df_covid19_ind=df_covid19[df_covid19.Country=='India']
df_covid19_ind.head()


# ## Check for NAN cells 

# In[6]:


df_covid19_ind.isna().values.any()


# ## Converting daily data to monthly data

# In[7]:


df_covid19_ind['Date_reported']=pd.to_datetime(df_covid19_ind['Date_reported'])
df_covid19_ind_monthly=df_covid19_ind.resample('M',on='Date_reported').last()


# In[8]:


df_covid19_ind_monthly.head()


# ## Plotting COVID19 line chart

# In[9]:


plt.figure(figsize=(14,8), dpi=120)
plt.title('Monthly COVID19 cases in India', fontsize=18)
 
# Increase the size and rotate the labels on the x-axis
plt.xticks(fontsize=14, rotation=45) 
 
plt.ylabel('Cumulative cases', color='#E6232E', fontsize=14)
plt.xlabel('Month', fontsize=14)
 
# Set the minimum and maximum values on the axes
plt.ylim([0, 450000])
plt.xlim([df_covid19_ind_monthly.Date_reported.min(), df_covid19_ind_monthly.Date_reported.max()])
 
plt.plot(df_covid19_ind_monthly.Date_reported,df_covid19_ind_monthly.New_cases, marker='o', color='red')

plt.show()


# # Section 2:

# # Importing data on India GDP

# In[10]:


df_ind_gdp=pd.read_csv('ind_gdp_fred_data.csv')
df_ind_gdp.head()


# ## Renaming GDP value column

# In[11]:


df_ind_gdp.rename(columns = {'INDLORSGPNOSTSAM':'GDP'}, inplace = True)
df_ind_gdp.head()


# ## Checking for NAN values

# In[12]:


df_ind_gdp.isna().values.any()


# In[13]:


df_ind_gdp.dtypes


# In[14]:


df_ind_gdp['DATE']=pd.to_datetime(df_ind_gdp['DATE'])


# In[15]:


df_covid19_ind_monthly_cropped = df_covid19_ind_monthly.drop(df_covid19_ind_monthly.index[26:31])


# ## Plotting COVID19 monthly new cases versus Monthly GDP values

# In[16]:


plt.figure(figsize=(14,8), dpi=120)
plt.title('COVID19 cases vs Monthly GDP', fontsize=18)
 
# Increase the size and rotate the labels on the x-axis
plt.xticks(fontsize=14, rotation=45)
 
ax1 = plt.gca()
ax2 = ax1.twinx()
 
ax1.set_ylabel('Monthly GDP', color='#E6232E', fontsize=14)
ax2.set_ylabel('COVID19 Monthly new cases', color='skyblue', fontsize=14)

 
# Set the minimum and maximum values on the axes
ax1.set_ylim([80, 110])
ax1.set_xlim([df_ind_gdp.DATE.min(), df_ind_gdp.DATE.max()])
 
ax1.plot(df_covid19_ind_monthly_cropped.Date_reported, df_ind_gdp.GDP, color='#E6232E', linewidth=3, linestyle='dashed', marker= 's')
ax2.plot(df_covid19_ind_monthly_cropped.Date_reported, df_covid19_ind_monthly_cropped.New_cases, color='skyblue', linewidth=3, marker= 'o')

ax1.grid(color='grey', linestyle='--')

plt.show()


# ### As is evident from the chart, in the year 2020 when COVID 19 cases started rising, India GDP was contracting. This suggests that the rising cases was clearly impacting the output and suggesting towards slowing economy.
# 
# ### Also in the year 2021, the sharp spike in COVID 19 cases took the GDP down but this time the impact was not as severe as in the year 2020. One reason might be the India's preparedness for the disease and businesses had adjusted to changed scenario due to COVID19

# # Section 3:

# ## Importing data on Central bank interest rates

# In[17]:


df_int_ind=pd.read_csv('ind_int_rate_fred_data.csv')
df_int_ind.head()


# ## Renaming CPI value column

# In[18]:


df_int_ind.rename(columns = {'INTDSRINM193N':'InterestRate'}, inplace = True)
df_int_ind.head()


# ## Checking for NAN values

# In[19]:


df_int_ind.isna().values.any()


# In[20]:


df_covid19_ind_monthly_croppedforINT = df_covid19_ind_monthly.drop(df_covid19_ind_monthly.index[29:31])


# ## Converting date format from 'object' to 'datetime'

# In[21]:


df_int_ind['DATE']=pd.to_datetime(df_int_ind['DATE'])
df_int_ind.dtypes


# ## Plotting COVID19 monthly new cases versus Monthly Interest Rate values

# In[22]:


plt.figure(figsize=(14,8), dpi=120)
plt.title('Monthly RBI Interest rates', fontsize=18)
 
# Increase the size and rotate the labels on the x-axis
plt.xticks(fontsize=14, rotation=45) 
 
plt.ylabel('Interest rates', color='#E6232E', fontsize=14)
plt.xlabel('Month', fontsize=14)
 
# Set the minimum and maximum values on the axes
plt.ylim([4, 5.5])
plt.xlim([df_int_ind.DATE.min(), df_int_ind.DATE.max()])
 
plt.plot(df_int_ind.DATE,df_int_ind.InterestRate, marker='o', color='red')

plt.show()


# In[23]:


plt.figure(figsize=(14,8), dpi=120)
plt.title('COVID19 cases vs Monthly RBI Interest Rate', fontsize=18)

 
# Increase the size and rotate the labels on the x-axis
plt.xticks(fontsize=14, rotation=45)
 
ax1 = plt.gca()
ax2 = ax1.twinx()
 
ax1.set_ylabel('Monthly Interest rate', color='#E6232E', fontsize=14)
ax2.set_ylabel('COVID19 Monthly new cases', color='skyblue', fontsize=14)

 
# Set the minimum and maximum values on the axes
ax1.set_ylim([4,5.5])
ax1.set_xlim([df_int_ind.DATE.min(), df_int_ind.DATE.max()])
 
ax1.plot(df_covid19_ind_monthly_croppedforINT.Date_reported, df_int_ind.InterestRate, color='#E6232E', linewidth=3, linestyle='dashed', marker= 's')
ax2.plot(df_covid19_ind_monthly_croppedforINT.Date_reported, df_covid19_ind_monthly_croppedforINT.New_cases, color='skyblue', linewidth=3, marker= 'o')

ax1.grid(color='grey', linestyle='--')

plt.show()


# ### To curb the adverse effects of Covid19 spread on economy, India had reduced the repo rates to help businesses and overall economy to stand on its feet. This can be observed in the chart above as the spread of Covid19 increased, the RBI reduced the interest rate quickly as a remedy.

# # Section 4:

# # Importing data on India Inflation Data

# In[24]:


df_cpi_ind= pd.read_csv('ind_cpi_fred_data.csv')
df_cpi_ind.tail()


# ## Renaming CPI value column

# In[25]:


df_cpi_ind.rename(columns = {'INDCPIALLMINMEI':'CPI'}, inplace = True)


# In[26]:


df_cpi_ind.tail()


# ## Checking for NAN values 

# In[27]:


df_cpi_ind.isna().values.any()


# ## Converting date column into datetime object

# In[28]:


df_cpi_ind.DATE = pd.to_datetime(df_cpi_ind.DATE)


# ## Cropping covid19 data with respect to CPI data

# In[29]:


df_covid19_ind_monthly_croppedforCPI = df_covid19_ind_monthly.drop(df_covid19_ind_monthly.index[29:31])


# ## Plotting COVID19 monthly new cases versus Monthly CPI values

# In[30]:


plt.figure(figsize=(14,8), dpi=120)
plt.title('COVID19 cases vs Monthly CPI', fontsize=18)
 
# Increase the size and rotate the labels on the x-axis
plt.xticks(fontsize=14, rotation=45)
 
ax1 = plt.gca()
ax2 = ax1.twinx()
 
ax1.set_ylabel('Monthly CPI', color='#E6232E', fontsize=14)
ax2.set_ylabel('COVID19 Monthly new cases', color='skyblue', fontsize=14)

 
# Set the minimum and maximum values on the axes
ax1.set_ylim([120, 145])
ax1.set_xlim([df_cpi_ind.DATE.min(), df_cpi_ind.DATE.max()])
 
ax1.plot(df_covid19_ind_monthly_croppedforCPI.Date_reported, df_cpi_ind.CPI, color='#E6232E', linewidth=3, linestyle='dashed', marker= 's')
ax2.plot(df_covid19_ind_monthly_croppedforCPI.Date_reported, df_covid19_ind_monthly_croppedforCPI.New_cases, color='skyblue', linewidth=3, marker= 'o')

ax1.grid(color='grey', linestyle='--')

plt.show()


# ### Effect of reduction in interest rate and Inflation:

# In[31]:


plt.figure(figsize=(14,8), dpi=120)
plt.title('Monthly Interest rates vs Monthly CPI', fontsize=18)
 
# Increase the size and rotate the labels on the x-axis
plt.xticks(fontsize=14, rotation=45)
 
ax1 = plt.gca()
ax2 = ax1.twinx()
 
ax1.set_ylabel('Monthly CPI', color='#E6232E', fontsize=14)
ax2.set_ylabel('Monthly interest Rates', color='skyblue', fontsize=14)

 
# Set the minimum and maximum values on the axes
ax1.set_ylim([120, 145])
ax1.set_xlim([df_cpi_ind.DATE.min(), df_cpi_ind.DATE.max()])
 
ax1.plot(df_covid19_ind_monthly_croppedforCPI.Date_reported, df_cpi_ind.CPI, color='#E6232E', linewidth=3, linestyle='dashed', marker= 's')
ax2.plot(df_covid19_ind_monthly_croppedforCPI.Date_reported, df_int_ind.InterestRate, color='skyblue', linewidth=3, marker= 'o')

ax1.grid(color='grey', linestyle='--')

plt.show()


# ### In the chart above, the aftermath effects of Reduction in interest rate and Increase in inflation can be seen. Even if it is an oversimplification of this data, but it can be generally concluded that easy money flow in the system because of reduction in interest rate has led to increase in demand and in turn lead to inflation.

# # Section 5:

# ## Statewise statistics on Covid19 spread:

# ### Importing data on statewise Covid19 data

# In[32]:


df_statewise_covid19 = pd.read_csv('covid_19_india_statewisecases.csv')


# In[33]:


df_statewise_covid19.tail()


# In[34]:


df_statewise_total = df_statewise_covid19.groupby('State/UnionTerritory').sum()


# In[35]:


df_statewise_total.Confirmed.nlargest(4)


# In[36]:


df_statewise_covid19.pivot(index= 'Date',columns= 'State/UnionTerritory', values = 'Confirmed')


# In[53]:


fig = px.pie(df_statewise_total, values='Confirmed', names=df_statewise_total.index, color_discrete_sequence=px.colors.sequential.RdBu)
fig.update_traces(textposition='inside')
fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
fig.show()


# ### From the chart above, it is evident that the most affected state from Covid19 in India was Maharashtra.

# In[57]:


fig = px.pie(df_statewise_total, values='Confirmed', names=df_statewise_total.index)
fig.update_traces(textposition='inside')
fig.update_layout(uniformtext_minsize=12, uniformtext_mode='hide')
fig.show()


# In[ ]:




