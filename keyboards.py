from aiogram.types import InlineKeyboardMarkup , InlineKeyboardButton , ReplyKeyboardMarkup , KeyboardButton


b01 = KeyboardButton('/calculator')
start_kb = ReplyKeyboardMarkup(resize_keyboard=True)
start_kb.add(b01)

kb = InlineKeyboardMarkup(row_width=4)
b1 = InlineKeyboardButton(' ', callback_data='no')
b2 = InlineKeyboardButton('C', callback_data='C')
b3 = InlineKeyboardButton('<=', callback_data='<=')
b4 = InlineKeyboardButton('/', callback_data='/')
b5 = InlineKeyboardButton('7', callback_data='7')
b6 = InlineKeyboardButton('8', callback_data='8')
b7 = InlineKeyboardButton('9', callback_data='9')
b8 = InlineKeyboardButton('*', callback_data='*')
b9 = InlineKeyboardButton('4', callback_data='4')
b10 = InlineKeyboardButton('5', callback_data='5')
b11 = InlineKeyboardButton('6', callback_data='6')
b12 = InlineKeyboardButton('-', callback_data='-')
b13 = InlineKeyboardButton('1',callback_data='1')
b14 = InlineKeyboardButton('2', callback_data='2')
b15 = InlineKeyboardButton('3', callback_data='3')
b16 = InlineKeyboardButton('+' , callback_data='+')
b17 = InlineKeyboardButton(' ', callback_data='no')
b18 = InlineKeyboardButton('0' , callback_data='0')
b19 = InlineKeyboardButton(',', callback_data=',')
b20 = InlineKeyboardButton('=', callback_data='=')

kb.add(b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19,b20)