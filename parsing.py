import hashlib
import json
from pprint import pprint

import requests


def get_data(articul,  products_list=[]):
    headers = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }

    pages = range(1, 7)
    count = 1

    for page in pages:
        response = requests.get(
            f'https://catalog.wb.ru/catalog/men_clothes2/catalog?appType=1&couponsGeo=12,3,18,15,21&curr=rub&dest=-1029256,-102269,-2162196,-1257786&emp=0&kind=1&lang=ru&locale=ru&page={page}&pricemarginCoeff=1.0&reg=1&regions=80,64,83,4,38,33,70,82,69,68,86,75,30,40,48,1,22,66,31,71&sort=popular&spp=27&sppFixGeo=4&subject=177;284;4853',
            headers=headers).json()
        products_ids = response['data']['products']

        for item in products_ids:
            if item['id'] == articul:
                products_list.append({
                    'pr_articul': item['id'],
                    'pr_name': item['name'],
                    'pr_page': count,
                })
                # print(products_list)
        count += 1
    return products_list

def add_prod_list(id):
    with open('catch_product.json', 'w', encoding='utf8') as file:
        json.dump(get_data(id), file, indent=4, ensure_ascii=False)


def main():
    add_prod_list(86210392)
    add_prod_list(39408901)
    add_prod_list(3358959)
    add_prod_list(43127482)
    add_prod_list(33589590)


if __name__ == '__main__':
    main()
