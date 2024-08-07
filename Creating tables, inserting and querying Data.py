#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3


# In[5]:


conn = sqlite3.connect('INSTRUCTOR.db')


# In[6]:


cursor_obj = conn.cursor()


# In[7]:


cursor_obj.execute("DROP TABLE IF EXISTS INSTRUCTOR")


# In[8]:


table = """ create table IF NOT EXISTS INSTRUCTOR(ID INTEGER PRIMARY KEY NOT NULL, FNAME VARCHAR(20), LNAME VARCHAR(20), CITY VARCHAR(20), CCODE CHAR(2));"""


# In[19]:


cursor_obj.execute(table)
 
#print("Table is Ready")
print(table)


# In[10]:


cursor_obj.execute('''insert into INSTRUCTOR values (1, 'Rav', 'Ahuja', 'TORONTO', 'CA')''')


# In[11]:


cursor_obj.execute('''insert into INSTRUCTOR values (2, 'Raul', 'Chong', 'Markham', 'CA'), (3, 'Hima', 'Vasudevan', 'Chicago', 'US')''')


# In[12]:


statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)

print("All the data")
output_all = cursor_obj.fetchall()
for row_all in output_all:
  print(row_all)


# In[13]:


## Fetch few rows from the table
statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)
  
# print("All the data")
output_many = cursor_obj.fetchmany(2) 
for row_many in output_many:
  print(row_many)


# In[14]:


# Fetch only FNAME from the table(column)
statement = '''SELECT FNAME FROM INSTRUCTOR'''
cursor_obj.execute(statement)
  
# print("All the data")
output_column = cursor_obj.fetchall()
for fetch in output_column:
  print(fetch)


# In[15]:


query_update='''update INSTRUCTOR set CITY='MOOSETOWN' where FNAME="Rav"'''
cursor_obj.execute(query_update)


# In[16]:


statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)
  
print("All the data")
output1 = cursor_obj.fetchmany(2)
for row in output1:
  print(row)


# ### Retrieve data into pandas

# In[20]:


import pandas as pd
#retrieve the query results into a pandas dataframe
df = pd.read_sql_query("select * from instructor;", conn)

#print the dataframe
df


# In[25]:


#print just the LNAME for first row in the pandas data frame
df.LNAME[0]


# In[26]:


# this prints how many rows and column in the db
df.shape


# In[27]:


# Close the connection
conn.close()


# In[ ]:




