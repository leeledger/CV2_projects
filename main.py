# data = [
#     [ 2000,  3050,  2050,  1980],
#     [ 7500,  2050,  2050,  1980],
#     [15450, 15050, 15550, 14900]
# ]
# result = []
# for i in data:
#     for j in i:
#         print(j * 1.00014)
#         result.append(j * 1.00014)
#     print("----")
# print(result)

# 300제 반복문 199번 문제
# ohlc = [["open", "high", "low", "close"],
#         [100, 110, 70, 100],
#         [200, 210, 180, 190],
#         [300, 310, 300, 310]]
#
# list = []
#
# for i in ohlc[1:]:
#     print(i[1]-i[2])
#

# # 300제 함수 235번 문제
# def convert_int(i):
#     return int(i.replace(",",""))
#
# print(convert_int("1,234,567"))

# 151번 문제
#
# 리스트 = [3, -20, -3, 44]
# for i in 리스트:
#     if i < 0:
#         print(i)
#
# for i in range(len(리스트)):
#     if i == 1 or i == 2:
#         print(리스트[i])

# 152번 문제
# 리스트 = [3, 100, 23, 44]
#
# for i in 리스트:
#     if i%3==0:
#         print(i)

#
# 153번 문제
# 리스트 = [13, 21, 12, 14, 30, 18]
#
# for i in 리스트:
#     if i <20 and i % 3 == 0 :
#         print(i)
#
# 154번 문제
# 리스트 = ["I", "study", "python", "language", "!"]
#
# for i in 리스트:
#     if len(i) >3:
#         print(i)
#
# 155번
# 리스트 = ["A", "b", "c", "D"]
#
# for i in 리스트:
#     if i.isupper() == True:
#         print(i)
#
# 156번
# 리스트 = ['dog', 'cat', 'parrot']
#
# for i in 리스트:
#     print(i[0].upper()+i[1:])

#
# 158번
# 리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
#
# for i in 리스트:
#     print(i.split(".")[0])

# 159
# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
#
#
# for i in 리스트:
#     if i.split(".")[-1] == "h":
#         print(i)
#
# 160번
#
# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
#
#
# for i in 리스트:
#     if i.split(".")[1] == "c" or i.split(".")[1] == "h":
#         print(i)

#
# 162번
# for i in range(2002,2051,4):
#     print(i)
#
# 165번
# for i in range(10):
#     print(float(i))
#
# 166번
# for i in range(1,10,1):
#     print("3x"+ str(i) + "=" + str(3*i))


# 166번
# for i in range(1,10,2):
#     print("3x"+ str(i) + "=" + str(3*i))

# 180번
# low_prices  = [100, 200, 400, 800, 1000]
# high_prices = [150, 300, 430, 880, 1000]
#
#
# volatility = []
#
# for i in range(len(low_prices)):
#     volatility.append(high_prices[i] - low_prices[i])
# print(volatility)
#
# 181번
# apt = [["101호","102호"],["201호","202호"],["301호","302호"]]
#
# print(apt)
#
# 182번
# stock = [["시가",100,200,300],["종가",80,210,330]]
#
# print(stock)
# 183번
#
# stock = {"시가":[10,200,300], "종가":[80,210,330]}
# print(stock)

# 185번
# apart = [ [101, 102], [201, 202], [301, 302] ]
#
# # for i in apart:
# #     print(str(i[0])+"호")
# #     print(str(i[1])+"호")
#
# for row in apart:
#     for col in row:
#         print(str(col) + "호")

# apart = [ [101, 102], [201, 202], [301, 302] ]
#
# for i in range(2,-1,-1):
#     for j in apart[i]:
#         print(str(j)+"호")


import turtle
import random
import threading
import playsound


s = turtle.Screen()
aim = turtle.Turtle()



color = ["red", "pink", "blue", "green", "white", "yellow", "purple", "violet", "orange"]
size = 0
target = []
max_target = 10


def turtle_move():
    for i in target:
        i.forward(10)
        if i.xcor() > 300 or i.xcor() < -300 or i.ycor() > 300 or i.ycor() < -300:
            i.setheading(((180 - i.heading()) * -1))
    s.ontimer(turtle_move, 10)


def create_turtle():
    aim.shape("circle")
    aim.color("white")
    aim.shapesize(0.2)
    aim.speed(0)
    aim.penup()
    s.bgcolor("black")
    while len(target) <= max_target:
        target.append(turtle.Turtle())
        target[-1].penup()
        target[-1].shape("turtle")
        target[-1].setposition(random.randint(-300, 300), random.randint(-300, 300))
        target[-1].color(random.choice(color))
        target[-1].shapesize(random.randint(1, 5))
        target[-1].setheading(random.randint(0, 359))
        target[-1].speed(0)
    turtle_move()

count = 0

def startTimer():
    global count
    timer = threading.Timer(0.0001, startTimer)
    timer.start()
    print(count)
    count += 1
    # if count > 5:
    #     timer.cancel()


# startTimer()


def click():
    pass

is_moving = False
def sound():
    playsound.playsound("163460__lemudcrab__sniper-shot-[AudioTrimmer.com].wav", False)

def on_mouse_clicked(x, y):
    global max_target
    # print("clicked ({0}, {1})".format(x, y))
    aim.goto(x, y)

    th_sound = threading.Thread(target=sound)
    th_sound.start()
    for i in range(len(target)):
        aim_range = (target[i].get_shapepoly()[3][0] - target[i].get_shapepoly()[3][1]) * -1
        if aim.distance(target[i]) < aim_range:
            target[i].hideturtle()
            max_target = max_target - 1

            # print("명중")
            break

def start_game():
    create_turtle()
    aim.showturtle()


s.onclick(on_mouse_clicked)

s.onkey(start_game,"space")
s.listen()

aim.hideturtle()
aim.write('press "space" to start', align="center", font=("Arial", 20, "bold"))



s.mainloop()
