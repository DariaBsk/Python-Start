import telebot
import log

bot = telebot.TeleBot("6118043917:AAH8IEZ0K5Ygkr6xmLUWKdM3jciS1tmMwT0")

temp_data = ''
old_temp_data = ''

cal_keyboard = telebot.types.InlineKeyboardMarkup()
cal_keyboard.row(   telebot.types.InlineKeyboardButton("C", callback_data= "C"),
                    telebot.types.InlineKeyboardButton("<=", callback_data= "<="),
                    telebot.types.InlineKeyboardButton("mod", callback_data= "%"),
                    telebot.types.InlineKeyboardButton("div", callback_data= "//"),)

cal_keyboard.row(   telebot.types.InlineKeyboardButton("7", callback_data= "7"),
                    telebot.types.InlineKeyboardButton("8", callback_data= "8"),
                    telebot.types.InlineKeyboardButton("9", callback_data= "9"),
                    telebot.types.InlineKeyboardButton("/", callback_data= "/"))

cal_keyboard.row(   telebot.types.InlineKeyboardButton("4", callback_data= "4"),
                    telebot.types.InlineKeyboardButton("5", callback_data= "5"),
                    telebot.types.InlineKeyboardButton("6", callback_data= "6"),
                    telebot.types.InlineKeyboardButton("x", callback_data= "*"))

cal_keyboard.row(   telebot.types.InlineKeyboardButton("1", callback_data= "1"),
                    telebot.types.InlineKeyboardButton("2", callback_data= "2"),
                    telebot.types.InlineKeyboardButton("3", callback_data= "3"),
                    telebot.types.InlineKeyboardButton("-", callback_data= "-"))

cal_keyboard.row(   telebot.types.InlineKeyboardButton("0", callback_data= "0"),
                    telebot.types.InlineKeyboardButton(",", callback_data= "."),
                    telebot.types.InlineKeyboardButton("=", callback_data= "="),
                    telebot.types.InlineKeyboardButton("+", callback_data= "+"))


@bot.message_handler(commands=['start', 'calculater'])
def getMessage(message):
    global temp_data
    log.log_data(message)
    if temp_data == '': 
        bot.send_message(message.chat.id, '0', reply_markup=cal_keyboard)
    else:
         bot.send_message(message.chat.id, temp_data, reply_markup=cal_keyboard)


@bot.callback_query_handler(func=lambda call: True)
def controler(query):
    global temp_data, old_temp_data
    data = query.data
    if data == "C": temp_data = ''
    elif data == '<=':
        if temp_data != '':
            temp_data = temp_data[:len(temp_data)-1]

    elif data == "=": 
        try:
            temp_data = str(eval(temp_data))
        except:
            temp_data = "Ошибка!"

    else: temp_data += data

    if (temp_data != old_temp_data and temp_data != '') or ("0" != old_temp_data and temp_data == ''):
        if temp_data == '':
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text = '0', reply_markup=cal_keyboard)
        else:
            bot.edit_message_text(chat_id=query.message.chat.id, message_id=query.message.message_id, text = temp_data, reply_markup=cal_keyboard)


    old_temp_data = temp_data
    if temp_data == "Ошибка!": temp_data = ''




bot.polling(non_stop = False, interval=0) 