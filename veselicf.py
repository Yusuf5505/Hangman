import turtle
import random



def stolby():
    turtle.penup()
    turtle.goto(300, -200)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(500)  # Высота основной стойки
        turtle.left(90)
    turtle.end_fill()

    # 2. Рисуем ВЕРХНЮЮ БАЛКУ виселицы (горизонтальная)
    turtle.penup()
    turtle.goto(300, 300)  # Верх основной стойки
    turtle.left(180)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(500)  # Длина верхней балки
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(500)  # Конец верхней балки
    turtle.pendown()
    turtle.left(90)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(500)  # Длина опорной балки
        turtle.left(90)
        turtle.forward(20)
        turtle.left(90)
    turtle.end_fill()
def golova():
    turtle.penup()
    turtle.left(90)
    turtle.forward(240)  # Отходим от края для веревки
    turtle.right(90)
    turtle.forward(20)
    turtle.pendown()

    turtle.forward(240)  # Длина веревки


    # 5. Рисуем ГОЛОВУ
    turtle.begin_fill()
    turtle.right(90)
    turtle.circle(20)  # Голова (круг радиусом 20)
    turtle.left(90)
    turtle.end_fill()
    turtle.penup()
def telo():
    # 6. Рисуем ТЕЛО
    turtle.forward(40)
    turtle.pendown()
    turtle.forward(80)
    turtle.left(180)
    turtle.penup()
    turtle.forward(50)  # Возвращаемся к центру тела
    turtle.left(50)
def left_ruka():
    turtle.pendown()
    turtle.forward(50)  # Левая рука
    turtle.penup()
    turtle.left(180)
    turtle.forward(50)  # Возврат к телу
    turtle.left(60)
def right_ruka():
    # 8. Рисуем ПРАВУЮ РУКУ
    turtle.pendown()
    turtle.forward(50)  # Правая рука
    turtle.penup()
    turtle.backward(50)  # Возврат к телу
    turtle.right(110)

def dva_nogy():
    turtle.pendown()
    turtle.forward(50)
    turtle.penup()
    turtle.right(20)
    # Рисуем левую ногу
    turtle.pendown()
    turtle.forward(50)
    turtle.penup()
    turtle.backward(50)
    turtle.left(40)
    turtle.pendown()
    turtle.forward(50)
    turtle.penup()

   # ========== НАСТРОЙКА ЭКРАНА И ПЕРЕМЕННЫХ ==========
screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(width=800, height=600)
screen.title("Виселица")



    # Создаем черепаху для рисования
turtle = turtle.Turtle()
turtle.speed(3)
turtle.fillcolor("red")
turtle.hideturtle()

    # Создаем черепаху для текста

turtle.hideturtle()
turtle.penup()
turtle.goto(-300, 200)

turtle.hideturtle()  # Скрываем черепаху после рисования

print("Добро пожаловать в виселицу!")


    # Словарь слов по категориям
categories = {
        "животные": ["лев", "тигр", "слон", "жираф", "обезьяна", "кенгуру",
                     "панда", "зебра", "носорог", "бегемот", "крокодил", "черепаха"],

        "фильмы": ["матрица", "терминатор", "титаник", "мстители", "властелин колец",
                   "звездные войны", "форсаж", "джон уик", "человек-паук", "побег из лабиринта"],

        "страны": ["россия", "китай", "египет", "индия", "бразилия", "германия",
                   "франция", "япония", "канада", "австралия", "италия", "испания"],

        "города": ["москва", "санкт петербург", "нью йорк", "лондон", "париж",
                   "токио", "берлин", "каир", "рим", "дубай", "эр-рияд", "стамбул"]}


var=input("Введите тему").lower()
ghost=[]
popytky=6
usp_slovo = []  # Уже использованные буквы
if var in categories:
    print(f"Ваша тема {var}")
    if var == "животные":
        sekret_slovo = random.choice(categories["животные"])
    elif var == "фильмы":
        sekret_slovo = random.choice(categories["фильмы"])
    elif var == "страны":
        sekret_slovo = random.choice(categories["страны"])
    elif var == "города":
        sekret_slovo = random.choice(categories["города"])
    else:
        print("Пожалуста введите коррекные данные")
for i in range(len(sekret_slovo)):
    ghost.append("_")



def vyvod_ekran():

    print(f"\nСлово: {ghost}")

    print(f"Попытки: {popytky} | Использовано: {usp_slovo}")

def wrong_answers(errors):
        if errors == 1:
            stolby()

        elif errors == 2:
            golova()

        elif errors == 3:
            telo()

        elif errors == 4:
            left_ruka()

        elif errors == 5:
            right_ruka()

        elif errors == 6:
            dva_nogy()
            turtle.goto(1, -200)
            turtle.write("GAME OVER \nDEAD", font=("Arial", 16, "normal"))
vyvod_ekran()

# Игровой цикл
while popytky > 0 and "_" in ghost:
    var1 = input("Введите букву: ").lower().strip()

    if len(var1) != 1 or var1 not in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя":
        print("Пожалуйста, введите одну букву.")
        continue

    if var1 in usp_slovo:
        print("Вы уже вводили эту букву.")
        continue

    usp_slovo.append(var1)
    if var1 in sekret_slovo:
        print("Правильно!Это буква есть в слове")
        for i in range(len(sekret_slovo)):
            if sekret_slovo[i] == var1:
                ghost[i] = var1
    else:
        print("Такой буквы нет слове")
        popytky -= 1
        print(f"Осталось {popytky} попыток")
        vyvod_ekran()

        wrong_answers(6-popytky)

    vyvod_ekran()

if "_" not in ghost:
    turtle.goto(-400, -300)
    turtle.write("ПОБЕДА! ПОЗДРАВЛЯЕМ!", font=("Arial", 20, "bold"))
    print(f"Поздравляем! Вы выиграли! Загаданное слово: {sekret_slovo}")
else:
    turtle.goto(1, -300)
    turtle.write(f"Загаданное слово: {sekret_slovo}", font=("Arial", 14, "normal"))
    print(f"Игра окончена. Загаданное слово было: {sekret_slovo}")

screen.exitonclick()












