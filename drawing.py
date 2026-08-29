import turtle as t

def on_button_click(x, y):
    t.onscreenclick(None)
    t.clear()
    t.bgcolor("dark blue")

    t.penup()
    t.goto(0, 80)
    t.color("white")
    t.write("7:55 Monday morning",align='center',font=("Courier",10,"bold"))

    t.goto(0,40)
    t.write("The bell is ringing in five minutes.",align='center',font=("Courier",10,"bold"))

    t.goto(0,20)
    t.write('Your backpack feels heavy. Your stomache is aching. It is your first day to a brand new school !',align='center',font=("Courier",10,"bold"))

    t.goto(0,-20)
    t.write('You are told to reach to room 242 to meet Ms Smith before the first bell',align='center',font=("Courier",10,"bold"))

    t.goto(0,-50)
    t.write('But are you ?',align='center',font=("Courier",10,"bold"))
    


t.bgcolor("light blue")
t.shapesize(3,3,3)
t.color("black", "light yellow")
t.hideturtle()
t.pencolor("white")
t.penup()
t.goto(0,100)
t.write(" Perfect Day \n Discover what actually is a perfect day",align='center',font=("Courier",25,"bold"))

t.goto(-60,-30)
t.pendown()
t.pen( pencolor="orange", pensize=10, speed=9 )
t.begin_fill()
t.forward(120)
t.left(90)
t.forward(40)
t.left(90)
t.forward(120)
t.left(90)
t.forward(40)
t.end_fill()


t.goto(0,-20)
t.pendown()
t.color("black")
t.write("START",align='center',font=("Courier",10,"bold"))

t.onscreenclick(on_button_click)
t.done

def start_game():
    t.clear()
    screen.onscreenclick(None)
    t.goto(0,50)
    t.bgcolor("yellow")
    t.pendown()
    t.color("black")
    t.write("7:55 Monday morning",align='center',font=("Courier",10,"bold"))

    t.shape("Square")
    t.turtlesize(stretch_width=120,stretch_height=40)
    t.showturtle()
    t.color("Red")

