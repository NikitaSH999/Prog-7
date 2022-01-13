import json
handle = open('file.json')
data_str = handle.readlines()

data_dict = json.load(data_str)

with open('data.json') as f:
	data_dict = json.load(f)
