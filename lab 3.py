'''words = []
while (new_word := str(input())) != "stop":
    words.append(new_word)

    print("".join(words))
'''
def p1():
 words = []
 while (new_word := str(input())) != "stop":

   if "ф" in new_word or "Ф" in new_word:
        print("это редкое слово")
   else:
        print("это вообще не редкое слово")

def p2():
    import random

    def generate_expression():
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        expression = f"{a} + {b} = "
        answer = a + b
        return expression, answer

    correct_answers = 0
    mistake_count = 0
    while mistake_count < 3:
        expression, answer = generate_expression()
        user_answer = input(expression)
        if int(user_answer) == answer:
            print("верно")
            correct_answers += 1
        else:
            print("учи математику")
            mistake_count += 1

    print(f"Игра окончена. Правильных ответов: {correct_answers}")


p2()




