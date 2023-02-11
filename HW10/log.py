import telebot
import datetime

def log_data(message):
    timenow = datetime.datetime.now()
    callogfile = open('CalLogFile', "a")
    print(timenow.strftime("%d-%m-%Y %H:%M"), 'User ' + message.from_user.first_name, message.from_user.id, message.text, file=callogfile)