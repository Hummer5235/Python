import json


# my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# with open('my_dict.json', 'w') as f:
#     json.dump(my_dict, f)

with open('my_dict.json', 'r+') as f:
    my_dict = json.load(f)
    f.seek(0)
    json.dump(my_dict,f)


print(my_dict)