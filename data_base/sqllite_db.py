import sqlite3 as sq
from create_bot import bot
from aiogram.types import Message

def sql_start():
    global base, cur 
    base = sq.connect('suggestions')
    cur = base.cursor()
    if base:
        print('Data base connect OK!')
    base.execute('CREATE TABLE IF NOT EXISTS menu(photo1 TEXT, photo2 TEXT, adress TEXT PRIMARY KEY, discription TEXT, price TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES (?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_read(message):
    for ret in cur.execute('SELECT * FROM menu').fetchall():
       
        await bot.send_photo(message.from_user.id, ret[0])
        await bot.send_photo(message.from_user.id, ret[1])
        await bot.send_message(message.from_user.id, f'\nАдрес:{ret[2]}\nОписание{ret[3]}\nЦена{ret[-1]}')

async def sql_read2():
    return cur.execute('SELECT * FROM menu ').fetchall()

async def sql_delete_command(data):
    cur.execute('DELETE FROM menu WHERE adress == ?', (data,))
    base.commit()
