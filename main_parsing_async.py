import asyncio
import json
import logging

import aiohttp

logging.basicConfig(
    level=logging.DEBUG,
    filename='main.log',
    filemode='w',
    format='%(asctime)s, %(levelname)s, %(message)s, %(name)s'
)


async def get_url(pages):
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    }
    search_list = []
    async with aiohttp.ClientSession() as session:
        for page in pages:
            async with session.get(
                    f"https://catalog.wb.ru/catalog/men_clothes2/catalog?appType=1&couponsGeo=12,3,18,15,21&curr=rub&dest=-1029256,-102269,-2162196,-1257786&emp=0&kind=1&lang=ru&locale=ru&page={page}&pricemarginCoeff=1.0&reg=1&regions=80,64,83,4,38,33,70,82,69,68,86,75,30,40,48,1,22,66,31,71&sort=popular&spp=28&sppFixGeo=4&subject=177;284;4853",
                    headers=headers,
            ) as response:
                r = await response.json(content_type=None)
                search_list.append(r["data"]["products"])
        return search_list


async def get_data(articuls_list):
    products_list = []
    count = 1
    curch_pages = range(1, 101)
    products = await get_url(curch_pages)
    for sub_item in products:
        for item in sub_item:
            for articul in articuls_list:
                if item["id"] == articul:
                    products_list.append(
                        {
                            "pr_articul": item["id"],
                            "pr_name": item["name"],
                            "pr_page": count,
                        }
                    )
        count += 1
    with open("result_data.json", mode="w", encoding="utf8") as f:
        json.dump(products_list, f, indent=4, ensure_ascii=False)


# """ПРОВЕРКА async парсинга - прошла успешна"""
# a_list = [
#     86210392,
#     39408901,
#     100749785,
#     43127482,
#     44325545,
#     64746739,
#     54673003,
#     74746118,
# ]
# asyncio.get_event_loop().run_until_complete(get_data(articuls_list=a_list))


# input_str = '39408901 100749785 43127482 64746739 54673003 74746118'
# list1 = [int(i) for i in input_str.split()]
# async def collect_data(add_list: list) -> json:
#     await get_data(add_list)
# if __name__ == '__main__':
#     start_time = time.time()
#     sup_value = asyncio.get_event_loop().run_until_complete(get_data(list1))
#     print('--- %s seconds ---' % (time.time() - start_time))
