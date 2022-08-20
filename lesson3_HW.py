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

    def __init__(self, x: int = None, y: int = None):
        self.__x = x
        self.__y = y
        self.__aria = x * y

    @property
    def aria(self):
        return self.__aria

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
    __counter = 0

    def __init__(self, name: str, age: int, size: int):
        super().__init__(name, age)
        self._size = size
        if isinstance(self, Cinderella):
            self.counter_up()

    def __str__(self):
        return str(self.__dict__)

    @classmethod
    def counter(cls):
        return cls.__counter

    @classmethod
    def counter_up(cls):
        cls.__counter += 1


class Prince(Cinderella):

    def __init__(self, name: str, age: int, size: int):
        super().__init__(name, age, size)
        self.__size = size

    def find_cinderella(self, cinderellas: list[Cinderella]):
        for cinderella in cinderellas:
            if cinderella._size == self.__size:
                return cinderella


cinderella_list = [
    Cinderella('Cinderella1', 25, 36),
    Cinderella('Cinderella3', 25, 39),
    Cinderella('Cinderella4', 25, 37),
    Cinderella('Cinderella4', 25, 35)
]

prince = Prince("Prince", 33, 37)
print(prince.find_cinderella(cinderella_list))

print("-" * 40 + "\n")
print("Cinderella counter: ", Cinderella.counter())
print("-" * 40 + "\n")

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
        print(self.__name)


class Magazine(Printable):

    def __init__(self, name):
        self.__name = name

    def print(self):
        print(self.__name)


class Main:
    __printable_list = list()

    @classmethod
    def add(cls,obj):
        cls.__printable_list.append(obj)

    @classmethod
    def show_all_magazines(cls):
        for item in cls.__printable_list:
            if isinstance(item, Magazine):
                item.print()

    @classmethod
    def show_all_books(cls):
        for item in cls.__printable_list:
            if isinstance(item, Book):
                item.print()


Main.add(Magazine('Magazine1'))
Main.add(Book('Book1'))
Main.add(Magazine('Magazine3'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book2'))

Main.show_all_magazines()
print('-' * 40)
Main.show_all_books()
