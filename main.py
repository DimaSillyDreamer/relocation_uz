
from aiogram.utils import executor
from config import TOKEN
from create_bot import dp
from handlers import client, admin, other
import os
from data_base import sqllite_db




async def on_startup(_):
    print('Bot is online')
    sqllite_db.sql_start()

admin.register_handlers_admin(dp)
client.register_handlers_client(dp)



executor.start_polling(dp, skip_updates=False, on_startup=on_startup)


