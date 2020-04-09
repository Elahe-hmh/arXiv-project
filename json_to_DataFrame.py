import pandas as pd

path = input("Enter the path of the json file(example --> D:/Machine Learning/data.json) -->")

r = pd.read_json(path)
r