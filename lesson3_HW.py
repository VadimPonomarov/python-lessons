from abc import ABC, abstractmethod
'''
Создать класс Rectangle:
-конструктор принимает две стороны x,y
-описать арифметические методы:
  + сума площадей двух экземпляров класса
  - разница площадей
  == или площади равны
  != не равны
  >, < меньше или больше
  при вызове метода len() подсчитывать сумму сторон

  ###############################################################################'''

class Rectangle:

    def __init__(self, x=None, y=None):
        self.__x = x
        self.__y = y

    @property
    def aria(self):
        return self.__x * self.__y

    def __add__(self, other):
        return other.aria + self.aria

    def __sub__(self, other):
        return other.aria - self.aria

    def __eq__(self, other):
        if other.aria == self.aria:
            return True
        else:
            return False

    def __ne__(self, other):
        if other.aria != self.aria:
            return True
        else:
            return False

    def __gt__(self, other):
        if other.aria < self.aria:
            return True
        else:
            return False

    def __lt__(self, other):
        if other.aria > self.aria:
            return True
        else:
            return False

    def __len__(self):
        return (self.__x + self.__y) * 2


rect1 = Rectangle(5, 8)
rect2 = Rectangle(5, 6)

print(rect1.aria)
print(rect1 + rect2)
print(rect1 == rect2)
print(rect1 != rect2)
print(rect1 > rect2)
print(rect1 < rect2)
print(len(rect1), len(rect2))

'''
создать класс Human (name, age)
создать два класса Prince и Cinderella:
у золушки должно быть имя возраст и размер ноги
у принца имя, возраст и размер найденной туфельки, так же должен быть метод который принимает лист золушек и ищет ту самую

в классе золушки должна быть переменная count которая будет считать сколько экземпляров класса золушка было создано
и метод класса который будет показывать это количество


###############################################################################
'''

class Human:

    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._name


class Cinderella(Human):
    __count = 0

    def __init__(self, name: str, age: int, size: int):
        super().__init__(name, age)
        self._size = size
        if type(self) is Cinderella:
            Cinderella.__count += 1

    @staticmethod
    def counter():
        return Cinderella.__count


class Prince(Cinderella):

    def __init__(self, name: str, age: int, size: int, cinderella_list: list):
        super().__init__(name, age, size)
        self.__size = size
        self.__cinderella_list = cinderella_list

    def find_cinderella(self):
        for item in self.__cinderella_list:
            if item._size == self.__size:
                return item.name


cinderella_list = list()

cinderella_list.append(Cinderella('Cinderella1', 25, 36))
cinderella_list.append(Cinderella('Cinderella2', 25, 37))
cinderella_list.append(Cinderella('Cinderella3', 25, 39))
cinderella_list.append(Cinderella('Cinderella4', 25, 35))

prince = Prince("Prince", 33, 37, cinderella_list)

print(prince.find_cinderella())
print(Cinderella.counter())


'''
1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
3) Створити клас Main в якому буде:
- змінна класу printable_list яка буде зберігати книжки та журнали
- метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
- метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
- метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу

Приклад:

Main.add(Magazine('Magazine1'))
    Main.add(Book('Book1'))
    Main.add(Magazine('Magazine3'))
    Main.add(Magazine('Magazine2'))
    Main.add(Book('Book2'))

    Main.show_all_magazines()
    print('-' * 40)
    Main.show_all_books()
'''
class Printable(ABC):

    @abstractmethod
    def print(self):
        pass


class Book(Printable):

    def __init__(self, name):
        self.__name = name

    def print(self):
        def print(self):
            print(self.__name)


class Magazine(Printable):

    def __init__(self, name):
        self.__name = name

    def print(self):
        print(self.__name)


class Main:

    __printable_list = list()

    @staticmethod
    def add(obj):
        Main.__printable_list.append(obj)

    @staticmethod
    def show_all_magazines():
        for item in Main.__printable_list:
            item.print()

    @staticmethod
    def show_all_books():
        for item in Main.__printable_list:
            item.print()


Main.add(Magazine('Magazine1'))
Main.add(Book('Book1'))
Main.add(Magazine('Magazine3'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book2'))

Main.show_all_magazines()
print('-' * 40)
Main.show_all_books()