import time
import hashlib
import json
from pprint import pprint
import asyncio
import aiohttp
import requests


def url(pages):
    headers = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }
    search_list = []

    for page in pages:
        response = requests.get(
            f'https://catalog.wb.ru/catalog/men_clothes2/catalog?appType=1&couponsGeo=12,3,18,15,21&curr=rub&dest=-1029256,-102269,-2162196,-1257786&emp=0&kind=1&lang=ru&locale=ru&page={page}&pricemarginCoeff=1.0&reg=1&regions=80,64,83,4,38,33,70,82,69,68,86,75,30,40,48,1,22,66,31,71&sort=popular&spp=27&sppFixGeo=4&subject=177;284;4853',
            headers=headers).json()
        products_ids = response['data']['products']
        search_list.append(products_ids)

    return search_list


def get_data(articul, products_list=[]):
    count = 1
    curch_pages = range(1, 7)

    products = url(curch_pages)

    for sub_item in products:
        for item in sub_item:
            if item['id'] == articul:
                products_list.append({
                    'pr_articul': item['id'],
                    'pr_name': item['name'],
                    'pr_page': count,
                })
        count += 1
    return products_list


def main():
    with open('catch_async.json', 'w', encoding='utf8') as file:
        json.dump(get_data(86210392), file, indent=4, ensure_ascii=False)
    with open('catch_async.json', 'w', encoding='utf8') as file:
        json.dump(get_data(39408901), file, indent=4, ensure_ascii=False)
    with open('catch_async.json', 'w', encoding='utf8') as file:
        json.dump(get_data(100749785), file, indent=4, ensure_ascii=False)
    with open('catch_async.json', 'w', encoding='utf8') as file:
        json.dump(get_data(43127482), file, indent=4, ensure_ascii=False)
    with open('catch_async.json', 'w', encoding='utf8') as file:
        json.dump(get_data(44325545), file, indent=4, ensure_ascii=False)
    with open('catch_async.json', 'w', encoding='utf8') as file:
        json.dump(get_data(64746739), file, indent=4, ensure_ascii=False)

    # get_data(86210392)
    # get_data(39408901)
    # get_data(100749785)
    # get_data(43127482)
    # get_data(44325545)
    # get_data(64746739)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print('--- %s seconds ---' % (time.time() - start_time))


