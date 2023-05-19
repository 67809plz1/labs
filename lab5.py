from random import randint

from numpy.random.mtrand import random


def p1():
    nomera = [2, 5, 8, 22, 11]
    v = int(input("нужно число"))
    if v in nomera:
        print("такое число есть")
        print("исходный список", nomera)
        print("число пользователя", v)
    else:
        print("нет такого числа")
        print("исходный список", nomera)
        print("число пользователя", v)

def p2():
    l = [0, 9, 6, 2, 8, 2]
    duplicates = set()
    for item in l:
        if l.count(item) > 1:
            duplicates.add(item)
    if duplicates:
        print("повторные элементы", duplicates)
    else:
        print("нет повторных элементов")
def p3():
    a = ('пнд','втр','ср','чет','пят','суб','вос')
    d = int(input("сколько  выхоных?"))
    for i in a:
     print("рабочие",a[:d])
     print("выходные",a[d:])
     break
def p4():
    import random
    p = ['Арабов', 'веер', 'хачев', 'чурков', 'падлов', 'Казак', 'баг', 'эрак', 'мимир',
         'Сакварелидзе']
    r = ['малинов', 'пипкин', 'Ватав', 'Шампунев', 'Иванов', 'Бурдов', 'Батюченко', 'Байров', 'Троикар',
         'Черника']
    s = []
    m = []
    print(p)
    print(r)
    s.append(p[random.randint(1, 9)])
    for i in range(4):
        k = p[random.randint(1, 9)]
        for j in range(len(s)):
            if s[j] == k:
                k = p[random.randint(1, 9)]
            else:
                continue
        s.append(k)
    m.append(r[random.randint(1, 9)])
    for i in range(4):
        f = r[random.randint(1, 9)]
        for j in range(len(m)):
            if m[j] == f:
                f = r[random.randint(1, 9)]
            else:
                continue
        m.append(f)

    n = sorted(tuple(s + m))
    i = 'Иванов' in n
    c = n.count('Иванов')
    print(n)
    print(len(n))
    if i == 1:
     print("есть", c)
    else:
       print("нету")


p4()

