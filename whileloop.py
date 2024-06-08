# while loop = execute some code WHILE some condition remains true.

name = input("Enter your name: ")
if name == "":
    print("You did not enter your name! ")
else:
    print(f"Hello {name}")

# но если я хочу чтобы программа снова и снова запрашивала у пользователя его имя, то я должен сделать так;

name = input("Enter your name: ")
while name == "":
    print("You did not enter your name! ")
    name = input("Enter your name: ")
print(f"Hello {name}")

"""если же мы уберем 13 строку, то программа будет без остановки выдавать текст из 12 строки.

сейчас, мы будем просить пользователя ввести свой возраст"""

age = int(input("Enter your age: "))
while age <0:
    print("Age can't be negative! ")
    age = int(input("Enter your age: "))
print(f"You are {age} years old ")

"""в следующем примере мы будем запрашивать у пользователся
ввести его любимое блюдо до тех пор пока он не введет определенный символ который мы укажем."""

food = input("Enter a food you like (q to quit) ")
while not food == "q": # соответственно цикл будет работать до тех пор пока пользователь не введет (q).
    print(f"You like {food}!")
    food = input("Enter another food you like (q to quit) ")
print("Bye!")

# в следующем примере мы задаем более узкое условие

num = int(input("Enter a number between 1 - 10: "))
while num < 1 or num > 10:
    print(f"{num} is invalid! ")
    num = int(input("Please, enter a number between 1 - 10: "))
print(f"Your number is {num}!")