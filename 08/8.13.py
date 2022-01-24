import json

with open("sample4.json") as file:
    data = json.load(file)

for k,v in data.items():
    print(k,":",v)
