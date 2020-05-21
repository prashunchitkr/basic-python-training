import json
'''
load
loads
dump
dumps
'''

#loads from dir
data = []
with open('data.json', 'r') as f:
    data = json.load(f)

print(data[0]['userId'])
print(type(data[0]))

#loads from string
dict_str = '{"name": "test", "age": 12}'
print(type(dict_str))
dict_obj = json.loads(dict_str)
print(type(dict_obj))


#writes to string
with open('try.json', 'w') as f:
    json.dump(dict_obj, f)


#object to string
dict_obj = {"name": "test", "age": 12}
dict_str = json.dumps(dict_obj)
print(type(dict_str))
