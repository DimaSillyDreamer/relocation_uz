from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardRemove
from data_base import sqllite_db
from create_bot import dp, bot
from keybords import kb_client_transport, kb_client_bank, kb_client_connection, kb_client_currency, kb_client_shops, kb_client_citizenship,\
    kb_client_medcine, kb_client_documents, kb_client_culture, kb_client_work, kb_client_appartments, kb_client_free_time, kb_client_documents
from text_input import citizenship               

#@dp.message_handler(commands=['start', 'help'])
async def commands_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Привет я могу рассказать о важных для релокации вещах')
        await message.delete()
    except:
        await message.reply('Общение с ботом через личные сообщения, напишите ему:\nhttps://t.me/relocant_UZ_bot')

# @dp.message_handler(commands=['Транспорт'])
async def command_transport(message : types.Message):
    photo = open('pictures/1.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo, reply_markup=kb_client_transport)

async def command_connection(message : types.Message):
    photo = open('pictures/1.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo, reply_markup=kb_client_connection)

async def command_bank(message : types.Message):
    photo = open('pictures/1.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo, reply_markup=kb_client_bank)

async def command_medcine(message : types.Message):
    photo = open('pictures/1.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo, reply_markup=kb_client_medcine)

async def command_documents(message : types.Message):
    photo = open('pictures/1.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo, reply_markup=kb_client_documents)

async def command_work(message : types.Message):
    photo = open('pictures/1.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo, reply_markup=kb_client_work)

async def command_connection_details(message : types.Message):
    photo = open('pictures/1.jpg', 'rb')
    if message.text == 'Работает ли российская симка':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.', reply_markup=ReplyKeyboardRemove())
    if message.text == 'Как получить карту в местном банке':
        await bot.send_photo(message.from_user.id, photo, reply_markup=kb_client_currency)
    if message.text == 'В сумах':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'В долл':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'Где взять местную симку':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'Что такое imei и что с ним делать':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'Самый выгодный местный оператор (мнение релокантов)':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'Как получить деньги с карты не уз':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'Как открыть счёт в местном банке':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'Какие документы нужны':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'Как вывести деньги через золотую корону':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'Условия получения карт крупнейших банков уз':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'Супермаркеты':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'Рынки':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'Список ТЦ':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'Строительные/все для дома':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'Жизнь без регистрации)))':
        await bot.send_message(message.from_user.id, citizenship['registartion'], reply_markup=ReplyKeyboardRemove(), parse_mode='html')
    if message.text == 'Временная регистрация':
        await bot.send_message(message.from_user.id, citizenship['temp_registr'], reply_markup=ReplyKeyboardRemove(), parse_mode='html')
    if message.text == 'Внж':
        await bot.send_message(message.from_user.id, citizenship['resident_card'], reply_markup=ReplyKeyboardRemove(), parse_mode='html')
    if message.text == 'Гражданство':
        await bot.send_message(message.from_user.id, citizenship['citezenship_forever'], reply_markup=ReplyKeyboardRemove(), parse_mode='html')
    if message.text == 'Специалисты':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'Стоматология':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'Экстренная помощь':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'Где получить доверенность':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'Как оформить доверенность':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'Запись в консульство':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'Правила культуры':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'Как есть плов':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'Где искать работу':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'Какие документы нужны нерезидента':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'Налогообложение нерезидентов':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'Где искать квартиру на долгосрок':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'Как оформить регистрацию':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'Каков максимальный срок регистрации, условия продления':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'Список проверенных (на опыте релокантов) риелторов':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'Еда':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'Парки':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'Достопримечательности':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'Театры':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'экскурсии, гиды':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'Какие виды транспорта есть в уз':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'Сколько стоит и как платить в общественном транспорте':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'Где посмотреть маршрут':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'Заказ такси':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text == 'Аренда авто':
        await bot.send_message(message.from_user.id, 'скоро здесь появится информация\n\n\n\n\nдля выбора категории жмите меню.')
    if message.text.isdigit():
        amount = int(message.text)
        rubles = round(amount * 0.0057, 2)
        dollars = round(amount * 0.000092, 2)
        await bot.send_message(message.from_user.id, f'Это примерно..\nRUB {rubles}\nUSD {dollars}')
    
async def command_culture(message : types.Message):
    photo = open('pictures/1.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo, reply_markup=kb_client_culture)

async def command_culture(message : types.Message):
    photo = open('pictures/1.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo, reply_markup=kb_client_culture)

async def command_shops(message : types.Message):
    photo = open('pictures/1.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo, reply_markup=kb_client_shops)


async def command_citizenship(message : types.Message):
    photo = open('pictures/1.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo, reply_markup=kb_client_citizenship)
    
async def command_appartments(message : types.Message):
    photo = open('pictures/1.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo, reply_markup=kb_client_appartments)
    
async def command_free_time(message : types.Message):
    photo = open('pictures/1.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo, reply_markup=kb_client_free_time)
    
async def offers(message: types.Message):
     await sqllite_db.sql_read(message)
    
# @dp.message_handler(content_types=['text'])



def register_handlers_client(dp : Dispatcher):
    
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(command_transport, commands=['transport'])
    dp.register_message_handler(command_work, commands=['work'])
    dp.register_message_handler(command_connection, commands=['connection'])    
    dp.register_message_handler(command_bank, commands=['bank'])   
    dp.register_message_handler(command_shops, commands=['shops'])
    dp.register_message_handler(command_citizenship, commands=['citezenship'])
    dp.register_message_handler(command_medcine, commands=['medcine'])
    dp.register_message_handler(command_culture, commands=['culture'])
    dp.register_message_handler(command_appartments, commands=['appartments'])
    dp.register_message_handler(command_free_time, commands=['free_time'])
    dp.register_message_handler(command_documents, commands=['documents'])
    
    # dp.register_message_handler(offers, commands=['offers'])
    dp.register_message_handler(command_connection_details)
    

