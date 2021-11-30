
class PhoneBook:

    def __init__(self):
        self.book = {}

    def addPerson(self, key, val):
        self.book[key] = val
        return self.book

    def find(self, name):
        for name in self.book:
            data = ' '.join(self.book[name])
            return f'{name} {data}'

    def info(self):
        return self.book.items()


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
            print(book.addPerson(fio, [born, num]))
        except ValueError:
            print("Please confirm values")

    elif command == '2':
        name = input("Введите имя контакта >:  ")
        print(book.find(name))

    elif command == '3':
        for name, data in book.info():
            data = ' '.join(data)
            print(name, data)
    else:
        print('неизвестная команда')