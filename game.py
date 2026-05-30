import turtle
import random

# Screen setup
screen = turtle.Screen()
screen.title("Space Shooter")
screen.bgcolor("black")
screen.setup(width=1000, height=600)

# Player
player = turtle.Turtle()
player.shape("square")
player.color("blue")
player.penup()
player.setheading(90)
player.goto(0, -250)

# Bullet
bullet = turtle.Turtle()
bullet.shape("square")
bullet.color("yellow")
bullet.shapesize(stretch_wid=0.3, stretch_len=0.8)
bullet.penup()
bullet.hideturtle()
bullet_speed = 20

# Enemy
enemy = turtle.Turtle()
enemy.shape("square")
enemy.color("white")
enemy.penup()
enemy.goto(random.randint(-250, 250), 250)

enemy_speed = 2
score = 0

# Score display
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.color("white")
score_display.penup()
score_display.goto(-280, 260)
score_display.write(f"Score: {score}", font=("Arial", 14, "bold"))

# Functions
def move_left():
    x = player.xcor()
    if x > -280:
        player.setx(x - 20)

def move_right():
    x = player.xcor()
    if x < 280:
        player.setx(x + 20)

def fire_bullet():
    if not bullet.isvisible():
        bullet.goto(player.xcor(), player.ycor() + 10)
        bullet.showturtle()

# Keyboard bindings
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(fire_bullet, "space")

# Main game loop
while True:

    # Move enemy
    enemy.sety(enemy.ycor() - enemy_speed)

    # Reset enemy if it goes off screen
    if enemy.ycor() < -300:
        enemy.goto(random.randint(-250, 250), 250)

    # Move bullet
    if bullet.isvisible():
        bullet.sety(bullet.ycor() + bullet_speed)

    # Hide bullet if off screen
    if bullet.ycor() > 300:
        bullet.hideturtle()

    # Collision detection
    if bullet.distance(enemy) < 20:
        bullet.hideturtle()
        bullet.goto(0, -400)

        enemy.goto(random.randint(-250, 250), 250)

        score += 1
        score_display.clear()
        score_display.write(f"Score: {score}", font=("Arial", 14, "bold"))

    # Game over condition
    if enemy.distance(player) < 20:
        score_display.goto(-70, 0)
        score_display.write("GAME OVER", font=("Arial", 24, "bold"))
        break

screen.mainloop()