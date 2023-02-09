#на столе лежат конфеты...
# def controller(message):
# От Артур Балухтин всем 09:05 PM
def bot_input(message):
    global sweets,bot_turn,flag
    if sweets <= max_sweet:
        bot_turn = sweets
    elif sweets % max_sweet == 0:
        bot_turn = max_sweet - 1
    else:
        bot_turn = sweets % max_sweet - 1
        if bot_turn == 0:
            bot_turn = 1
    sweets -= bot_turn
    bot.send_message(message.chat.id, f"бот взял {bot_turn} конфет")
    bot.send_message(message.chat.id, f"осталось {sweets}")
    flag = "user" if flag == "bot" else "bot"
    controller(message)

def user_input(message):
    global flag,user_turn,sweets
    user_turn = int(message.text)
    sweets -= user_turn
    bot.send_message(message.chat.id, f"осталось {sweets}")
    flag = "user" if flag == "bot" else "bot"
    controller(message)

bot.infinity_polling()
# 1. Прикрутить бота к задачам с предыдущего семинара:
#     1. **Создать калькулятор для работы с рациональными и комплексными числами, организовать меню**
# От David всем 09:08 PM
# t.mr/guitaristdave
# t.me/guitaristdave
# От Андрей всем 09:12 PM
# 4 лекция
# есть  арзив с калькулятором
# архив

###
import telebot
import random
from telebot import types

bot = telebot.TeleBot("5607477987:AAE4TFU2qtOa4dw902y8VA-SHUFrFq8n-t8")
typeNums = 0


@bot.message_handler(commands=["start"])
@bot.message_handler(content_types=['text'])
def buttons(message):
    global typeNums
    a = types.ReplyKeyboardRemove()
    if message.text == 'Рациональные':
        bot.send_message(message.chat.id, f'Выбран режим рациональных чисел', reply_markup=a)
        bot.send_message(message.chat.id, f'Введите выражение разделяя пробелом')
        bot.register_next_step_handler(message, controller)
        typeNums = 0
    elif message.text == 'Комплексные':
        bot.send_message(message.chat.id, f'Выбран режим комплексных чисел', reply_markup=a)
        bot.send_message(message.chat.id, f'Введите выражение разделяя пробелом')
        bot.register_next_step_handler(message, controller)
        typeNums = 1
#
@bot.message_handler(co
От Иван Грабов всем 09:59 PM
def controller(message):
    line = message.text.split()
    znak = line[1]
    if typeNums == 0:
        a = int(line[0])
        b = int(line[2])
    else:
        a = complex(line[0])
        b = complex(line[2])

    if znak == '+':
        res = summ_nums(a, b)
    elif znak == '-':
        res = sub_nums(a, b)
    elif znak == '*':
        res = mult_nums(a, b)
    elif znak == '/':
        res = div_nums(a, b)
    elif typeNums == 1 and (znak == '//' or znak == '%'):
        bot.send_message(message.chat.id, f'Неверный ввод, повторите')
        bot.register_next_step_handler(message, controller)
        return
    elif znak == '//':
        res = div_int(a, b)
def summ_nums(a, b):
    return a + b


def sub_nums(a, b):
    return a - b


def mult_nums(a, b):
    return a * b


def div_nums(a, b):
    return a / b


def div_int(a, b):
    return a // b


def div_rem(a, b):
    return a % b


bot.infinity_polling()

#####
import telebot
@bot.message_handler(co
От Иван Грабов всем 09:59 PM
def controller(message):
    line = message.text.split()
    znak = line[1]
    if typeNums == 0:
        a = int(line[0])
        b = int(line[2])
    else:
        a = complex(line[0])
        b = complex(line[2])

    if znak == '+':
        res = summ_nums(a, b)
    elif znak == '-':
        res = sub_nums(a, b)
    elif znak == '*':
        res = mult_nums(a, b)
    elif znak == '/':
        res = div_nums(a, b)
    elif typeNums == 1 and (znak == '//' or znak == '%'):
        bot.send_message(message.chat.id, f'Неверный ввод, повторите')
        bot.register_next_step_handler(message, controller)
        return
    elif znak == '//':
        res = div_int(a, b)
def summ_nums(a, b):
    return a + b


def sub_nums(a, b):
    return a - b


def mult_nums(a, b):
    return a * b


def div_nums(a, b):
    return a / b


def div_int(a, b):
    return a // b


def div_rem(a, b):
    return a % b


bot.infinity_polling()

