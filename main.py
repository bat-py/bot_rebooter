import aiogram
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from database import clear_table_members

API_TOKEN = '5315731872:AAHqvZx2j8KMxgDbL-KtJEp-dzu20JT61pw'
password = 'assfucker.'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


def main_menu_button():
    buttons = InlineKeyboardMarkup(row_width=2)

    samiykrasniybot = InlineKeyboardButton(text='Samiykrasniybot', callback_data='samiykrasniybot')
    samiykrasniybot2 = InlineKeyboardButton(text='Samiykrasniybot 2', callback_data='samiykrasniybot2')
    samiykrasniybot3 = InlineKeyboardButton(text='Samiykrasniybot 3', callback_data='samiykrasniybot3')
    samiykrasniybot4 = InlineKeyboardButton(text='Samiykrasniybot (Первый Информативный)', callback_data='samiykrasniybot4')
    samiykrasniybot_zapas = InlineKeyboardButton(text='Samiykrasniybot (Запасной бот)', callback_data='samiykrasniybot_zapas')
    samiykrasniybot5 = InlineKeyboardButton(text='Samiykrasniybot 5', callback_data='samiykrasniybot5')
    samiykrasniybot6 = InlineKeyboardButton(text='Samiykrasniybot 6', callback_data='samiykrasniybot6')
    samiykrasniybot7 = InlineKeyboardButton(text='Samiykrasniybot 7', callback_data='samiykrasniybot7')

    kd_bot1 = InlineKeyboardButton(text='kd_bot 1', callback_data='kd_bot1')
    kd_bot2 = InlineKeyboardButton(text='kd_bot 2', callback_data='kd_bot2')
    kd_bot3 = InlineKeyboardButton(text='kd_bot 3', callback_data='kd_bot3')
    dragsbarblack = InlineKeyboardButton(text='DRAGSBARBLACK', callback_data='dragsbarblack')
    oksana = InlineKeyboardButton(text='oksana', callback_data='oksana')
    oksana2 = InlineKeyboardButton(text='oksana 2', callback_data='oksana2')

    info_bot = InlineKeyboardButton(text='Info Bot', callback_data='info_bot')

    reboot = InlineKeyboardButton(text='Перезагрузить сервер', callback_data='reboot')

    buttons.add(samiykrasniybot)
    buttons.add(samiykrasniybot2)
    buttons.add(samiykrasniybot3)
    buttons.add(samiykrasniybot4)
    buttons.add(samiykrasniybot_zapas)
    buttons.add(samiykrasniybot5)
    buttons.add(samiykrasniybot6)
    buttons.add(samiykrasniybot7)
    buttons.add(kd_bot1)
    buttons.add(kd_bot2)
    buttons.add(kd_bot3)
    buttons.add(dragsbarblack)
    buttons.add(oksana)
    buttons.add(oksana2)
    buttons.add(info_bot)
#    buttons.add(reboot)

    return buttons


@dp.message_handler(commands=['start'])
async def start_command_handler(message: types.Message):
    buttons = main_menu_button()

    mesg = 'Выберете бот который хотите перезагрузить:'
    await message.answer(mesg, reply_markup=buttons)


@dp.callback_query_handler(lambda c: c.data == 'samiykrasniybot')
async def reboot_samiykrasniybot(callback_query: types.CallbackQuery):
    command = f'echo {password} | sudo -S systemctl restart samiykrasniybot.service'
    os.system(command)

    clear_table_members('')

    await callback_query.answer('Сделано!')


@dp.callback_query_handler(lambda c: c.data == 'samiykrasniybot2')
async def reboot_samiykrasniybot2(callback_query: types.CallbackQuery):
    command = f'echo {password} | sudo -S systemctl restart samiykrasniybot2.service'
    os.system(command)

    clear_table_members('2')

    await callback_query.answer('Сделано!')


@dp.callback_query_handler(lambda c: c.data == 'samiykrasniybot3')
async def reboot_samiykrasniybot3(callback_query: types.CallbackQuery):
    command = f'echo {password} | sudo -S systemctl restart samiykrasniybot3.service'
    os.system(command)

    clear_table_members('3')

    await callback_query.answer('Сделано!')


@dp.callback_query_handler(lambda c: c.data == 'samiykrasniybot4')
async def reboot_samiykrasniybot4(callback_query: types.CallbackQuery):
    command = f'echo {password} | sudo -S systemctl restart samiykrasniybot_first_information.service'
    os.system(command)

    await callback_query.answer('Сделано!')


@dp.callback_query_handler(lambda c: c.data == 'samiykrasniybot_zapas')
async def reboot_samiykrasniybot_zapas(callback_query: types.CallbackQuery):
    command = f'echo {password} | sudo -S systemctl restart samiykrasniybot_zapas.service'
    os.system(command)

    await callback_query.answer('Сделано!')


@dp.callback_query_handler(lambda c: c.data == 'samiykrasniybot5')
async def reboot_samiykrasniybot5(callback_query: types.CallbackQuery):
    command = f'echo {password} | sudo -S systemctl restart samiykrasniybot5.service'
    os.system(command)

    clear_table_members('5')

    await callback_query.answer('Сделано!')


@dp.callback_query_handler(lambda c: c.data == 'samiykrasniybot6')
async def reboot_samiykrasniybot6(callback_query: types.CallbackQuery):
    command = f'echo {password} | sudo -S systemctl restart samiykrasniybot6.service'
    os.system(command)

    clear_table_members('6')

    await callback_query.answer('Сделано!')


@dp.callback_query_handler(lambda c: c.data == 'samiykrasniybot7')
async def reboot_samiykrasniybot7(callback_query: types.CallbackQuery):
    command = f'echo {password} | sudo -S systemctl restart samiykrasniybot7.service'
    os.system(command)

    clear_table_members('7')

    await callback_query.answer('Сделано!')


@dp.callback_query_handler(lambda c: c.data == 'kd_bot1')
async def reboot_zuy(callback_query: types.CallbackQuery):
    command = f'echo {password} | sudo -S systemctl restart kd_bot1.service'
    os.system(command)

    await callback_query.answer('Сделано!')


@dp.callback_query_handler(lambda c: c.data == 'kd_bot2')
async def rebootsamiykrasniybot_pantera(callback_query: types.CallbackQuery):
    command = f'echo {password} | sudo -S systemctl restart kd_bot2.service'
    os.system(command)

    await callback_query.answer('Сделано!')


@dp.callback_query_handler(lambda c: c.data == 'kd_bot3')
async def rebootsamiykrasniybot_pantera(callback_query: types.CallbackQuery):
    command = f'echo {password} | sudo -S systemctl restart kd_bot3.service'
    os.system(command)

    await callback_query.answer('Сделано!')


@dp.callback_query_handler(lambda c: c.data == 'dragsbarblack')
async def rebootsamiykrasniybot_pantera(callback_query: types.CallbackQuery):
    command = f'echo {password} | sudo -S systemctl restart dragsbarblack.service'
    os.system(command)

    await callback_query.answer('Сделано!')


@dp.callback_query_handler(lambda c: c.data == 'oksana')
async def rebootsamiykrasniybot_pantera(callback_query: types.CallbackQuery):
    command = f'echo {password} | sudo -S systemctl restart oksana.service'
    os.system(command)

    await callback_query.answer('Сделано!')


@dp.callback_query_handler(lambda c: c.data == 'oksana2')
async def rebootsamiykrasniybot_pantera(callback_query: types.CallbackQuery):
    command = f'echo {password} | sudo -S systemctl restart oksana2.service'
    os.system(command)

    await callback_query.answer('Сделано!')


@dp.callback_query_handler(lambda c: c.data == 'info_bot')
async def rebootsamiykrasniybot_pantera(callback_query: types.CallbackQuery):
    command = f'echo {password} | sudo -S systemctl restart info_bot.service'
    os.system(command)

    await callback_query.answer('Сделано!')


@dp.callback_query_handler(lambda c: c.data == 'reboot')
async def reboot_server(callback_query: types.CallbackQuery):
    await callback_query.answer('Через 20 секунд боты начнут работать')

    command = f'echo {password} | sudo -S reboot'
    os.system(command)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
