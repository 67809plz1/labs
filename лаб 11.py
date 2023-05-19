def p1():
    class restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f"ресторан {self.restaurant_name}, кухня {self.cuisine_type} итальянская")

        def open_restaurant(self):
            print("ресторан открыт")

    newRestaurant = restaurant("у ашота","")
    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)

def  p2():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print(f"Название ресторана {self.restaurant_name}, Кухня {self.cuisine_type}")
    newRestaurant1 = Restaurant("KFC", "Американская")
    newRestaurant2 = Restaurant("шашлычная", "Руская")
    newRestaurant3 = Restaurant("мама мия", "Итальянская")
    newRestaurant1.describe_restaurant()
    newRestaurant2.describe_restaurant()
    newRestaurant3.describe_restaurant()

def p3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, rating):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating
        def describe_restaurant(self):
            print(f"Название ресторана {self.restaurant_name}")
            print(f"Кухня:{self.cuisine_type}")
            print(f"Рейтинг:{self.rating}")
    newRestaurant = Restaurant("у ашота", "Грузинская", "3")
    newRestaurant.describe_restaurant()
    newRestaurant.rating=input("Введите новый рейтинг: ")
    newRestaurant.describe_restaurant()

p3()