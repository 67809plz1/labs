def p1():
    try:
        a = int(input('Введите число'))
        b = a % 3
    except ValueError:
        print('это не число, дурак!')
    else:
        if a == 0:
           print('ноль не делится, тупица!')
        elif b == 0 and a != 0:
             print('Число', a, 'делится на 3!')
        else:
             print('Число', a, 'не делится на 3!')


def p2():
    try:
        a = int(input('Введи число '))
        b = 100 / a
    except ValueError:
        print('это не число!')
    except ZeroDivisionError:
        print('ноль не делится')
    else:
        print(' ответ: ', b)
def p3():
    date = input('Введите дату')
    date = date.split('.')
    if int(date[0]) * int(date[1]) == int(date[2]):
        print('Дата магическая')
    else:
        print('Дата не магическая')
def p4():
    ticket = input('Введите номер билета: ')
    x = 0
    y = 0
    if len(ticket) % 2 == 0:
        for i in ticket[0:int(len(ticket) / 2)]:
            x = x + int(i)
        for i in ticket[int(len(ticket) / 2):int(len(ticket))+1]:
            y = y + int(i)
        if x == y:
            print('Билет счастливый!')
        else:
            print('вы неудачник')
    else:
        print('Количество цифр нечётно!')
p4()

