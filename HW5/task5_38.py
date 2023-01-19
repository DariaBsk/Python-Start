# 38.Напишите программу, удаляющую из текста все слова, содержащие "абв".

text = 'Аб абв где ежзабв, гдежз. Иклмноп абвгдеж, эюяабв.'

new_text= text.split()
clear_text = ''
for element in new_text:
    if not 'абв' in element:
        clear_text += element + ' '
print(clear_text)

