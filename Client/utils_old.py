
# coding: utf-8

# In[1]:

import json
from pprint import pprint
import os
import shutil


# In[2]:

path = "/Users/hsienhaochen/Documents/9487/HsienHao's_SmartHome"
dataPath = "/Users/hsienhaochen/Documents/專題_張宏慶/fgfgf/Hsien-Hao's_Home.json"


# In[3]:

def InsertFiles(filePointer, dataPath):
    print ("infunc")
    if not os.path.isdir(path):#check if path exists, else, make the path.
        os.makedirs(path)
    shutil.move(os.getcwd()+"/"+filePointer.name,path)#Moves the got json file to the object path.
    dfp = open(dataPath, 'w')#write the new element to datafile
    dfp["Hsien-Hao's_Home"]["PhysicalSpaceRelation"]["Kitchen"].append(file_name[:-5])
    
    
    


# In[7]:




    


# In[5]:




# In[ ]:



