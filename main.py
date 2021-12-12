import aiogram
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

API_TOKEN = '5060862104:AAGJeWhtHK3vp8-VP7iUmlGo2bxpqhc360c'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


def main_menu_button():
    buttons = InlineKeyboardMarkup(row_width=2)

    zuy = InlineKeyboardButton(text='Зуй', callback_data='zuy')
    pantera = InlineKeyboardButton(text='Pantera', callback_data='pantera')
    oksana = InlineKeyboardButton(text='Oksana', callback_data='oksana')
    the_first = InlineKeyboardButton(text='Самый Первый', callback_data='the_first')

    buttons.add(zuy, pantera)
    buttons.add(oksana, the_first)

    return buttons


@dp.message_handler(commands=['start'])
async def start_command_handler(message: types.Message):
    buttons = main_menu_button()

    mesg = 'Выберете бот который хотите перезагрузить:'
    await message.answer(mesg, reply_markup=buttons)


@dp.callback_query_handler(lambda c: c.data == 'zuy')
async def reboot_zuy(callback_query: types.CallbackQuery):
    command = 'echo futurist | sudo -S systemctl restart zuy.service'
    os.system(command)

    await callback_query.answer('Сделано!')


@dp.callback_query_handler(lambda c: c.data == 'pantera')
async def reboot_pantera(callback_query: types.CallbackQuery):
    command = 'echo futurist | sudo -S systemctl restart pantera.service'
    os.system(command)

    await callback_query.answer('Сделано!')


@dp.callback_query_handler(lambda c: c.data == 'oksana')
async def reboot_oksana(callback_query: types.CallbackQuery):
    command = 'echo futurist | sudo -S systemctl restart oksana.service'
    os.system(command)

    await callback_query.answer('Сделано!')


@dp.callback_query_handler(lambda c: c.data == 'the_first')
async def reboot_the_first(callback_query: types.CallbackQuery):
    command = 'echo futurist | sudo -S systemctl restart the_first.service'
    os.system(command)

    await callback_query.answer('Сделано!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
