import urllib.request as libreq
import pandas as pd
import csv
import json
import xml.etree.ElementTree as et
import xmltodict
import collections

with libreq.urlopen(
        'http://export.arxiv.org/api/query?search_query=all:astro-ph&sortBy=submittedDate&sortOrder'
        '=descending&start=0&max_results=1') as url:
    r = url.read()

# print(r)
# type(r)


xml = r
my_dict = xmltodict.parse(xml)
json_data = json.dumps(my_dict)
data_list = json_data

# with open('jsondata.json', 'w') as json_file:
# json.dump(data_list, json_file)

#val = []
for key, value in my_dict.items():
    for ke, val in value.items():
        a = (value['entry'])



aut=a['author']
#print(aut[1].keys())
#print(aut[1].values())

affli=aut[1].values()
#print(name)
#print(type(affli))
#for af in affli:
#print(af)
#for key , val in a.items():
#print(key)
#print(val)
# print(a.keys())
# print(a['title'])
# print(type(a.values()))

# print(type(val))
# print(my_dict.items())
