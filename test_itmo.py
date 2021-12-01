import sqlite3

connection = sqlite3.connect('PB.sqlite')
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS contacts(
    fio TEXT,
    born TEXT,
    num TEXT);
    """)
connection.commit()

class PhoneBook:

    def __init__(self):
        self.book = {}

    def addPerson(self,fio , born , num):
        local_connection = sqlite3.connect('PB.sqlite')
        local_cursor = local_connection.cursor()
        local_cursor.execute("INSERT OR IGNORE INTO contacts VALUES(?,?,?);",
                             (fio, born, num))
        local_connection.commit()
        all_results = local_cursor.fetchall()
        return all_results

    def find(self, name):
        local_connection = sqlite3.connect('PB.sqlite')
        local_cursor = local_connection.cursor()
        local_cursor.execute("SELECT * FROM contacts WHERE name = name")
        all_results = local_cursor.fetchall()
        return all_results

    def info(self):
        local_connection = sqlite3.connect('PB.sqlite')
        local_cursor = local_connection.cursor()
        local_cursor.execute("SELECT * FROM contacts")
        all_results = local_cursor.fetchall()
        return all_results


print('Телефонная книга')
print('''Выберите что вы хотите сделать
* 1 - Добавить контакт
* 2 - Найти контакт
* 3 - просмотреть контакты''')

book = PhoneBook()

while True:
    print("Введите команду \n")
    command = input()

    if command == '1':
        try:
            fio = str(input("Фамилия: "))
            born = str(input("Дата рождения: "))
            num = int(input("Номер телефона: "))
            print(book.addPerson(fio,born, num))
        except ValueError:
            print("Please confirm values")

    elif command == '2':
        name = input("Введите фамилию контакта >:  ")
        print(book.find(name))

    elif command == '3':
        print(book.info())
    else:
        print('неизвестная команда')