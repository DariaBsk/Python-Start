import telebot
from telebot import types
import random

total_sweets = 15
candies_one_turn = 5
turn = 0
token="6175966424:AAHLcvyuSMWJhG_zId1pJx3mzQO8roZ1FAk"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start']) # Вызов функции посл ведения /start
def start(message):
    bot.send_message(message.chat.id, f'''Привет, {str(message.from_user.first_name)}! Это бот игры в конфеты.\n
    Правила игры: На столе лежит, например: 221 конфета. Играют два игрока делая ход друг после друга.\n
    Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем, например: 28 конфет.\n
    Все конфеты оппонента достаются сделавшему последний ход, то есть выигрывает тот кто взял последние конфеты.''') 
    bot.send_message(message.chat.id, f'Если хочешь сыграть, введи команду: /game')

@bot.message_handler(commands=['game']) # Вызов функции после ведения /game
def button_game(message):
    keyboard = types.ReplyKeyboardMarkup(True, True) #две кнопки в два столбца
    button_start = types.KeyboardButton("start")
    but_total_sweets = types.KeyboardButton("Всего конфет")
    but_candies_one_turn = types.KeyboardButton("Конфет за 1 ход")
    but_start_game = types.KeyboardButton("Let's go")
    keyboard.add(but_total_sweets, but_candies_one_turn)
    keyboard.row(button_start, but_start_game)

    bot.send_message(message.chat.id, 'Введи данные для игры, через кнопки', reply_markup=keyboard)

################################
def input_total_sweet(message):
    global total_sweets
    total_sweets = int(message.text)
    bot.send_message(message.chat.id, f'Вы ввели: {total_sweets} конфет')

def input_candies_one_turn(message):
    global candies_one_turn
    candies_one_turn = int(message.text)
    bot.send_message(message.chat.id, f'Вы ввели: {candies_one_turn} конфет, которые можно взять за один ход')


def input_bot():
    global turn
    if candies_one_turn == total_sweets:
            turn = candies_one_turn
    elif total_sweets%candies_one_turn==0:
            turn = candies_one_turn-1
    else: 
            turn = total_sweets%candies_one_turn-1
    if turn == 0:
            turn = 1
    return turn

def input_turn(message):
    turn = int(message.text)
    bot.send_message(message.chat.id, f'Вы ввели: {turn} конфет.')
    return turn

######################################

@bot.message_handler(content_types=['text']) #можно фото, видио, аудио
def controller(message):
    if message.text == "Всего конфет":
       bot.send_message(message.chat.id, f'Введите общее количество конфет для игры: ')
       bot.register_next_step_handler(message, input_total_sweet)
    if message.text == "Конфет за 1 ход":
       bot.send_message(message.chat.id, f'Введите максимальное количество конфет, которое можно взять за один ход: ')
       bot.register_next_step_handler(message, input_candies_one_turn)
    if message.text == "Let's go":
       game_sweets(message)
    if message.text == "game":
       game_sweets(message)  
    if message.text == ("start"):
       start(message)

def game_sweets(message):
    global total_sweets, candies_one_turn, turn
    player_1 = str(message.from_user.first_name)
    player_2 = "Smart bot"

    bot.send_message(message.chat.id, f'Начнем! Общее колличество конфет: {total_sweets}, количество конфет за один ход: {candies_one_turn}.\n{player_1} против {player_2}.\n Удачи {player_1}!')
    toss = random.choice([player_1, player_2])
    bot.send_message(message.chat.id, f'Первый ходит {toss}: ')

    while total_sweets > 0:
        if toss == player_1:
           bot.send_message(message.chat.id, f"{toss}, возьмите конфеты, но не больше {candies_one_turn}: ")
           bot.register_next_step_handler(message, input_turn)

        else:
            input_bot()
            bot.send_message(message.chat.id, f"bot взял {turn} конфет")

        total_sweets = total_sweets - turn

        if total_sweets > 0:
            bot.send_message(message.chat.id, f"Осталось {total_sweets} конфет.")

        else:
            bot.send_message(message.chat.id, f"Конфет больше нет, победил {toss}! Поздравляем!")
            break
        toss = player_2 if toss == player_1 else player_1

bot.infinity_polling()