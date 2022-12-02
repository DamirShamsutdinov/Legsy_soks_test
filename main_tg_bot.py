import json
import os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from dotenv import load_dotenv

from main_parsing_async import get_data

load_dotenv()

bot = Bot(token=os.getenv("TOKEN"))
dp = Dispatcher(bot, storage=MemoryStorage())

start_buttons = ['Москва']
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(*start_buttons)


class SearchParameters(StatesGroup):
    articul = State()


@dp.message_handler(commands=["start"])
async def command_start(message: types.Message):
    await message.answer(
        'Привет! Выбери город',
        reply_markup=keyboard
    )


@dp.message_handler(Text(equals='Москва'), state="*")
async def get_city(message: types.Message, state: FSMContext):
    await message.answer(
        'Введи артикул товара или несколько (чз пробел)',
    )
    await state.set_state(SearchParameters.articul.state)


@dp.message_handler(state=SearchParameters.articul)
async def post_data(message: types.Message):
    try:
        list_com = [int(i) for i in message.text.split()]
        await get_data(articuls_list=list_com)
    except Exception:
        await message.answer(
            "Данные введены некорректно, попробуйте еще раз!\n"
            "Либо обратитесь к разработчикам."
        )
    else:
        # print("Very good")
        with open("result_data.json", encoding="utf8") as file:
            data = json.load(file)
        for item in data:
            card = (
                f"{item['pr_articul']} - "
                f"{item['pr_name']} - "
                f"{item['pr_page']}"
            )
            await message.answer(card)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
