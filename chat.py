import sqlite3
import telebot

token = '2113777266:AAFuwhvyVTgiiOWP5yj3cwm81ZJlN70PrBQ'

bot = telebot.TeleBot(token)


connection = sqlite3.connect('PhoneBook.db')
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS contacts(
    userChatId INT PRIMARY KEY,
    userName TEXT,
    userContactNumber TEXT);
    """)
connection.commit()

@bot.message_handler(commands=['start'])
def send_description(message):
    bot.send_message(message.chat.id, '/add - добавить пользователя /check - получить данные от пользователя')

@bot.message_handler(commands=['add'])
def send_description(message):
    try:
        number = message.text
        local_connection = sqlite3.connect('PhoneBook.db')
        local_cursor = local_connection.cursor()
        local_cursor.execute("INSERT OR IGNORE INTO contacts VALUES(? ,? , ? );",
                             (message.chat.id, message.from_user.first_name , number))
        local_connection.commit()
        bot.send_message(message.chat.id, "Приятно познакомится ," + str(message.from_user.first_name))

    except Exception:
        bot.send_message(message.chat.id, "Вы уже в базе данных.")

@bot.message_handler(commands=['check'])
def check(message):
    name_person = message.text
    local_connection = sqlite3.connect('PhoneBook.db')
    local_cursor = local_connection.cursor()
    local_cursor.execute("SELECT * FROM contacts WHERE userName = name_person")
    all_results = local_cursor.fetchall()
    if all_results != None:
        bot.send_message(message.chat.id, str(all_results))
    else:
        bot.send_message(message.chat.id,"Error")


bot.polling(none_stop=True, interval=0)