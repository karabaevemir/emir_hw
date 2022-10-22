import sqlite3
import random
from config import bot


def sql_create():
    global db, cursor
    db = sqlite3.connect('bot.sqlite3')
    cursor = db.cursor()

    db.execute("CREATE TABLE IF NOT EXISTS mentors "
               "(id INTEGER PRIMARY KEY, name TEXT, "
               "direction TEXT, age INTEGER, "
               "group TEXT)")
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO mentors VALUES (?, ?, ?, ?, ?)", tuple(data.values()))
        db.commit()


async def sql_command_random(message):
    result = cursor.execute("SELECT * FROM mentors").fetchall()
    random_user = random.choice(result)
    await bot.send_message(message.from_user.id,
                           f"Id: {random_user[0]}, Name: {random_user[1]}, Direction: {random_user[2]},"
                           f"Age: {random_user[3]}, Group: {random_user[4]}")


async def sql_command_all():
    return cursor.execute("SELECT * FROM mentors").fetchall()


async def sql_command_delete(user_id):
    cursor.execute("DELETE FROM mentors WHERE id = ?", (user_id,))
    db.commit()
