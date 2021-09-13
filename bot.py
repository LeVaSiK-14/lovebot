import telebot
from random import choice

TOKEN = '1907783142:AAH7m3KCzlM4t4TV24L_EhfVCnsUJlWtRF8'

bot = telebot.TeleBot(TOKEN)

love_text1 = 'I love you, my princess❤️❤️'
love_text2 = 'Ты самая лучшая❤️❤️'
love_text3 = 'Я люблю тебя❤️❤️'
love_text4 = 'Ты самая красивая❤️❤️'
love_text5 = 'Ты моя принцесса❤️❤️'
love_text6 = 'Ты самая милая❤️❤️'

love_arr = [love_text1, love_text2, love_text3, love_text4, love_text5, love_text6]

@bot.message_handler(commands=['start'])
def send_mess_love(message):
    chat_id = message.chat.id
    
    bot.send_message(chat_id, 'Привет, введи число от 1 до 100 :)')



@bot.message_handler(content_types=['text'])
def send_mess_love(message):
    chat_id = message.chat.id
    lola_id = 1177312416
    try:
        quantity = int(message.text) + 1
        for i in range(1, quantity):
            rand_love = (f'{i}) {choice(love_arr)}')
            night = 'Спокойной ночи❤️❤️\nсладких снов❤️❤️\nлюблю тебя❤️❤️'
            photo = 'Скинь фотку зай🥺🥺❤️'

            bot.send_message(lola_id, rand_love)
    except:
        bot.send_message(chat_id, 'Введи число дурочка моя😂😂')

# @bot.message_handler(content_types=['document'])
# def handle_docs_photo(message):
#     try:
#         chat_id = message.chat.id

#         file_info = bot.get_file(message.document.file_id)
#         downloaded_file = bot.download_file(file_info.file_path)

#         src = '/Users/user/Desktop/loveBot/lola/' + message.document.file_name;
#         with open(src, 'wb') as new_file:
#             new_file.write(downloaded_file)

#         bot.reply_to(message, "Пожалуй, я сохраню это")
#     except Exception as e:
#         bot.reply_to(message, e)


if __name__ == '__main__':
    bot.polling(none_stop = True)