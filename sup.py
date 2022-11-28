import json
from pprint import pprint

with open('catch_product.json', 'r', encoding='utf8') as file:
    data = json.load(file)
for i in data:
    print(i)
print()
pprint(data)
