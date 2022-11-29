import asyncio
import json

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text

from main_parsing_async import get_data

TOKEN = "5965362552:AAFiQZESJXjKaOmClto7jRQf9hB_k2a_cCc"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start_message(message: types.Message):
    await message.answer(
        "Введите артикул товара или несколько (чз пробел)"
    )


@dp.message_handler(Text(equals="Мужские костюмы"))
async def get_discount_sneakers(message: types.Message):
    try:
        # sup_value = message.text
        # print(sup_value)
        list2 = [int(i) for i in message.text.split()]
        asyncio.get_event_loop().run_until_complete(
            get_data(articuls_list=list2)
        )
    except:
        print('Неправильные вводные данные')
    else:
        with open("result_data.json") as file:
            data = json.load(file)
    for item in data:
        card = f"{item['pr_articul']} {item['pr_name']} {item['pr_page']}"
        await message.answer(card)


def main():
    executor.start_polling(dp)


if __name__ == "__main__":
    main()
