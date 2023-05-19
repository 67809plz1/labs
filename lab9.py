def p1():
    import os
    from PIL import Image, ImageFilter

    os.mkdir(path = ("D:\\ternovoy\\lab 9" + '\\p'))

    rez = os.listdir(path=("D:\\ternovoy\\lab 9" + '\\картинки'))
    for f in rez:
        with Image.open("D:\\ternovoy\\lab 9" + '\\картинки\\' + f) as img:
            img.load()
            img = img.filter(ImageFilter.FIND_EDGES)
            img.save("D:\\ternovoy\\lab 9" +"\\p\ " + f)

def p2():
    import os
    from os import path
    from PIL import Image, ImageFilter

    os.mkdir(path = "D:\\ternovoy\\lab 9" + '\\tt')

    rez = os.listdir(path="D:\\ternovoy\\lab 9" + "\\картинки с png\\")
    for f in rez:
        r = str(path.splitext(f)[1])
        if r == '.jpg':
            with Image.open("D:\\ternovoy\\lab 9" + '\\картинки с png\\' + f) as img:

                img.load()
                img = img.filter(ImageFilter.FIND_EDGES)
                img.save("D:\\ternovoy\\lab 9" + "\\tt\ "  + f)

def p3():
    import csv
    print("Нужно купить:")
    sum = 0
    with open('file.csv', newline='', encoding='utf-8') as f:
        r = csv.reader(f)
        for n in r:
            sum += int(n[2]) * int(n[1])
            print(n[0] + ' - ' + n[1] + ' шт. за ' + n[2] + ' руб.')
    print("Итоговая сумма: " + str(sum))

p1()
p2()
p3()