import turtle
import random
screen=turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("black")

t=turtle.Turtle()
#menu
t. penup()
t.goto(-0,300)
t.pendown()
t.pencolor("white")
t.write ("Background Color",font=("arial",30,"normal"),align="center")

t. penup()
t.goto(-150,150)
t.pendown()
t.pencolor("tan")
t.write ("1. Tan",font=("arial",20,"normal"),align="left")

t. penup()
t.goto(-150,100)
t.pendown()
t.pencolor("Azure")
t.write ("2. Azure ",font=("arial",20,"normal"),align="left")

t. penup()
t.goto(-150,50)
t.pendown()
t.pencolor("AquaMarine")
t.write ("3. AquaMarine",font=("arial",20,"normal"),align="left")

t. penup()
t.goto(-150,0)
t.pendown()
t.pencolor("DarkKhaki")
t.write ("4. DarkKhaki",font=("arial",20,"normal"),align="left")

t. penup()
t.goto(0,-100)
t.pendown()
t.pencolor("white")
t.write ("Select a color",font=("arial",30,"normal"),align="center")

choose = int(input("Select a color: "))
if choose == 1:
    screen.bgcolor("tan")

elif choose==2:
    screen.bgcolor("azure")

elif choose==3:
    screen.bgcolor("aquamarine")

else:
    screen.bgcolor("darkkhaki")
t.clear()

t.pendown()
t.pencolor("Black")



name =  input("Enter your name: ")
operation = random.randint(1,4)
#num1 = int(input("Enter a number: "))
#num2 = int(input("Enter a number: "))


if operation == 1:
    symbol = "+"
    num1 = random.randint(-10,10)
    num2 = random.randint(-10,10)
    solution = num1 + num2

elif operation == 2:
    symbol = "-"
    num1 = random.randint(-10,10)
    num2 = random.randint(-10,10)
    solution = num1 - num2

elif operation == 3:
    symbol = "*"
    num1 = random.randint(-10,10)
    num2 = random.randint(-10,10)
    solution = num1 * num2

elif operation == 4:
    symbol = "/"
    num1 = random.randint(-10,10)
    num2 = random.randint(1,10)
    sign = random.randint(1,2)
    if sign == 2:
        solution = num1 / num2

t.penup()
t.goto(0,100)
t.pendown()
t.pencolor("black")
t.write(name, font=("arial",30,"normal"),align="center")

t.penup()
t.goto(-200,0)
t.pendown()
t.pencolor("black")
t.write(num1, font=("arial",30,"normal"),align="center")

t.penup()
t.goto(-100,0)
t.pendown()
t.pencolor("black")
t.write(symbol, font=("arial",30,"normal"),align="center")

t.penup()
t.goto(0,0)
t.pendown()
t.pencolor("black")
t.write(num2, font=("arial",30,"normal"),align="center")

t.penup()
t.goto(100,0)
t.pendown()
t.write('=', font=("arial",30,"normal"),align="center")

ans = float(input("Enter the answer: "))

t.penup()
t.goto(200,0)
t.pendown()
t.pencolor("black")
t.write(solution, font=("arial",30,"normal"),align="center")

t.penup()
t.goto(0,-100)
t.pendown()
t.pencolor("black")
t.write("Your answer: "+str(ans), font=("arial",30,"normal"),align="center")

if ans==solution:
    screen.bgcolor("dodgerblue")
    t.penup()
    t.goto(0,50)
    t.pendown()
    t.pencolor("black")
    t.write("correct!", font=("arial",30,"normal"),align="center")

else:
    screen.bgcolor("red")
    t.penup()
    t.goto(0,50)
    t.pendown()
    t.pencolor("black")
    t.write("incorrect", font=("arial",30,"normal"),align="center")








#No code after this
turtle.done()