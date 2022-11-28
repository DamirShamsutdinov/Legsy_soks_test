import json
from pprint import pprint

with open('catch_product.json', 'r', encoding='utf8') as file:
    data = json.load(file)
for i in data:
    print(i)
print()
pprint(data)


# a = [12, 213, 323, 545, 234, 67, 7, 4, 3, 2, 1]
# l = []
#
# for i in range(20):
#     try:
#         print(a[i])
#         l.append(i)
#     except:
#         print(f'Страницы {i} не существует')
#         break
# print(l)
