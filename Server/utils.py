
# coding: utf-8

# In[1]:

import json
from pprint import pprint
import os
import shutil


# In[2]:

class SmartHomeIndex:
    
    def __init__(self, index_path = ""):
        self.path = index_path
        self.name = ""
    def GetIndexPath(self):
        return self.path
    
    def expandIndex(self, relation_name, relation_item, device_name):
        #check if the relation item exist, add it if not.
        with open (self.path, 'r') as index:
            data = json.load(index)
            print("selfName", self.name)
            if (data[self.name][relation_name] == []):
                data[self.name][relation_name].update({relation_item:[]})
            else:
                if not(data[self.name][relation_name].get(relation_item)):
                    data[self.name][relation_name].update({relation_item:[]})
                 
            #print(data)
            #print(data[self.name][relation_name])
            data[self.name][relation_name][relation_item].append(device_name)
    
        with open (self.path, 'w') as index:
            json.dump(data, index)





# In[3]:

    def InsertFiles(self, DeviceFile, HomeName, device_data):
        print ("infunc")
        #setName
        self.name = HomeName
        #new home -> initialazation
        if(os.stat(self.path).st_size == 0): #empty index
            print("empty index, initializing...")
            data = dict()
            data.update({self.name:{}})
            data[self.name].update({"DeviceRelation":{}})
            data[self.name].update({"PhysicalSpaceRelation":{}})
        
            with open(self.path, 'w') as index:
                json.dump(data, index)
           
        
            
        device_name = DeviceFile.name[:-5]
        file_path = os.path.join(os.getcwd(), "Data", HomeName, "Devices")
        if not os.path.isdir(file_path):#check if path exists, else, make the path.
            os.makedirs(file_path)
        
        #open device file and check for necessary information
        with open(DeviceFile.name, 'r') as device_file:
            device = json.load(device_file)
            #pprint(device)
            print(device_name)
            device_manufacturer = device[device_name]["Manufacturer"]
            #device_location = device[device_name]["Location"]
    
        #write the new element to datafile
        self.expandIndex("DeviceRelation", device_manufacturer, device_name)
        #self.expandIndex("PhysicalSpaceRelation", device_location, device_name)
        
    #make a new file to store device data/
        json_file = os.path.join(file_path, DeviceFile.name)
        
        """
        with open(json_file, 'w') as jf:
            jf.write(device_data)
            jf.close()
        """
    
        try:
            shutil.move(os.path.join(os.getcwd(), DeviceFile.name) , file_path )
        
        except:
            print("file exists, try to update......")
            os.remove(json_file)
            shutil.move(os.path.join(os.getcwd(), DeviceFile.name) , file_path )





