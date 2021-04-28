#!/usr/bin/env python
# coding: utf-8

# In[24]:


#!pip install db-sqlite3
import sqlite3


# In[25]:


conn=sqlite3.connect('LabProgram2.db')
cur=conn.cursor()
conn=sqlite3.connect('test.db')
print("Opened database successfully");


# In[26]:


conn.execute('''CREATE TABLE COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')
print("Table created successfully");


# In[27]:


conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)       VALUES (1, 'Paul', 32, 'California', 20000.00)");
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)       VALUES (2, 'Alien', 25, 'Texas', 15000.00)");
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)       VALUES (3, 'Teddy', 23, 'Norway', 20000.00)");
conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)       VALUES (4, 'Mark', 25, 'Rich-Mond', 65000.00)");

conn.commit()
print ("Records created successfully");


# In[28]:


for row in conn.execute('select * from COMPANY'):
        print(row)


# In[29]:


conn.commit()


# In[30]:


conn.close()


# In[ ]:




