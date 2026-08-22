# Here I Just Converted My project.txt file content into json to get structured .

import os
import string
import json

file_name = "project.txt"

# if os.path.exists(file_name):
#     os.remove(file_name)

# Writes In File
def write_data(data):
    with open(file_name,"w") as f:
        f.write(data)

# Reads From File
def read_data():
    with open(file_name,'r') as f:
        data = f.read()
        return data
# It Conertes The Fetched Data Into List Of Users In Dictionary Form 
def structure_data(data_list):
    all_user =[]
    for data in data_list:
        info = data.split(",")
        user_dict = {
                "Name": info[0].strip(),
                "Age": info[1].strip(),
                "Course": info[2].strip()
            }
        all_user.append(user_dict)
    
    return all_user

# It Store The Structured Data As Json In Structured_Data.json file
def create_json(data):
    with open("Structured_Data.json",'w') as file:
        json.dump(data,file,indent=4)

# Here We Split The Data Into List From A Single String 
user_data_list = read_data().split("\n")
# Here We Get The Data As List But Structured As Dictionary 
structured_data = structure_data(user_data_list)
# Here We Convert The Data In json And Stored It In A File
create_json(structured_data)