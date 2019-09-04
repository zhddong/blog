import json

def load_config(path):
	with open(path,"r") as f:
		data = f.read()
		return json.loads(data)