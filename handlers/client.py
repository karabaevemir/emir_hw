from aiogram import types, Dispatcher
from database.bot_db import sql_command_random


async def get_random_user(message: types.Message):
    await sql_command_random(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(get_random_user, commands=['get'])

