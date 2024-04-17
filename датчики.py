import telebot;
import socket
s.bind(('localhost', 3030)) # Привязываем серверный сокет к localhost и 3030 порту.
s.listen(1) # Начинаем прослушивать входящие соединения
conn, addr = s.accept()
while True: # Создаем вечный цикл.
	data = conn.recv(1024) # Получаем данные из сокета.
	if not data:
		break
	conn.sendall(data) # Отправляем данные в сокет.
	print(data.decode('utf-8')) # Выводим информацию на печать.
conn.close()
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 3030)) # Подключаемся к нашему серверу.
s.sendall('Hello, Habr!'.encode('utf-8')) # Отправляем фразу.
data = s.recv(1024) #Получаем данные из сокета.
s.close()





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




bot.polling(none_stop=True, interval=0)



