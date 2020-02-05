#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from termcolor import colored,cprint
import getpass
data=pd.DataFrame({"ID":['Ami','Kir','Shiv','Dinu','Dhanu'],'Password':np.array([100,200,300,400,500]).astype(str)})
get_ipython().run_line_magic('matplotlib', '')


# In[2]:


data=pd.read_csv('D:/sample.csv',dtype=str)
data=data.append({'Name':'Imran Sayyed','ID':'sayyed950@gmail.com','City':'Pune','Password':'123'},ignore_index=True)
data


# In[14]:


while True:
    ID=input('\033[1mEnter ur ID: ')
    if ID not in data.ID.values:
        print (colored("\033[1mSorry ID doesn't exist",'red'))
        continue  
    while True:
        Pass=getpass.getpass('\033[1mEnter ur password: ')
        ind=data[data['ID']==ID].index[0]
        if (Pass!=data.Password[ind]):
            print(colored("\033[1mID & password doesn't matched",'red'))
            continue
        else:
            break
    if (Pass==data.Password[ind]):
        print(colored('\033[1mCongratulations!!! Access granted','green'))
        print(colored('\033[1mWelcome '+data['Name'][ind],'blue'))
        break



