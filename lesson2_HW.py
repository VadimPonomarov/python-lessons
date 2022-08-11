'''
1) написать функцию на замыкания которая будет в себе хранить лист дел, вам нужно реализовать два метода
- первый записывает в эту переменную запись
- второй возвращает все записи

запишите 5 тудушек
и выведете все

2) протипизировать первое задание
'''


def notebook() -> list[callable]:
    todo_list: list = []

    def add_todo(todo) -> None:
        todo_list.append(todo)

    def get_all() -> list[str]:
        return todo_list

    return [add_todo, get_all]


add_todo, get_all = notebook()

add_todo('To do - 1')
add_todo('To do - 2')
add_todo('To do - 3')
add_todo('To do - 4')
add_todo('To do - 5')

to_do_list = list(get_all())

print(('\n'* 2 + '# Task - 1, 2\n' + '*' * 40))

for item in to_do_list:
    print(item)

'''
3) создать функцию которая будет возвращать сумму разрядов числа в виде строки (тоже с типизацией)

Пример:

expanded_form(12) # return '10 + 2'
expanded_form(42) # return '40 + 2'
expanded_form(70304) # return '70000 + 300 + 4'
'''


def expanded_form(num):
    l = list(str(num))
    length = len(l)
    res_list = list()
    j = 0

    for i in l[:-1]:
        if int(i) == 0:
            j += 1
            continue
        res_list.append(str(i) + '0' * (length - j - 1))
        j += 1
    else:
        res_list.append(l[-1])

    print(' + '.join(res_list))


print(('\n'* 2 + '# Task - 3\n' + '*' * 40))

expanded_form(7030411)

'''
4) создать декоратор который будет считать сколько раз была запущена функция и будет выводит это значение после каждого запуска функции
'''


def decor(func):
    count = 0

    def inner():
        nonlocal count
        count += 1
        print(count)
        func()

    return inner


@decor
def my_function():
    pass


print(('\n'* 2 + '# Task - 4\n' + '*' * 40))

my_function()
my_function()
my_function()

print(('\n'* 2))
