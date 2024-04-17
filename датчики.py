import telebot
# import socket
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# s.bind(('localhost', 3030))
# s.listen(1)
# conn, addr = s.accept()
#
# while True:
# 	data = conn.recv(1024)
# 	if not data:
# 		break
# 	conn.sendall(data)
# 	print(data.decode('utf-8'))
# conn.close()





from telebot import types
bot = telebot.TeleBot('6811531765:AAGQVyp0f8ixax-yLyahBw_MK7sJbBUMIJM');
@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message):
    if message.text == "45":
        bot.send_message(message.from_user.id, "Горячий-охлаждаю")
    elif message.text == "/temp":
        bot.send_message(message.from_user.id, "напиши температуру")
    else:
        bot.send_message(message.from_user.id, "Температера. Напиши /temo.")



    if message.text == "исправен":
        bot.send_message(message.from_user.id, "ок")
    elif message.text == "/sostoy":
        bot.send_message(message.from_user.id, "напиши состояние")
    else:
        bot.send_message(message.from_user.id, "состояние. Напиши /sostoy.")



    if message.text == "вправо":
        bot.send_message(message.from_user.id, "ок")
    elif message.text == "/dvpravo":
        bot.send_message(message.from_user.id, "напиши направление")
    else:
        bot.send_message(message.from_user.id, "движение. Напиши /dvpravo.")




bot.polling(none_stop=True, interval=0)



