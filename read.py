
import json

with open('data.json') as json_data:
    d = json.load(json_data)
    print(d[0].keys())

