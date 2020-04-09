import pandas as pd
import json

def merging_json_files():
    
    num = int(input("Enter the number of json files -->"))
    Path = input("Enter the path that you want to save the merged json file(example --> D:/Machine Learning/merged.json) --> ")
    dict_list = []
    
    choosing_variable = input("all of them have the same path?[yes/no] :")
    if choosing_variable == 'yes' :
        path = input("enter the path of the files ( D:/Machine Learning/ ) :")
        for n in range(num):
            name = input("Enter the name of %ith json file (example --> data.json) --> " %(n+1))
            r = pd.read_json(path+name)
            dict_list.append(dict(r))
    
    if choosing_variable == 'no' :
    
        for n in range(num):
            path = input("Enter the path of %ith json file (example --> D:/Machine Learning/data.json) --> " %(n+1))
            r = pd.read_json(path)
            dict_list.append(dict(r))
        
    if num > 0:
        temp = len(list(dict_list[0].keys()))
    for n in range(num):
        if len(list(dict_list[n].keys())) != temp:
            print("--EROR-- \n json files must have the same informations, try again :)")
            merging_json_files()
            return
    
    final_dict = {}
    if num > 0:
        for key in list(dict_list[0].keys()):
            final_dict[key] = []
            for n in range(num):
                final_dict[key].extend(list(dict_list[n][key]))
    
    with open(Path, 'w') as f:
        json.dump(final_dict, f)
        
    print("the merged json file is ready now :)\n you can find it here %s" %(Path))
    
    return
    
merging_json_files()
    
        