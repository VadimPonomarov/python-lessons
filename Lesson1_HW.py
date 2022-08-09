# 1 написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.
# #################################################################################

def digit_in_string():
    st = input('Введите строку символов, в т.ч. числа: ')
    l = list()

    for i in st:
        if i.isdigit():
            l.append(i)

    print(','.join(l))


digit_in_string()


# 2 написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі
# #################################################################################

def digits_in_string():
    st = input('Введите строку символов, в т.ч. числа: ')
    l = list()

    for i in st:
        if i.isdigit():
            l.append(i)
        else:
            l.append(' ')

    l1 = ''.join(l).split(' ')

    for i in l1:
        if i:
            l1.remove('')

    print(','.join(l1))


digits_in_string()


# 3 є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

def capitalize_list():
    greeting = 'Hello, world'
    l = list()

    for i in greeting:
        l.append(i.capitalize())

    print(l)

capitalize_list()

# 4 - з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
#приклад:
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

def pow_even():
    print([i**2 for i in range(50) if i%2==0])

pow_even()




# 5
# 5.1 - створити функцію яка виводить ліст

def get_list(*args):
    return print(list(args))


get_list(1, 'lili', 3)

#5.2 - створити функцію яка приймає три числа та виводить та повертає найбільше.

def max_num(num1: int, num2: int, num3: int):
    return print(max([num1, num2, num3]))

max_num(5,1,2)


#5.3 - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

def min_num(*args: int):
    print(max(*args))
    return min(*args)

min_num(5, 1, 2, 0, 99)

#5.4 - створити функцію яка повертає найбільше число з ліста

def max_list_num(lst:list):
    print(max(lst))
    return max(lst)

max_list_num([5, 1, 2, 0, 99])

#5.5 - створити функцію яка повертає найменьше число з ліста

def min_list_num(lst:list):
    print(min(lst))
    return min(lst)

min_list_num([5, 1, 2, 0, 99])

#5.6 - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

def sum_list(lst:list):
    sum = 0
    for l in lst:
        sum += l

    print(sum)
    return sum

sum_list([5, 1, 2, 0, 99])

#5.7 - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

def sum_list_avg(lst:list):
    sum = 0
    for l in lst:
        sum += l

    print(sum / len(lst))
    return sum / len(lst)

sum_list_avg([5, 1, 2, 0, 99])


#6
# -Дані list:  list = [22, 3,5,2,8,2,-23, 8,23,5]

def list_calc(list: list):
    # - знайти мін число
    print(min(list))
    # - видалити усі дублікати
    print(set(list))
    # - замінити кожне 4-те значення на 'X'
    i = 0
    for l in list:
        if i !=0 and (i+1) % 4 == 0:
            list[i] = 'X'
        i += 1
    print(list)

list_calc([22, 3, 5, 2, 8, 2, -23, 8, 23, 5])

# 7 - вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції

def square(num: int):
    lst1 = ['*' for i in range(num)]
    lst2 = ['*'] + [' ' for i in range(num-2)] + ['*']
    for i in range(num+1):
        if i == 1 or i == num:
            print(''.join(lst1))
        else:
            print(''.join(lst2))

square(15)




# 8.1 - вывести табличку множення

def pow_table():
    for i in range(1, 10):
        l = [f'{str(i * j):3}' for j in range(1, 10)]
        print(' '.join(l))


pow_table()

# 8.2 - вывести табличку множення циклом while

def pow_table_while():
    i = 1
    while i <= 9:
        l = [f'{str(i * j):3}' for j in range(1, 10)]
        i += 1
        print(' '.join(l))

pow_table_while()