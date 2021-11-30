from test_itmo import *
import time

if PhoneBook.find() == None:
    print("Contact not found , try again")

if command == 1:
    for key , value in book.items():
        if key == fio and value == born and value == num:
            print("This person has been writen")

if PhoneBook.info() == None:
    print("DB is empty")

try:
  born = time.strptime(born, '%m/%d/%Y')
except ValueError:
  print('Invalid date!')