import sqlite3

from aiogram import types, Dispatcher
from config import bot, DESTINATION
from database.sql_commands import Database
from keyboards.inline_buttons import start_keyboard
from const import START_MENU


async def start_button(message: types.Message):
    print(message)
    db = Database()
    db.sql_insert_users(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )

    # with open(DESTINATION + "/bot_pic.jpeg", 'rb') as photo:
    #     await bot.send_photo(
    #         chat_id=message.from_user.id,
    #         photo=photo,
    #         caption=START_MENU.format(
    #             user=message.from_user.first_name
    #         ),
    #         reply_markup=await start_keyboard()
    #     )

    with open(DESTINATION + "bot_ani.gif", 'rb') as animation:
        await bot.send_animation(
            chat_id=message.from_user.id,
            animation=animation,
            caption=START_MENU.format(
                user=message.from_user.first_name
            ),
            reply_markup=await start_keyboard()
        )


def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(start_button, commands=['start'])
