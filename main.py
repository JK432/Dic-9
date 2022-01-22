# Create a dictionary with empty items. Write a python program to drop empty items from the given dictionary
dict1 = {'name': 'SK302', 'age': '19', 'phno':None}

print("after dropping empty items:")
dict1 = {key:value for (key, value) in dict1.items() if value is not None}
print(dict1)