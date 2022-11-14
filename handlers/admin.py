from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import dp, bot
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from data_base import sqllite_db
from keybords.admin_kb import button_case_admin
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


ID = None

class FSMAdmin(StatesGroup):
    photo1 = State()
    photo2 = State()
    adress = State()
    discription = State()
    price = State()
    
    
# @dp.message_handler(commands=['moderator'], is_chat_admin=True)
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'what are you want, Boss?', reply_markup=button_case_admin)
    await message.delete()

# @dp.message_handler(commands='Загрузить', state=None)
async def cm_start(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.photo1.set()
        await bot.send_message(message.from_user.id, 'Загрузи фото')

# @dp.message_handler(state='*', commands='cancel')
# @dp.message_handler(Text(equals='cancel', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return
        await state.finish()
        await message.reply('OK')


# @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo1)
async def load_photo(message: types.Message, state=FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo1'] = message.photo[0].file_id
        await FSMAdmin.next()
        await bot.send_message(message.from_user.id, 'Загрузи второе фото')

# @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo2)
async def load_photo2(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo2'] = message.photo[0].file_id
        await FSMAdmin.next()
        await bot.send_message(message.from_user.id, 'Введи адрес')

# @dp.message_handler(state=FSMAdmin.adress)
async def load_adress(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['adress'] = message.text
        await FSMAdmin.next()
        await bot.send_message(message.from_user.id, 'Введи описание')


# @dp.message_handler(state=FSMAdmin.discription)
async def load_discription(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['discription'] = message.text
        await FSMAdmin.next()
        await bot.send_message(message.from_user.id, 'Введи цену')

# @dp.message_handler(state=FSMAdmin.price)
async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = message.text
        
        await sqllite_db.sql_add_command(state)
        await state.finish()

# dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def del_callback_run(call: types.CallbackQuery):
    await sqllite_db.sql_delete_command(call.data.replace('del ', ''))
    await call.answer(text=f'{call.data.replace("del ", "")} удалена.', show_alert=True)




# @dp.message_handler(commands='delete')
async def delete_offer(message: types.Message):
    if message.from_user.id == ID:
        read = await sqllite_db.sql_read2()
        for ret in read:
            await bot.send_photo(message.from_user.id, ret[0], f'{ret[2]}\nОписание: {ret[3]}\nЦена: {ret[-1]}')
            await bot.send_message(message.from_user.id, text='^^^', reply_markup=InlineKeyboardMarkup().\
                add(InlineKeyboardButton(f'Удалить {ret[2]}', callback_data=f'del {ret[2]}')))






def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(cm_start, commands=['load'], state=None)
    dp.register_message_handler(cancel_handler, state='*', commands='cancel')
    dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(make_changes_command, commands=['moderator'], is_chat_admin=True)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo1)
    dp.register_message_handler(load_photo2, content_types=['photo'], state=FSMAdmin.photo2)
    dp.register_message_handler(load_adress, state=FSMAdmin.adress)
    dp.register_message_handler(load_discription, state=FSMAdmin.discription)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_callback_query_handler(del_callback_run, lambda x: x.data and x.data.startswith('del '))
    dp.register_message_handler(delete_offer, commands='delete')
