def copy_if(substr: str) -> None:
    try:
        with open('emails.txt', 'r') as file, open('emails_copy.txt', 'w') as file_copy:
            while True:
                string = file.readline().strip()
                if not string:
                    break
                if substr in string:
                    print(string.split('\t')[-1], file=file_copy)

    except Exception as err:
        print(err)
    finally:
        print('!!! Done')


copy_if('@gmail.com')

from typing import TypedDict
import json

textbook_rec = TypedDict('textbook_rec', {'purchase_name': str, 'price': float})


class Note_Book():

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__record_arr: [textbook_rec] = []
        self.read_file()

    def create_rec(self, record: textbook_rec):
        try:
            self.__record_arr.append(record)
            self.write_file()
        except:
            pass

    def all_rec(self):
        try:
            if not len(self.__record_arr) > 0:
                print('*' * 40)
                print('!!! Список пуст')
                print('*' * 40)
                return
            else:
                print('*' * 40)
                for item in self.__record_arr:
                    print(item)
                print('*' * 40)
        except:
            pass

    def purchase_total(self):
        print(sum([item['price'] for item in self.__record_arr]))

    def max_price(self):
        print(max([item['price'] for item in self.__record_arr]))

    def find_first_by_name(self, name: str):
        for item in self.__record_arr:
            if name.lower() in item['purchase_name'].lower():
                print(item)
                return

    def clear_all(self):
        self.__record_arr = []
        self.write_file()
        print('*' * 40)
        print('!!! Список пуст')
        print('*' * 40)

    def read_file(self):
        try:
            with open(self.__file_name, 'r') as file:
                self.__record_arr = json.load(file)
        except:
            pass

    def write_file(self):
        try:
            with open(self.__file_name, 'w') as file:
                json.dump(self.__record_arr, file)
        except:
            pass


notebook = Note_Book('file1')

while True:
    print('1) Создать запись')
    print('2) Список все записей')
    print('3) Общая сумма всех покупок')
    print('4) Самая дорогая покупка')
    print('5) Поиск по названию покупки')
    print('8) Очистить все')
    print('9) Выход')

    choice = input('Выберите п. меню: ')

    match choice:
        case '1':
            purchase_name = input('Наименование покупки: ')
            price = input('Цена: ')
            rec: textbook_rec = {'purchase_name': purchase_name, 'price': int(price)}
            notebook.create_rec(rec)
        case '2':
            notebook.all_rec()
        case '3':
            notebook.purchase_total()
        case '4':
            notebook.max_price()
        case '5':
            notebook.find_first_by_name(input('Введите часть имени: '))
        case '8':
            notebook.clear_all()
        case '9':
            break
