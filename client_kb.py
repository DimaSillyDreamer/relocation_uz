from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

t1 = KeyboardButton('Какие виды транспорта есть в уз')
t2 = KeyboardButton('Сколько стоит и как платить в общественном транспорте')
t3 = KeyboardButton('Где посмотреть маршрут')
t4 = KeyboardButton('Заказ такси')
t5 = KeyboardButton('Аренда авто')

c1 = KeyboardButton('Работает ли российская симка')
c2 = KeyboardButton('Где взять местную симку')
c3 = KeyboardButton('Что такое imei и что с ним делать')
c4 = KeyboardButton('Самый выгодный местный оператор (мнение релокантов)')

m1 = KeyboardButton('Как получить деньги с карты не уз')
m2 = KeyboardButton('Как открыть счёт в местном банке')
m3 = KeyboardButton('Как получить карту в местном банке')
m4 = KeyboardButton('Какие документы нужны')
m5 = KeyboardButton('Как вывести деньги через золотую корону')
m6 = KeyboardButton('Условия получения карт крупнейших банков уз')

mm1 = KeyboardButton('В сумах')
mm2 = KeyboardButton('В долл')

s1 = KeyboardButton('Супермаркеты')
s2 = KeyboardButton('Рынки')
s3 = KeyboardButton('Список ТЦ')
s4 = KeyboardButton('Строительные/все для дома')

cit1 = KeyboardButton('Жизнь без регистрации)))')
cit2 = KeyboardButton('Временная регистрация')
cit3 = KeyboardButton('Внж')
cit4 = KeyboardButton('Гражданство')

med1 = KeyboardButton('Специалисты')
med2 = KeyboardButton('Стоматология')
med3 = KeyboardButton('Экстренная помощь')

doc1 = KeyboardButton('Где получить доверенность')
doc2 = KeyboardButton('Как оформить доверенность')
doc3 = KeyboardButton('Запись в консульство')

cult1 = KeyboardButton('Правила культуры')
cult2 = KeyboardButton('Как есть плов')

work1 = KeyboardButton('Где искать работу')
work2 = KeyboardButton('Какие документы нужны нерезидента')
work3 = KeyboardButton('Налогообложение нерезидентов')

ap1 = KeyboardButton('Где искать квартиру на долгосрок')
ap2 = KeyboardButton('Как оформить регистрацию')
ap3 = KeyboardButton('Каков максимальный срок регистрации, условия продления')
ap4 = KeyboardButton('Список проверенных (на опыте релокантов) риелторов')

fr1 = KeyboardButton('Еда')
fr2 = KeyboardButton('Парки')
fr3 = KeyboardButton('Театры')
fr4 = KeyboardButton('Достопримечательности')
fr5 = KeyboardButton('экскурсии, гиды')





kb_client_free_time = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client_appartments = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client_work = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client_culture = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client_shops = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client_transport = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client_bank = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client_connection = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client_currency = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client_citizenship = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client_medcine = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client_documents = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client_shops.add(s1).add(s2).add(s3).add(s4)
kb_client_currency.add(mm1).add(mm2)
kb_client_bank.add(m1).add(m2).add(m3).add(m4).add(m5).add(m6)
kb_client_transport.add(t1).add(t2).add(t3).add(t4).add(t5)
kb_client_connection.add(c1).add(c2).add(c3).add(c4)
kb_client_citizenship.add(cit1).add(cit2).add(cit3).add(cit4)
kb_client_medcine.add(med1).add(med2).add(med3)
kb_client_documents.add(doc1).add(doc2).add(doc3)
kb_client_culture.add(cult1).add(cult2)
kb_client_work.add(work1).add(work2).add(work3)
kb_client_appartments.add(ap1).add(ap2).add(ap3).add(ap4)
kb_client_free_time.add(fr1).add(fr2).add(fr3).add(fr4).add(fr5)
