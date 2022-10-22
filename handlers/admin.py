from aiogram import types, Dispatcher
from config import bot, ADMINS, dp
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.bot_db import sql_command_all, sql_command_delete


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(delete_data(), commands=["del"])
    dp.register_callback_query_handler(
        complete_delete,
        lambda call: call.data and call.data.startswith("delete ")
    )


async def delete_data(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.answer("Ты не мой босс!")
    else:
        users = await sql_command_all()
        for user in users:
            await bot.send_message(message.from_user.id, f"{user[0]}"
                                                         f"{user[1]}, {user[2]}, {user[3]}, "
                                                         f"{user[4]}",
                                    reply_markup =InlineKeyboardMarkup().add(
                                        InlineKeyboardButton(f"delete {user[3]}",
                                                                callback_data=f"delete {user[0]}")
                                    ))


async def complete_delete(call: types.CallbackQuery):
    await sql_command_delete(int(call.data.replace('delete ', '')))
    await call.answer(text="Deletion from the database was successful!", show_alert=True)
    await bot.delete_message(call.message.chat.id, call.message.message_id)

