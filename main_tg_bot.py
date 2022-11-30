import json

from aiogram import Bot, Dispatcher, executor, types

from main_parsing_async import get_data

TOKEN = "5965362552:AAFiQZESJXjKaOmClto7jRQf9hB_k2a_cCc"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start_message(message: types.Message):
    await message.answer(
        "Введите артикул товара или несколько (чз пробел)",
    )


@dp.message_handler()
async def post_data(message: types.Message):
    try:
        list_com = [int(i) for i in message.text.split()]
        await get_data(articuls_list=list_com)
    except:
        await message.answer(f"Данные введены некорректно, попробуйте еще раз!\n"
                             f"Либо обратитесь к разработчикам.")
    else:
        print('Very good')
        with open("result_data.json", encoding='utf8') as file:
            data = json.load(file)
        for item in data:
            card = f'{item["pr_articul"]} - {item["pr_name"]} - {item["pr_page"]}'
            await message.answer(card)


def main():
    executor.start_polling(dp)


if __name__ == "__main__":
    main()
