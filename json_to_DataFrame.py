import pandas as pd

path = input("Enter the path of the json file -->")

r = pd.read_json(path)
r