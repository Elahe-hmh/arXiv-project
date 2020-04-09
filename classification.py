import pandas as pd

def data_for_classification():
    my_dict = {}
    
    path = input("Enter the path of the json file(example --> D:/Machine Learning/data.json) -->")

    r = pd.read_json(path)
    
    my_dict["title"] = list(dict(r)["title"])
    my_dict["categories"] = list(dict(r)["categories"])
    my_dict["abstract"] = list(dict(r)["abstract"])
    
    return my_dict

data_for_classification()
    
    