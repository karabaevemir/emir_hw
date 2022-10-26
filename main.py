from aiogram.utils import executor
from config import bot, dp
import logging
from handlers import admin, callback, extra, client, notifications
from database.bot_db import sql_create
import asyncio

async def on_startup(_):
    sql_create()
asyncio.create_task(notifications.scheduler())
client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
admin.register_handlers_admin(dp)
notifications.register_handlers_notification(dp)
extra.register_handlers_extra(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)