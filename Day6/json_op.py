import json

#load the file with json and turns in to dictionary
data = []
with open('data.json', 'r') as f:
    data = json.load(f)

#chages the dictionary to string
json_str = json.dumps(data[0])

print(json_str)
print(type(json_str))

#loads the json string and converts to the dictionary
temp = json.loads(json_str)
print(type(temp))

#save the dictionary to the opened file
with open('second.json', 'w') as f:
    json.dump(temp, f)