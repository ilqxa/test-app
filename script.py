#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials


# In[2]:


scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('time-controller-cdd4a3104027.json', scope)
gc = gspread.authorize(credentials)


# In[3]:


spreadsheet_key = '1o2dZty4Nj659wNo-o4H5kCD_R-5UYOd-YBP5NztBHQU'
book = gc.open_by_key(spreadsheet_key)
worksheet = book.worksheet("Лист1")
table = worksheet.get_all_values()


# In[4]:


df = pd.DataFrame(table[1:], columns = table[0])
df.head()


# In[5]:


from df2gspread import df2gspread as d2g
wks_name = 'Лист2'
d2g.upload(df, spreadsheet_key, wks_name, credentials = credentials, row_names = True)


# In[ ]:




