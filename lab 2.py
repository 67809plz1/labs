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






p1()




