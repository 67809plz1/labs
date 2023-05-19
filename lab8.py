def p1():
    from PIL import Image
    name = "dr.jpg"
    with Image.open(name) as img:
        img.load()

    img = img.crop((100, 200, 400, 600))
    img.save('dr_ob.jpg')
    img.show()

def p2():
    from PIL import Image

    n = {"dr": "dr.jpg", "8 марта ": "8 марта.jpg", "дщо": "дщо.jpg"}
    m = str(input("Какой праздник"))
    file = n[m]
    with Image.open(file) as img:
        img.load()
    img.show()

def p3():
    from PIL import Image, ImageDraw, ImageFont

    name = str(input("Ваше имя"))
    image = Image.open("dr.jpg")

    font = ImageFont.truetype("arial.ttf", 50)
    drawer = ImageDraw.Draw(image)
    drawer.text((20, 30), name + ", поздравляю!", font=font, fill='red', stroke_width=2, stroke_fill="black")
    image.save('new_img.png')
    image.show()

p3()