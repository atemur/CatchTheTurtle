import turtle
import random

board = turtle.Screen()
board.bgcolor("light blue")
board.title("Catch the Turtle")
top_height = board.window_height() / 2


turtle_instance = turtle.Turtle()
turtle_instance.shape("turtle")
turtle_instance.color("darkgreen")
turtle_instance.shapesize(2)
turtle_instance.speed(0)

text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.penup()

score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.color("dark blue")
score_turtle.goto(0, top_height * 0.9)

running = True
remaining_time = 20
score = 0
score_turtle.write(f"Score: {score}", align="center", font=("Arial", 16, "bold"))

def move_randomly():
    if running:
        random_x = random.randint(-100, 100)
        random_y = random.randint(-100,100)
        turtle_instance.penup()
        turtle_instance.goto(random_x, random_y)
        board.ontimer(move_randomly, 600)

def update_timer():
    global remaining_time, running
    if remaining_time > 0:
        text_turtle.clear()
        text_turtle.goto(0, top_height * 0.8)
        text_turtle.write(f"Time Left: {remaining_time:02}", align="center", font=("Arial", 16, "bold"))
        remaining_time -= 1
        board.ontimer(update_timer, 1000)
    else: #when time stops
        running = False
        text_turtle.clear()
        text_turtle.write("Game Over!", align="center", font=("Arial", 16, "bold"))
        turtle_instance.hideturtle()

def update_score(x, y):
    global score
    if turtle_instance.distance(x, y) < 20:
        score += 1
        print(turtle_instance.position())
        score_turtle.clear()
        score_turtle.goto(0, top_height * 0.9)
        score_turtle.write(f"Score: {score}", align="center", font=("Arial", 16, "bold"))

move_randomly(), update_timer(), turtle_instance.onclick(update_score)
turtle.mainloop()