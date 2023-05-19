def p1():
    from PIL import Image

    filename = "3.jpg"
    with Image.open(filename) as img:
        img.load()
    img.show()
    width, height = img.size

    format = img.format

    mode = img.mode

    print("Ширина: ", width)
    print("Высота:  ", height)
    print("Формат: ", format)
    print("Цветовая модель:", mode)

def p2():
    from PIL import Image

    filename = "3.jpg"
    with Image.open(filename) as img:
        img.load()

    new_img = img.resize((img.width // 3, img.height // 3))
    new_img.save("уменьшенный 3.jpg")

    new_img = img.rotate(180)
    new_img.save("перевернутый 3.jpg")

    new_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    new_img.save("другой перевернутый 3.jpg")

def p3():
    from PIL import Image, ImageFilter
    name = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
    for p in name:
        with Image.open(p) as img:
            img.load()
            img = img.filter(ImageFilter.CONTOUR)
            img.save("D:\\ternovoy\\lab7\\фильтр\ " + p)



def p4():
    from PIL import Image

    img = Image.open('3.jpg')
    watermark = Image.open('watermark.png')

    img.paste(watermark, (40, 60), watermark)
    img.save("nnn.png")


p4()




