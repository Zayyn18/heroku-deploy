from aiogram import Bot, types, Dispatcher, executor
from keyboards import *
from config import *
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
value = ''
old_value = ''
async def on_startup(_):
    print('Bot is online')


@dp.message_handler(commands=['start'])
async def get_message(message:types.Message):
    await bot.send_message(message.from_user.id , f'Привет {message.from_user.first_name}', reply_markup=start_kb)
    print(message.from_user)

@dp.message_handler(commands=['calculator'])
async def get_calculator(message:types.Message):
    global value
    if value == '':
        await bot.send_message(message.from_user.id, '0' ,reply_markup=kb)
    else:
        await bot.send_message(message.from_user.id , value, reply_markup=kb)

@dp.callback_query_handler(lambda call: True)
async def func(query):
    global value , old_value
    data = query.data

    if data == 'no':
        pass
    elif data =='C':
        value = ''
    elif data == '<=':
        if value != '':
            value = value[:len(value)-1]
    elif data == '=':
        try:
            value = str(eval(value))
        except:
            value = 'Ошибка!'
    else:
        value += data

    if (value != old_value and value != '') or ('0' != old_value and value == ''):
        if value == '':
            await bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text='0',reply_markup=kb)
            old_value = '0'
        else:
            await bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id , text=value , reply_markup=kb)
            old_value = value

    old_value=value
    if value == 'Ошибка!': value = ''


executor.start_polling(dp, skip_updates=True , on_startup=on_startup)